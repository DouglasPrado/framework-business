## Propósito

Garantir que a execução semanal do processo de OutreachCampaign atingiu qualidade suficiente para alimentar o funil comercial e produzir aprendizados acionáveis.

## Como Usar Este Validador

1. Realize a verificação ao final da semana, após preencher todos os templates em `_DATA/`.
2. Avalie cada critério marcando Aprovado/Reprovado/Parcial.
3. Registre evidências nos campos indicados (arquivo, linha, print, link).
4. Se houver reprovação, corrija e revalide antes de iniciar a próxima semana.
5. Arquive o validador preenchido em `_DATA/` junto ao relatório semanal.

## Critérios de Validação

### V1: Volume de abordagens

Critério: foram registradas pelo menos 50 abordagens semanais com distribuição adequada por canal.

Verificações:
- [ ] `registro-interacoes.MD` contém ≥ 50 entradas únicas.
- [ ] Há registros em pelo menos dois canais diferentes.
- [ ] Cada entrada possui status e próxima ação preenchidos.
- [ ] Metas diárias documentadas em `planejamento-semanal.MD` foram atingidas ou justificadas.

Status: [ ] Aprovado [ ] Reprovado [ ] Parcial

Evidência:
```
Número total de abordagens:
Canais utilizados:
Observações:
```

Ação corretiva (se reprovado):
- Revisar Etapas 1 a 4 para aumentar volume.
- Expandir lista de contatos e canais na próxima semana.
- Ajustar blocos de tempo e responsáveis.

---

### V2: Taxa de resposta e conversas qualificadas

Critério: taxa de resposta ≥ 10% e pelo menos 5 conversas qualificadas registradas.

Verificações:
- [ ] `analise-metricas.MD` apresenta taxa de resposta calculada.
- [ ] Taxa de resposta ≥ 10% (ou justificativa documentada se inferior).
- [ ] `registro-interacoes.MD` identifica ≥ 5 conversas qualificadas com notas.
- [ ] Conversas qualificadas incluem próximos passos definidos.

Status: [ ] Aprovado [ ] Reprovado [ ] Parcial

Evidência:
```
Taxa de resposta:
Número de conversas qualificadas:
Principais aprendizados:
```

Ação corretiva (se reprovado):
- Ajustar scripts em `_DATA/matriz-mensagens.MD`.
- Revisar segmentação em `planejamento-semanal.MD`.
- Executar testes A/B com novas abordagens.

---

### V3: Calls agendadas

Critério: pelo menos 2 calls agendadas com briefing completo.

Verificações:
- [ ] Agenda da semana registra ≥ 2 calls confirmadas.
- [ ] Cada call possui objetivo, data/hora e link definidos.
- [ ] Mini-briefing inclui dor, contexto e CTA desejado.
- [ ] Follow-up pós-call agendado em `registro-interacoes.MD`.

Status: [ ] Aprovado [ ] Reprovado [ ] Parcial

Evidência:
```
Call 1: (data, objetivo, link)
Call 2: (data, objetivo, link)
Call 3: (se existir)
Observações adicionais:
```

Ação corretiva (se reprovado):
- Intensificar follow-ups nas Etapas 5 e 6.
- Reforçar CTA de call nas mensagens principais.
- Avaliar oferta de valor e objeções registradas.

---

### V4: Registro e rastreabilidade

Critério: todos os registros estão completos e padronizados.

Verificações:
- [ ] `planejamento-semanal.MD` contém blocos preenchidos e metas.
- [ ] `registro-interacoes.MD` possui status atualizado para cada contato.
- [ ] Objeções documentadas em `controle-objecoes.MD` com segmento, causa e resposta.
- [ ] Evidências (prints, áudios, agendas) armazenadas em subpastas datadas.

Status: [ ] Aprovado [ ] Reprovado [ ] Parcial

Evidência:
```
Arquivos revisados:
Itens ausentes ou inconsistentes:
```

Ação corretiva (se reprovado):
- Atualizar registros faltantes imediatamente.
- Treinar responsáveis sobre padrão de preenchimento.
- Implementar checkpoints diários na Etapa 8.

---

### V5: Aprendizados e ajustes

Critério: relatório semanal contém análise, aprendizados e plano de ajustes.

Verificações:
- [ ] `analise-metricas.MD` lista métricas principais e comparação com metas.
- [ ] Aprendizados e hipóteses documentados ao final do relatório.
- [ ] Próximos passos definidos com responsável e data.
- [ ] Decisão sobre tráfego pago registrada (executar, testar, pausar, não usar).

Status: [ ] Aprovado [ ] Reprovado [ ] Parcial

Evidência:
```
Principais aprendizados:
Ajustes propostos:
Status do tráfego pago:
```

Ação corretiva (se reprovado):
- Revisitar Etapa 7 e preencher relatório completo.
- Alinhar com stakeholders antes da próxima semana.
- Garantir que decisões influenciem o planejamento seguinte.

---

### V6: Compliance e ética

Critério: campanha respeitou políticas de canais e boas práticas de dados.

Verificações:
- [ ] Nenhum canal reportou bloqueio ou denúncia.
- [ ] Todos os envios respeitaram limites e regras das comunidades.
- [ ] Links e UTMs configurados corretamente (sem erros 404 ou redirecionamentos proibidos).
- [ ] Consentimentos registrados quando houve compartilhamento de dados pessoais sensíveis.

Status: [ ] Aprovado [ ] Reprovado [ ] Parcial

Evidência:
```
Incidentes ou alertas registrados:
Ações tomadas:
```

Ação corretiva (se reprovado):
- Ajustar cadência de envios.
- Revisar mensagens para garantir conformidade.
- Comunicar stakeholders sobre incidentes e plano de mitigação.

---

## Resumo da Validação

Total de critérios avaliados: 6
Critérios aprovados: _____
Critérios parciais: _____
Critérios reprovados: _____

Porcentagem de aprovação: _____%

Resultado final:
- [ ] APROVADO (≥ 85% critérios aprovados, sem reprovação crítica)
- [ ] APROVADO COM RESSALVAS (70-84% aprovados)
- [ ] REPROVADO (< 70% aprovados)

Principais gaps identificados:
```
1.
2.
3.
```

Próximos passos:
```
1.
2.
3.
```

Validador responsável:
Nome:
Data: ___/___/___
Assinatura/Aprovação:
