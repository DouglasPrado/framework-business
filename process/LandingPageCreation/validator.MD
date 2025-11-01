# Validador - LandingPageCreation

## Propósito

Assegurar que a landing page publicada cumpre padrões de qualidade, mensuração e alinhamento com hipóteses validadas. Use este validador após concluir todas as etapas do processo para aprovar (ou reprovar) a entrega antes de encaminhar tráfego.

## Como Usar

1. Revise cada seção correspondente às etapas do processo.
2. Marque os critérios atendidos com base em evidências armazenadas em `_DATA/`.
3. Registre observações e ações corretivas quando necessário.
4. Utilize o checklist de decisão final para aprovar ou solicitar ajustes.

---

## Validação da Etapa 1 – Briefing

**Critério 1.1 – Hipóteses e objetivos claros**
- [ ] `briefing-landing.MD` contém objetivo principal (lead, pré-venda ou outro) e meta de conversão.
- [ ] Hipóteses validadas foram referenciadas (link para UserInterviewValidation ou ProblemHypothesisDefinition).
- [ ] Público-alvo e proposta de valor estão descritos com clareza.

**Critério 1.2 – Preparação operacional**
- [ ] Ferramenta selecionada consta no catálogo `tools/` (ou aprovação documentada).
- [ ] Acessos a contas, domínios e analytics registrados.
- [ ] Pendências pré-produção listadas e endereçadas.

Evidência: `_DATA/briefing-landing.MD`

---

## Validação da Etapa 2 – Estrutura

**Critério 2.1 – Narrativa completa**
- [ ] `estrutura-secoes.MD` inclui todas as seções obrigatórias (Hero, Problema, Solução, Benefícios, Prova Social, Oferta, FAQ, CTA).
- [ ] A ordem das seções segue fluxo lógico (dor → solução → prova → chamada).
- [ ] CTA principal definindo próxima ação está destacado.

**Critério 2.2 – Recursos mapeados**
- [ ] Assets necessários foram listados com owner e status.
- [ ] Possíveis gaps (imagens, ícones, vídeos) possuem plano B.

Evidência: `_DATA/estrutura-secoes.MD`

---

## Validação da Etapa 3 – Copy

**Critério 3.1 – Aderência à linguagem do cliente**
- [ ] Headlines e bullets utilizam termos provenientes da biblioteca de linguagem.
- [ ] Pelo menos três bullets de benefícios estão presentes.
- [ ] FAQ responde às objeções identificadas em entrevistas.

**Critério 3.2 – Prova social e CTA**
- [ ] Prova social contém citação com contexto (nome/cargo ou segmento) e autorização.
- [ ] CTA principal e microcopy estão alinhados à ação desejada.
- [ ] Copy passou por revisão ortográfica.

Evidência: `_DATA/copy-draft.MD`, referências às entrevistas em `_DATA/` anterior

---

## Validação da Etapa 4 – Construção

**Critério 4.1 – Fidelidade ao planejamento**
- [ ] Página em staging reproduz estrutura e copy previstas.
- [ ] Links internos e externos funcionalmente testados (preview).
- [ ] Estilos visuais preservam consistência (cores, tipografia, espaçamento).

**Critério 4.2 – Documentação**
- [ ] Link de preview registrado em `_DATA/`.
- [ ] Pendências pré-QA listadas e resolvidas antes da publicação.

Evidência: Link de preview, notas de implementação

---

## Validação da Etapa 5 – Integrações e Analytics

**Critério 5.1 – Formulários e integrações**
- [ ] Formulário envia dados corretamente (testes registrados com prints ou logs).
- [ ] Integração com CRM/planilha/e-mail confirmada.
- [ ] Mensagens de sucesso/erro configuradas.

**Critério 5.2 – Mensuração**
- [ ] Scripts/pixels instalados e validados (modo debug, print do disparo).
- [ ] Eventos principais configurados (PageView, Lead, Purchase/clique CTA).
- [ ] `_DATA/plano-analytics.MD` contém UTMs padrão, responsáveis e cadência de análise.

---

## Validação da Etapa 6 – QA e Publicação

**Critério 6.1 – Qualidade técnica**
- [ ] `_DATA/checklist-qa.MD` concluído sem pendências críticas.
- [ ] Tempo de carregamento ≤ 3s desktop e ≤ 4s mobile (print ou relatório anexado).
- [ ] Página responsiva (prints ou evidências em pelo menos duas resoluções).

**Critério 6.2 – Publicação e comunicação**
- [ ] URL final publicada e acessível.
- [ ] Stakeholders notificados com link e instruções (registro em notas).
- [ ] Backlog de otimizações pós-lançamento criado (quando necessário).

---

## Checklist de Decisão Final

- [ ] Todos os critérios das etapas 1-6 estão atendidos.
- [ ] Evidências e arquivos armazenados em `_DATA/`.
- [ ] Ferramentas utilizadas constam no catálogo `tools/` ou possuem aprovação registrada.
- [ ] Plano de métricas e monitoramento ativado.
- [ ] Próximos passos definidos (ex: iniciar tráfego, preparar teste A/B, acionar CheckoutSetup).

### Resultado

- [ ] Aprovar lançamento (pronto para tráfego)
- [ ] Aprovar com ajustes menores (detalhar abaixo)
- [ ] Não aprovado (requer correções antes do tráfego)

Observações finais:

Responsável pela validação:
Data:
