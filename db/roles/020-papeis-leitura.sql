-- =====================================================================
-- Atlas do Tempo 3D — Passo A3 · D-A3.5
-- 020-papeis-leitura.sql — PORTÃO POR GRANT (dois papéis de leitura)
-- ADIÇÃO. Depende de 011 (as funções-envelope já existem). NÃO toca DDL/010/011.
--
-- Princípio (Constituição Art.6 / R-A3.7): o portão é PROPRIEDADE DO GRANT,
-- não um `if` de runtime. Quem pode ver a porta curatorial é decidido por quem
-- tem EXECUTE — não por código da aplicação.
--
--   * atlas_public      → EXECUTE SÓ em f_momento_publico. Sem acesso à
--                         curatorial (EXECUTE já revogado de PUBLIC em 011;
--                         revogação explícita aqui por robustez). Sem escrita.
--   * atlas_curatorial  → EXECUTE nas DUAS funções. Autenticação é da borda HTTP;
--                         no banco, é só mais EXECUTE. Sem escrita.
--
-- As funções-envelope são SECURITY DEFINER (dono = atlas): o chamador precisa
-- APENAS de EXECUTE + USAGE no schema — nenhum SELECT direto em tabela/view.
-- Logo nenhum dos dois papéis recebe (nem precisa de) qualquer privilégio de
-- escrita. A3-HTTP-1 fica VERMELHO se alguém der EXECUTE da curatorial ao público.
-- =====================================================================

-- Papéis idempotentes (LOGIN: a borda HTTP conecta como cada papel).
-- Senhas locais (casam com o DSN do serviço/teste; ambiente de desenvolvimento).
DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='atlas_public') THEN
    CREATE ROLE atlas_public LOGIN PASSWORD 'atlas_public';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='atlas_curatorial') THEN
    CREATE ROLE atlas_curatorial LOGIN PASSWORD 'atlas_curatorial';
  END IF;
END $$;

-- Conexão + uso do schema (necessário para chamar função; NÃO dá leitura de tabela).
GRANT CONNECT ON DATABASE atlas TO atlas_public, atlas_curatorial;
GRANT USAGE   ON SCHEMA   core  TO atlas_public, atlas_curatorial;

-- PORTA PÚBLICA: EXECUTE para ambos os papéis (o curatorial também lê o público).
GRANT EXECUTE ON FUNCTION core.f_momento_publico(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[])
  TO atlas_public, atlas_curatorial;

-- PORTA CURATORIAL: EXECUTE SÓ para atlas_curatorial. Revogação explícita do
-- público (defesa em profundidade sobre o REVOKE FROM PUBLIC de 011).
REVOKE EXECUTE ON FUNCTION core.f_momento_curatorial(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[])
  FROM atlas_public;
GRANT  EXECUTE ON FUNCTION core.f_momento_curatorial(DOUBLE PRECISION,DOUBLE PRECISION,TEXT[])
  TO atlas_curatorial;

-- Sem grant de escrita em lugar nenhum: ambos os papéis são estritamente leitura
-- via função. (Não há GRANT INSERT/UPDATE/DELETE neste arquivo — por desenho.)
