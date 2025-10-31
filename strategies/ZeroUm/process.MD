# Processo de Execução - Estratégia ZeroUm

Este documento detalha o fluxo de execução da estratégia ZeroUm, incluindo sequências, dependências, pontos de decisão e loops de feedback.

## Visão geral do fluxo

```
ETAPA 0 → ETAPA 1 → ETAPA 2 → ETAPA 3 → ETAPA 5 → ETAPA 6 → ETAPA 7
  (30m)    (2-4d)     (1d)      (horas)              (1-2d)   (contínuo)
                                    ↓
                                ETAPA 4
                               (1-2 sem)
```

## Etapa 0: Esclarecer a ideia (30 minutos)

### Objetivo
Cristalizar a proposta de valor em uma frase que qualquer pessoa entenda em 10 segundos.

### Sequência de ações

```
1. Listar usuários-alvo (5 min)
   ↓
2. Identificar dor central (10 min)
   ↓
3. Redigir 3 variações da frase (10 min)
   ↓
4. Ler em voz alta e validar clareza (5 min)
```

### Ponto de decisão 1
**A frase está clara?**
- ✅ SIM → Avançar para Etapa 1
- ❌ NÃO → Voltar ao passo 3 e simplificar

### Critério de qualidade
- [ ] Explica quem é o público
- [ ] Descreve o resultado específico
- [ ] Menciona a dor principal evitada
- [ ] Pode ser compreendida em 10 segundos
- [ ] Não menciona funcionalidades técnicas

### Output
`proposta-de-valor.txt` com a frase validada

---

## Etapa 1: Validação de problema (2-4 dias)

### Objetivo
Confirmar que a dor existe e coletar linguagem real dos clientes.

### Sequência de ações

```
DIA 1
├─ Manhã: Criar 3 personas detalhadas (2h)
├─ Tarde: Definir 3 hipóteses testáveis (1h)
└─ Noite: Preparar script de entrevista (1h)

DIA 2-3
├─ Realizar 10 entrevistas (5-15 min cada)
├─ Anotar dores, soluções atuais, objeções
└─ Gravar ou documentar linguagem exata

DIA 4
├─ Analisar padrões nas respostas
├─ Classificar hipóteses (validada/refutada/inconclusiva)
└─ Documentar aprendizados
```

### Ponto de decisão 2
**Pelo menos 7 de 10 entrevistados confirmam a dor?**
- ✅ SIM → Avançar para Etapa 2
- ❌ NÃO → Pivotar persona ou problema

### Ponto de decisão 3
**Ao menos 3 entrevistados demonstraram disposição a pagar?**
- ✅ SIM → Confirmar preço e avançar
- ❌ NÃO → Revisar valor percebido ou público-alvo

### Critério de qualidade
- [ ] 10 entrevistas realizadas
- [ ] Anotações com padrões identificados
- [ ] Linguagem real documentada
- [ ] Hipóteses classificadas
- [ ] Personas ajustadas com base no feedback

### Output
- `personas.md` com 3 personas validadas
- `hipoteses.md` com status de validação
- `entrevistas.csv` com anotações
- `linguagem-cliente.txt` com termos exatos

---

## Etapa 2: Landing page de pré-venda (1 dia)

### Objetivo
Medir interesse real antes de construir produto.

### Sequência de ações

```
MANHÃ (3-4h)
├─ Escolher ferramenta (30 min)
├─ Estruturar layout (1h)
│  ├─ Headline (frase da Etapa 0)
│  ├─ 3 bullets de benefícios
│  ├─ Prova social (quotes das entrevistas)
│  ├─ Preço ou oferta
│  └─ CTAs (formulário + comprar)
└─ Criar primeira versão (2h)

TARDE (2-3h)
├─ Configurar analytics (30 min)
├─ Testar em desktop e mobile (30 min)
├─ Validar CTAs e formulários (30 min)
└─ Publicar e obter URL final (30 min)
```

### Ponto de decisão 4
**Landing page carrega em menos de 3 segundos?**
- ✅ SIM → Prosseguir
- ❌ NÃO → Otimizar imagens e código

### Ponto de decisão 5
**CTAs funcionam corretamente em mobile?**
- ✅ SIM → Publicar
- ❌ NÃO → Corrigir responsividade

### Critério de qualidade
- [ ] Headline clara e direta
- [ ] 3 bullets focados em benefícios
- [ ] Prova social real das entrevistas
- [ ] Preço visível (ou "a partir de")
- [ ] 2 CTAs funcionais
- [ ] Analytics configurado
- [ ] Testado em mobile e desktop

### Output
- URL da landing page publicada
- `landing-metrics.xlsx` para tracking

---

## Etapa 3: Checkout mínimo (algumas horas)

### Objetivo
Configurar sistema de pagamento funcional.

### Sequência de ações

```
1. Escolher solução de pagamento (30 min)
   ↓
2. Criar link de pagamento (30 min)
   ↓
3. Testar pagamento simbólico (15 min)
   ↓
4. Integrar link ao botão "Comprar" (30 min)
   ↓
5. Preparar e-mail de confirmação (30 min)
   ↓
6. Criar página de obrigado (30 min)
```

### Ponto de decisão 6
**Pagamento de teste funcionou completamente?**
- ✅ SIM → Ativar checkout na landing
- ❌ NÃO → Revisar integração

### Ponto de decisão 7
**Notificação de pagamento chega em tempo real?**
- ✅ SIM → Prosseguir
- ❌ NÃO → Configurar webhooks ou alertas

### Critério de qualidade
- [ ] Link de pagamento ativo
- [ ] Teste de pagamento realizado
- [ ] Notificação funcionando
- [ ] E-mail de confirmação pronto
- [ ] Página de obrigado configurada
- [ ] Recibo ou contrato simples preparado

### Output
- Link de checkout funcional
- `pagamentos.xlsx` para controle manual

---

## Etapa 4: MVP operável manual (1-2 semanas)

⚠️ **Atenção:** Esta etapa pode ser executada em paralelo com Etapa 5.

### Objetivo
Preparar processo de entrega sem automação complexa.

### Sequência de ações

```
SEMANA 1
├─ Dia 1-2: Mapear fluxo de entrega
│  ├─ Recebimento do pedido
│  ├─ Onboarding do cliente
│  ├─ Produção/execução
│  └─ Entrega e follow-up
│
├─ Dia 3-4: Escolher ferramentas
│  └─ Google Sheets / Notion / Trello
│
└─ Dia 5: Criar templates
   ├─ E-mails de onboarding
   ├─ Checklist de entrega
   └─ Materiais padrão

SEMANA 2
├─ Dia 1-2: Teste piloto interno
├─ Dia 3: Cronometrar etapas
├─ Dia 4: Ajustar gargalos
└─ Dia 5: Documentar processo final
```

### Ponto de decisão 8
**Consegue entregar resultado em menos de 7 dias?**
- ✅ SIM → Processo viável para primeiros clientes
- ❌ NÃO → Simplificar escopo ou aumentar preço

### Ponto de decisão 9
**Processo pode ser replicado sem você?**
- ✅ SIM → Documentação suficiente
- ❌ NÃO → Criar checklist mais detalhado

### Critério de qualidade
- [ ] Fluxo completo mapeado
- [ ] Templates de comunicação prontos
- [ ] Checklist de entrega criado
- [ ] Teste piloto realizado
- [ ] Tempo de entrega cronometrado
- [ ] Processo documentado

### Output
- `processo-entrega.md` detalhado
- `templates-email/` com mensagens prontas
- `checklist-entrega.md` passo a passo

---

## Etapa 5: Tração inicial (contínuo)

### Objetivo
Gerar primeiros leads qualificados com baixo custo.

### Sequência de ações (ciclo semanal)

```
SEGUNDA
├─ Listar 10 contatos qualificados (1h)
└─ Personalizar abordagem para cada um (1h)

TERÇA-QUARTA
├─ Enviar 10 mensagens personalizadas/dia (2x 30 min)
└─ Registrar status em planilha (30 min)

QUINTA-SEXTA
├─ Responder conversas iniciadas (1h)
├─ Agendar calls de vendas (30 min)
└─ Publicar 1 conteúdo (LinkedIn/Instagram) (1h)

SÁBADO
└─ Analisar métricas da semana (1h)
   ├─ Abordagens enviadas
   ├─ Respostas recebidas
   ├─ Conversas qualificadas
   └─ Vendas fechadas
```

### Ponto de decisão 10
**Taxa de resposta está abaixo de 10%?**
- ✅ SIM → Revisar personalização da mensagem
- ❌ NÃO → Manter abordagem atual

### Ponto de decisão 11
**Após 50 abordagens, menos de 2 conversas qualificadas?**
- ✅ SIM → Revisar público-alvo ou oferta
- ❌ NÃO → Escalar volume de prospecção

### Canais prioritários

```
1. REDE DE CONTATOS (primeiro)
   └─ 50 mensagens personalizadas

2. COMUNIDADES ONLINE (segundo)
   ├─ WhatsApp, Telegram
   ├─ LinkedIn, Facebook Groups
   └─ Fóruns especializados

3. CONTEÚDO ORGÂNICO (paralelo)
   ├─ 1 post LinkedIn/semana
   └─ 1 post Instagram/semana

4. COLD OUTREACH (se necessário)
   └─ DMs personalizados

5. TRÁFEGO PAGO (opcional)
   └─ R$ 50-150 para teste
```

### Critério de qualidade
- [ ] 50 contatos abordados
- [ ] 5-10 conversas iniciadas
- [ ] Mensagens personalizadas (não massa)
- [ ] Status rastreado em planilha
- [ ] Objeções documentadas

### Output
- `leads.xlsx` com status atualizado
- `objecoes.md` com padrões identificados

---

## Etapa 6: Fechamento do primeiro cliente (1-2 dias)

### Objetivo
Converter lead em cliente pagante e entregar valor.

### Sequência de ações

```
DIA 1: FECHAMENTO
├─ 1. Agendar call de 15-20 min
├─ 2. Conduzir conversa de vendas
│  ├─ Abertura: reconhecer contexto
│  ├─ Diagnóstico: confirmar dor
│  ├─ Proposta: apresentar solução
│  └─ Alinhamento: próximos passos
│
├─ 3. Enviar link de pagamento
├─ 4. Confirmar recebimento
└─ 5. Enviar e-mail com próximos passos

DIA 2: ENTREGA
├─ 1. Onboarding rápido
├─ 2. Executar processo documentado
├─ 3. Entregar resultado
├─ 4. Check-in com cliente
└─ 5. Solicitar depoimento
```

### Ponto de decisão 12
**Cliente demonstrou objeção ao preço?**
- ✅ SIM → Reforçar valor e urgência da oferta piloto
- ❌ NÃO → Prosseguir para pagamento

### Ponto de decisão 13
**Cliente adiou decisão?**
- ✅ SIM → Agendar follow-up em 48h
- ❌ NÃO → Enviar link de pagamento

### Ponto de decisão 14
**Cliente recebeu e percebeu valor entregue?**
- ✅ SIM → Solicitar depoimento
- ❌ NÃO → Agendar call para alinhar expectativas

### Critério de qualidade
- [ ] Call realizada e gravada (se autorizado)
- [ ] Pagamento confirmado
- [ ] Entrega realizada no prazo
- [ ] Cliente satisfeito (NPS > 8)
- [ ] Depoimento coletado com autorização

### Output
- `cliente-001/` com dossiê completo
- Depoimento em texto/áudio/vídeo
- `metricas-entrega.txt` com tempos

---

## Etapa 7: Aprendizado e iteração (contínuo)

### Objetivo
Extrair lições e planejar melhorias com base em dados reais.

### Sequência de ações (ciclo quinzenal)

```
RETROSPECTIVA (a cada 2 semanas)
├─ 1. Compilar métricas
│  ├─ Tráfego landing
│  ├─ Taxa de conversão
│  ├─ Leads gerados
│  ├─ Vendas fechadas
│  └─ Tempo de entrega
│
├─ 2. Analisar feedback dos clientes
│  ├─ Motivo real da compra
│  ├─ Objeções mais comuns
│  └─ Sugestões de melhoria
│
├─ 3. Categorizar aprendizados
│  ├─ O que funcionou (manter)
│  ├─ O que não funcionou (corrigir)
│  └─ O que testar (experimentos)
│
└─ 4. Priorizar próximas ações (máx 3)
   ├─ Melhorias de processo
   ├─ Ajustes de copy/oferta
   └─ Automações necessárias
```

### Matriz de decisão

| Situação | Métrica | Ação |
|----------|---------|------|
| **Conversão baixa** | < 3% na landing | Revisar copy, testar novo público |
| **Lead não converte** | < 5% lead→venda | Ajustar preço ou oferta |
| **Entrega demorada** | > 7 dias | Automatizar etapa mais lenta |
| **Preço aceito fácil** | Sem objeção | Testar preço maior (+30%) |
| **Muita execução manual** | > 10h/cliente | Priorizar automação |

### Ponto de decisão 15
**Processo está escalável para 5 clientes simultâneos?**
- ✅ SIM → Focar em aquisição
- ❌ NÃO → Automatizar gargalos críticos

### Ponto de decisão 16
**Métricas melhoraram após ajustes?**
- ✅ SIM → Documentar o que funcionou
- ❌ NÃO → Considerar mudança de posicionamento

### Critério de qualidade
- [ ] Retrospectiva quinzenal realizada
- [ ] Métricas atualizadas
- [ ] 3 melhorias priorizadas
- [ ] Hipótese de negócio atualizada
- [ ] Aprendizados documentados

### Output
- `retrospectiva-[data].md` com lições
- `metricas-historico.xlsx` atualizado
- `roadmap-proximas-acoes.md`

---

## Loops de feedback

### Loop 1: Validação contínua de problema
```
Entrevistas (Etapa 1)
    ↓
Landing page (Etapa 2)
    ↓
Leads qualificados?
    ├─ SIM → Prosseguir
    └─ NÃO → Voltar e ajustar personas
```

### Loop 2: Otimização de conversão
```
Tração (Etapa 5)
    ↓
Conversão < 10%?
    ├─ SIM → Ajustar copy/oferta → Testar novamente
    └─ NÃO → Escalar volume
```

### Loop 3: Melhoria de entrega
```
Entregar cliente (Etapa 6)
    ↓
Tempo > 7 dias ou NPS < 8?
    ├─ SIM → Simplificar processo (Etapa 4) → Testar
    └─ NÃO → Documentar e padronizar
```

### Loop 4: Iteração de produto
```
Retrospectiva (Etapa 7)
    ↓
Identificar maior gargalo
    ↓
Priorizar 1 melhoria
    ↓
Implementar
    ↓
Medir impacto (2 semanas)
    ↓
Avaliar resultado → Nova retrospectiva
```

---

## Pontos de travamento comuns

### Travamento 1: Paralisia na Etapa 0
**Sintoma:** Passar mais de 2h refinando a frase
**Solução:** Escolher a melhor versão em 30 min e testar com público real

### Travamento 2: Entrevistas sem padrão (Etapa 1)
**Sintoma:** 10 entrevistas com respostas dispersas
**Solução:** Revisar perfil de persona e focar em nicho menor

### Travamento 3: Landing sem tráfego (Etapa 2)
**Sintoma:** Menos de 20 visitas na primeira semana
**Solução:** Começar com Etapa 5 (tração) antes de otimizar landing

### Travamento 4: MVP complexo demais (Etapa 4)
**Sintoma:** Processo de entrega com mais de 15 passos
**Solução:** Reduzir escopo para apenas o resultado principal

### Travamento 5: Nenhuma resposta na prospecção (Etapa 5)
**Sintoma:** 50 abordagens e 0 respostas
**Solução:** Aumentar personalização, testar novo canal

### Travamento 6: Cliente não paga (Etapa 6)
**Sintoma:** Interesse verbal mas não conclui compra
**Solução:** Reduzir fricção (pagamento mais simples, prazo menor)

---

## Fluxo de decisão rápido

Use este diagrama para decisões rápidas em cada etapa:

```
┌─────────────────────────────────────────────┐
│ Tenho ideia clara em 1 frase?               │
└────┬─────────────────────────┬──────────────┘
     │ NÃO                      │ SIM
     ↓                          ↓
 ETAPA 0                   ETAPA 1

┌─────────────────────────────────────────────┐
│ 7 de 10 entrevistados confirmam dor?        │
└────┬─────────────────────────┬──────────────┘
     │ NÃO                      │ SIM
     ↓                          ↓
 Pivotar persona          ETAPA 2

┌─────────────────────────────────────────────┐
│ Landing tem CTAs funcionais?                │
└────┬─────────────────────────┬──────────────┘
     │ NÃO                      │ SIM
     ↓                          ↓
 Corrigir CTAs            ETAPA 3

┌─────────────────────────────────────────────┐
│ Checkout funciona end-to-end?               │
└────┬─────────────────────────┬──────────────┘
     │ NÃO                      │ SIM
     ↓                          ↓
 Testar novamente      ETAPA 4 + ETAPA 5
                          (paralelo)

┌─────────────────────────────────────────────┐
│ 50 abordagens → 5+ conversas?               │
└────┬─────────────────────────┬──────────────┘
     │ NÃO                      │ SIM
     ↓                          ↓
 Ajustar oferta/público    ETAPA 6

┌─────────────────────────────────────────────┐
│ Cliente pagou e percebeu valor?             │
└────┬─────────────────────────┬──────────────┘
     │ NÃO                      │ SIM
     ↓                          ↓
 Revisar entrega          ETAPA 7
                     (coletar depoimento)
```

---

## Cronograma recomendado (14 dias)

| Dia | Etapa | Atividade principal | Tempo |
|-----|-------|---------------------|-------|
| 1 | 0 → 1 | Frase + personas + hipóteses | 4h |
| 2-3 | 1 | Realizar 10 entrevistas | 3h/dia |
| 4 | 1 | Analisar entrevistas | 3h |
| 5 | 2 | Criar e publicar landing | 6h |
| 6 | 3 + 4 | Checkout + iniciar MVP | 4h |
| 7-9 | 4 | Documentar processo entrega | 3h/dia |
| 8-14 | 5 | Prospecção contínua (paralelo) | 2h/dia |
| 12-14 | 6 | Fechar primeiro cliente | 4h |
| 14+ | 7 | Retrospectiva e próximos passos | 2h |

**Total:** ~50-60 horas em 14 dias (~4h/dia)

---

## Checkpoints de progresso

Use estes checkpoints para validar que está no caminho certo:

### Checkpoint Dia 1
- [ ] Frase de 1 linha validada
- [ ] 3 personas documentadas
- [ ] Script de entrevista pronto

### Checkpoint Dia 4
- [ ] 10 entrevistas realizadas
- [ ] Dor confirmada por pelo menos 7 pessoas
- [ ] Linguagem real documentada

### Checkpoint Dia 5
- [ ] Landing publicada
- [ ] CTAs funcionais
- [ ] Analytics configurado

### Checkpoint Dia 6
- [ ] Checkout testado e funcionando
- [ ] Processo de entrega mapeado

### Checkpoint Dia 10
- [ ] 50+ contatos abordados
- [ ] 5+ conversas qualificadas
- [ ] Pelo menos 2 calls agendadas

### Checkpoint Dia 14
- [ ] Primeiro cliente pagante
- [ ] Resultado entregue
- [ ] Depoimento coletado
- [ ] Retrospectiva realizada

---

**Próximo passo:** Use [tasks.MD](tasks.md) para checklist operacional detalhado.
