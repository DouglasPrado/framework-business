# Processo: SaaSReverseEngineering

## Visão Geral

Processo sistemático de análise de competidores SaaS através de materiais públicos para identificar oportunidades de criar produto similar mas diferenciado.

**Tempo estimado:** 3-5 horas
**Resultado:** Hipóteses de diferenciação acionáveis prontas para validação (ex: estratégia ZeroUm)

---

## Quando Usar Este Processo

Use este processo quando você quer:
- Entrar em mercado SaaS já validado com diferencial claro
- Entender competidores antes de definir posicionamento
- Identificar gaps e oportunidades em mercado existente
- Gerar hipóteses de produto baseadas em análise competitiva
- Ter base estruturada antes de executar ZeroUm ou validação

**NÃO use se:**
- Você quer criar produto completamente novo (sem competidores)
- Você já tem diferencial claro e só precisa validar
- Você não tem 3-5 horas para análise sistemática

---

## Estrutura do Processo

### Arquivos Principais

1. **[process.MD](process.MD)** - Fluxo operacional detalhado
   - 6 etapas do processo
   - Pontos de decisão
   - Resultados esperados
   - Avisos e armadilhas

2. **[knowledge.MD](knowledge.MD)** - Base de conhecimento
   - Conceitos fundamentais
   - Frameworks de análise
   - Boas práticas
   - Exemplos de referência
   - FAQs

3. **[tasks.MD](tasks.MD)** - Checklist operacional
   - Tarefas detalhadas por etapa
   - Responsáveis e critérios de conclusão
   - Outputs esperados
   - Exemplos de preenchimento

4. **[validator.MD](validator.MD)** - Critérios de qualidade
   - Validação por etapa
   - Checklist de qualidade completa
   - Indicadores de sucesso
   - Sinais de alerta

### Pasta _DATA

**Templates (_DATA/templates/):**
- [contexto-negocio.md](_DATA/templates/contexto-negocio.md) - Captura de objetivos e restrições
- [mapeamento-urls.md](_DATA/templates/mapeamento-urls.md) - Organização de competidores e URLs
- [analise-competidor.md](_DATA/templates/analise-competidor.md) - Estrutura de análise individual
- [hipoteses-diferenciacao.md](_DATA/templates/hipoteses-diferenciacao.md) - Geração de hipóteses

**Exemplos (_DATA/examples/):**
- [exemplo-analise-completa.md](_DATA/examples/exemplo-analise-completa.md) - Exemplo fictício do processo end-to-end

---

## Fluxo em 6 Etapas

### Etapa 1: Coleta de Contexto (15 min)
Capture objetivos, mercado-alvo e restrições antes de analisar competidores.

**Output:** Documento de contexto
**Template:** `_DATA/templates/contexto-negocio.md`

### Etapa 2: Mapeamento de URLs (20 min)
Identifique 3-5 competidores e organize 15-30 URLs para análise.

**Output:** Lista organizada de competidores e URLs
**Template:** `_DATA/templates/mapeamento-urls.md`

### Etapa 3: Extração de Informações (60-90 min)
Colete informações das URLs via scraping automatizado + fallback manual.

**Output:** 3-5 arquivos com dados brutos por competidor
**Template:** `_DATA/templates/analise-competidor.md` (Parte 1)

### Etapa 4: Análise Individual (45-60 min)
Sintetize informações coletadas em análise estruturada por competidor.

**Output:** 3-5 análises completas
**Template:** `_DATA/templates/analise-competidor.md` (Parte 2)

### Etapa 5: Síntese Comparativa (30-45 min)
Compare competidores para identificar convergências, divergências e gaps.

**Output:** Documento de síntese com oportunidades identificadas

### Etapa 6: Hipóteses de Diferenciação (30-45 min)
Transforme gaps em hipóteses acionáveis, priorize e defina próximos passos.

**Output:** 5-10 hipóteses, top 2-3 priorizadas, próximos passos
**Template:** `_DATA/templates/hipoteses-diferenciacao.md`

---

## Como Começar

### Opção 1: Leitura Rápida (5 minutos)
1. Leia este README completamente
2. Leia "Visão Geral" e "Quando Usar" no [knowledge.MD](knowledge.MD)
3. Veja [exemplo-analise-completa.md](_DATA/examples/exemplo-analise-completa.md)
4. Comece pela Etapa 1 usando template

### Opção 2: Preparação Completa (20 minutos)
1. Leia [process.MD](process.MD) - entenda fluxo completo
2. Leia "Conceitos Fundamentais" no [knowledge.MD](knowledge.MD)
3. Revise templates em `_DATA/templates/`
4. Prepare contexto de negócio (Etapa 1)
5. Execute processo passo a passo

### Opção 3: Execução Guiada (use [tasks.MD](tasks.MD))
1. Abra [tasks.MD](tasks.MD)
2. Execute Tarefa 1 (usa template de contexto)
3. Execute Tarefa 2 (usa template de mapeamento)
4. Continue sequencialmente até Tarefa 6
5. Use [validator.MD](validator.MD) para verificar qualidade

---

## Checklist Rápido de Qualidade

Antes de concluir, verifique:

- [ ] **Contexto claro:** Objetivos, mercado, restrições documentados
- [ ] **3-5 competidores** analisados
- [ ] **70%+ de completude** na extração de informações
- [ ] **Síntese comparativa** identifica pelo menos 3 gaps/oportunidades
- [ ] **5+ hipóteses** geradas
- [ ] **Top 2-3 hipóteses** priorizadas com justificativa
- [ ] **Próximos passos** definidos (ex: executar ZeroUm)
- [ ] **Alinhamento** com contexto de negócio mantido

---

## Próximos Passos Após Conclusão

Após completar este processo, você terá hipótese(s) de diferenciação pronta(s) para validação.

**Processos subsequentes recomendados:**

1. **Estratégia ZeroUm**
   - Use hipótese escolhida como Etapa 0 (Clarificação)
   - Valide problema e diferencial com usuários
   - Lance MVP diferenciado em 14 dias

2. **Entrevistas de Validação de Problema**
   - Teste hipótese de diferenciação com ICP específico
   - Confirme que gap identificado é oportunidade real
   - Refine hipótese baseado em feedback

3. **Definição de Posicionamento**
   - Use insights de análise para posicionamento claro
   - Articule diferencial de forma que ressoe com ICP
   - Crie messaging baseado em linguagem observada

---

## Referências e Conexões

### Conecta com Estratégias
- **ZeroUm:** Usa hipótese de diferenciação como Etapa 0
- **MVPBuilder:** Usa análise competitiva para definir features e posicionamento

### Conecta com Processos
- **ProblemHypothesisDefinition:** Pode ser complementado por análise competitiva
- **TargetUserIdentification:** ICP observado informa identificação de usuários-alvo

### Artefatos Compartilhados
Nenhum identificado ainda. Se templates deste processo forem usados por outros processos, considere mover para `process/_SHARED/`.

---

## Manutenção e Versionamento

**Versão atual:** 1.0
**Última atualização:** 2025-01-06
**Mantido por:** Equipe de Produto

### Quando revisar este processo:
- Após cada execução, documente aprendizados
- Se novos padrões de análise forem identificados
- Se ferramentas melhores de scraping emergirem
- Se exemplos adicionais forem criados
- A cada 3-6 meses para manutenção geral

---

## Suporte e Dúvidas

- **Dúvidas sobre conceitos:** Consulte [knowledge.MD](knowledge.MD) seção FAQs
- **Dúvidas sobre execução:** Consulte [tasks.MD](tasks.MD) com passos detalhados
- **Dúvidas sobre qualidade:** Consulte [validator.MD](validator.MD) com critérios
- **Ver exemplo prático:** Consulte [_DATA/examples/exemplo-analise-completa.md](_DATA/examples/exemplo-analise-completa.md)

---

**Pronto para começar? Abra [tasks.MD](tasks.MD) e execute Tarefa 1!**
