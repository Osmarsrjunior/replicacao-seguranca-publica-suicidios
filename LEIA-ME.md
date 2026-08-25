# Pacote reprodutível — artigo 2

Este pacote acompanha o manuscrito **“Quem desaparece das estatísticas?”**. Ele reconstrói códigos da Classificação Brasileira de Ocupações (CBO) e reproduz tabelas, modelos e figuras sobre suicídios entre profissionais de segurança pública no Brasil, 2010–2019.

## Estrutura

- `codigo/01_analise_sim.py`: limpeza, reconstrução, agregações, modelos e figuras.
- `codigo/02_validacao.py`: testes de reconciliação dos resultados.
- `dados_brutos/CBO.csv`: dicionário oficial de códigos e ocupações usado na reconstrução.
- `dados_processados/`: tabelas agregadas e resultados dos modelos.
- `figuras/`: figuras em PNG a 300 dpi.
- `manuscrito.md`: versão-fonte do texto.
- `requirements.txt`: dependências Python.
- `MANIFESTO_SHA256.txt`: checksums da entrada externa e dos arquivos distribuídos.

## Obtenção da entrada do SIM

O script espera o arquivo `fontes/suicide_in_brazil/data/df.csv`, proveniente do repositório aberto:

https://github.com/GabrielReisR/suicide_in_brazil

O repositório documenta a extração original do SIM/DATASUS com PySUS. Para uma submissão definitiva, recomenda-se repetir a extração diretamente dos microdados oficiais e preservar `OCUP` como texto de seis posições. A base individual não é redistribuída neste suplemento.

## Execução

Na raiz do pacote:

```bash
python codigo/01_analise_sim.py
python codigo/02_validacao.py
```

O segundo comando deve terminar com `status: APROVADO`.

## Regra de reconstrução

A rotina auditada havia aplicado `rstrip('.0')` após converter o CBO numérico em texto. Essa função remove qualquer ponto ou zero terminal, não apenas a sequência literal `.0`. A reconstrução calcula, para cada um dos 2.428 códigos oficiais, a chave danificada equivalente. O mapeamento foi unívoco, sem colisões, e todos os 27.440 valores numéricos residuais encontraram correspondência.

## Privacidade e interpretação

As saídas compartilháveis são agregadas. Datas completas e municípios não são exportados. As razões de chances são caso-caso: comparam arma de fogo com outros métodos entre pessoas que morreram por suicídio. Elas não estimam risco, incidência ou efeito causal da ocupação.

## Licenças e atribuição

O repositório de origem de Reis (2021) utiliza licença MIT. Os dados do SIM e a CBO seguem as condições das fontes públicas brasileiras. Cite as fontes e o artigo ao reutilizar os resultados.

