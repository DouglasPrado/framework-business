# Processo de Design de MVP Manual

## Propósito

Desenhar, testar e documentar um fluxo de entrega 100% manual que permita validar oferta e experiência do cliente antes de investir em desenvolvimento automatizado. O processo garante que cada etapa — do recebimento ao follow-up — esteja padronizada, mensurável e suportada por materiais reutilizáveis.

## Objetivo

Em até duas semanas, construir um pacote operacional que inclua:
- Fluxo detalhado de entrega com tempos estimados por etapa
- Ferramenta de acompanhamento configurada (planilha ou board) com status padronizados
- Templates de comunicação (onboarding, entrega e follow-up)
- Checklist de execução e padrões de qualidade
- Registro de piloto interno com ajustes documentados
- Pasta organizada com materiais padrão para replicação imediata

## Escopo

### Dentro do escopo
- Consolidar briefing e critérios de sucesso do MVP manual
- Mapear fluxo ponta a ponta (recebimento → onboarding → produção → entrega → follow-up)
- Definir tempos estimados, responsáveis e dependências por etapa
- Configurar planilha/board de gestão aprovado em `tools/`
- Criar templates de e-mail e mensagens padrão
- Executar piloto interno cronometrado e registrar aprendizados
- Documentar versão final do processo com padrões de qualidade e inventário de materiais

### Fora do escopo
- Desenvolvimento de automações, integrações ou ferramentas proprietárias
- Produção de materiais de marketing fora do pacote mínimo (ex: site completo, vídeos complexos)
- Configuração de canais de aquisição ou vendas
- Implementação de métricas de produto em larga escala (analytics avançado, BI)
- Treinamento de equipe externa sem material final aprovado

## Etapas do Processo

### Etapa 1: Preparar briefing e critérios do MVP manual (90 minutos)

Objetivo: alinhar o escopo do serviço manual, público-alvo, expectativas de entrega e métricas de sucesso antes de mapear o fluxo.

Passos principais:
- Revisar hipóteses centrais do produto ([Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md)) e anotações de descoberta (`process/ZeroUm/01-ProblemHypothesisDefinition`, `process/UserInterviewValidation`)
- Registrar objetivo de negócio, segmentos atendidos, promessas e limites de escopo
- Definir metas mínimas (tempo de resposta, SLA de entrega, satisfação esperada)
- Identificar recursos disponíveis (time, ferramentas aprovadas, materiais existentes)
- Listar riscos conhecidos e suposições a validar durante o piloto

Use o template: `_DATA/briefing-manual-mvp.MD`

Outputs esperados:
- Briefing preenchido com escopo, metas e restrições
- Lista preliminar de materiais existentes que podem ser reaproveitados
- Critérios de sucesso aprovados (qualidade, tempo, experiência do cliente)

### Etapa 2: Mapear fluxo de entrega ponta a ponta e estimar tempos (3 horas)

Objetivo: desenhar o processo completo do primeiro contato ao follow-up, com tempos e responsáveis estimados para cada etapa.

Passos principais:
- Desdobrar o fluxo em macro etapas: recebimento, onboarding, produção, QA, entrega, follow-up
- Para cada macro etapa, listar tarefas granularizadas com tempo estimado, responsável primário e dependências
- Definir pontos de controle (qualidade, aprovação, comunicação)
- Identificar gargalos potenciais e anotar mitigadores
- Validar o fluxo com stakeholders principais antes de seguir

Use o template: `_DATA/mapa-fluxo-entrega.MD`

Outputs esperados:
- Fluxo detalhado com tempos estimados por tarefa
- Lista de checkpoints críticos e critérios de passagem
- Registro de gargalos previstos com plano de mitigação inicial

### Etapa 3: Configurar gestão operacional e checklist (4 horas)

Objetivo: transformar o fluxo em um sistema de acompanhamento visual e checklist operável pela equipe.

Passos principais:
- Escolher ferramenta de gestão aprovada em `tools/` (Sheets, Notion, Trello ou equivalente)
- Definir colunas/status que representem o fluxo mapeado e campos obrigatórios (SLA, responsável, data limite)
- Criar visões auxiliares (ex: fila atual, entregas da semana, pendências de QA)
- Popular checklist passo a passo com responsáveis, tempos e critérios de conclusão
- Validar acessos, permissões e convenções de preenchimento com o time

Use os templates:
- `_DATA/estrutura-board.MD`
- `_DATA/checklist-execucao.MD`

Outputs esperados:
- Board/planilha configurado com exemplos preenchidos
- Checklist operacional salvo e referenciado na ferramenta
- Convenções de uso documentadas (nomeação, status, handoff)

### Etapa 4: Produzir templates de comunicação com o cliente (2 horas)

Objetivo: garantir mensagens consistentes nas principais interações (onboarding, entrega e follow-up).

Passos principais:
- Definir gatilhos de envio (quando cada e-mail é disparado e por quem)
- Redigir mensagens alinhadas ao tom de voz e promessas do MVP
- Incluir campos obrigatórios (CTA, prazos, próximos passos, suporte)
- Validar linguagem com base em aprendizados de entrevistas (`process/UserInterviewValidation`) e hipóteses
- Salvar versões aprovadas e anexar no board/planilha quando aplicável

Use os templates:
- `_DATA/modelo-email-onboarding.MD`
- `_DATA/modelo-email-entrega.MD`
- `_DATA/modelo-email-follow-up.MD` (derivado de [`../_SHARED/templates/email-followup.MD`](../_SHARED/templates/email-followup.MD))

Outputs esperados:
- Três templates aprovados prontos para uso (e-mail ou mensagem)
- Lista de adaptações por segmento ou cenário especial
- Referência cruzada no checklist para cada momento de envio

### Etapa 5: Executar piloto interno e medir tempos reais (1-2 dias corridos)

Objetivo: validar o fluxo na prática, medir tempos reais e identificar gargalos antes de atender clientes.

Passos principais:
- Selecionar caso real ou cenário simulado representativo
- Executar o fluxo completo utilizando o checklist e o board configurado
- Cronometrar cada etapa e registrar desvios entre tempo planejado e real
- Coletar feedback dos envolvidos (operadores e “cliente teste”)
- Registrar problemas, causas, soluções aplicadas e itens de backlog

Use o template: `_DATA/relatorio-piloto.MD`

Outputs esperados:
- Relatório do piloto com tempos reais, gargalos e ajustes sugeridos
- Checklist anotado com melhorias encontradas
- Atualização do board com status e comentários do piloto

### Etapa 6: Ajustar processo final e organizar materiais padrão (1 dia)

Objetivo: consolidar aprendizados do piloto, atualizar documentação final e garantir armazenamento organizado dos artefatos.

Passos principais:
- Atualizar o fluxo e tempos com base nos resultados do piloto
- Revisar checklist e board, incorporando novos campos ou automações manuais
- Definir padrões de qualidade finais (critérios de aprovação, inspeção, SLA confirmado)
- Documentar orientações de execução passo a passo no manual operacional
- Organizar pasta `_DATA/` com materiais padrão e inventário atualizado
- Validar com stakeholder responsável e registrar próximos experimentos (ex: automações futuras)

Use os templates:
- `_DATA/padroes-qualidade.MD`
- `_DATA/manual-operacional-final.MD`
- `_DATA/inventario-materiais.MD`

Outputs esperados:
- Manual operacional final atualizado
- Padrões de qualidade aprovados e checklist ajustado
- Inventário de materiais com links ou caminhos de acesso
- Plano de próximos passos (ex: melhorias, métricas adicionais)

## Pontos de Decisão

1. **Após Etapa 1 (Briefing):** O escopo definido cabe no tempo e recursos disponíveis?  
   - Se não, reduza entregáveis ou ajuste metas antes de mapear o fluxo.

2. **Após Etapa 2 (Fluxo):** O processo cobre todas as interações críticas sem lacunas?  
   - Se não, revisite o fluxo com stakeholders e adicione tarefas ausentes.

3. **Após Etapa 3 (Gestão):** O board/planilha oferece visibilidade suficiente para operar diariamente?  
   - Se não, adicione campos ou visões antes de produzir templates de comunicação.

4. **Após Etapa 5 (Piloto):** Tempos reais diferem mais de 20% dos estimados?  
   - Se sim, ajuste estimativas e reavalie capacidade antes de atender clientes.

5. **Antes de encerrar Etapa 6:** Os padrões de qualidade e materiais estão completos e acessíveis?  
   - Se não, bloqueie a go-live até completar documentação e inventário.

## Resultados Esperados

1. Briefing do MVP manual com metas e limites claros
2. Mapa completo do fluxo com tempos, responsáveis e checkpoints
3. Ferramenta de acompanhamento configurada e checklist de execução
4. Templates de comunicação aprovados para onboarding, entrega e follow-up
5. Relatório do piloto interno com ajustes e decisões documentadas
6. Manual operacional final com padrões de qualidade e métricas alvo
7. Pasta `_DATA/` organizada com materiais padrão e inventário atualizado
8. Lista de próximos experimentos ou melhorias priorizadas

## Indicadores-Chave de Desempenho

- Tempo total do fluxo (meta definida no briefing; variação ≤ 20% após ajustes)
- SLA de resposta no onboarding (meta definida no briefing, cumprir no piloto)
- Taxa de tarefas concluídas sem retrabalho no piloto (meta ≥ 90%)
- Percentual de itens do checklist concluídos no tempo estimado (meta ≥ 80%)
- Satisfação do cliente teste (escala qualitativa documentada, meta ≥ “Atende”)
- Cobertura de materiais padrão (meta: 100% dos itens críticos inventariados)

## Avisos e Armadilhas Comuns

1. **Escopo inflado:** tentar entregar mais do que o MVP exige atrasa validação. Mantenha o foco no mínimo necessário para aprender.
2. **Gargalos não medidos:** operar sem cronometrar etapas cria falsa confiança. Registre tempos reais no piloto.
3. **Ferramenta escolhida sem alinhamento:** confirmar aprovações em `tools/` evita refazer implementação.
4. **Templates genéricos demais:** use linguagem validada com clientes para evitar comunicações frias.
5. **Checklist desatualizado:** ajuste o checklist sempre que identificar exceções. Operadores não devem depender de memória.
6. **Materiais espalhados:** centralize tudo em `_DATA/` ou em pasta referenciada para reduzir atrito na execução diária.

## Dependências

Entradas necessárias:
- Definição do produto/serviço e hipótese central ([ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD))
- Perfis priorizados e dores principais ([TargetUserIdentification](../02-TargetUserIdentification/process.MD))
- Insights de linguagem e objeções ([UserInterviewValidation](../03-UserInterviewValidation/process.MD))
- Catálogo de ferramentas aprovadas (`tools/`)

Saídas habilitam:
- Processos futuros de automação ou productização do serviço
- Criação de landing pages e materiais de venda usando padrões definidos
- Implementação de métricas e integrações (quando automatização for priorizada)
- Treinamento de novos operadores com base no manual e checklist

## Referências

- Estratégia: `strategies/ZeroUm/process-analysis.md` (seção ManualMVPDesign)
- Processos relacionados:
  - [ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD)
  - [TargetUserIdentification](../02-TargetUserIdentification/process.MD)
  - [UserInterviewValidation](../03-UserInterviewValidation/process.MD)
  - [LandingPageCreation](../LandingPageCreation/process.MD)
- Templates compartilhados: [_SHARED/templates/declaracao-hipotese.md](../_SHARED/templates/declaracao-hipotese.md)
- Checklists e materiais deste processo: `process/ManualMVPDesign/_DATA/`
