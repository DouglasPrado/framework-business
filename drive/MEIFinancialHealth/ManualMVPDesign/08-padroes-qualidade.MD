# Padrões de Qualidade – LucroSeparado MVP Manual

## Critérios Gerais

- Todos os clientes recebem diagnóstico dentro de 3 horas úteis após envio completo dos dados.
- Planilha entregue sem erros de fórmula (validação feita no QA).
- Comunicação coerente com a promessa da landing e do checkout (mesma linguagem e prazos).
- Registro de tempo e status atualizado no board em até 15 minutos após cada etapa.

## Recebimento e Onboarding

- Dados obrigatórios preenchidos: faturamento bruto, custos principais, canais de venda, conta bancária utilizada, objetivos pessoais.
- Confirmação do cliente recebida (e-mail ou WhatsApp) com entendimento da promessa e prazo.
- Checklist de subcontas enviado e respondido (cliente confirma se já separa valores).
- SLA de resposta ao cliente ≤ 1 hora (em horário comercial).

## Produção do Diagnóstico

- Planilha com abas:
  - Dados brutos (não editáveis)
  - Resumo financeiro (pró-labore, reservas, métricas chave)
  - Ajustes semanais (fácil de preencher)
  - Histórico de alertas
- Valores arredondados para múltiplos de R$10.
- Recomendação de pró-labore entre 15% e 25% da receita líquida, salvo justificativa registrada.
- Alertas semanais configurados com mensagem padrão + personalização (margem atual, próximos passos).

## QA

- Checklist QA concluído com evidência de revisão (iniciais do revisor + horário).
- Nenhum link quebrado (planilha, PDF, Calendly, Notion).
- Texto da entrega sem termos técnicos não explicados (“pró-labore” acompanhado de “retirada ideal”).
- Observações do QA documentadas na planilha e resolvidas antes da entrega.

## Entrega

- E-mail e WhatsApp enviados, com logs arquivados no CRM (ou planilha).
- Plano anexado com permissões corretas (visualização + cópia; edição somente para a equipe).
- Follow-up agendado e link compartilhado.

## Follow-up e Acompanhamento

- Feedback obtido em até 48h (escala 1-3 + comentário).
- Alertas semanais enviados com diferenciais personalizados (ex.: lembrete de metas do cliente).
- Ajustes solicitados registrados e tratados em até 24h.
- Relatório semanal interno enviado (tempo real vs. estimado, gargalos, melhorias propostas).

## Exceções e Tratamento

- Solicitações fora do escopo avaliadas em até 12h; se aprovadas, documentar impacto e decisão.
- Atrasos justificados (ex.: cliente demorou nos dados) sinalizados no board com tag `Dependência do cliente`.
- Erros identificados pelo cliente → prioridade máxima; corrigir em até 4h e registrar no relatório de piloto.

## Atualização dos Padrões

- Revisar este documento ao término de cada rodada de 10 clientes ou quando surgirem mudanças relevantes no processo.
- Registrar alterações no `manual-operacional-final.MD` com data e responsável.
