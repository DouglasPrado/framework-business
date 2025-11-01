# Briefing do MVP Manual

## Identificação do Projeto

- Nome do MVP: Controle Diário de Caixa Varejo (versão manual)
- Owner responsável: Douglas Prado (Growth Ops)
- Stakeholder decisor: Letícia Martins (Head de Produto)
- Data prevista para início da operação: 05/11/2025
- Data alvo para primeira validação com cliente: 18/11/2025

## Objetivo e Hipóteses

- Resultado principal a validar (ex: adesão, satisfação, disposição a pagar): Micro varejistas conseguem registrar movimento diário e receber alertas manuais de risco de caixa em até 48h, relatando ganho de clareza e intenção de pagar pelo serviço piloto.
- Hipótese central (link para Declaração de Hipótese): Ver "ProblemHypothesisDefinition/hypothesis-sistema-financeiro-varejo.MD".
- Métricas de sucesso (qualitativas ou quantitativas):
  - 80% dos clientes piloto registram dados por 5 dias úteis consecutivos.
  - Redução auto-relatada de tempo de consolidação manual de 3-4 horas semanais para no máximo 1 hora.
  - Nota mínima "Atende" no feedback qualitativo sobre clareza dos alertas e recomendações.
- Critérios de aprovação (o que precisa acontecer para avançar para automação?):
  - Dois clientes pagantes confirmam disposição a migrar para versão contínua após piloto.
  - Tempo operacional por cliente ≤ 2h por semana com equipe atual.
  - Checklist executado sem retrabalho crítico em 90% das entregas.

## Oferta e Escopo

- Descrição da entrega manual: Serviço de acompanhamento financeiro diário feito por analista dedicado que consolida entradas e saídas em planilha estruturada e envia resumo com alertas e recomendações simples.
- O que está incluído:
  - Configuração inicial da planilha padrão com histórico de 30 dias.
  - Atualização manual diária de entradas/saídas enviadas pelo cliente.
  - Relatório de alerta 2x por semana com recomendações de caixa e margem.
- O que NÃO está incluído:
  - Integração automática com maquininhas ou ERPs.
  - Consultoria tributária ou renegociação com fornecedores.
  - Projeções financeiras além de 30 dias ou modelagem de estoque.
- Limites de volume (ex: nº de clientes simultâneos, entregas por semana): Máximo de 5 clientes simultâneos, com até 10 lançamentos por dia cada, entregas de alerta às terças e sextas.

## Público e Contexto

- Segmento prioritário: Proprietários de minimercados, mercearias e lojas de variedades com faturamento anual entre R$240 mil e R$500 mil.
- Persona ou situação principal: Dono que controla pessoalmente caixa, pagamentos e compras, usa caderno/WhatsApp para registrar movimento e sente falta de previsibilidade semanal.
- Principais dores que queremos resolver: Falta de visibilidade antecipada de falta de caixa, dificuldade para consolidar meios de pagamento e ausência de orientação sobre quando segurar compras.
- Promessas/comunicados essenciais: "Ajudo você a enxergar sobras e faltas de caixa antes de pagar fornecedores"; "Resumo em linguagem simples com próximos passos"; "Sem necessidade de sistema novo ou integração complexa".
- Canais de aquisição utilizados: Indicação de contadores parceiros, Sebrae local, grupos de WhatsApp de comerciantes de bairro.

## Metas Operacionais

- SLA de resposta inicial: 4 horas úteis após recebimento do briefing do cliente.
- SLA de entrega principal: Relatório consolidado enviado em até 48h após recebimento de lançamentos do dia anterior.
- Prazos de follow-up: Contato 24h após cada entrega principal para confirmar entendimento.
- Tempo máximo tolerado por etapa (planejado):
  - Recebimento: 15 minutos
  - Onboarding: 45 minutos
  - Produção: 60 minutos diários (divididos em blocos de 2 clientes)
  - QA: 15 minutos por entrega
  - Entrega: 10 minutos
  - Follow-up: 10 minutos

## Recursos Disponíveis

- Pessoas envolvidas e funções:
  - Douglas Prado / Growth Ops / 12 horas semanais (coordenação e QA)
  - Ana Souza / Analista Financeira / 20 horas semanais (produção e atendimento)
  - Felipe Ramos / Assistente Administrativo / 8 horas semanais (lançamentos e organização de arquivos)
- Ferramentas aprovadas (confirmar presença em `tools/`):
  - Google Sheets / Consolidação e controle diário / Acesso concedido aos três operadores
  - Trello / Pipeline de status e registro de pendências / Espaço de trabalho compartilhado
  - Google Drive / Armazenamento seguro de relatórios e comprovantes / Pastas organizadas por cliente
- Materiais existentes que podem ser reaproveitados: Modelos de relatórios do contador parceiro, scripts de entrevista e frases validadas em UserInterviewValidation, checklist de follow-up de consultoria financeira usado em projeto anterior.
- Orçamento disponível (se aplicável): R$2.500 para gratificações a clientes piloto e despesas operacionais (telefonia, deslocamentos pontuais).

## Riscos e Suposições

- Riscos críticos:
  1. Clientes atrasarem o envio de lançamentos diários → Impacto: quebra do SLA e necessidade de retrabalho; Mitigação: lembretes automatizados via WhatsApp Business e reforço no onboarding.
  2. Volume de lançamentos superar limite planejado → Impacto: aumento de tempo de produção acima de 60 minutos; Mitigação: revisar limites no contrato piloto e priorizar itens críticos (entradas maiores e contas fixas).
- Suposições a validar no piloto:
  1. Proprietários conseguem enviar foto dos comprovantes ou resumo das vendas até 20h diariamente sem suporte adicional.
  2. O relatório com linguagem simplificada (3 blocos principais) é suficiente para orientar decisões de compra e pagamento.

## Aprovações

- Briefing revisado por: Letícia Martins
- Data da revisão: 04/11/2025
- Comentários adicionais: Reforçar coleta de depoimentos escritos ao final do piloto para uso em materiais de venda.
