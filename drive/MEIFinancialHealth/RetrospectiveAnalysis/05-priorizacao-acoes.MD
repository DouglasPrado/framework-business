# Matriz de Decisão e Priorização de Ações - Retrospectiva 07/11/2025

## Contexto
- Data da retrospectiva: 07/11/2025
- Facilitador: Douglas Prado
- Participantes envolvidos na priorização: Douglas Prado, Ana Luiza

## Status dos Gatilhos Obrigatórios
- Conversão da landing < 3%?
  - Status (Ativo/Inativo): Ativo (sem dados, landing offline)
  - Evidência (métrica, período): 0 visitas e 0 leads entre 24/10 e 06/11
  - Diagnóstico inicial: publicação bloqueada pelo QA pendente
  - Ação obrigatória sugerida: finalizar QA, publicar landing e coletar primeiros 120 visitantes para medir conversão.

- Conversão lead → cliente < 5%?
  - Status: Ativo
  - Evidência: 2 leads quentes, 0 fechamentos
  - Diagnóstico: cadência parada e calls não agendadas
  - Ação sugerida: disparar cadência + confirmar calls com Carla e João até 08/11.

- Tempo de entrega > 7 dias?
  - Status: Inativo (nenhum cliente entregue ainda)
  - Evidência: piloto ainda não começou; backlog vazio
  - Diagnóstico: acompanhar a partir da primeira entrega
  - Ação sugerida: registrar tempo real no board e revisar SLA após primeiro caso.

- Preço aceito sem objeções relevantes?
  - Status: Ativo
  - Evidência: Carla e João aceitaram R$99/mês sem negociação
  - Diagnóstico: margem para testar valor maior assim que primeira entrega gerar prova social
  - Ação sugerida (ex: teste de aumento de preço): preparar proposta de plano a R$129 com bônus de alertas premium pós-entrega.

- Trabalho manual > 10h por cliente?
  - Status: Inativo (baseline planejado 2h45; sem dados reais)
  - Evidência: manual do MVP define limite atual
  - Diagnóstico: monitorar na execução do piloto
  - Ação sugerida (ex: automação, padronização): mapear tarefas passíveis de automação após medir esforço real nas duas primeiras entregas.

## Avaliação de Ações Potenciais
- Ação proposta: Publicar landing após QA completo
  - Origem (Manter/Corrigir/Testar): Corrigir
  - Métrica impactada: Conversão de landing e volume de leads
  - Impacto estimado (alto/médio/baixo): Alto
  - Esforço estimado (alto/médio/baixo): Médio
  - Dependências / riscos: Homologação Typeform, revisão final de copy e assets.

- Ação proposta: Disparar cadência com 50 abordagens e agendar calls
  - Origem: Corrigir
  - Métrica impactada: Leads quentes, taxa lead → cliente
  - Impacto estimado: Alto
  - Esforço estimado: Médio
  - Dependências: disponibilidade de Douglas, mensagens aprovadas, landing publicada (link preferencial).

- Ação proposta: Concluir testes de checkout (cartão/boleto) e liberar link final
  - Origem: Corrigir
  - Métrica impactada: Receita nova, rapidez no fechamento
  - Impacto estimado: Médio
  - Esforço estimado: Médio
  - Dependências: acesso PagSeguro, logs de teste, resposta do suporte.

- Ação proposta: Preparar plano para teste de preço a R$129
  - Origem: Testar
  - Métrica impactada: Receita média por cliente
  - Impacto estimado: Médio
  - Esforço estimado: Baixo
  - Dependências: obter primeira prova social e medir entrega.

## Ações Prioritárias (máximo 3)
- Prioridade 1:
  - Owner: Douglas Prado
  - Prazo de entrega: 08/11/2025 12h
  - Métrica de sucesso: Landing publicada com checklist QA concluído e GA4 ativo
  - Evidência que justifica: gargalo central sem tráfego registrado; impede metrificação da oferta
  - Próximo checkpoint: 08/11 15h (verificação de acesso e captura dos primeiros 20 leads)

- Prioridade 2:
  - Owner: Douglas Prado
  - Prazo: 10/11/2025 22h
  - Métrica: 50 abordagens enviadas, ≥5 respostas, ≥2 calls agendadas
  - Evidência: funil de vendas zerado e leads quentes aguardando retorno
  - Checkpoint: 09/11 20h (25 abordagens registradas)

- Prioridade 3:
  - Owner: Ana Luiza
  - Prazo: 09/11/2025 18h
  - Métrica: 100% dos testes do checkout concluídos com evidência anexada
  - Evidência: log atual 60% completo; sem checkout validado não há cobrança
  - Checkpoint: 09/11 12h (confirmação do teste de cartão)

## Backlog Secundário
- Ação: Preparar aumento de preço para R$129 com bônus de alertas semanais personalizados
  - Razão para ficar no backlog: depende da primeira entrega do piloto e depoimento para sustentar valor
  - Condições para ativação: concluir 2 entregas com NPS ≥8 e confirmar ausência de objeções de preço.

- Ação: Automatizar envio de lembretes de rotina financeira via WhatsApp API
  - Razão: precisa validar esforço manual real primeiro
  - Condições: medir horas investidas >5h por cliente em duas semanas consecutivas.

## Observações Finais
- Alinhamentos adicionais: revisar disponibilidade diária para dividir cadência com apoio de freelancer se volume crescer.
- Suportes ou aprovações necessárias: suporte PagSeguro para liberar sandbox de cartão; designer externo para revisão rápida da seção “como funciona” (se necessário).
- Data para revisão das ações priorizadas: 12/11/2025 durante check-in de execução.
