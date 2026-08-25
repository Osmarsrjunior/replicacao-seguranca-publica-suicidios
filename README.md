# Quem desaparece das estatísticas?

Pacote de replicação do estudo sobre suicídios entre profissionais de segurança pública no Brasil, de 2010 a 2019. O código reconstrói códigos da Classificação Brasileira de Ocupações (CBO) e reproduz tabelas, modelos e figuras do manuscrito.

## Conteúdo do repositório

- `codigo/01_analise_sim.py`: limpeza, reconstrução da CBO, agregações, modelos e figuras;
- `codigo/02_validacao.py`: nove testes automáticos de reconciliação;
- `dados_brutos/CBO.csv`: dicionário público de códigos e ocupações;
- `dados_processados/`: resultados exclusivamente agregados;
- `figuras/`: figuras reproduzidas em PNG a 300 dpi;
- `manuscrito.md`: versão-fonte do artigo;
- `requirements-lock.txt`: versões exatas usadas na validação registrada;
- `MANIFESTO_SHA256.txt`: hashes para conferência de integridade.

## Requisitos

- Python 3.10 ou superior;
- acesso à internet somente para obter a fonte externa e instalar dependências.

Crie um ambiente isolado e instale as dependências:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --no-cache-dir -r requirements.txt
```

No Linux ou macOS:

```bash
source .venv/bin/activate
python -m pip install --no-cache-dir -r requirements.txt
```

## Obtenção da entrada do SIM

O arquivo individual não é distribuído neste repositório. Obtenha a fonte pública documentada por Reis (2021):

```bash
git clone --depth 1 https://github.com/GabrielReisR/suicide_in_brazil.git fontes/suicide_in_brazil
```

O script espera `fontes/suicide_in_brazil/data/df.csv`. Antes da execução, confira seu SHA-256 com o valor registrado no manifesto. Para uma replicação definitiva, recomenda-se repetir a extração nos microdados oficiais do SIM/DATASUS e preservar `OCUP` como texto de seis posições.

A validação registrada usou o commit `652a91eada46b9c812b25efdcb9c4e79ed92e9d0` da fonte externa.

## Reprodução e validação

Na raiz do projeto, execute:

```bash
python codigo/01_analise_sim.py
python codigo/02_validacao.py
```

A segunda etapa deve terminar com `"status": "APROVADO"`. A análise recria os arquivos de `dados_processados/` e `figuras/`.

## Regra de reconstrução

A rotina auditada originalmente aplicou `rstrip('.0')` após converter a CBO numérica em texto. Essa operação remove qualquer ponto ou zero terminal, não apenas a sequência literal `.0`. O script calcula, para cada código oficial, a chave danificada equivalente e inverte o mapeamento somente se ele for unívoco.

## Privacidade e interpretação

Este repositório contém apenas resultados agregados. A base externa individual, datas completas e municípios são excluídos pelo `.gitignore`. Algumas tabelas apresentam células ocupacionais pequenas, mas não contêm nomes, datas, municípios ou registros individuais.

As razões de chances são caso-caso: comparam arma de fogo com outros métodos entre pessoas que morreram por suicídio. Elas não estimam risco, incidência nem efeito causal da ocupação.

## Fontes e atribuição

- Reis, G. (2021). *Suicídios no Brasil entre 2010 e 2019: base e código aberto*. [Repositório de origem](https://github.com/GabrielReisR/suicide_in_brazil).
- Sistema de Informações sobre Mortalidade (SIM/DATASUS).
- Classificação Brasileira de Ocupações (CBO).

O repositório de origem está sob licença MIT. A reutilização dos dados públicos permanece sujeita às condições das fontes oficiais. A licença do código específico deste pacote deve ser definida pelos autores antes de tornar o repositório público.

