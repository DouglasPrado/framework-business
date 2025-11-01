# Processo de Execução de Call de Vendas Consultiva

## Propósito

Conduzir calls de vendas com leads qualificados de forma consultiva, garantindo diagnóstico real, apresentação de valor alinhada à dor do cliente e fechamento rápido com follow-up estruturado. O processo assegura consistência, rastreabilidade e transferência imediata para onboarding após pagamento.

## Objetivo

Completar o ciclo de venda de cada lead em até 1 dia, entregando:
- Call agendada e realizada com roteiro registrado.
- Proposta personalizada apresentada e próximo passo acordado.
- Link de pagamento enviado e status monitorado até confirmação.
- Registro completo de dores, objeções e decisão do lead.
- Handoff para onboarding documentado (quando fechado) ou motivo de perda (quando não fechado).

## Escopo

### Dentro do escopo
- Preparar briefing detalhado do lead e definir meta da call.
- Personalizar materiais (deck, demo, piloto) e garantir logística.
- Conduzir call consultiva com diagnóstico, proposta e alinhamento.
- Tratar objeções comuns com roteiros aprovados.
- Executar follow-up imediato e registrar evidências.
- Atualizar pipeline, confirmar pagamento e iniciar onboarding.

### Fora do escopo
- Geração de leads ou agendamento inicial (tratado em OutreachCampaign).
- Criação de novas ofertas, preços ou termos (alinhado previamente com liderança).
- Implementação de automações complexas de CRM.
- Entrega do serviço/produto após fechamento (processo ClientDelivery).
- Gestão financeira de longo prazo (financeiro/contabilidade).

## Etapas do Processo

### Etapa 1: Preparar briefing e meta da call (45-60 minutos)

Objetivo: consolidar todas as informações relevantes do lead antes da call para personalizar a conversa e confirmar se a oportunidade permanece qualificada.

Passos:
- Revisar origem do lead, interações anteriores, landing page/conteúdo consumido e notas no CRM.
- Identificar dor principal percebida, urgência declarada e expectativa de resultado.
- Confirmar decisores envolvidos, orçamento indicado e timeline desejada.
- Definir objetivo da call (fechamento imediato, validação final, envolvimento de decisor).
- Registrar hipóteses, gaps de informação e métricas-alvo no template `_DATA/prep-call-briefing.MD`.

Outputs:
- Briefing preenchido com contexto completo, objetivo da call e red flags registradas.
- Agenda da call confirmada (data, horário, link, participantes) com lembrete enviado.

### Etapa 2: Personalizar proposta e materiais (45-60 minutos)

Objetivo: garantir que demonstrações, argumentos e oferta estejam alinhados ao cenário do lead.

Passos:
- Selecionar casos, provas sociais e métricas relevantes para o segmento do lead.
- Ajustar deck, demo ou piloto (se aplicável) com dados e linguagem aderentes.
- Definir estrutura do investimento: preço, condições de pagamento, bônus, garantias.
- Pré-configurar link de pagamento ou contrato simplificado.
- Validar coerência entre promessa feita em `LandingPageCreation` e oferta atual.
- Anotar gatilhos e perguntas específicas a explorar durante a call.

Outputs:
- Materiais atualizados e salvos em pasta compartilhada.
- Link de pagamento ou instruções de cobrança testados.
- Lista de bullets-chave para reforçar valor e diferencial.

### Etapa 3: Ensaiar roteiro e garantir logística (15-20 minutos)

Objetivo: assegurar fluidez da call e ausência de fricções técnicas.

Passos:
- Revisar `_DATA/roteiro-sales-call.MD` adaptando abertura, diagnóstico, proposta e fechamento.
- Ensaiar perguntas críticas e possíveis transições conforme respostas esperadas.
- Checar equipamentos (áudio, vídeo), ambiente, conexões e gravação (se autorizada).
- Preparar documento de notas ou planilha para registro em tempo real.
- Reenviar confirmação da call ao lead (quando agendada com antecedência > 24h).

Outputs:
- Roteiro personalizado com anotações de reforço e perguntas adicionais.
- Ambiente e ferramentas testados; gravação autorizada (quando aplicável).

### Etapa 4: Conduzir call consultiva (15-25 minutos)

Objetivo: diagnosticar dor, apresentar proposta de valor e alinhar decisão com clareza.

Estrutura recomendada:
1. **Abertura (2 min)** – reconhecer contexto, reforçar agenda e tempo.
2. **Diagnóstico (5-7 min)** – explorar dor, impacto, soluções atuais, urgência.
3. **Proposta (5 min)** – conectar dor ao resultado prometido, apresentar oferta.
4. **Tratamento de objeções (3-5 min)** – aprofundar bloqueios, responder com valor.
5. **Fechamento (2-3 min)** – confirmar próximos passos, empresa envolvida e timing.

Passos:
- Atualizar notas em tempo real citando palavras do lead (linguagem literal).
- Qualificar decisão (quem aprova, orçamento disponível, janela de implementação).
- Co-construir próximos passos (pagamento imediato, segunda call, envio de materiais).
- Registrar objeções e compromissos no template `_DATA/objection-log.MD`.
- Obter compromisso claro (data e responsável) para ação seguinte.

Outputs:
- Notas completas no documento de resumo, com status e compromissos definidos.
- Objeções registradas com respostas dadas e necessidade de follow-up.

### Etapa 5: Executar follow-up imediato (30 minutos)

Objetivo: reforçar decisão, enviar materiais e manter momento da venda.

Passos:
- Preencher `_DATA/pos-call-resumo.MD` com principal dor, proposta apresentada, condição acordada e próximos passos.
- Enviar e-mail ou mensagem de follow-up em até 30 minutos com resumo, link de pagamento e prazos combinados.
- Compartilhar gravação ou materiais extras prometidos durante a call.
- Atualizar pipeline/CRM com status (Fechado, Follow-up, Perdeu) e data da próxima ação.
- Programar lembretes automáticos ou pessoais para confirmação do pagamento.

Outputs:
- Follow-up documentado (mensagem enviada e anexos).
- Pipeline atualizado com data de follow-up e responsável.
- Registro de compromissos com horário/dia definidos.

### Etapa 6: Confirmar pagamento e acionar onboarding (até 4 horas após call)

Objetivo: garantir que a venda seja concluída operacionalmente e o cliente seja integrado sem fricção.

Passos:
- Monitorar confirmações do gateway ou comprovantes manuais.
- Confirmar recebimento com o cliente e agradecer (mesmo se pagamento for futuro, confirmar status).
- Se pagamento atrasar, executar sequência de follow-up predefinida (D+1, D+3).
- Notificar time de entrega (ClientDelivery) com resumo da call e expectativas.
- Atualizar indicadores (taxa de fechamento, ticket, motivo de perda se aplicável).
- Arquivar evidências (comprovante, confirmação, resumo final) em `_DATA/`.

Outputs:
- Pagamento confirmado e onboarding acionado com handoff documentado.
- Motivo de perda registrado quando venda não se concretiza.
- Indicadores atualizados para análise em `RetrospectiveAnalysis`.

## Pontos de Decisão

1. **Após Etapa 1 – Qualificação do lead:** Lead possui dor aderente, autoridade e urgência?  
   - Se não, requalificar via OutreachCampaign ou descartar com justificativa.

2. **Após Etapa 3 – Prontidão para call:** Materiais e logística estão 100% prontos?  
   - Se não, reagendar call com antecedência mínima de 12h e concluir preparação.

3. **Após Etapa 5 – Próximo passo claro:** Existe compromisso concreto do lead para pagamento ou decisão?  
   - Se não, agendar nova interação imediatamente e definir data limite. Se sim, prosseguir para confirmação.

## Resultados Esperados

1. Briefing e roteiro personalizados para cada lead.
2. Call realizada com notas estruturadas e objeções documentadas.
3. Follow-up enviado em até 30 minutos com link de pagamento e próximos passos.
4. Pagamento confirmado ou plano de follow-up datado.
5. Handoff para onboarding com resumo completo da conversa.
6. Base de objeções alimentada para melhoria contínua.

## Indicadores-Chave de Desempenho

- Taxa de comparecimento (shows/agendamentos). Meta: ≥ 80%.
- Tempo médio para envio de follow-up pós-call. Meta: ≤ 30 min.
- Taxa de fechamento por lead qualificado. Meta inicial: ≥ 30%.
- Tempo médio entre pagamento e início do onboarding. Meta: ≤ 2 horas.
- Volume de objeções recorrentes documentadas por call. Meta: ≥ 1 registro por objeção relevante.

## Avisos e Armadilhas Comuns

1. **Call sem objetivo claro:** defina meta antes de ligar (fechar, validar, envolver decisor). Caso contrário, você sai sem compromissos.
2. **Pular diagnóstico:** apresentar solução cedo demais impede identificação da dor real. Reserve tempo para perguntas abertas.
3. **Ignorar decisores adicionais:** se outro decisor surgir, agende nova call na hora e forneça material de apoio específico.
4. **Follow-up tardio:** atrasar follow-up reduz conversão. Tenha templates prontos e envie dentro da meta.
5. **Objeções sem registro:** documentação insuficiente impede ajustes em copy e oferta. Use `_DATA/objection-log.MD` em todas as calls.
6. **Pagamento sem confirmação:** sempre confirme recebimento antes de considerar venda concluída e iniciar onboarding.

## Dependências

Entradas necessárias:
- Leads qualificados vindos de `OutreachCampaign` ou tráfego da landing (quando ativo).
- Linguagem e objeções mapeadas em `UserInterviewValidation`.
- Oferta e promessa comunicada em `LandingPageCreation`.
- Link de pagamento configurado (via `CheckoutSetup`, quando disponível) ou instruções financeiras aprovadas.

Saídas habilitam:
- `ClientDelivery` para execução do serviço/produto.
- `RetrospectiveAnalysis` para refinar argumentos e proposta.
- Atualização de copy e materiais em `LandingPageCreation` e outreach.

## Referências

- [README.MD](README.MD)
- [knowledge.MD](knowledge.MD)
- [tasks.MD](tasks.MD)
- [validator.MD](validator.MD)
- Templates em `_DATA/`
- Registros históricos de calls (CRM, planilhas ou pasta compartilhada)
