# Mapa do Fluxo de Entrega Manual

Preencha para cada macro etapa do serviço. Use um item por linha para facilitar atualização. Atualize tempos planejados após o piloto com tempos reais.

## Visão Geral

- Data da versão: 04/11/2025
- Owner da atualização: Ana Souza
- Capacidade semanal planejada: 5 clientes ativos com entregas duas vezes por semana
- Capacidade semanal após piloto: Atualizar após ciclo 0 (estimado para 22/11/2025)
- Observações gerais: Fluxo estruturado para operação 100% manual com consolidação diária; tempos reais serão cronometrados no piloto interno com cliente simulado "Mercearia São Lucas".

## Recebimento

- Objetivo: Garantir que apenas clientes dentro do escopo entrem no pipeline e receber dados mínimos para iniciar setup.
- Checklist mínimo antes de aceitar nova solicitação: Confirmar segmento, faturamento ≤ R$500 mil, disponibilidade para enviar lançamentos diários e concordância com limites do MVP.

### Tarefas

1. Triagem de oportunidade
   - Descrição: Receber indicação ou formulário, validar segmento e critérios financeiros.
   - Responsável primário: Douglas Prado
   - Tempo planejado: 0h15
   - Tempo real (piloto): Registrar após 11/11/2025
   - Dependências: Formulário completo ou indicação confirmada
   - Critério de passagem: Critérios de escopo aprovados e cliente concorda com ritmo diário
2. Confirmação e criação no board
   - Descrição: Abrir card no Trello/Sheets com dados básicos e anexar briefing enviado pelo cliente.
   - Responsável primário: Felipe Ramos
   - Tempo planejado: 0h10
   - Tempo real (piloto): Registrar após 11/11/2025
   - Dependências: Aprovação da triagem
   - Critério de passagem: Card criado com status Recebido e dados essenciais preenchidos

## Onboarding

- Objetivo: Configurar planilha com histórico inicial e garantir que o cliente entenda entregas, prazos e responsabilidades.
- Materiais necessários do cliente: Extrato de vendas dos últimos 30 dias, lista de contas fixas, calendário de pagamentos críticos e contatos preferenciais.

### Tarefas

1. Reunião de alinhamento remoto
   - Descrição: Videoconferência de 30 minutos para revisar promessas, explicar rotina e coletar dúvidas.
   - Responsável primário: Douglas Prado
   - Tempo planejado: 0h30
   - Tempo real (piloto): Registrar após 12/11/2025
   - Dependências: Disponibilidade do cliente, formulários assinados
   - Critério de passagem: Cliente confirma entendimento das entregas e responsabilidade de envio diário
2. Configuração da planilha base
   - Descrição: Inserir dados históricos na planilha padrão, criar abas de lançamentos diários e resumo de caixa.
   - Responsável primário: Felipe Ramos
   - Tempo planejado: 0h45
   - Tempo real (piloto): Registrar após 12/11/2025
   - Dependências: Recebimento de extratos e contas fixas
   - Critério de passagem: Planilha compartilhada com cliente e link registrado no board
3. Mensagem de onboarding
   - Descrição: Enviar template personalizado reforçando entregas, prazos e materiais pendentes.
   - Responsável primário: Ana Souza
   - Tempo planejado: 0h15
   - Tempo real (piloto): Registrar após 12/11/2025
   - Dependências: Planilha pronta e validada
   - Critério de passagem: Cliente responde confirmando recebimento e compromisso com envios diários

## Produção

- Objetivo: Consolidar diariamente entradas e saídas, atualizar dashboards simples e preparar insights curtos para o relatório de alerta.
- Recursos utilizados (templates, checklists, ferramentas): Planilha Google "Controle Diário Varejo", checklist de produção na aba interna, biblioteca de mensagens aprovadas.

### Tarefas

1. Consolidação diária de lançamentos
   - Descrição: Importar dados enviados (foto, áudio ou planilha), normalizar categorias e registrar no painel de fluxo de caixa.
   - Responsável primário: Ana Souza
   - Tempo planejado: 0h40 por cliente ativo
   - Tempo real (piloto): Cronometrar por cliente após 15/11/2025
   - Dependências: Envio do cliente até 20h do dia anterior
   - Critério de passagem: Lançamentos do dia com status "Conferido" e sem campos vazios
2. Atualização de indicadores-chave
   - Descrição: Rodar fórmulas de projeção simples, atualizar saldo futuro de 7 dias, margem bruta por categoria e alertas visuais.
   - Responsável primário: Felipe Ramos
   - Tempo planejado: 0h15 por cliente
   - Tempo real (piloto): Registrar após 15/11/2025
   - Dependências: Consolidação concluída
   - Critério de passagem: Dashboard diário com alertas destacados e comentários iniciais
3. Preparação de resumo para entrega
   - Descrição: Redigir parágrafos curtos com status de caixa, ações recomendadas e riscos observados.
   - Responsável primário: Ana Souza
   - Tempo planejado: 0h20
   - Tempo real (piloto): Registrar após 15/11/2025
   - Dependências: Indicadores atualizados
   - Critério de passagem: Rascunho enviado para QA com checklist preenchido

## QA Interno

- Objetivo: Garantir consistência dos números e clareza das recomendações antes da comunicação com o cliente.
- Itens críticos de verificação: Conciliação de totais, coerência entre recomendação e dados, ortografia e tom aderente à linguagem validada.

### Tarefas

1. Revisão financeira
   - Descrição: Validar fórmulas, comparar saldo inicial/final e garantir que lançamentos duplicados foram removidos.
   - Responsável primário: Douglas Prado
   - Tempo planejado: 0h10
   - Tempo real (piloto): Registrar após 15/11/2025
   - Dependências: Resumo de produção disponível
   - Critério de passagem: Checklist de QA assinado no board
2. Revisão de comunicação
   - Descrição: Checar clareza das mensagens, ajustar termos para linguagem validada e inserir CTA específico.
   - Responsável primário: Ana Souza
   - Tempo planejado: 0h05
   - Tempo real (piloto): Registrar após 15/11/2025
   - Dependências: Revisão financeira aprovada
   - Critério de passagem: Mensagem final pronta para envio e salva no drive

## Entrega ao Cliente

- Objetivo: Enviar resumo do caixa com recomendações acionáveis no prazo definido e registrar evidências de envio.
- Canal de entrega: E-mail principal + resumo via WhatsApp Business para confirmação rápida.
- Documentos anexados: Planilha atualizada (visualização), PDF com resumo semanal, checklist de ações.

### Tarefas

1. Envio do relatório
   - Descrição: Personalizar template de entrega, anexar materiais e enviar ao responsável do cliente.
   - Responsável primário: Ana Souza
   - Tempo planejado: 0h10
   - Tempo real (piloto): Registrar após 15/11/2025
   - Dependências: QA concluído
   - Critério de passagem: Confirmação de leitura ou recebimento registrada
2. Registro de evidências
   - Descrição: Salvar cópia do e-mail e atualização do status no board, anexar logs na pasta do cliente.
   - Responsável primário: Felipe Ramos
   - Tempo planejado: 0h05
   - Tempo real (piloto): Registrar após 15/11/2025
   - Dependências: Envio realizado
   - Critério de passagem: Card movido para Follow-up com links das evidências

## Follow-up e Aprendizados

- Objetivo: Coletar feedback rápido, medir satisfação e atualizar backlog de melhorias.
- Perguntas-chave para feedback: "O que ficou mais claro no seu caixa?", "Qual ação você conseguiu tomar?", "Algo ficou confuso ou incompleto?".
- Decisões que dependem deste passo: Continuidade do cliente após piloto, ajustes no checklist, priorização de automações manuais.

### Tarefas

1. Contato pós-entrega
   - Descrição: Enviar template de follow-up e agendar call curta se necessário.
   - Responsável primário: Douglas Prado
   - Tempo planejado: 0h10
   - Tempo real (piloto): Registrar após 16/11/2025
   - Dependências: Evidência de entrega registrada
   - Critério de passagem: Resposta recebida ou tentativa registrada por 3 dias
2. Consolidação de aprendizados
   - Descrição: Registrar insights no board e atualizar backlog de melhorias e inventário de materiais.
   - Responsável primário: Ana Souza
   - Tempo planejado: 0h15
   - Tempo real (piloto): Registrar após 18/11/2025
   - Dependências: Feedback coletado
   - Critério de passagem: Backlog atualizado com prioridade e responsável

## Métricas do Fluxo

- Tempo total estimado: 2h05 por cliente na semana (excluindo monitoramento diário de entrada de dados)
- Tempo total real (piloto): Atualizar após piloto em 18/11/2025
- Desvio percentual: A calcular com base nos tempos reais
- Principais gargalos identificados: Dependência de envio diário do cliente; necessidade de normalizar categorias manualmente
- Ações corretivas em andamento: Criar checklist de envio para cliente e biblioteca de categorias padrão para acelerar normalização
