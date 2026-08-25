#!/usr/bin/env python3
"""Reproduz as análises do artigo sobre suicídio na segurança pública.

Entrada esperada:
  fontes/suicide_in_brazil/data/df.csv
  dados_brutos/CBO.csv

As saídas não contêm datas completas nem municípios, para reduzir risco de
reidentificação em células ocupacionais pequenas.
"""

from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MPL_CACHE = ROOT / "work" / "matplotlib"
MPL_CACHE.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CACHE))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm


RAW_SIM = ROOT / "fontes" / "suicide_in_brazil" / "data" / "df.csv"
RAW_CBO = ROOT / "dados_brutos" / "CBO.csv"
OUT = ROOT / "dados_processados"
FIG = ROOT / "figuras"
OUT.mkdir(parents=True, exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)


PUBLIC_CODES = {
    "020105", "020110", "020115", "020205", "020305", "020310",
    "021105", "021110", "021205", "021210",  # Polícia Militar
    "030105", "030110", "030115", "030205", "030305",
    "031105", "031110", "031205", "031210",  # Bombeiro Militar
    "204105", "242305", "351420", "351810", "351815",  # PC/perícia
    "517205", "517210",  # PF e PRF
    "517215",  # Guarda civil municipal
    "517315",  # Segurança penitenciária/polícia penal
}

PRIVATE_CODES = {"517305", "517310", "517320", "517325", "517330", "517420"}

PM_CODES = {c for c in PUBLIC_CODES if c.startswith("02")}
BM_CODES = {c for c in PUBLIC_CODES if c.startswith("03")}
PC_CODES = {"204105", "242305", "351420", "351810", "351815"}
FED_CODES = {"517205", "517210"}
PRISON_CODES = {"517315"}
MUNICIPAL_CODES = {"517215"}


def damaged_key(code6: str) -> str:
    """Replica o efeito de `rstrip('.0')` aplicado ao CBO numérico."""
    return str(int(code6)).rstrip("0")


def parse_ddmmyyyy(series: pd.Series) -> pd.Series:
    s = series.astype("string").str.replace(r"\.0$", "", regex=True).str.zfill(8)
    return pd.to_datetime(s, format="%d%m%Y", errors="coerce")


def career(code: str | float) -> str:
    if code in PM_CODES:
        return "Polícia Militar"
    if code in BM_CODES:
        return "Bombeiro Militar"
    if code in PC_CODES:
        return "Polícia Civil e perícia"
    if code in FED_CODES:
        return "Polícia Federal e PRF"
    if code in PRISON_CODES:
        return "Polícia penal/penitenciária"
    if code in MUNICIPAL_CODES:
        return "Guarda civil municipal"
    return "Fora do recorte"


def method(cause: str | float) -> str:
    c = str(cause)
    if re.match(r"^X7[2-4]", c):
        return "Arma de fogo"
    if c.startswith("X70"):
        return "Enforcamento"
    if re.match(r"^X6[0-9]", c):
        return "Autointoxicação"
    if c.startswith("X80"):
        return "Precipitação"
    return "Outros meios"


def region(uf: str | float) -> str:
    x = str(uf)
    if x in {"AC", "AP", "AM", "PA", "RO", "RR", "TO"}:
        return "Norte"
    if x in {"AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"}:
        return "Nordeste"
    if x in {"DF", "GO", "MT", "MS"}:
        return "Centro-Oeste"
    if x in {"ES", "MG", "RJ", "SP"}:
        return "Sudeste"
    if x in {"PR", "RS", "SC"}:
        return "Sul"
    return "Ignorado"


def binomial_logit_robust(x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Logit por IRLS com erros-padrão sanduíche HC1."""
    beta = np.zeros(x.shape[1], dtype=float)
    for _ in range(100):
        eta = np.clip(x @ beta, -30, 30)
        p = 1.0 / (1.0 + np.exp(-eta))
        w = np.clip(p * (1 - p), 1e-8, None)
        z = eta + (y - p) / w
        xtwx = x.T @ (w[:, None] * x)
        beta_new = np.linalg.pinv(xtwx) @ (x.T @ (w * z))
        if np.max(np.abs(beta_new - beta)) < 1e-9:
            beta = beta_new
            break
        beta = beta_new
    eta = np.clip(x @ beta, -30, 30)
    p = 1.0 / (1.0 + np.exp(-eta))
    w = np.clip(p * (1 - p), 1e-8, None)
    bread = np.linalg.pinv(x.T @ (w[:, None] * x))
    score = x * (y - p)[:, None]
    meat = score.T @ score
    n, k = x.shape
    cov = bread @ meat @ bread * (n / max(n - k, 1))
    return beta, np.sqrt(np.clip(np.diag(cov), 0, None))


def logistic_table(data: pd.DataFrame, comparison: str = "all") -> pd.DataFrame:
    d = data.copy()
    d = d[(d["idade"] >= 18) & (d["idade"] <= 69) & d["cbo_valido"]].copy()
    d["grupo_ocupacional"] = np.select(
        [d["seg_publica"], d["seg_privada"]],
        ["Segurança pública", "Segurança privada"],
        default="Outras ocupações",
    )
    if comparison == "security":
        d = d[d["grupo_ocupacional"].isin(["Segurança privada", "Segurança pública"])].copy()
    d["idade_faixa"] = pd.cut(
        d["idade"], [17, 29, 39, 49, 59, 69],
        labels=["18–29", "30–39", "40–49", "50–59", "60–69"],
    ).astype("string")
    d["raca_modelo"] = np.where(d["RACACOR"].isin(["Preta", "Parda"]), "Preta/parda", "Outra/ignorada")
    d["uniao_modelo"] = np.where(d["ESTCIV"].isin(["Casado", "União consensual"]), "Com união", "Sem união/ignorado")
    d["sexo_modelo"] = np.where(d["SEXO"].eq("Masculino"), "Masculino", "Feminino/ignorado")
    d["regiao"] = d["estado"].map(region)
    d["ano_c"] = d["ano"] - 2010
    y = d["arma_fogo"].astype(int).to_numpy()

    occupation_levels = (
        ["Segurança privada", "Segurança pública"]
        if comparison == "security"
        else ["Outras ocupações", "Segurança privada", "Segurança pública"]
    )
    cats = {
        "grupo_ocupacional": occupation_levels,
        "sexo_modelo": ["Feminino/ignorado", "Masculino"],
        "idade_faixa": ["18–29", "30–39", "40–49", "50–59", "60–69"],
        "raca_modelo": ["Outra/ignorada", "Preta/parda"],
        "uniao_modelo": ["Sem união/ignorado", "Com união"],
        "regiao": ["Sudeste", "Norte", "Nordeste", "Centro-Oeste", "Sul"],
    }
    cols = [np.ones(len(d))]
    names = ["Intercepto"]
    for var, levels in cats.items():
        for level in levels[1:]:
            cols.append((d[var].astype(str) == level).astype(float).to_numpy())
            names.append(f"{var}: {level}")
    cols.append(d["ano_c"].astype(float).to_numpy())
    names.append("Ano (incremento anual)")
    x = np.column_stack(cols)
    beta, se = binomial_logit_robust(x, y)
    z = beta / se
    pval = 2 * norm.sf(np.abs(z))
    out = pd.DataFrame({
        "termo": names,
        "OR": np.exp(beta),
        "IC95_inf": np.exp(beta - 1.96 * se),
        "IC95_sup": np.exp(beta + 1.96 * se),
        "p": pval,
    })
    out.attrs["n"] = len(d)
    return out


def main() -> None:
    sim = pd.read_csv(RAW_SIM, low_memory=False)
    cbo = pd.read_csv(RAW_CBO)
    cbo["code6"] = cbo["CODIGO"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(6)
    cbo["key_bad"] = cbo["code6"].map(damaged_key)
    if cbo["key_bad"].duplicated().any():
        raise ValueError("A chave reversa de CBO não é unívoca.")

    desc_to_code = dict(zip(cbo["OCUPACAO"], cbo["code6"]))
    bad_to_code = dict(zip(cbo["key_bad"], cbo["code6"]))
    code_to_desc = dict(zip(cbo["code6"], cbo["OCUPACAO"]))

    occupation_raw = sim["OCUP"].astype("string")
    is_numeric = occupation_raw.str.fullmatch(r"\d+").fillna(False)
    sim["cbo_reconstruido"] = occupation_raw.map(desc_to_code)
    sim.loc[is_numeric, "cbo_reconstruido"] = occupation_raw[is_numeric].map(bad_to_code)
    sim["ocupacao_reconstruida"] = sim["cbo_reconstruido"].map(code_to_desc)
    sim["cbo_valido"] = sim["cbo_reconstruido"].notna()
    sim["codigo_recuperado"] = is_numeric & sim["cbo_valido"]
    sim["seg_publica"] = sim["cbo_reconstruido"].isin(PUBLIC_CODES)
    sim["seg_privada"] = sim["cbo_reconstruido"].isin(PRIVATE_CODES)
    sim["carreira"] = sim["cbo_reconstruido"].map(career)
    sim["metodo"] = sim["CAUSABAS"].map(method)
    sim["arma_fogo"] = sim["metodo"].eq("Arma de fogo")
    sim["data_obito"] = parse_ddmmyyyy(sim["DTOBITO"])
    sim["data_nasc"] = parse_ddmmyyyy(sim["DTNASC"])
    sim["idade"] = np.floor((sim["data_obito"] - sim["data_nasc"]).dt.days / 365.2425)
    sim.loc[(sim["idade"] < 0) | (sim["idade"] > 110), "idade"] = np.nan
    sim["idade_faixa"] = pd.cut(
        sim["idade"], [17, 29, 39, 49, 59, 69, np.inf],
        labels=["18–29", "30–39", "40–49", "50–59", "60–69", "70+"],
    )
    sim["regiao"] = sim["estado"].map(region)

    public = sim[sim["seg_publica"]].copy()
    public_before = public[~public["codigo_recuperado"]]
    public_recovered = public[public["codigo_recuperado"]]

    annual = public.groupby("ano", as_index=False).agg(
        obitos=("seg_publica", "size"),
        recuperados=("codigo_recuperado", "sum"),
        armas_fogo=("arma_fogo", "sum"),
    )
    annual["percentual_recuperado"] = 100 * annual["recuperados"] / annual["obitos"]
    annual["percentual_arma_fogo"] = 100 * annual["armas_fogo"] / annual["obitos"]

    career_year = public.groupby(["ano", "carreira"], as_index=False).size().rename(columns={"size": "obitos"})
    career_total = public.groupby("carreira", as_index=False).agg(
        obitos=("seg_publica", "size"),
        recuperados=("codigo_recuperado", "sum"),
        armas_fogo=("arma_fogo", "sum"),
    )
    career_total["percentual_recuperado"] = 100 * career_total["recuperados"] / career_total["obitos"]
    career_total["percentual_arma_fogo"] = 100 * career_total["armas_fogo"] / career_total["obitos"]

    methods = public.groupby(["carreira", "metodo"], as_index=False).size().rename(columns={"size": "obitos"})
    methods["percentual_na_carreira"] = 100 * methods["obitos"] / methods.groupby("carreira")["obitos"].transform("sum")

    profile_vars = ["SEXO", "RACACOR", "ESTCIV", "ESC", "idade_faixa", "regiao", "LOCOCOR"]
    profile_frames = []
    for var in profile_vars:
        tmp = public[var].astype("string").fillna("Ignorado").value_counts(dropna=False).rename_axis("categoria").reset_index(name="obitos")
        tmp["variavel"] = var
        tmp["percentual"] = 100 * tmp["obitos"] / len(public)
        profile_frames.append(tmp[["variavel", "categoria", "obitos", "percentual"]])
    profile = pd.concat(profile_frames, ignore_index=True)

    correction_by_code = public.groupby(["cbo_reconstruido", "ocupacao_reconstruida"], as_index=False).agg(
        obitos=("seg_publica", "size"),
        recuperados=("codigo_recuperado", "sum"),
    ).sort_values(["recuperados", "obitos"], ascending=False)

    logit_all = logistic_table(sim, comparison="all")
    logit_all_n = logit_all.attrs["n"]
    logit_security = logistic_table(sim, comparison="security")
    logit_security_n = logit_security.attrs["n"]
    logit_all.insert(0, "modelo", "Todas as ocupações")
    logit_security.insert(0, "modelo", "Segurança pública vs. privada")
    logit = pd.concat([logit_all, logit_security], ignore_index=True)

    # Comparação externa conservadora: efetivo RAIS/MTE citado pelo Atlas do Estado/Ipea.
    pm_bm_2017_n = int(public[(public["ano"] == 2017) & public["cbo_reconstruido"].isin(PM_CODES | BM_CODES)].shape[0])
    rais_2017_approx = 486_000
    rate_2017 = pm_bm_2017_n / rais_2017_approx * 100_000

    # Agregados publicáveis; sem datas, municípios ou combinações individuais.
    annual.to_csv(OUT / "serie_anual.csv", index=False)
    career_year.to_csv(OUT / "carreira_ano.csv", index=False)
    career_total.to_csv(OUT / "carreiras_total.csv", index=False)
    methods.to_csv(OUT / "metodos_carreira.csv", index=False)
    profile.to_csv(OUT / "perfil_agregado.csv", index=False)
    correction_by_code.to_csv(OUT / "correcao_por_cbo.csv", index=False)
    logit.to_csv(OUT / "modelos_logisticos.csv", index=False)

    stats = {
        "n_total_sim_suicidios": int(len(sim)),
        "n_cbo_valido_antes": int((~is_numeric & sim["cbo_valido"]).sum()),
        "n_cbo_recuperado": int(sim["codigo_recuperado"].sum()),
        "n_cbo_valido_depois": int(sim["cbo_valido"].sum()),
        "n_seguranca_publica": int(len(public)),
        "n_seguranca_publica_antes": int(len(public_before)),
        "n_seguranca_publica_recuperado": int(len(public_recovered)),
        "percentual_seg_recuperado": float(100 * len(public_recovered) / len(public)),
        "n_arma_fogo_seg": int(public["arma_fogo"].sum()),
        "percentual_arma_fogo_seg": float(100 * public["arma_fogo"].mean()),
        "n_homens_seg": int(public["SEXO"].eq("Masculino").sum()),
        "percentual_homens_seg": float(100 * public["SEXO"].eq("Masculino").mean()),
        "idade_mediana_seg": float(public["idade"].median()),
        "n_modelo_todas_ocupacoes": int(logit_all_n),
        "n_modelo_seguranca_publica_privada": int(logit_security_n),
        "pm_bm_2017_obitos": pm_bm_2017_n,
        "pm_bm_2017_denominador_rais_aprox": rais_2017_approx,
        "pm_bm_2017_taxa_100mil_aprox": rate_2017,
        "pm_pc_2019_sim_reconstruido": int(public[(public["ano"] == 2019) & public["cbo_reconstruido"].isin(PM_CODES | PC_CODES)].shape[0]),
        "pm_pc_2019_sim_sem_reconstrucao": int(public[(public["ano"] == 2019) & public["cbo_reconstruido"].isin(PM_CODES | PC_CODES) & ~public["codigo_recuperado"]].shape[0]),
        "pm_pc_2019_fbsp": 91,
    }
    for term in ["grupo_ocupacional: Segurança pública", "grupo_ocupacional: Segurança privada"]:
        row = logit_all.loc[logit_all["termo"].eq(term)].iloc[0]
        key = "publica" if "pública" in term else "privada"
        stats[f"or_arma_{key}"] = float(row["OR"])
        stats[f"or_arma_{key}_ic95"] = [float(row["IC95_inf"]), float(row["IC95_sup"])]
        stats[f"or_arma_{key}_p"] = float(row["p"])
    row = logit_security.loc[logit_security["termo"].eq("grupo_ocupacional: Segurança pública")].iloc[0]
    stats["or_arma_publica_vs_privada"] = float(row["OR"])
    stats["or_arma_publica_vs_privada_ic95"] = [float(row["IC95_inf"]), float(row["IC95_sup"])]
    stats["or_arma_publica_vs_privada_p"] = float(row["p"])
    (OUT / "estatisticas.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")

    plt.style.use("seaborn-v0_8-whitegrid")
    colors = {"Óbitos observados": "#1B4965", "Códigos recuperados": "#CA6702"}
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    ax.plot(annual["ano"], annual["obitos"], marker="o", linewidth=2.3, color=colors["Óbitos observados"], label="Óbitos após reconstrução")
    ax.plot(annual["ano"], annual["obitos"] - annual["recuperados"], marker="o", linewidth=2.0, color=colors["Códigos recuperados"], label="Casos reconhecidos sem reconstrução")
    ax.set(xlabel="Ano", ylabel="Número de óbitos")
    ax.set_xticks(annual["ano"])
    ax.legend(frameon=False, ncol=2, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG / "figura1_serie_correcao.png", dpi=300)
    plt.close(fig)

    order = career_total.sort_values("obitos")["carreira"]
    fig, ax = plt.subplots(figsize=(8.2, 4.9))
    plot = career_total.set_index("carreira").loc[order]
    ax.barh(plot.index, plot["obitos"], color="#1B4965")
    for y_idx, (label, row) in enumerate(plot.iterrows()):
        ax.text(row["obitos"] + 4, y_idx, f"{int(row['obitos'])}", va="center", fontsize=9)
    ax.set(xlabel="Óbitos, 2010–2019", ylabel="")
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    fig.savefig(FIG / "figura2_carreiras.png", dpi=300)
    plt.close(fig)

    pivot = methods.pivot(index="carreira", columns="metodo", values="percentual_na_carreira").fillna(0)
    preferred = ["Arma de fogo", "Enforcamento", "Autointoxicação", "Precipitação", "Outros meios"]
    pivot = pivot.reindex(columns=preferred, fill_value=0).loc[career_total.sort_values("percentual_arma_fogo", ascending=False)["carreira"]]
    palette = ["#AE2012", "#005F73", "#E9D8A6", "#94D2BD", "#6C757D"]
    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    left = np.zeros(len(pivot))
    for col, color in zip(pivot.columns, palette):
        ax.barh(pivot.index, pivot[col], left=left, label=col, color=color)
        left += pivot[col].to_numpy()
    ax.set(xlabel="Distribuição dos métodos (%)", ylabel="", xlim=(0, 100))
    ax.legend(frameon=False, ncol=3, loc="lower center", bbox_to_anchor=(0.5, -0.28))
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    fig.savefig(FIG / "figura3_metodos.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(json.dumps(stats, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

