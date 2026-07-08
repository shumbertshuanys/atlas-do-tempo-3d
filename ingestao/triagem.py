# -*- coding: utf-8 -*-
"""
Triagem de tier (spec §5) — conservadora: na dúvida, Tier 0 (Art.9).

Elegível a Tier 1 SOMENTE se TODAS:
  - PG5 = 'público';
  - sem ClaimSet;
  - TODOS os claims com claim_type ∈ {fato-documentado, medição-direta};
  - TODAS as fontes authority_tier = 'A';
  - sem pessoa viva citada;
  - sem reconstrução/paleo (na prática tempo profundo já cai pela regra de
    claim_type);
  - licença da fonte sem restrição de uso.
Qualquer outra coisa — inclusive dúvida — é Tier 0.

A IA PROPÕE (tier_proposto no pacote); o humano CONFIRMA na montagem do lote.
O triador pode ENDURECER T1→T0 sem justificativa; AFROUXAR T0→T1 exige
justificativa registrada no manifesto (regra aplicada na CLI, não aqui).
"""

CLAIM_TYPES_T1 = frozenset({"fato-documentado", "medição-direta"})

# marcadores de licença com restrição de uso (heurística v0; conservadora):
# qualquer coisa fora de domínio público / CC BY / CC0 é tratada como restrita
# para efeito de elegibilidade T1 (o revisor confere no §6.1.8).
_LICENCA_LIVRE = ("domínio público", "dominio publico", "public domain",
                  "cc0", "cc by", "cc-by")


def _licenca_livre(lic):
    if not isinstance(lic, str):
        return False
    l = lic.strip().lower()
    if not l:
        return False
    if "nc" in l or "share" in l or "sa" in l.split() or "nd" in l.split():
        return False
    return any(marca in l for marca in _LICENCA_LIVRE)


def triar(pkg):
    """Retorna (tier_calculado, motivos). tier_calculado ∈ {'T0','T1'}.
    motivos: lista das razões que forçaram T0 (vazia ⇒ elegível a T1)."""
    motivos = []

    if pkg.get("pg5") != "público":
        motivos.append(f"PG5 = {pkg.get('pg5')!r} (≠ público)")
    if pkg.get("claim_set") is not None:
        motivos.append("possui ClaimSet (leituras concorrentes ⇒ T0)")
    if pkg.get("pessoa_viva_citada") is True:
        motivos.append("cita pessoa viva (§4.7 ⇒ T0 forçado)")

    for i, c in enumerate(pkg.get("claims") or []):
        ct = c.get("claim_type")
        if ct not in CLAIM_TYPES_T1:
            motivos.append(f"claims[{i}].claim_type = {ct!r} ∉ {{fato-documentado, medição-direta}}")

    for i, s in enumerate(pkg.get("sources") or []):
        if s.get("authority_tier") != "A":
            motivos.append(f"sources[{i}].authority_tier = {s.get('authority_tier')!r} (≠ A)")
        if not _licenca_livre(s.get("license")):
            motivos.append(f"sources[{i}].license = {s.get('license')!r} (restrição de uso / não-livre)")

    item = pkg.get("item") or {}
    geo = item.get("geo")
    if isinstance(geo, dict) and (geo.get("is_paleo") or geo.get("is_reconstruction")):
        motivos.append("geometria reconstruída/paleo (⇒ T0)")

    tier = "T1" if not motivos else "T0"
    return tier, motivos
