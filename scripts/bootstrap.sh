#!/usr/bin/env bash
# Atlas do Tempo 3D — bootstrap reproduzível.
# Sobe o banco persistente, aplica esquema + camada de leitura, migra os 35 itens,
# e roda as suítes de teste. Sucesso = verify.py 10/10 E test_a4.py 10/10.
set -euo pipefail

cd "$(dirname "$0")/.."   # raiz do repo

DSN="host=localhost port=5432 dbname=atlas user=atlas password=atlas"

echo "==> (1/6) subindo Postgres + PostGIS (volume persistente atlas-pgdata)…"
docker compose up -d

echo "==> (2/6) aguardando o banco ficar pronto…"
for i in $(seq 1 60); do
  if docker compose exec -T db pg_isready -U atlas -d atlas >/dev/null 2>&1; then break; fi
  sleep 1
  if [ "$i" -eq 60 ]; then echo "ERRO: banco não respondeu em 60s"; exit 1; fi
done

echo "==> (3/6) aplicando DDL (esquema reificado)…"
docker compose exec -T db psql -v ON_ERROR_STOP=1 -U atlas -d atlas < db/ddl/001-esquema-reificado.sql

echo "==> (4/6) aplicando camada de leitura gateada…"
docker compose exec -T db psql -v ON_ERROR_STOP=1 -U atlas -d atlas < db/read-layer/010-leitura-simultaneidade.sql

echo "==> (5/6) instalando deps Python e migrando 35 itens…"
python3 -m pip install -q -r db/requirements.txt
python3 db/migration/migrate.py

echo "==> (6/6) verificando invariantes (T1–T10) e simultaneidade A4 (A4-T1..T10)…"
python3 db/migration/verify.py
python3 db/migration/test_a4.py

echo ""
echo "==> OK. Banco persistente pronto."
echo "    Reabra com 'docker compose up -d' — os dados permanecem no volume."
echo "    Consulte: docker compose exec db psql -U atlas -d atlas \\"
echo "      -c \"select id,title,selo,is_fact from core.f_simultaneidade_publica(-212,-210,'{}');\""
