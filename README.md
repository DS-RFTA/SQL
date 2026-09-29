

Visão geral
Projeto de análise de lead time em supply chain com foco em compras, integração de bases heterogêneas e geração de indicadores para tomada de decisão. O pipeline lê um arquivo Excel de pedidos e um CSV de notas fiscais, normaliza chaves de documento, cruza as fontes, calcula o lead time em dias, remove duplicidades com critério analítico e disponibiliza o resultado final para consumo em Excel, SQLite e dashboards. Ferramentas como README estruturado, código reproduzível e narrativa orientada a impacto ajudam a transformar um script técnico em portfólio de dados para GitHub.

Storytelling 
Em operações de compras, atrasos entre a data do pedido e a entrada fiscal geram ruptura, excesso de estoque de segurança e perda de previsibilidade. Neste projeto, o objetivo é transformar dados operacionais dispersos em uma visão confiável do tempo de atendimento do fornecedor, permitindo acompanhar desempenho, identificar anomalias e priorizar ações de melhoria contínua.

O valor do projeto está menos no cálculo isolado e mais na construção de uma camada analítica: padronização de NF, tratamento de inconsistências, integração entre fontes, persistência em banco e preparação da base para visualização em Power BI. Em portfólios de ciência de dados, um bom README deve explicar objetivo, método, execução e resultados de forma reprodutível para que outra pessoa consiga entender e rodar o projeto.

Situação
A área de compras possuía informações de pedidos em Excel e registros fiscais em CSV, mas sem uma visão consolidada do lead time entre emissão do pedido e entrada da nota. Isso limitava a medição do desempenho do fornecedor e dificultava o desenho de dashboards e KPIs de supply chain.

Tarefa
Estruturar um pipeline analítico capaz de integrar as duas fontes, limpar números de NF, calcular lead time por documento, eliminar duplicidades com um critério consistente e disponibilizar a base final para exploração em SQL e visualização em Power BI.

Ação
Desenvolvi a leitura e padronização dos arquivos com Python e pandas, tratando diferenças de formato entre Excel e CSV e extraindo apenas a parte numérica relevante da NF para garantir o cruzamento entre tabelas.

Converti colunas de datas com tolerância a erro para evitar falhas silenciosas e permitir o cálculo robusto de lead time.

Realizei o merge entre pedidos e notas fiscais pela NF normalizada, criando uma base analítica única para compras.

Defini a regra de deduplicação por menor lead time por NF, uma escolha útil quando o objetivo é evitar contagem duplicada do mesmo documento e manter a ocorrência mais representativa para análise operacional.

Exportei o resultado para Excel e carreguei a tabela em SQLite, viabilizando consultas SQL e integração com dashboards no Power BI.

Estruturei o projeto como peça de portfólio com narrativa de negócio, stack utilizada, KPIs sugeridos e próximos passos analíticos, alinhando técnica e comunicação executiva.

Resultado
O projeto gera uma base final pronta para monitorar lead time de compras, comparar fornecedores, investigar desvios e alimentar dashboards gerenciais. Além disso, demonstra competências valiosas para um portfólio de dados: engenharia leve de dados, modelagem analítica, definição de métricas, uso de SQL e capacidade de traduzir dados em decisões operacionais.

Arquitetura analítica
Entrada de dados: Orders.xls e relatorioAnaliticoDeNotasFiscaisCompra.csv

Tratamento: limpeza de NF, validação de registros inválidos e padronização de datas

Integração: junção entre pedido e nota fiscal por chave normalizada

Métrica principal: LeadTime_dias = Data de entrada - Data Pedido MAR

Camada de persistência: exportação para lead_time_resultado.xlsx e carga em leadtime.db

Consumo analítico: consultas SQL e dashboard em Power BI

KPIs recomendados
Os painéis de supply chain costumam acompanhar lead time do fornecedor, variabilidade do lead time e indicadores ligados a cumprimento de prazo, pois essas métricas ajudam a identificar gargalos e priorizar melhorias com fornecedores.

Lead time médio de compras

Mediana de lead time

Desvio padrão do lead time

Percentual de pedidos dentro do SLA

Top fornecedores com maior atraso médio

Quantidade de NFs com lead time negativo ou inconsistente

Evolução mensal do lead time

Ranking de documentos críticos por atraso
