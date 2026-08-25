# Verificação pré-publicação

Este relatório registra a auditoria técnica da cópia preparada para GitHub. A pasta original em Downloads não foi alterada.

## Escopo

- inventário e leitura do código e da documentação;
- busca por segredos, credenciais e caminhos pessoais;
- avaliação da granularidade e do risco de reidentificação;
- conferência de hashes;
- compilação dos scripts;
- reprodução integral a partir da entrada externa;
- execução dos testes automáticos.

## Política de dados

O arquivo `fontes/suicide_in_brazil/data/df.csv` é microdado individual e **não deve ser enviado ao GitHub**. A pasta `fontes/` está bloqueada no `.gitignore`. Os dados distribuídos são agregados e não incluem nomes, datas completas ou municípios.

## Resultado

- Python 3.12.13;
- dependências instaladas sem cache a partir de `requirements.txt`;
- compilação dos dois scripts: **aprovada**;
- execução integral de `01_analise_sim.py`: **aprovada**;
- execução de `02_validacao.py`: **APROVADA**, com 9 de 9 verificações satisfeitas;
- saídas principais: 112.491 registros na fonte, 1.070 no recorte de segurança pública, 638 códigos recuperados e 663 ocorrências por arma de fogo;
- segredos, credenciais e caminhos pessoais: **não encontrados** nos arquivos publicáveis.

## Observações de auditoria

1. A fonte externa usada foi o commit `652a91eada46b9c812b25efdcb9c4e79ed92e9d0`. O `df.csv` desse commit tem SHA-256 `8ff4e031aeea64d2667c4a34cb4f8f476beddeab40392988779c2b48c3c91260`, diferente do hash `269d...` que constava no manifesto recebido. Apesar disso, a reprodução gerou as mesmas contagens substantivas e passou todos os testes. O manifesto preparado foi atualizado para a fonte efetivamente validada.
2. Há células agregadas com contagem 1 em tabelas por carreira, método e perfil. Elas não contêm nomes, datas ou municípios, mas representam risco residual de inferência. Recomenda-se manter o repositório **privado** até a revisão dos autores ou aplicar supressão de células pequenas antes de torná-lo público.
3. `dados_processados/modelo_logistico.csv` era uma saída redundante e não era gerada pelo script atual. Ela foi retirada da cópia preparada; `modelos_logisticos.csv` é a saída reproduzível correta.
4. A licença do código deste pacote ainda não foi definida. Não tornar o repositório público antes de escolher uma licença e preencher os campos de autoria do manuscrito.

## Conclusão

O pacote está tecnicamente reproduzível e pode ser enviado a um repositório privado. A publicação pública deve aguardar a decisão sobre células pequenas, autoria e licença.

