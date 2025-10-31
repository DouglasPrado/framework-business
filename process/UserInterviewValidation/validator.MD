# Validador - UserInterviewValidation

## Propósito

Este validador garante que a rodada de entrevistas foi executada com rigor e que as conclusões sobre as hipóteses estão suportadas por evidências. Utilize-o após completar todas as etapas para confirmar se os critérios de qualidade foram atendidos antes de avançar para decisões estratégicas.

## Como Usar

1. Revise cada seção correspondente às etapas do processo.
2. Marque os itens cumpridos com base nas evidências armazenadas em `_DATA/`.
3. Registre observações quando o critério não for atendido e defina ação corretiva.
4. Ao final, utilize o checklist de decisão para aprovar, revisar ou repetir a rodada.

---

## Validação da Etapa 1 – Briefing de validação

**Critério 1.1 – Hipóteses priorizadas e claras**
- [ ] Há no máximo três hipóteses listadas no briefing
- [ ] Cada hipótese descreve QUEM, DOR e RESULTADO esperado
- [ ] Hipóteses estão alinhadas à declaração oficial ([Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md))

**Critério 1.2 – Perfis e métricas definidos**
- [ ] Perfis-alvo estão definidos com base em [TargetUserIdentification](../TargetUserIdentification/process.MD)
- [ ] Métricas de sucesso das entrevistas foram registradas (ex: % confirmando a dor)
- [ ] Riscos ou suposições críticas foram documentados

Evidência: `briefing-entrevistas.MD`

---

## Validação da Etapa 2 – Roteiro

**Critério 2.1 – Perguntas abertas e não indutivas**
- [ ] As 5 perguntas principais são abertas e exploratórias
- [ ] Follow-ups incentivam exemplos concretos e detalhes
- [ ] Nenhuma pergunta sugere a solução ou validação direta de preço

**Critério 2.2 – Preparação de consentimento e fechamento**
- [ ] Roteiro inclui frase padrão de consentimento para gravação/notas
- [ ] Há pergunta de encerramento para captar objeções e próximos passos
- [ ] O roteiro foi revisado por outra pessoa ou em voz alta

Evidência: `roteiro-entrevista-base.MD`

---

## Validação da Etapa 3 – Recrutamento

**Critério 3.1 – Pipeline suficiente**
- [ ] Plano de recrutamento lista ao menos 15 prospects aderentes
- [ ] Existem pelo menos dois canais distintos de abordagem
- [ ] Mensagens de convite e follow-up estão redigidas no template

**Critério 3.2 – Rastreamento disciplinado**
- [ ] Tracker registra status atualizado de todos os convites
- [ ] Há registro de follow-ups enviados e respostas recebidas
- [ ] Consentimento para gravação está documentado no tracker ou notas

Evidência: `plano-recrutamento.MD`, `tracker-recrutamento.MD`

---

## Validação da Etapa 4 – Execução das entrevistas

**Critério 4.1 – Quantidade e aderência**
- [ ] 10 entrevistas foram concluídas com perfis-alvo aderentes
- [ ] Ausências e remarcações foram registradas no tracker
- [ ] Taxa de comparecimento ≥ 80%

**Critério 4.2 – Registro completo**
- [ ] Cada entrevista possui arquivo de notas nomeado corretamente
- [ ] Consentimento (gravado ou anotado) está registrado em cada arquivo
- [ ] Notas incluem dores, soluções atuais, objeções e citações literais

Evidência: Subpasta `_DATA/entrevistas/` e arquivos relacionados

---

## Validação da Etapa 5 – Consolidação e análise

**Critério 5.1 – Padrões e insights**
- [ ] `_DATA/analise-padroes.MD` lista ao menos três padrões validados
- [ ] Cada padrão cita entrevistas específicas ou trechos relevantes
- [ ] Há registro de oportunidades ou riscos emergentes fora das hipóteses iniciais

**Critério 5.2 – Classificação das hipóteses**
- [ ] Todas as hipóteses receberam status (Validada, Refutada ou Inconclusiva)
- [ ] Justificativas incluem citações ou comportamentos observados
- [ ] Se status for Inconclusiva, próximos passos estão definidos (nova rodada, ajuste, etc.)

**Critério 5.3 – Linguagem do cliente**
- [ ] `_DATA/biblioteca-linguagem.MD` contém pelo menos 10 citações literais
- [ ] Cada citação tem contexto (perfil, situação, hipótese) e interpretação
- [ ] Linguagem capturada está pronta para uso em copy ou mensagens

Evidência: `analise-padroes.MD`, `classificacao-hipoteses.MD`, `biblioteca-linguagem.MD`

---

## Checklist de Decisão Final

- [ ] Todas as entrevistas previstas foram realizadas e documentadas
- [ ] Critérios das etapas 1 a 5 foram atendidos sem pendências críticas
- [ ] Hipóteses possuem classificação clara com evidências
- [ ] Próximas ações foram definidas com owner e prazo
- [ ] Stakeholders principais receberam ou receberão resumo executivo

### Resultado

- [ ] Aprovar resultados e avançar para próximos passos planejados
- [ ] Aprovar com ressalvas (listar ajustes necessários abaixo)
- [ ] Repetir ou estender rodada de entrevistas antes de prosseguir

Observações finais:

Responsável pela validação:
Data:
