# Quem desaparece das estatísticas?

## Reconstrução de códigos ocupacionais e métodos de suicídio entre profissionais de segurança pública no Brasil, 2010–2019

**Título curto:** Suicídio e reconstrução ocupacional na segurança pública  
**Autores:** [INSERIR NOMES]  
**Afiliações:** [INSERIR AFILIAÇÕES]  
**Autor correspondente:** [INSERIR NOME, E-MAIL E ORCID]  
**Contagem aproximada:** 4.900 palavras no texto principal; 2 tabelas; 3 figuras; material suplementar.

## Resumo

**Objetivo.** Avaliar quanto uma transformação inadequada dos códigos da Classificação Brasileira de Ocupações (CBO) altera a identificação de suicídios entre profissionais de segurança pública e examinar a escolha do método nesse grupo.

**Métodos.** Estudo retrospectivo nacional de 112.491 óbitos por lesão autoprovocada intencional (CID-10 X60–X84) registrados no Sistema de Informações sobre Mortalidade entre 2010 e 2019. Auditou-se uma base aberta derivada do SIM na qual a remoção de sufixos decimais também eliminou zeros terminais de códigos CBO. Foi construído um dicionário reverso com 2.428 códigos oficiais; a chave danificada permaneceu unívoca e permitiu reconstruir todos os 27.440 valores numéricos residuais. Segurança pública foi definida a priori por 27 CBOs, separadamente da segurança privada. Os desfechos foram completude ocupacional, número de casos identificados e método de suicídio. Regressões logísticas caso-caso estimaram as chances de uso de arma de fogo, ajustadas por sexo, idade, raça/cor, situação conjugal, região e ano.

**Resultados.** A proporção de registros com CBO reconhecida passou de 53,6% para 78,0%. Na segurança pública, os casos identificados aumentaram de 432 para 1.070 (+147,7%); 638 (59,6%) dependiam da reconstrução. Homens representaram 94,0% dos casos; a idade mediana foi 41 anos (IIQ 33–50). Armas de fogo responderam por 62,0% dos óbitos. Entre pessoas que morreram por suicídio, a ocupação em segurança pública associou-se a maiores chances ajustadas de método por arma de fogo em comparação com outras ocupações (OR=18,57; IC95% 16,05–21,47) e com a segurança privada (OR=6,44; IC95% 5,23–7,91). Em 2019, a reconstrução identificou 90 casos em policiais militares e civis, frente a 91 informados por fonte administrativa independente; sem a correção, seriam 30.

**Conclusão.** Decisões aparentemente triviais de limpeza podem produzir grande subidentificação ocupacional e distorcer comparações entre carreiras. A associação com armas de fogo descreve escolha do método entre óbitos, não risco de suicídio. A vigilância deve preservar códigos CBO, separar segurança pública e privada e integrar prevenção organizacional a protocolos confidenciais de segurança dos meios letais.

**Palavras-chave:** suicídio; profissionais de segurança pública; sistemas de informação em saúde; ocupações; armas de fogo; qualidade de dados.

## Abstract

**Objective.** To assess how an inappropriate transformation of Brazilian Classification of Occupations (CBO) codes changes the ascertainment of suicide deaths among public safety workers and to examine suicide method choice in this group.

**Methods.** Nationwide retrospective study of 112,491 intentional self-harm deaths (ICD-10 X60–X84) recorded in Brazil’s Mortality Information System from 2010 to 2019. We audited an open SIM-derived dataset in which stripping decimal suffixes also removed terminal zeros from CBO codes. A reverse dictionary based on 2,428 official codes was built; the damaged key was one-to-one and reconstructed all 27,440 residual numeric values. Public safety was defined a priori using 27 CBO codes and kept separate from private security. Outcomes were occupational-data completeness, identified case counts, and suicide method. Case-case logistic regression estimated the odds of firearm use, adjusted for sex, age, race/skin color, marital status, region, and year.

**Results.** Records with a recognized CBO increased from 53.6% to 78.0%. Public safety cases increased from 432 to 1,070 (+147.7%); 638 (59.6%) depended on reconstruction. Men accounted for 94.0% of cases, and median age was 41 years (IQR 33–50). Firearms accounted for 62.0% of deaths. Among suicide decedents, public safety occupation was associated with higher adjusted odds of firearm use compared with other occupations (OR=18.57; 95%CI 16.05–21.47) and private security (OR=6.44; 95%CI 5.23–7.91). In 2019, reconstruction identified 90 military and civil police cases, compared with 91 reported by an independent administrative source; without correction, only 30 would have been recognized.

**Conclusion.** Seemingly minor data-cleaning decisions can lead to substantial occupational under-ascertainment and distort comparisons across careers. The firearm association concerns method choice among deaths and must not be interpreted as suicide risk. Surveillance should preserve CBO codes, distinguish public from private security, and combine organizational prevention with confidential lethal-means safety protocols.

**Keywords:** suicide; public safety personnel; health information systems; occupations; firearms; data quality.

## Introdução

O suicídio entre profissionais de segurança pública ocupa uma posição paradoxal no debate brasileiro. As instituições dispõem de registros administrativos, serviços de saúde ocupacional e mecanismos disciplinares, mas a produção nacional permanece fragmentada entre corporações, unidades federativas e definições distintas de quem integra a segurança pública. A consequência é uma agenda em que a gravidade do fenômeno é reconhecida, enquanto sua magnitude e sua distribuição entre carreiras continuam vulneráveis a problemas de comparabilidade.

Há razões substantivas para investigar esse grupo. Policiais, bombeiros, guardas municipais e profissionais do sistema penal estão expostos a violência, morte, trabalho em turnos, escrutínio público, conflito entre demandas operacionais e recursos, além de estressores organizacionais como baixo apoio, práticas disciplinares percebidas como injustas e reduzida autonomia (Minayo, Assis & Oliveira, 2011; Souza et al., 2012; Krishnan et al., 2022; Cruz et al., 2026). O acesso e a familiaridade com armas acrescentam uma dimensão preventiva específica. Estudos internacionais mostram que ocupações com acesso cotidiano a meios letais tendem a utilizar esses meios com maior frequência em suicídios, embora isso não dispense explicações organizacionais, sociais e clínicas (Barber & Miller, 2014; Milner et al., 2017).

A literatura brasileira produziu contribuições relevantes, mas com recortes predominantemente locais ou corporativos. Uma coorte de policiais militares do Rio Grande do Sul encontrou maior incidência entre praças e profissionais mais jovens; um estudo documental em Santa Catarina descreveu concentração dos casos na base hierárquica; e autópsias psicossociais no Espírito Santo destacaram a interação entre fatores operacionais, organizacionais e relacionais (Gomes, Araújo & Gomes, 2018; Pereira, Madruga & Kawahala, 2020; Cruz et al., 2026). Esses desenhos aprofundam mecanismos, porém não oferecem classificação nacional uniforme das diferentes carreiras.

Em escala nacional, Palma et al. (2024) analisaram suicídio e ocupação no Brasil e encontraram, para 2019, uma taxa bruta de 20,4 por 100 mil em um agrupamento de “forças de segurança”. O grupo, entretanto, reuniu policiais, bombeiros e agentes carcerários com vigias e guardas, combinando segurança pública e privada. Essa opção é compreensível diante das limitações dos dados, mas dificulta atribuir o padrão observado às instituições públicas, ao acesso ocupacional a armas ou às condições da vigilância privada. O mesmo estudo informou que 27,4% dos registros ocupacionais não puderam ser reconhecidos, lembrando que conclusões sobre ocupação dependem tanto do preenchimento da Declaração de Óbito quanto das rotinas de processamento posteriores.

Essa dependência é particularmente importante na CBO. Seus códigos têm seis posições e vários cargos centrais da segurança pública terminam em zero: soldado da Polícia Militar (021210), sargento da Polícia Militar (021110), investigador de polícia (351810) e policial rodoviário federal (517210), por exemplo. Em ambientes de análise, códigos lidos como números podem perder o zero inicial; se uma rotina destinada a retirar a terminação decimal “.0” usar uma operação que remove qualquer ponto ou zero no final da cadeia, também apaga zeros que pertencem ao código. O resultado não é ausência no SIM, mas invisibilidade criada na transformação analítica.

Estudos de qualidade do SIM concentram-se, com razão, em cobertura, completude e definição da causa básica (Messias et al., 2016; Costa et al., 2020). Menos atenção é dedicada à integridade semântica de variáveis ocupacionais durante a limpeza e ao efeito desse problema sobre grupos pequenos, mas politicamente relevantes. Uma perda distribuída de modo não aleatório — determinada pela forma do código — pode alterar a composição hierárquica, institucional e regional dos casos mesmo quando o número total de óbitos permanece inalterado.

Este estudo preenche essa lacuna por meio de uma auditoria reprodutível seguida de análise epidemiológica caso-caso. Os objetivos foram: (1) reconstruir códigos CBO danificados em uma base aberta derivada do SIM; (2) quantificar a mudança na identificação de suicídios entre profissionais de segurança pública; (3) descrever a distribuição dos casos por carreira, características sociodemográficas e método; (4) estimar se a ocupação em segurança pública se associa à utilização de arma de fogo entre pessoas que morreram por suicídio; e (5) avaliar a validade convergente da reconstrução contra uma fonte administrativa independente. A hipótese principal foi que a perda de zeros terminais produziria subidentificação desproporcional de policiais militares e civis e que, entre os óbitos por suicídio, profissionais de segurança pública apresentariam maior participação de armas de fogo do que outras ocupações, inclusive a segurança privada.

## Métodos

### Desenho, universo e período

Foi realizado estudo retrospectivo nacional de mortalidade com componente de auditoria de dados. O universo incluiu todos os 112.491 registros de óbito por lesão autoprovocada intencional (CID-10 X60–X84) disponíveis na base analisada para o Brasil entre 1º de janeiro de 2010 e 31 de dezembro de 2019. O período foi escolhido por constituir série contínua anterior à pandemia de COVID-19 e por coincidir com a base aberta cuja cadeia de transformação pôde ser integralmente auditada.

### Fonte e proveniência dos dados

Os registros originam-se do Sistema de Informações sobre Mortalidade (SIM), do Ministério da Saúde. Utilizou-se a base aberta organizada por Reis (2021), extraída do DATASUS com PySUS e acompanhada do código original de obtenção e pré-processamento. Essa opção permitiu auditar não apenas o resultado, mas a operação exata que transformou a variável ocupacional. O SIM registra a ocupação habitual informada na Declaração de Óbito; portanto, o campo não comprova vínculo ativo na data da morte. A Classificação Brasileira de Ocupações foi obtida da tabela oficial do Ministério do Trabalho e Emprego.

O arquivo original e todos os produtos analíticos foram preservados separadamente. O conjunto compartilhável deste estudo contém apenas agregados; datas completas e municípios não foram exportados, reduzindo a possibilidade de reidentificação em combinações ocupacionais raras.

### Auditoria e reconstrução dos códigos CBO

A rotina auditada converteu a variável CBO para texto e aplicou `rstrip('.0')`. Nessa linguagem, a função não remove a sequência literal “.0”; ela retira, repetidamente, qualquer caractere pertencente ao conjunto {ponto, zero} no final da cadeia. Assim, o código 021210, previamente lido como 21210.0, tornou-se 2121.

Para reconstrução, todos os 2.428 códigos oficiais foram padronizados em seis posições. Para cada código c, gerou-se a chave que seria produzida pela rotina danificada: conversão para inteiro, remoção dos zeros terminais e conversão para texto. Verificou-se a ausência de colisões: cada chave danificada correspondia a um único código oficial. Todos os 27.440 valores numéricos residuais encontrados no banco tiveram correspondência exata. Registros já convertidos em rótulos ocupacionais foram mapeados de volta ao código oficial. Não houve imputação probabilística nem uso de características pessoais para inferir ocupação.

Foram calculados quatro indicadores de auditoria: proporção de CBO reconhecida antes e depois da reconstrução; número absoluto de códigos recuperados; mudança relativa no número de casos de segurança pública; e proporção recuperada em cada carreira. O termo “recuperado” designa restauração determinística de um código presente antes da transformação, e não correção do preenchimento original da Declaração de Óbito.

### Definição de segurança pública e grupos comparadores

O recorte foi especificado antes das análises de desfecho e incluiu 27 códigos CBO, organizados em seis carreiras: Polícia Militar; Polícia Civil e perícia; Polícia Federal e Polícia Rodoviária Federal; Corpo de Bombeiros Militar; polícia penal/agente de segurança penitenciária; e guarda civil municipal. A relação completa consta no Quadro Suplementar S1.

Segurança privada foi mantida como grupo distinto e incluiu agente de proteção de aeroporto, agente de segurança, vigia florestal, vigia portuário, vigilante e vigia (CBO 517305, 517310, 517320, 517325, 517330 e 517420). Porteiros foram excluídos. As demais CBOs reconhecidas formaram “outras ocupações”. Forças Armadas não foram classificadas como segurança pública.

Essa separação responde a uma fonte de heterogeneidade conceitual: uso de uniforme, vigilância patrimonial ou presença de risco ocupacional não tornam segurança privada e segurança pública exposições equivalentes. As instituições diferem quanto ao mandato legal, seleção, disciplina, disponibilidade de armamento, assistência ocupacional e organização do trabalho.

### Variáveis e desfechos

O primeiro desfecho foi a identificação ocupacional: CBO reconhecida e pertencimento ao recorte de segurança pública antes e depois da reconstrução. O segundo foi o método de suicídio, classificado pela causa básica: arma de fogo (X72–X74), enforcamento (X70), autointoxicação (X60–X69), precipitação de lugar elevado (X80) e outros meios (demais X60–X84).

Foram descritos sexo, idade, raça/cor, situação conjugal, escolaridade, região de residência e local de ocorrência. Idade foi calculada a partir das datas de nascimento e óbito e agrupada em 18–29, 30–39, 40–49, 50–59, 60–69 e 70 anos ou mais. Valores impossíveis foram tratados como ausentes. Raça/cor foi mantida nas categorias do SIM na descrição e dicotomizada em preta/parda versus outra/ignorada apenas no modelo ajustado. Situação conjugal foi dicotomizada em com união (casado ou união consensual) versus sem união/ignorada.

### Análise estatística

Frequências absolutas e percentuais foram calculados para o período e por ano. A diferença entre 2010 e 2019 foi descrita como variação de contagem, não de risco, porque não havia denominadores anuais compatíveis para todas as carreiras. Percentuais de método foram estimados por carreira; células pequenas foram interpretadas com cautela.

Para examinar a escolha do método, foram ajustados modelos logísticos caso-caso entre pessoas de 18 a 69 anos com CBO reconhecida. O desfecho foi uso de arma de fogo (sim/não). O modelo principal comparou segurança pública e segurança privada com outras ocupações, ajustando por sexo, faixa etária, raça/cor, situação conjugal, região e ano linear. Um segundo modelo foi restrito às seguranças pública e privada, tendo a privada como referência. Foram estimadas razões de chances (odds ratios, OR) com intervalos de 95% de confiança e erros-padrão robustos HC1.

O desenho caso-caso foi deliberado. As ORs estimam a chance relativa de arma de fogo em comparação com outros métodos entre pessoas que já morreram por suicídio. Elas não estimam incidência de suicídio, risco de morrer, efeito causal do trabalho ou efeito causal do acesso à arma. Essa distinção foi mantida na redação e nos materiais gráficos.

### Análises de validade e sensibilidade

A validade convergente foi avaliada comparando a contagem de policiais militares e civis do SIM reconstruído em 2019 com o total de suicídios de policiais da ativa publicado pelo 14º Anuário Brasileiro de Segurança Pública. Não se esperava igualdade necessária: a fonte administrativa restringe-se à ativa, enquanto o SIM registra ocupação habitual. Ainda assim, aproximação substancial seria incompatível com a hipótese de reconstrução arbitrária.

Como análise secundária, calculou-se uma taxa aproximada para policiais e bombeiros militares em 2017 usando o efetivo de aproximadamente 486 mil vínculos da RAIS/MTE publicado pelo Atlas do Estado Brasileiro. Essa estimativa foi mantida fora do desfecho principal porque o numerador do SIM pode incluir pessoa sem vínculo ativo e o denominador mede vínculos, não indivíduos. Sua função é oferecer ordem de grandeza, não estimativa definitiva de risco.

### Aspectos éticos e reprodutibilidade

Foram usados dados públicos, desidentificados e sem ligação individual com outras bases. Não houve contato com participantes. Os autores deverão confirmar, antes da submissão, a exigência do comitê de ética da instituição responsável e inserir a declaração correspondente. Código, dicionário de CBO, tabelas agregadas e registro das decisões analíticas acompanham o manuscrito. A análise foi executada em Python; a regressão logística foi implementada por máxima verossimilhança com matriz de variância robusta e verificada por reconciliação dos totais.

## Resultados

### Efeito da reconstrução sobre a identificação ocupacional

Antes da reconstrução, 60.274 dos 112.491 registros (53,6%) tinham CBO reconhecida na base aberta. A restauração determinística recuperou 27.440 códigos e elevou a completude analítica para 87.714 (78,0%). Não houve colisão entre chaves danificadas nem valores numéricos residuais sem correspondência na lista oficial.

O efeito foi maior na segurança pública. O recorte continha 432 casos reconhecidos sem a correção e 1.070 após a reconstrução, aumento de 638 casos ou 147,7%. Em outras palavras, 59,6% do conjunto final dependia da restauração dos zeros terminais. A série corrigida variou de 78 casos em 2010 a 132 em 2019, com máximo de 146 em 2018. A diferença entre o primeiro e o último ano foi de 69,2% nas contagens, sem interpretação como crescimento da taxa.

[[FIGURA 1]]

O padrão de perda não foi uniforme. A reconstrução respondeu por 72,9% dos casos da Polícia Militar e 71,1% dos casos da Polícia Civil e perícia. Todos os 408 registros de soldado da Polícia Militar, 87 de investigador de polícia, 44 de policial rodoviário federal e 39 de sargento da Polícia Militar haviam permanecido como valores numéricos não rotulados. Em contraste, guarda civil municipal e agente de segurança penitenciária, cujos códigos não terminam em zero, não tiveram casos recuperados pela rotina.

### Distribuição por carreira e perfil dos casos

A Polícia Militar concentrou 619 casos (57,9%), seguida por Polícia Civil e perícia (n=152; 14,2%), polícia penal/penitenciária (n=88; 8,2%), guarda civil municipal (n=80; 7,5%), Polícia Federal/PRF (n=68; 6,4%) e bombeiros militares (n=63; 5,9%). Soldados da Polícia Militar foram a ocupação individual mais frequente (n=408), seguidos por cabos (n=143), agentes de segurança penitenciária (n=88) e investigadores de polícia (n=87).

[[FIGURA 2]]

Homens representaram 1.006 casos (94,0%) e mulheres, 64 (6,0%). A idade estava disponível para 956 registros; a mediana foi 41 anos (IIQ 33–50). As faixas de 40–49 anos (26,3% do total) e 30–39 anos (25,2%) foram as mais frequentes. Pessoas brancas corresponderam a 58,5%, pardas a 34,5% e pretas a 4,4%; 2,1% tinham raça/cor ignorada. Casados representaram 47,5%, solteiros 30,7% e separados judicialmente 10,0%. Aproximadamente 44,0% tinham oito a onze anos de estudo e 32,4%, doze anos ou mais; escolaridade estava ausente em 15,0%. O Sudeste concentrou 43,2% dos casos e o Sul, 20,1%. O domicílio foi o local de ocorrência em 53,6%.

**Tabela 1. Casos identificados, recuperação do CBO e método por carreira, Brasil, 2010–2019**

| Carreira | Óbitos, n | Recuperados, n (%) | Arma de fogo, n (%) |
|---|---:|---:|---:|
| Polícia Militar | 619 | 451 (72,9) | 404 (65,3) |
| Polícia Civil e perícia | 152 | 108 (71,1) | 98 (64,5) |
| Polícia penal/penitenciária | 88 | 0 (0,0) | 49 (55,7) |
| Guarda civil municipal | 80 | 0 (0,0) | 41 (51,3) |
| Polícia Federal e PRF | 68 | 44 (64,7) | 50 (73,5) |
| Bombeiro Militar | 63 | 35 (55,6) | 21 (33,3) |
| **Total** | **1.070** | **638 (59,6)** | **663 (62,0)** |

Fonte: elaboração própria com dados do SIM/DATASUS e CBO/MTE. “Recuperado” indica código restaurado após dano na rotina de transformação, não correção do registro original.

### Método de suicídio

Armas de fogo foram o método mais frequente no conjunto da segurança pública (n=663; 62,0%), seguidas por enforcamento (n=292; 27,3%), outros meios (n=69; 6,4%), autointoxicação (n=29; 2,7%) e precipitação (n=17; 1,6%). As categorias foram mutuamente exclusivas e totalizaram 1.070 registros.

As proporções diferiram entre carreiras. Arma de fogo respondeu por 73,5% dos óbitos na Polícia Federal/PRF, 65,3% na Polícia Militar, 64,5% na Polícia Civil/perícia, 55,7% na polícia penal, 51,3% nas guardas municipais e 33,3% entre bombeiros militares. Entre bombeiros, o enforcamento foi mais frequente (50,8%). Dado o número limitado de casos em algumas carreiras, essas diferenças foram tratadas como descritivas.

[[FIGURA 3]]

Entre registros com CBO reconhecida, a participação de armas de fogo foi 7,7% nas demais ocupações, 19,9% na segurança privada e 62,0% na segurança pública. No modelo ajustado com 68.381 óbitos de pessoas de 18 a 69 anos, segurança pública associou-se a OR de 18,57 (IC95% 16,05–21,47) para arma de fogo versus outros métodos, comparada às demais ocupações. Para segurança privada, a OR foi 2,94 (IC95% 2,54–3,40). No modelo restrito aos dois setores de segurança (n=2.096), a OR da segurança pública em relação à privada foi 6,44 (IC95% 5,23–7,91). Todos os três contrastes tiveram p<0,001.

**Tabela 2. Associação ajustada entre grupo ocupacional e método por arma de fogo entre óbitos por suicídio, Brasil, 2010–2019**

| Comparação | N do modelo | OR ajustada | IC95% | p |
|---|---:|---:|---:|---:|
| Segurança pública vs. outras ocupações | 68.381 | 18,57 | 16,05–21,47 | <0,001 |
| Segurança privada vs. outras ocupações | 68.381 | 2,94 | 2,54–3,40 | <0,001 |
| Segurança pública vs. segurança privada | 2.096 | 6,44 | 5,23–7,91 | <0,001 |

Modelos ajustados por sexo, faixa etária, raça/cor, situação conjugal, região e ano. ORs referem-se à chance de arma de fogo versus outros métodos entre pessoas que morreram por suicídio; não estimam risco ou incidência de suicídio.

### Validação externa e análise secundária de taxa

Em 2019, o SIM reconstruído identificou 90 casos classificados como Polícia Militar ou Polícia Civil/perícia. O 14º Anuário Brasileiro de Segurança Pública informou 91 suicídios de policiais militares e civis da ativa. Sem a reconstrução, a base aberta reconheceria 30 casos nesses grupos. A diferença de uma unidade entre fontes após a correção é consistente com validade convergente, embora não elimine diferenças de cobertura e definição.

Para 2017, houve 80 óbitos classificados como policiais ou bombeiros militares. Usando o denominador arredondado de 486 mil vínculos informado pelo Atlas do Estado Brasileiro com base na RAIS, a taxa aproximada foi 16,5 por 100 mil. A estimativa deve ser lida apenas como análise de ordem de grandeza, pois combina ocupação habitual no numerador com vínculos ativos no denominador.

## Discussão

### Principais achados

O estudo apresenta três resultados centrais. Primeiro, um erro de transformação simples e determinístico reduziu de modo expressivo a identificação de ocupações na base aberta e atingiu desproporcionalmente carreiras cujos códigos terminam em zero. Na segurança pública, quase seis em cada dez casos finais dependiam da reconstrução; soldados, investigadores, sargentos e policiais rodoviários federais estavam entre os grupos mais afetados. Segundo, a classificação estrita mostrou que armas de fogo foram usadas em 62,0% dos suicídios, com diferenças entre carreiras. Terceiro, entre pessoas que morreram por suicídio, profissionais de segurança pública tiveram chances muito superiores de utilização de arma de fogo mesmo em comparação com a segurança privada e após ajuste sociodemográfico.

Esses achados deslocam a lacuna da literatura. A pergunta não é apenas “qual a taxa de suicídio policial?”, frequentemente respondida com séries corporativas incompletas ou denominadores incompatíveis. É também “quem permanece classificável depois que o registro percorre as rotinas de extração, limpeza e agrupamento?” e “o que se perde quando segurança pública e segurança privada são tratadas como uma única categoria?”. A qualidade inferencial começa antes do modelo estatístico.

### Integridade do código como problema epidemiológico

O dano observado não estava na causa básica nem implicava que o SIM tivesse apagado ocupações. Ele surgiu na camada analítica aberta, durante a conversão do CBO. Essa distinção é crucial para evitar atribuir ao sistema oficial uma falha de software externo. Ao mesmo tempo, o caso demonstra por que reprodutibilidade não equivale automaticamente a validade: uma transformação integralmente documentada pode reproduzir com precisão um erro.

A perda foi informativa, não aleatória. Códigos terminados em zero foram afetados; códigos terminados em cinco, comuns na mesma família ocupacional, foram preservados. Na Polícia Militar, isso favorecia cabos (021205) e apagava soldados (021210); na Polícia Civil, preservava delegados (242305) e papiloscopistas (351815), mas apagava investigadores (351810) e escrivães (351420). Uma análise não auditada produziria uma força de segurança artificialmente mais graduada e com composição institucional distorcida.

A restauração foi possível porque a chave danificada era unívoca no universo da CBO. Essa propriedade não deve ser presumida em outras classificações ou versões. O procedimento recomendável é conservar a variável original como texto de seis posições, retirar apenas uma terminação decimal literal com expressão ancorada e validar o resultado contra o dicionário oficial. Registros que não mapeiem devem ser inspecionados, nunca silenciosamente convertidos em ausência.

A aproximação entre 90 casos de policiais militares e civis no SIM reconstruído e 91 no registro administrativo de 2019 oferece evidência convergente particularmente relevante. Sem a correção, apenas um terço do total administrativo seria reconhecido. A comparação não transforma o Anuário em padrão-ouro: o escopo de atividade e a ocupação habitual diferem. Ainda assim, a melhora abrupta da concordância após uma regra determinística e semanticamente justificável torna improvável que os códigos recuperados sejam meros falsos positivos.

### Armas de fogo e escolha do método

A literatura internacional associa disponibilidade, familiaridade e conhecimento técnico à escolha de meios letais (Barber & Miller, 2014; Milner et al., 2017). O padrão brasileiro é compatível com esse mecanismo: a proporção de arma de fogo foi aproximadamente oito vezes a observada em outras ocupações reconhecidas e três vezes a da segurança privada. Após ajuste, o contraste permaneceu grande, inclusive entre os dois setores de segurança.

Essa associação não autoriza concluir que armas “causaram” os suicídios nem que o risco global é 18 vezes maior. O desenho condiciona a análise ao óbito por suicídio. A OR de 18,57 responde: entre pessoas de características observadas semelhantes que morreram por suicídio, quão diferentes foram as chances de o método ser arma de fogo na segurança pública em relação a outras ocupações? Ela não compara quem morreu com quem permaneceu vivo. Confundir esses estimandos produziria grave exagero.

Mesmo com essa cautela, a escolha do método é relevante porque meios variam em letalidade e oportunidade de resgate. A segurança dos meios letais constitui uma estratégia baseada em criar tempo e distância durante crises, sem reduzir prevenção a uma decisão disciplinar ou estigmatizante. Para profissionais armados, protocolos precisam conciliar dever funcional, confidencialidade clínica, avaliação individual e proteção de direitos. Afastamento automático, perda irreversível de função ou comunicação indiscriminada à cadeia de comando pode desestimular a procura por cuidado.

Os resultados sugerem uma arquitetura em camadas: acesso confidencial e independente a saúde mental; planos de segurança construídos com o profissional; armazenamento seguro fora do serviço; possibilidade de custódia temporária voluntária por pessoa autorizada; critérios clínicos claros e revisáveis para restrição excepcional; acompanhamento após crises, afastamentos e retorno ao trabalho; e revisão de incidentes sem finalidade punitiva. Medidas sobre armas devem complementar — não substituir — intervenções sobre jornada, assédio, justiça organizacional, endividamento, exposição a eventos críticos e apoio entre pares.

### Heterogeneidade entre carreiras

Separar carreiras revelou padrões que um agregado amplo esconderia. A participação de arma de fogo foi maior na Polícia Federal/PRF, Polícia Militar e Polícia Civil/perícia e menor entre bombeiros. Parte da diferença pode refletir disponibilidade funcional, porte fora de serviço e treinamento; parte pode decorrer de sexo, idade, região, tamanho amostral ou erro de classificação. Como não havia denominadores específicos por carreira e ano, não se deve ordenar “risco” a partir dessas proporções.

O predomínio de praças no número absoluto também requer cautela. Soldados e cabos formam parcela grande dos efetivos policiais militares; contagens maiores não demonstram por si sós desigualdade de incidência. Estudos corporativos brasileiros encontraram associações com menor posto hierárquico, mas dispuseram de denominadores ou arquivos de pessoal que este estudo não possui (Gomes, Araújo & Gomes, 2018; Pereira, Madruga & Kawahala, 2020). A contribuição nacional aqui é identificar e descrever corretamente os casos, criando base para futura ligação segura com registros de efetivo.

### Implicações para vigilância e política institucional

Três mudanças são imediatamente aplicáveis. A primeira é técnica: variáveis de classificação devem ser tratadas como identificadores, não números; zeros iniciais e terminais fazem parte do dado. Scripts de produção precisam incluir testes unitários com códigos sentinela, relatório de valores não mapeados e reconciliação com totais externos.

A segunda é conceitual: estudos e painéis devem publicar definições explícitas. “Forças de segurança”, “profissionais de segurança”, “policiais” e “trabalhadores da vigilância” não são sinônimos. Resultados devem separar, no mínimo, segurança pública, segurança privada e Forças Armadas; dentro da primeira, distinguir corporações quando o tamanho das células permitir.

A terceira é institucional: o monitoramento de suicídio precisa integrar saúde e gestão sem transformar cuidado em investigação disciplinar. Indicadores mínimos incluem óbitos e tentativas por corporação, sexo, faixa etária, posto/cargo, situação funcional, método e circunstâncias de trabalho; cobertura e qualidade do campo ocupação; tempo até atendimento; continuidade do cuidado após afastamento; e ações de posvenção. Pequenos números exigem agregação temporal e regras de supressão para proteger famílias e equipes.

### Pontos fortes e limitações

Entre os pontos fortes estão a abrangência nacional de dez anos, a definição estrita e transparente das carreiras, a separação da segurança privada, a auditoria reproduzível do pipeline, a reconstrução sem ambiguidade e a validação contra fonte independente. O estudo também explicita o estimando caso-caso e evita converter associação de método em risco de suicídio.

As limitações são importantes. Primeiro, a base é derivada do SIM por uma cadeia aberta de terceiros; embora sua extração seja auditável e os totais nacionais sejam compatíveis, a reprodução ideal deve ser repetida diretamente nos arquivos oficiais. Segundo, ocupação habitual não equivale a vínculo ativo. Aposentados, afastados ou pessoas que mudaram de carreira podem ser classificados pelo trabalho anterior. Terceiro, 22,0% dos registros permaneceram sem CBO após a reconstrução porque já não continham código ocupacional válido; a recuperação corrige o dano da transformação, não a ausência na fonte.

Quarto, não havia denominadores anuais consistentes para todas as carreiras, sexo, idade e região. Por isso, o artigo não estima incidência comparativa nem tendência de risco. A taxa de 2017 é apenas sensibilidade com incompatibilidade entre ocupação habitual e vínculo. Quinto, os modelos não incluem posto, situação funcional, posse pessoal de arma, diagnóstico, eventos críticos, jornada, endividamento ou apoio organizacional. A associação residual não identifica mecanismo causal. Sexto, as categorias raça/cor e situação conjugal contêm valores ausentes e foram simplificadas no ajuste. Finalmente, pequenos números em algumas carreiras ampliam a incerteza das proporções descritivas.

Essas limitações orientam o próximo estudo: ligação probabilística ou determinística, em ambiente seguro, entre SIM e registros anonimizados de efetivo/RAIS, com pessoa-tempo, situação funcional e denominadores estratificados. Tal desenho permitiria taxas padronizadas, modelos de contagem e comparação entre carreiras sem depender da ocupação habitual como proxy de emprego atual.

## Conclusão

Uma operação de limpeza destinada a retirar “.0” eliminou zeros que pertenciam aos códigos ocupacionais e tornou invisível a maior parte dos suicídios identificáveis na segurança pública de uma base aberta nacional. A reconstrução elevou os casos de 432 para 1.070 e aproximou o total de policiais militares e civis de 2019 de uma fonte administrativa independente. Depois da correção, armas de fogo responderam por 62,0% dos óbitos e apresentaram forte associação com a segurança pública entre pessoas que morreram por suicídio, inclusive em relação à segurança privada.

O achado tem dupla implicação. Para a ciência, códigos ocupacionais devem ser preservados, validados e acompanhados de definições explícitas; taxas não devem ser calculadas quando numerador e denominador representam populações diferentes. Para a prevenção, segurança dos meios letais deve integrar uma política mais ampla de cuidado confidencial, justiça organizacional, redução de estressores e continuidade assistencial. Melhorar a saúde mental dos agentes começa também por impedir que eles desapareçam dos dados usados para formular as políticas.

## Declarações

**Aprovação ética:** [INSERIR DECLARAÇÃO DA INSTITUIÇÃO/CEP ANTES DA SUBMISSÃO]. Foram utilizados dados públicos e desidentificados, sem contato com participantes ou ligação individual entre bases.

**Financiamento:** [INSERIR “Não houve financiamento” OU AGÊNCIA E PROCESSO].

**Conflitos de interesse:** [INSERIR DECLARAÇÃO].

**Contribuições dos autores (CRediT):** [INSERIR INICIAIS] — conceituação, metodologia, análise formal, curadoria de dados, redação da versão inicial, revisão e edição, visualização e supervisão.

**Disponibilidade de dados e código:** O pacote suplementar contém scripts, dicionário de códigos, agregados analíticos e instruções para reconstrução a partir da base pública. Dados individuais do SIM devem ser obtidos em fonte oficial ou no repositório de origem; o pacote não redistribui datas completas nem municípios.

**Uso de inteligência artificial:** [ADEQUAR À POLÍTICA DO PERIÓDICO]. Ferramentas de IA foram utilizadas para apoio à organização textual e programação. A responsabilidade por análise, interpretação, verificação das fontes e versão submetida é integralmente dos autores.

## Referências

1. Violanti JM, Owens SL, McCanlies E, Fekedulegn D, Andrew ME. Law enforcement suicide: a review. *Policing: An International Journal*. 2019;42(2):141–164. doi:10.1108/PIJPSM-05-2017-0061.

2. Barber CW, Miller MJ. Reducing a suicidal person’s access to lethal means of suicide: a research agenda. *Am J Prev Med*. 2014;47(3 Suppl 2):S264–S272. doi:10.1016/j.amepre.2014.05.028.

3. Brasil. Lei nº 13.819, de 26 de abril de 2019. Institui a Política Nacional de Prevenção da Automutilação e do Suicídio. Brasília: Presidência da República; 2019.

4. Costa LFL, de Mesquita Silva Montenegro M, Rabello Neto DL, et al. Estimating completeness of national and subnational death reporting in Brazil: application of record linkage methods. *Popul Health Metr*. 2020;18:22. doi:10.1186/s12963-020-00223-2.

5. Cruz FN, Miranda DA, Melo DLB, Ferro PL. Desvendando os suicídios entre profissionais de segurança pública: um olhar sobre fatores operacionais e organizacionais. *Soc Estado*. 2026;41(1):e56366. doi:10.1590/s0102-6992-20264101e56366.

6. Fórum Brasileiro de Segurança Pública. *14º Anuário Brasileiro de Segurança Pública*. São Paulo: FBSP; 2020. Disponível em: https://static.poder360.com.br/2020/11/Anuario-Brasileiro-de-Seguranca-Publica-2020.pdf.

7. Gomes DAR, de Araújo RMF, Gomes MS. Incidence of suicide among military police officers in South Brazil: an 11-year retrospective cohort study. *Compr Psychiatry*. 2018;85:61–66. doi:10.1016/j.comppsych.2018.06.006.

8. Krishnan N, Steene LMB, Lewis M, Marshall D, Ireland JL. A systematic review of risk factors implicated in the suicide of police officers. *J Police Crim Psychol*. 2022;37:939–951. doi:10.1007/s11896-022-09539-1.

9. Loo R. A meta-analysis of police suicide rates: findings and issues. *Suicide Life Threat Behav*. 2003;33(3):313–325. doi:10.1521/suli.33.3.313.23209.

10. Mann JJ, Apter A, Bertolote J, et al. Suicide prevention strategies: a systematic review. *JAMA*. 2005;294(16):2064–2074. doi:10.1001/jama.294.16.2064.

11. Messias KLM, Bispo Júnior JP, Pegado MFQ, et al. The quality of certification of deaths due to external causes in the city of Fortaleza in the State of Ceará, Brazil. *Ciên Saúde Colet*. 2016;21(4):1255–1266. doi:10.1590/1413-81232015214.07922015.

12. Milner A, Witt K, Maheen H, LaMontagne AD. Access to means of suicide, occupation and the risk of suicide: a national study over 12 years of coronial data. *BMC Psychiatry*. 2017;17:125. doi:10.1186/s12888-017-1288-0.

13. Minayo MCS, Assis SG, Oliveira RVC. Impacto das atividades profissionais na saúde física e mental dos policiais civis e militares do Rio de Janeiro. *Ciên Saúde Colet*. 2011;16(4):2199–2209. doi:10.1590/S1413-81232011000400019.

14. Ministério do Trabalho e Emprego. Classificação Brasileira de Ocupações — CBO. Brasília: MTE. Disponível em: https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/cbo.

15. Palma TF, Teixeira JRB, Bandini MCD, Lucca SR, Araújo TM. Quando a saída é a própria morte: suicídio entre trabalhadores e trabalhadoras no Brasil. *Ciên Saúde Colet*. 2024;29(10):e00922023. doi:10.1590/1413-81232024291000922023.

16. Pereira GK, Madruga AB, Kawahala E. Suicídios em uma organização policial-militar do sul do Brasil. *Cad Saúde Colet*. 2020;28(4):500–509. doi:10.1590/1414-462X202028040562.

17. Reis G. *Suicídios no Brasil entre 2010 e 2019: base e código aberto*. 2021. Disponível em: https://github.com/GabrielReisR/suicide_in_brazil.

18. Saldanha RF, Bastos RR, Barcellos C. Microdatasus: pacote para download e pré-processamento de microdados do Departamento de Informática do SUS (DATASUS). *Cad Saúde Pública*. 2019;35(9):e00032419. doi:10.1590/0102-311X00032419.

19. Souza ER, Minayo MCS, Silva JG, Pires TO. Fatores associados ao sofrimento psíquico de policiais militares da cidade do Rio de Janeiro. *Cad Saúde Pública*. 2012;28(7):1297–1311. doi:10.1590/S0102-311X2012000700008.

20. Stanley IH, Hom MA, Joiner TE. A systematic review of suicidal thoughts and behaviors among police officers, firefighters, EMTs, and paramedics. *Clin Psychol Rev*. 2016;44:25–44. doi:10.1016/j.cpr.2015.12.002.

21. Violanti JM, Steege A. Law enforcement worker suicide: an updated national assessment. *Policing: An International Journal*. 2021;44(1):18–31. doi:10.1108/PIJPSM-09-2019-0157.

22. World Health Organization. *Preventing suicide: a global imperative*. Geneva: WHO; 2014.

23. World Health Organization. *Suicide worldwide in 2019: global health estimates*. Geneva: WHO; 2021.

24. Instituto de Pesquisa Econômica Aplicada. Ocupações no funcionalismo público (2003–2017). *Atlas do Estado Brasileiro*. Brasília: Ipea; 2019. Disponível em: https://www.ipea.gov.br/atlasestado/arquivos/rmd/8825-conjunto-08-update.html.

## Material suplementar

### Quadro S1. Códigos CBO incluídos em segurança pública

**Polícia Militar:** 020105, 020110, 020115, 020205, 020305, 020310, 021105, 021110, 021205, 021210.  
**Bombeiro Militar:** 030105, 030110, 030115, 030205, 030305, 031105, 031110, 031205, 031210.  
**Polícia Civil e perícia:** 204105, 242305, 351420, 351810, 351815.  
**Polícia Federal e PRF:** 517205, 517210.  
**Guarda civil municipal:** 517215.  
**Polícia penal/penitenciária:** 517315.

### Quadro S2. Interpretação correta dos estimandos

| Estimando | O que responde | O que não responde |
|---|---|---|
| Mudança de 432 para 1.070 | Quantos casos adicionais se tornam classificáveis após reconstruir o CBO | Quantos suicídios “novos” ocorreram |
| Percentual de arma de fogo | Como os métodos se distribuem dentro dos óbitos identificados | Qual carreira tem maior incidência de suicídio |
| OR caso-caso | Chance relativa de arma de fogo versus outros métodos entre óbitos | Risco de morrer por suicídio ou efeito causal da ocupação |
| Taxa aproximada de 2017 | Ordem de grandeza sob numerador e denominador imperfeitamente compatíveis | Taxa definitiva dos profissionais ativos |

### Lista de verificação antes da submissão

1. Inserir autoria, afiliações, ORCID e autor correspondente.
2. Confirmar a declaração ética com a instituição responsável.
3. Escolher o periódico e adequar extensão, estilo de referências, resumo e número de figuras.
4. Executar novamente o script diretamente sobre os microdados oficiais do SIM, preservando o CBO como texto.
5. Registrar versão do código, ambiente e checksum dos arquivos de entrada.
6. Realizar revisão por pesquisador de epidemiologia ocupacional e por profissional de segurança pública.
7. Adequar a declaração de uso de IA à política editorial vigente.

