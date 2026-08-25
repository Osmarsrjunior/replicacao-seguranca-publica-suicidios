#!/usr/bin/env python3
"""Testes de reconciliação para o pacote analítico."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dados_processados"


def main() -> None:
    stats = json.loads((OUT / "estatisticas.json").read_text(encoding="utf-8"))
    annual = pd.read_csv(OUT / "serie_anual.csv")
    careers = pd.read_csv(OUT / "carreiras_total.csv")
    methods = pd.read_csv(OUT / "metodos_carreira.csv")
    models = pd.read_csv(OUT / "modelos_logisticos.csv")

    checks = {
        "serie_soma_1070": int(annual["obitos"].sum()) == 1070,
        "carreiras_soma_1070": int(careers["obitos"].sum()) == 1070,
        "metodos_soma_1070": int(methods["obitos"].sum()) == 1070,
        "recuperados_soma_638": int(careers["recuperados"].sum()) == 638,
        "armas_soma_663": int(careers["armas_fogo"].sum()) == 663,
        "cbo_depois_igual_antes_mais_recuperado": (
            stats["n_cbo_valido_depois"]
            == stats["n_cbo_valido_antes"] + stats["n_cbo_recuperado"]
        ),
        "sim_2019_proximo_fbsp": abs(
            stats["pm_pc_2019_sim_reconstruido"] - stats["pm_pc_2019_fbsp"]
        ) <= 2,
        "modelos_sem_intervalo_invertido": bool(
            (models["IC95_inf"] <= models["OR"]).all()
            and (models["OR"] <= models["IC95_sup"]).all()
        ),
        "modelos_p_validos": bool(models["p"].between(0, 1).all()),
    }
    failed = [name for name, ok in checks.items() if not ok]
    report = {
        "status": "APROVADO" if not failed else "REPROVADO",
        "checks": checks,
        "falhas": failed,
    }
    (OUT / "relatorio_validacao.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

