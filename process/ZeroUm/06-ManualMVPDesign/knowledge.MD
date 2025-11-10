# Base de Conhecimento - ManualMVPDesign

## Visão Geral

Manual MVP é uma versão mínima do produto/serviço entregue com operações manuais, desenhada para validar proposta de valor, experiência do cliente e viabilidade operacional antes de investir em tecnologia. Também chamado de “concierge” ou “wizard of oz”, o formato privilegia contato direto, aprendizado rápido e flexibilidade para experimentar entregas.

## Objetivo Central

Criar um sistema manual replicável que permita:
- Testar a proposta de valor com clientes reais entregando a experiência prometida
- Medir tempos, custos e esforço operacional por etapa
- Documentar padrões e exceções para orientar automações futuras
- Garantir consistência na comunicação e na qualidade da entrega

## Princípios Fundamentais

1. **Clareza de promessas:** defina exatamente o que o MVP entrega, quando e em qual formato.
2. **Processo visível:** todo passo deve estar documentado e rastreável na ferramenta escolhida.
3. **Medição constante:** registre tempo, esforço e feedback em cada rodada.
4. **Feedback rápido:** use follow-up manual para coletar percepção do cliente e ajustar rapidamente.
5. **Padrões rígidos:** qualidade manual precisa ser mais alta que a esperada da versão automatizada.

## Conceitos-Chave

### Concierge vs. Wizard of Oz
- **Concierge:** usuário sabe que há suporte humano (ex: consultor dedicado).
- **Wizard of Oz:** usuário acredita em automação, mas operações são manuais. Exige atenção extra à consistência e timing.

### Macro Etapas do Fluxo
1. **Recebimento:** entrada de pedido ou solicitação.
2. **Onboarding:** confirmação de dados, alinhamento de expectativas.
3. **Produção:** execução manual da entrega principal.
4. **QA:** validação interna antes de entregar ao cliente.
5. **Entrega:** envio do resultado com instruções.
6. **Follow-up:** captura de feedback, upsell e próximos passos.

### SLA Manual
Tempo máximo combinado para cada etapa. Use o briefing para definir metas e ajuste após o piloto.

### Ciclo de Aprendizado
Executar → medir → ajustar → documentar → treinar → repetir. O manual MVP só gera valor quando cada iteração deixa o processo mais previsível.

## Materiais Essenciais (ver `_DATA/`)

- `briefing-manual-mvp.MD`: visão geral, metas e restrições.
- `mapa-fluxo-entrega.MD`: descrição granular do fluxo.
- `estrutura-board.MD`: configuração sugerida da ferramenta de gestão.
- `checklist-execucao.MD`: tarefas passo a passo com responsáveis.
- `modelo-email-*.MD`: templates de comunicação.
- `relatorio-piloto.MD`: registro de tempos e aprendizados do piloto.
- `padroes-qualidade.MD`: critérios mínimos por etapa.
- `manual-operacional-final.MD`: compilação da versão aprovada.
- `inventario-materiais.MD`: lista de assets, links e donos.

## Boas Práticas por Etapa

### Recebimento
- Validar dados essenciais imediatos (contato, formato esperado, prazo).
- Confirmar escopo conforme briefing antes de aceitar entrega.

### Onboarding
- Reforçar promessa, prazo e condições.
- Solicitar insumos com data limite clara.
- Usar checklist para evitar omissões (acessos, arquivos, responsáveis).

### Produção Manual
- Quebrar tarefas em blocos pequenos com estimativa.
- Registrar tempo real gasto por bloco (cronômetro + anotação).
- Anotar improvisos ou recursos adicionais usados.

### QA
- Revisar contra padrões de qualidade (consistência, completude, precisão).
- Incluir dupla checagem quando possível (operador e revisor).
- Documentar erros encontrados para análise posterior.

### Entrega
- Personalizar mensagens com próximos passos.
- Anexar instruções para uso e canais de suporte.
- Registrar confirmação de recebimento.

### Follow-up
- Agendar contato nas primeiras 24-48h.
- Perguntar sobre clareza, valor percebido e pontos de atrito.
- Atualizar inventário com feedback que gera novos materiais.

## Perguntas Frequentes

**Quanto tempo deve durar um ciclo manual?**  
Idealmente 1-2 semanas de operação completa, permitindo ajustes semanais.

**Quando devo automatizar etapas?**  
Após completar múltiplos ciclos com tempos estáveis e entender onde a automação gera maior impacto (custos altos, gargalos constantes).

**Como lidar com variações entre clientes?**  
Documente exceções no relatório do piloto e crie fluxos alternativos só quando a variação se repetir em pelo menos 20% dos casos.

**E se o cliente pedir algo fora do escopo?**  
Use o checklist para avaliar impacto. Se aceitar, documente a exceção e ajuste o briefing futuro ou crie oferta complementar.

**Qual ferramenta usar para o board?**  
Priorize o que o time domina (Google Sheets, Notion, Trello), garantindo que conste em `tools/`. O importante é permitir filtros por status, responsável e SLA.

## Checkpoints de Qualidade

1. **Briefing aprovado:** escopo e SLA validados por stakeholder de negócio.
2. **Fluxo com tempos:** cada etapa possui estimativa e responsável definido.
3. **Board testado:** equipe consegue atualizar status sem suporte adicional.
4. **Templates revisados:** linguagem alinha promessa e limitações do MVP manual.
5. **Piloto concluído:** tempos reais registrados, gargalos identificados.
6. **Documentação final:** manual, padrões e inventário prontos para operação.

## Riscos e Mitigações

- **Tempo excedido:** acompanhe variação diária; se ultrapassar 20%, redefina escopo ou acrescente recurso.
- **Dependência de pessoas-chave:** documente cada etapa no manual operacional para facilitar treinamento.
- **Erros na entrega:** aplique QA rigoroso e revise padrões de qualidade após cada incidente.
- **Comunicação desalinhada:** mantenha templates atualizados e considere checklists específicos de comunicação.
- **Materiais dispersos:** use inventário e links estáveis (Drive, Notion) com versão controlada.

## Integrações com Outros Processos

- **Antes:** validar hipótese e público ([ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD), [TargetUserIdentification](../02-TargetUserIdentification/process.MD), [UserInterviewValidation](../03-UserInterviewValidation/process.MD)).
- **Depois:** utilizar materiais para landing pages, campanhas e automações futuras ([LandingPageCreation](../LandingPageCreation/process.MD)).
- **Paralelos:** atualizar estratégia em `strategies/ZeroUm` com aprendizados operacionais.

## Métricas Sugeridas

- Tempo médio por etapa vs. meta.
- Custo/hora estimado vs. real (opcional).
- Taxa de tarefas concluídas sem retrabalho.
- Nível de satisfação coletado no follow-up (escala textual).
- Volume de exceções registradas por ciclo.

## Recursos Externos Recomendados

- Conceitos de “Concierge MVP” (The Lean Startup).
- Estudos de caso de “Wizard of Oz” aplicados em SaaS e serviços.
- Guias de mapeamento de processos (ex: SIPOC simplificado).
- Ferramentas de cronometragem (Toggl, Clockify) — confirmar aprovação em `tools/`.

## Próximos Passos Após Conclusão

1. Planejar nova rodada com clientes reais monitorando métricas definidas.
2. Avaliar quais etapas merecem automação parcial ou templates adicionais.
3. Atualizar estratégia e backlog com aprendizados do piloto.
4. Treinar novos operadores usando o manual e checklist final.
5. Reavaliar padrões de qualidade a cada duas rodadas ou quando surgirem novas demandas.
