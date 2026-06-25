#!/usr/bin/env bash
# Atlas do Tempo 3D — bootstrap reproduzível.
# Sobe o banco persistente, aplica esquema + camada de leitura + envelope A3 +
# papéis de leitura, migra os 35 itens, e roda as suítes de teste.
# Sucesso = verify 10/10 E test_a4 10/10 E test_a3 10/10 E test_a3_http 5/5.
set -euo pipefail

cd "$(dirname "$0")/.."   # raiz do repo

DSN="host=localhost port=5432 dbname=atlas user=atlas password=atlas"

# Interpretador Python: 'python3' (Linux/macOS) ou 'python' (Windows). Override com PY=...
# Valida EXECUÇÃO real, não só presença no PATH: no Windows o alias da Microsoft
# Store cria um 'python3.exe' que aparece no PATH mas não roda (abre a loja).
PY="${PY:-}"
py_ok() { command -v "$1" >/dev/null 2>&1 && "$1" -c 'import sys' >/dev/null 2>&1; }
if [ -z "$PY" ]; then
  if   py_ok python3; then PY=python3
  elif py_ok python;  then PY=python
  else echo "ERRO: Python executável não encontrado (instale python3 ou python)"; exit 1; fi
fi

echo "==> (1/8) subindo Postgres + PostGIS (volume persistente atlas-pgdata)…"
docker compose up -d

echo "==> (2/8) aguardando o banco ficar pronto…"
# Checa prontidão via TCP (-h 127.0.0.1), não pelo socket: durante a 1ª init o
# entrypoint sobe um servidor TEMPORÁRIO com listen_addresses='' (só socket) e
# depois reinicia. O socket responderia cedo demais e o passo seguinte morreria
# com "the database system is shutting down". Só o servidor REAL aceita TCP.
for i in $(seq 1 60); do
  if docker compose exec -T db pg_isready -h 127.0.0.1 -U atlas -d atlas >/dev/null 2>&1; then break; fi
  sleep 1
  if [ "$i" -eq 60 ]; then echo "ERRO: banco não respondeu em 60s"; exit 1; fi
done

echo "==> (3/8) aplicando DDL (esquema reificado)…"
docker compose exec -T db psql -v ON_ERROR_STOP=1 -U atlas -d atlas < db/ddl/001-esquema-reificado.sql

echo "==> (4/8) aplicando camada de leitura gateada…"
docker compose exec -T db psql -v ON_ERROR_STOP=1 -U atlas -d atlas < db/read-layer/010-leitura-simultaneidade.sql

echo "==> (5/8) aplicando envelope MomentResult (D-A3.3 — adição ao lado do A4)…"
docker compose exec -T db psql -v ON_ERROR_STOP=1 -U atlas -d atlas < db/read-layer/011-momento-envelope.sql

echo "==> (6/8) aplicando papéis de leitura (D-A3.5 — portão por grant)…"
docker compose exec -T db psql -v ON_ERROR_STOP=1 -U atlas -d atlas < db/roles/020-papeis-leitura.sql

echo "==> (7/8) instalando deps Python e migrando 35 itens…"
"$PY" -m pip install -q -r db/requirements.txt
"$PY" db/migration/migrate.py

echo "==> (8/8) verificando invariantes (T1–T10), simultaneidade A4 (A4-T1..T10), envelope A3 (A3-T1..T10) e portão/HTTP (A3-HTTP-1..5)…"
"$PY" db/migration/verify.py
"$PY" db/migration/test_a4.py
"$PY" db/migration/test_a3.py
"$PY" db/migration/test_a3_http.py

echo ""
echo "==> OK. Banco persistente pronto."
echo "    Reabra com 'docker compose up -d' — os dados permanecem no volume."
echo "    Consulte: docker compose exec db psql -U atlas -d atlas \\"
echo "      -c \"select id,title,selo,is_fact from core.f_simultaneidade_publica(-212,-210,'{}');\""
