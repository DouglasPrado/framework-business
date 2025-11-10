# Checklist Operacional - ManualMVPDesign

Este checklist orienta a criação completa de um MVP manual em até duas semanas, garantindo padronização do fluxo, comunicação com o cliente e documentação de aprendizados. Utilize-o como ferramenta de controle durante todo o ciclo (planejamento → piloto → ajustes finais).

## Como Utilizar

1. Preencha as informações do projeto antes de iniciar.
2. Execute cada etapa na ordem sugerida, registrando responsáveis e datas.
3. Use os templates da pasta `_DATA/` e mantenha links atualizados.
4. Documente desvios, decisões e aprendizados diretamente nos campos indicados.
5. Ao final, revise o checklist de qualidade e consolide evidências no validador.

## Informações do Projeto

Nome do MVP:
Owner principal:
Segmento/Perfil prioritário:
Promessa central (hipótese):
Período planejado (início e fim):

---

## Etapa 1 – Preparar briefing e critérios do MVP manual (90 minutos)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Revisar hipóteses e aprendizados prévios ([ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD), [UserInterviewValidation](../03-UserInterviewValidation/process.MD))
- [ ] Definir objetivo do MVP manual (resultado a ser validado)
- [ ] Descrever oferta, público-alvo, promessas e limites de escopo
- [ ] Estabelecer metas operacionais (SLA, indicadores de qualidade, capacidade semanal)
- [ ] Listar recursos disponíveis (time, ferramentas aprovadas, materiais existentes)
- [ ] Registrar riscos críticos e suposições a validar no piloto
- [ ] Salvar briefing preenchido em `_DATA/briefing-manual-mvp.MD`

### Campos do Briefing

- Objetivo de negócio:
- Público/segmento:
- Oferta e entrega prometida:
- Metas de tempo (recebimento, entrega, follow-up):
- Qualidade mínima aceitável:
- Riscos e hipóteses:

### Output

- [ ] `briefing-manual-mvp.MD` atualizado e aprovado pelo stakeholder responsável

---

## Etapa 2 – Mapear fluxo de entrega ponta a ponta (3 horas)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Listar macro etapas: recebimento, onboarding, produção, QA, entrega, follow-up
- [ ] Detalhar tarefas dentro de cada macro etapa (ordem, responsáveis, dependências)
- [ ] Estimar tempo planejado para cada tarefa e registrar no template
- [ ] Definir checkpoints de qualidade e critérios de passagem
- [ ] Identificar gargalos potenciais e possíveis mitigadores
- [ ] Compartilhar fluxo com stakeholders para feedback
- [ ] Salvar mapa final em `_DATA/mapa-fluxo-entrega.MD`

### Output

- [ ] `mapa-fluxo-entrega.MD` completo com tempos, responsáveis e checkpoints

---

## Etapa 3 – Configurar ferramenta de gestão e checklist (4 horas)

Owner:
Ferramenta escolhida (confirmar em `tools/`):
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Definir estrutura do board/planilha (colunas, status, campos obrigatórios)
- [ ] Criar visões auxiliares (fila atual, entregas da semana, pendências)
- [ ] Registrar convenções de preenchimento e responsáveis por atualização
- [ ] Popular exemplo de item completo para referência da equipe
- [ ] Adaptar checklist operacional com base no fluxo (`_DATA/checklist-execucao.MD`)
- [ ] Inserir link do checklist na ferramenta de gestão
- [ ] Garantir acessos e permissões para todos os envolvidos

### Outputs

- [ ] Board/planilha configurado e linkado no briefing
- [ ] `estrutura-board.MD` com instruções e convenções
- [ ] `checklist-execucao.MD` preenchido com tarefas, responsáveis e critérios

---

## Etapa 4 – Produzir templates de comunicação (2 horas)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Definir gatilhos de envio para onboarding, entrega e follow-up
- [ ] Copiar `../_SHARED/templates/email-followup.MD` para `_DATA/modelo-email-follow-up.MD` antes de personalizar
- [ ] Redigir e revisar mensagens usando linguagem validada com clientes
- [ ] Incluir campos obrigatórios (CTA, SLA, próximos passos, canais de suporte)
- [ ] Validar tom e clareza com stakeholder (produto/atendimento)
- [ ] Adaptar versões alternativas se houver segmentos diferentes
- [ ] Atualizar links para templates no board/checklist
- [ ] Salvar versões finais em `_DATA/modelo-email-onboarding.MD`, `_DATA/modelo-email-entrega.MD`, `_DATA/modelo-email-follow-up.MD`

### Output

- [ ] Três templates aprovados e referenciados na operação

---

## Etapa 5 – Executar piloto interno e medir tempos (1-2 dias corridos)

Owner:
Caso/teste escolhido:
Data de execução:

### Antes de iniciar

- [ ] Selecionar cenário representativo e validar escopo do teste
- [ ] Preparar cronômetros ou ferramenta de time tracking
- [ ] Confirmar que checklist e board estão atualizados
- [ ] Comunicar equipe envolvida sobre objetivos do piloto

### Durante o piloto

- [ ] Executar cada etapa seguindo o checklist
- [ ] Cronometrar tempos reais e registrar no board ou template
- [ ] Notar ajustes ad-hoc, exceções e recursos adicionais utilizados
- [ ] Capturar feedback do “cliente teste” (real ou simulado)

### Após o piloto

- [ ] Preencher `_DATA/relatorio-piloto.MD` com tempos, gargalos, soluções
- [ ] Atualizar estimativas de tempo e capacidade no briefing
- [ ] Registrar aprendizados e backlog de melhorias
- [ ] Comunicar resultados ao stakeholder responsável

### Output

- [ ] `relatorio-piloto.MD` completo com métricas e decisões tomadas

---

## Etapa 6 – Ajustar documentação final e organizar materiais (1 dia)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas

- [ ] Atualizar `mapa-fluxo-entrega.MD` com tempos e ajustes pós-piloto
- [ ] Revisar checklist e board incorporando melhorias e campos extras
- [ ] Definir padrões de qualidade finais em `_DATA/padroes-qualidade.MD`
- [ ] Compilar manual operacional final em `_DATA/manual-operacional-final.MD`
- [ ] Organizar materiais padrão na pasta `_DATA/` (subpastas se necessário)
- [ ] Atualizar `inventario-materiais.MD` com links, donos e revisão
- [ ] Registrar próximos experimentos/automação em seção específica do manual
- [ ] Validar pacote final com stakeholder e registrar aprovação

### Checklist de Encerramento

- [ ] Manual operacional final revisado e salvo
- [ ] Padrões de qualidade aprovados
- [ ] Inventário atualizado com 100% dos itens críticos
- [ ] Board/planilha com convenções documentadas
- [ ] Templates de comunicação publicados

---

## Checklist Final de Qualidade

- [ ] Briefing alinhado a hipóteses e metas de negócio
- [ ] Fluxo mapeado com tempos reais pós-piloto
- [ ] Ferramenta de gestão e checklist prontos para uso diário
- [ ] Templates de comunicação personalizados e aprovados
- [ ] Piloto executado com métricas registradas e decisões tomadas
- [ ] Manual, padrões de qualidade e inventário completos
- [ ] Próximos passos definidos (experimentos, automações, métricas adicionais)
- [ ] Validador final preenchido (`validator.MD`)

---

## Estrutura sugerida para `_DATA/`

```
_DATA/
├── briefing-manual-mvp.MD
├── mapa-fluxo-entrega.MD
├── estrutura-board.MD
├── checklist-execucao.MD
├── modelo-email-onboarding.MD
├── modelo-email-entrega.MD
├── modelo-email-follow-up.MD
├── relatorio-piloto.MD
├── padroes-qualidade.MD
├── manual-operacional-final.MD
└── inventario-materiais.MD
```

Adicione subpastas (ex: `templates/`, `assets/`, `scripts/`) conforme necessário e mantenha o inventário atualizado com todos os arquivos criados.
