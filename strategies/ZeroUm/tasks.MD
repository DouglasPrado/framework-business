# Checklist Operacional - Estratégia ZeroUm

Este documento oferece um checklist prático e acionável para executar a estratégia ZeroUm passo a passo, com owners, prazos e templates prontos.

---

## Como usar este checklist

1. **Marque tarefas concluídas** conforme avança
2. **Anote owners** (quem é responsável)
3. **Registre datas** de início e conclusão
4. **Documente outputs** gerados em cada etapa
5. **Revise critérios de aceite** antes de avançar

---

## Etapa 0: Esclarecer a ideia (30 minutos)

**Owner:** ________________
**Data início:** ___/___/___
**Data conclusão:** ___/___/___

### Tarefas

- [ ] Listar 5 possíveis usuários-alvo (profissão, momento, onde estão)
- [ ] Identificar a dor central observando soluções atuais
- [ ] Redigir 3 variações da frase de proposta de valor
- [ ] Ler cada frase em voz alta e testar clareza
- [ ] Validar frase com 1 pessoa do público-alvo
- [ ] Ajustar linguagem baseado no feedback

### Template: Frase de proposta de valor

```
Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR PRINCIPAL].

Exemplo:
"Ajudo cabeleireiros a agendar clientes online sem precisar depender do WhatsApp."
```

### Critério de aceite

- [ ] Frase pode ser compreendida em 10 segundos
- [ ] Não menciona funcionalidades técnicas
- [ ] Foca no resultado gerado
- [ ] Testada com pelo menos 1 pessoa do público

### Output gerado

- `proposta-de-valor.txt` com frase validada

---

## Etapa 1: Validação de problema (2-4 dias)

**Owner:** ________________
**Data início:** ___/___/___
**Data conclusão:** ___/___/___

### Tarefas - Dia 1

- [ ] Criar documento de personas com template abaixo
- [ ] Definir 3 personas detalhadas (nome, ocupação, dor, onde estão)
- [ ] Anotar 3 hipóteses testáveis sobre cada persona
- [ ] Criar planilha de controle de entrevistas
- [ ] Preparar script de entrevista com 5 perguntas

### Template: Persona

```
PERSONA #1
Nome fictício: [Ex: Marina, designer freelancer]
Ocupação: [Ex: Designer gráfica autônoma há 3 anos]
Maior dor: [Ex: Perde tempo respondendo orçamentos repetitivos]
Onde está online: [Ex: Instagram, Behance, grupos de Facebook]
Momento de compra: [Ex: Quando recebe muitos pedidos simultâneos]

HIPÓTESES
1. Pagaria R$ [X] por mês pela solução
2. Prefere [característica A] vs [característica B]
3. Maior objeção seria [X]
```

### Template: Script de entrevista (5-15 min)

```
ABERTURA (1 min)
"Olá [Nome], obrigado por aceitar conversar comigo! Estou validando uma ideia
e preciso entender melhor como você resolve [problema]. Pode levar 10-15 minutos.
Tudo bem?"

PERGUNTAS (10 min)
1. Como você resolve [problema] hoje? Me conta o passo a passo.
2. Quanto tempo você gasta com isso por semana?
3. Qual é a parte mais frustrante desse processo?
4. Já tentou usar alguma ferramenta para isso? O que aconteceu?
5. Se existisse uma solução que [resultado], quanto valeria para você?

ENCERRAMENTO (2 min)
"Perfeito, suas respostas foram muito úteis! Posso te contactar quando tiver
algo pronto para testar?"
```

### Tarefas - Dia 2-3

- [ ] Listar 15-20 possíveis entrevistados
- [ ] Enviar convite personalizado (template abaixo)
- [ ] Realizar 10 entrevistas (5-15 min cada)
- [ ] Gravar áudio (com permissão) ou anotar palavras exatas
- [ ] Registrar dores citadas, soluções atuais e objeções
- [ ] Atualizar planilha após cada entrevista

### Template: Convite para entrevista

```
Assunto: Preciso de 15 minutos do seu tempo

Olá [Nome],

Estou validando uma ideia relacionada a [problema] e você trabalha nessa área.

Posso te fazer 3-5 perguntas rápidas sobre como você resolve isso hoje?
Leva só 10-15 minutos.

Como agradecimento, te envio [cupom/benefício/café digital].

Pode ser?

[Seu nome]
```

### Tarefas - Dia 4

- [ ] Compilar anotações de todas as entrevistas
- [ ] Identificar padrões (dores comuns, linguagem repetida)
- [ ] Classificar cada hipótese: validada / refutada / inconclusiva
- [ ] Ajustar personas baseado nos aprendizados
- [ ] Documentar top 3 dores e top 3 objeções
- [ ] Coletar termos exatos para usar na copy

### Planilha de controle: `entrevistas.xlsx`

| Nome | Contato | Data | Persona | Dor principal | Solução atual | Objeção | Pagaria? | Status |
|------|---------|------|---------|---------------|---------------|---------|----------|--------|
| | | | | | | | | Agendado/Realizado |

### Critério de aceite

- [ ] 10 entrevistas realizadas e documentadas
- [ ] Pelo menos 7 confirmaram a dor
- [ ] Pelo menos 3 demonstraram disposição a pagar
- [ ] Padrões identificados nas respostas
- [ ] Linguagem real documentada

### Output gerado

- `personas.md` com 3 personas validadas
- `hipoteses.md` com classificação (validada/refutada/inconclusiva)
- `entrevistas.xlsx` com anotações completas
- `linguagem-cliente.txt` com termos exatos usados

---

## Etapa 2: Landing page de pré-venda (1 dia)

**Owner:** ________________
**Data início:** ___/___/___
**Data conclusão:** ___/___/___

### Tarefas - Manhã (3-4h)

- [ ] Escolher ferramenta (Carrd, Webflow, Wix, Netlify)
- [ ] Criar conta e iniciar novo projeto
- [ ] Escrever headline (usar frase da Etapa 0)
- [ ] Escrever 3 bullets de benefícios (template abaixo)
- [ ] Selecionar 2-3 quotes reais das entrevistas
- [ ] Definir preço ou oferta de pré-venda
- [ ] Criar estrutura de layout (template abaixo)

### Template: Estrutura de landing page

```
═══════════════════════════════════════════
SEÇÃO 1: HERO
───────────────────────────────────────────
HEADLINE: [Frase da Etapa 0]
SUBHEADLINE: [Oferta específica + urgência]

CTA PRIMÁRIO: [Quero testar] → Formulário
CTA SECUNDÁRIO: [Comprar agora] → Checkout
───────────────────────────────────────────

═══════════════════════════════════════════
SEÇÃO 2: PROBLEMA
───────────────────────────────────────────
Você passa horas [dor] sem conseguir [resultado]?

[Descrever cenário frustrante do dia a dia]
───────────────────────────────────────────

═══════════════════════════════════════════
SEÇÃO 3: SOLUÇÃO
───────────────────────────────────────────
Com [Nome do produto], você consegue:

✓ [Benefício 1: resultado específico + tempo]
✓ [Benefício 2: o que evita + facilidade]
✓ [Benefício 3: diferencial + garantia]
───────────────────────────────────────────

═══════════════════════════════════════════
SEÇÃO 4: PROVA SOCIAL
───────────────────────────────────────────
"[Quote real de entrevistado]"
— [Nome/profissão se autorizado]

"[Quote real de entrevistado]"
— [Nome/profissão se autorizado]
───────────────────────────────────────────

═══════════════════════════════════════════
SEÇÃO 5: OFERTA
───────────────────────────────────────────
Teste piloto: [R$ X] por [período]
[Número] vagas disponíveis

[Listar o que está incluído]

CTA: [Garantir minha vaga]
───────────────────────────────────────────

═══════════════════════════════════════════
SEÇÃO 6: FAQ (opcional)
───────────────────────────────────────────
P: [Objeção comum]
R: [Resposta curta]
───────────────────────────────────────────
```

### Template: 3 bullets de benefícios

```
✓ Resolva [DOR] em [TEMPO] sem [ESFORÇO]
  Exemplo: "Resolva agendamentos em 2 minutos sem trocar mensagens"

✓ Sem [FRICÇÃO] - começa em [PRAZO]
  Exemplo: "Sem instalação - começa em 24 horas"

✓ [DIFERENCIAL ÚNICO] durante o piloto
  Exemplo: "Suporte direto comigo via WhatsApp durante 30 dias"
```

### Tarefas - Tarde (2-3h)

- [ ] Montar landing na ferramenta escolhida
- [ ] Adicionar formulário de captura (nome + e-mail + WhatsApp)
- [ ] Integrar botão "Comprar" (irá configurar na Etapa 3)
- [ ] Configurar Google Analytics ou ferramenta similar
- [ ] Testar página em Chrome, Safari, Firefox
- [ ] Testar em dispositivo mobile real
- [ ] Validar tempo de carregamento (< 3 segundos)
- [ ] Publicar e obter URL final

### Ferramentas sugeridas

| Ferramenta | Custo | Complexidade | Recomendado para |
|------------|-------|--------------|------------------|
| Carrd | $0-19/ano | Baixa | Páginas simples e rápidas |
| Webflow | $0-18/mês | Média | Design customizado |
| Wix | $0-27/mês | Baixa | Arrasta e solta |
| HTML+Netlify | $0 | Média | Quem sabe código |

### Critério de aceite

- [ ] Headline clara e direta (frase da Etapa 0)
- [ ] 3 bullets focados em benefícios, não funcionalidades
- [ ] 2-3 quotes reais com autorização
- [ ] Preço ou faixa de preço visível
- [ ] 2 CTAs funcionais (formulário + comprar)
- [ ] Analytics configurado corretamente
- [ ] Carrega em menos de 3 segundos
- [ ] Responsiva em mobile

### Output gerado

- URL da landing publicada
- `landing-metrics.xlsx` para tracking de visitas/conversões
- Screenshots da versão inicial

---

## Etapa 3: Checkout mínimo (algumas horas)

**Owner:** ________________
**Data início:** ___/___/___
**Data conclusão:** ___/___/___

### Tarefas

- [ ] Escolher solução de pagamento (comparar tabela abaixo)
- [ ] Criar conta na plataforma escolhida
- [ ] Criar link de pagamento com valor definido
- [ ] Realizar pagamento de teste simbólico (R$ 1-5)
- [ ] Validar recebimento de notificação
- [ ] Integrar link ao botão "Comprar" da landing
- [ ] Criar página de "Obrigado" com próximos passos
- [ ] Preparar e-mail automático de confirmação (template abaixo)
- [ ] Preparar recibo/contrato simples (template abaixo)
- [ ] Criar planilha de controle de pagamentos

### Comparação de soluções de pagamento

| Solução | Taxa | Prazo recebimento | Sem CNPJ | Recorrência |
|---------|------|-------------------|----------|-------------|
| PIX | 0-2% | Imediato | ✅ Sim | ❌ Não |
| Stripe | 2,99% + R$0,39 | D+2 | ✅ Sim | ✅ Sim |
| Hotmart | 9,9% | D+30 | ✅ Sim | ✅ Sim |
| Kiwify | 9% | D+1 | ✅ Sim | ✅ Sim |
| PagSeguro | 4,99% | D+14 | ✅ Sim | ✅ Sim |

**Recomendação inicial:** PIX para teste rápido, depois migrar para Stripe/Kiwify

### Template: E-mail de confirmação de pagamento

```
Assunto: ✅ Pagamento confirmado - Próximos passos

Olá [Nome],

Seu pagamento foi confirmado! 🎉

Aqui estão os próximos passos:

1️⃣ Agora: responda este e-mail com [informação necessária]
2️⃣ Em até 24h: você receberá [o que será enviado]
3️⃣ Durante o processo: estou disponível via [WhatsApp/e-mail]

DETALHES DA COMPRA
━━━━━━━━━━━━━━━━━━━
Produto: [Nome]
Valor: R$ [X]
Data: [DD/MM/AAAA]
━━━━━━━━━━━━━━━━━━━

Dúvidas? Responda este e-mail ou me chame no WhatsApp: [seu número]

[Seu nome]
[Link para suporte se tiver]
```

### Template: Recibo simples

```
RECIBO DE PAGAMENTO

Valor: R$ [X,XX]
Data: [DD/MM/AAAA]
Referente a: [Descrição do serviço/produto]

PRESTADOR
Nome: [Seu nome completo]
CPF: [xxx.xxx.xxx-xx]
Contato: [e-mail/telefone]

CONTRATANTE
Nome: [Nome do cliente]
CPF/CNPJ: [documento]
E-mail: [e-mail]

DESCRIÇÃO DO SERVIÇO
[Descrever o que será entregue, prazo e forma de entrega]

Prazo de entrega: [X dias úteis]
Forma de entrega: [E-mail, plataforma, call, etc.]

_______________________
Assinatura do prestador

[Cidade], [Data]
```

### Planilha de controle: `pagamentos.xlsx`

| Data | Cliente | E-mail | Valor | Status | Método | Comprovante | Entregue? |
|------|---------|--------|-------|--------|--------|-------------|-----------|
| | | | | Pendente/Confirmado | PIX/Link | Link/arquivo | Sim/Não |

### Critério de aceite

- [ ] Link de pagamento criado e testado
- [ ] Teste de pagamento realizado com sucesso
- [ ] Notificação de pagamento recebida em tempo real
- [ ] Botão "Comprar" da landing integrado ao link
- [ ] Página de obrigado configurada
- [ ] E-mail de confirmação pronto
- [ ] Recibo/contrato template preparado
- [ ] Planilha de controle criada

### Output gerado

- Link de checkout funcional
- `pagamentos.xlsx` para controle manual
- Templates de e-mail e recibo prontos

---

## Etapa 4: MVP operável manual (1-2 semanas)

**Owner:** ________________
**Data início:** ___/___/___
**Data conclusão:** ___/___/___

### Tarefas - Semana 1

- [ ] Mapear fluxo completo de entrega (usar template abaixo)
- [ ] Listar todas as etapas desde recebimento até follow-up
- [ ] Escolher ferramentas para gestão (Sheets/Notion/Trello)
- [ ] Criar board/planilha de acompanhamento
- [ ] Criar template de e-mail de onboarding (template abaixo)
- [ ] Criar template de e-mail de entrega
- [ ] Criar template de e-mail de follow-up
- [ ] Criar checklist de entrega passo a passo

### Template: Fluxo de entrega

```
ETAPA 1: RECEBIMENTO DO PEDIDO
├─ Ação: Confirmar pagamento
├─ Tempo estimado: 5 min
├─ Ferramenta: Planilha de pagamentos
└─ Output: Status atualizado + e-mail confirmação

ETAPA 2: ONBOARDING DO CLIENTE
├─ Ação: Coletar informações necessárias
├─ Tempo estimado: 15 min
├─ Ferramenta: E-mail ou formulário
└─ Output: Briefing completo

ETAPA 3: PRODUÇÃO/EXECUÇÃO
├─ Ação: [Descrever o que você faz]
├─ Tempo estimado: [X horas]
├─ Ferramenta: [Lista de ferramentas]
└─ Output: [Entregável principal]

ETAPA 4: ENTREGA
├─ Ação: Enviar resultado + instruções
├─ Tempo estimado: 10 min
├─ Ferramenta: E-mail ou plataforma
└─ Output: Cliente com acesso ao resultado

ETAPA 5: FOLLOW-UP
├─ Ação: Agendar check-in 24-48h depois
├─ Tempo estimado: 15 min
├─ Ferramenta: Call ou WhatsApp
└─ Output: Feedback + depoimento

TEMPO TOTAL: [Somar todos os tempos]
```

### Template: E-mail de onboarding

```
Assunto: Vamos começar! Preciso de algumas informações

Olá [Nome],

Agora vamos iniciar! Para eu entregar exatamente o que você precisa,
responda as perguntas abaixo:

1. [Pergunta específica 1]
2. [Pergunta específica 2]
3. [Pergunta específica 3]

Assim que eu receber, começo imediatamente e você terá o resultado
em até [X dias].

Dúvidas? É só responder este e-mail!

[Seu nome]
```

### Tarefas - Semana 2

- [ ] Realizar teste piloto interno ou com contato de confiança
- [ ] Cronometrar cada etapa do processo
- [ ] Identificar gargalos e etapas que consomem mais tempo
- [ ] Ajustar processo baseado no piloto
- [ ] Documentar processo final em formato repetível
- [ ] Criar pasta com todos os templates e materiais
- [ ] Definir padrões mínimos de qualidade

### Checklist de entrega: `checklist-entrega.md`

```
CHECKLIST DE ENTREGA - [NOME DO SERVIÇO]

PRÉ-PRODUÇÃO
□ Pagamento confirmado na planilha
□ E-mail de confirmação enviado
□ Briefing recebido do cliente
□ Briefing validado (completo e claro)
□ Prazo acordado e anotado

PRODUÇÃO
□ [Etapa específica 1]
□ [Etapa específica 2]
□ [Etapa específica 3]
□ Revisão de qualidade realizada
□ Materiais complementares preparados

ENTREGA
□ Resultado exportado no formato correto
□ E-mail de entrega redigido
□ Instruções de uso incluídas
□ Resultado enviado ao cliente
□ Cliente confirmou recebimento

PÓS-ENTREGA
□ Check-in agendado (24-48h depois)
□ Call/mensagem de follow-up realizada
□ Feedback coletado
□ Depoimento solicitado
□ Caso documentado na pasta do cliente
```

### Ferramentas sugeridas

| Necessidade | Ferramenta | Custo | Complexidade |
|-------------|------------|-------|--------------|
| Gestão de clientes | Google Sheets | Grátis | Baixa |
| Kanban visual | Trello | Grátis | Baixa |
| Base de conhecimento | Notion | Grátis | Média |
| Formulários | Google Forms | Grátis | Baixa |
| Agendamento | Calendly | Grátis-$12/mês | Baixa |

### Critério de aceite

- [ ] Fluxo completo mapeado do início ao fim
- [ ] Todas as etapas têm tempo estimado
- [ ] Templates de comunicação prontos (onboarding, entrega, follow-up)
- [ ] Checklist de entrega criado e testado
- [ ] Teste piloto realizado
- [ ] Processo completo documentado
- [ ] Consegue entregar em menos de 7 dias

### Output gerado

- `processo-entrega.md` detalhado
- `templates-email/` com mensagens prontas
- `checklist-entrega.md` passo a passo
- Pasta com materiais padrão

---

## Etapa 5: Tração inicial (contínuo)

**Owner:** ________________
**Data início:** ___/___/___
**Meta:** 50 abordagens → 5 conversas → 1 venda

### Tarefas semanais

#### Segunda-feira
- [ ] Listar 10 contatos qualificados do seu network
- [ ] Pesquisar contexto de cada um (LinkedIn, Instagram, etc.)
- [ ] Personalizar primeira linha da mensagem para cada
- [ ] Enviar 10 mensagens (template abaixo)
- [ ] Registrar na planilha de leads

#### Terça-quarta
- [ ] Listar mais 10 contatos por dia
- [ ] Enviar 10 mensagens personalizadas/dia
- [ ] Responder conversas iniciadas no mesmo dia
- [ ] Atualizar status na planilha
- [ ] Agendar calls com leads qualificados

#### Quinta-sexta
- [ ] Enviar últimas 10 mensagens da semana
- [ ] Realizar calls agendadas
- [ ] Publicar 1 post no LinkedIn com CTA
- [ ] Publicar 1 post no Instagram Stories com link
- [ ] Participar de 2 comunidades/grupos relevantes

#### Sábado
- [ ] Analisar métricas da semana
- [ ] Calcular taxa de resposta
- [ ] Identificar padrões nas respostas positivas
- [ ] Ajustar abordagem para próxima semana
- [ ] Planejar lista de contatos da próxima semana

### Template: Mensagem de abordagem personalizada

**Versão 1 - Contato direto**
```
Olá [Nome],

Vi que você [CONTEXTO ESPECÍFICO - post, trabalho, projeto].

Estou testando um [PRODUTO] que ajuda [QUEM] a [RESULTADO] sem [DOR].

Separei 3 vagas piloto com desconto. Posso te mandar mais info?

[Seu nome]
```

**Versão 2 - Valor primeiro**
```
Oi [Nome]!

Criei um guia rápido sobre [TEMA DO INTERESSE DELE].

Achei que poderia ser útil pra você que [CONTEXTO].

Posso enviar? É grátis.

PS: Também tenho um teste piloto de [PRODUTO] se você quiser saber mais.

[Seu nome]
```

**Versão 3 - Pergunta de validação**
```
[Nome], tudo bem?

Você [FAZ X / TEM Y / TRABALHA COM Z]?

Estou validando uma solução para [PROBLEMA].

Se fizer sentido, te mando info. Pode ser?

[Seu nome]
```

### Template: Post LinkedIn/Instagram

```
[HOOK - Problema relatable]
Você passa horas [ATIVIDADE FRUSTRANTE]?

[AGITAÇÃO]
Eu cansei de [SITUAÇÃO RUIM] e decidi criar uma solução.

[SOLUÇÃO]
Agora em 3 vagas de teste piloto:
→ [BENEFÍCIO 1]
→ [BENEFÍCIO 2]
→ [BENEFÍCIO 3]

[CTA]
Quer ser um dos 3? Comenta "EU" que te envio os detalhes.

#[hashtag1] #[hashtag2] #[hashtag3]
```

### Planilha de controle: `leads.xlsx`

| Data | Nome | Canal | Status | Resposta | Objeção | Próxima ação | Resultado |
|------|------|-------|--------|----------|---------|--------------|-----------|
| | | WhatsApp/LinkedIn/DM | Enviado/Respondeu/Negociação/Perdido | Sim/Não | Texto | Call/Follow-up | Venda/Não |

### Canais por ordem de prioridade

**Nível 1 - Contatos diretos (começar aqui)**
- [ ] Lista de contatos pessoais do WhatsApp
- [ ] Conexões do LinkedIn
- [ ] Seguidores/amigos do Instagram
- [ ] Contatos de e-mail profissional

**Nível 2 - Comunidades online**
- [ ] Grupos de WhatsApp do nicho
- [ ] Grupos de Telegram relevantes
- [ ] Facebook Groups
- [ ] LinkedIn Groups
- [ ] Reddit / Fóruns especializados

**Nível 3 - Conteúdo orgânico**
- [ ] Posts no LinkedIn (1-2x/semana)
- [ ] Stories no Instagram (diário)
- [ ] Comentários em posts relevantes

**Nível 4 - Cold outreach (se necessário)**
- [ ] DMs personalizados no LinkedIn
- [ ] DMs no Instagram de perfis do nicho
- [ ] E-mails frios (se tiver lista)

**Nível 5 - Tráfego pago (opcional)**
- [ ] Anúncios Facebook/Instagram (R$ 50-150)
- [ ] Anúncios LinkedIn (R$ 100-200)

### Critério de aceite

- [ ] 50 contatos abordados na semana
- [ ] Todas as mensagens personalizadas (não cópia e cola)
- [ ] Pelo menos 5 conversas iniciadas
- [ ] Status rastreado na planilha
- [ ] Taxa de resposta > 10%

### Output gerado

- `leads.xlsx` atualizado semanalmente
- `objecoes.md` com padrões documentados
- Lista de melhores mensagens que converteram

---

## Etapa 6: Fechamento do primeiro cliente (1-2 dias)

**Owner:** ________________
**Data início:** ___/___/___
**Data conclusão:** ___/___/___

### Tarefas - Dia 1: Fechamento

- [ ] Agendar call de 15-20 min via Calendly ou WhatsApp
- [ ] Preparar roteiro de call (template abaixo)
- [ ] Realizar call de vendas
- [ ] Gravar call se cliente autorizar
- [ ] Enviar resumo da call por escrito
- [ ] Enviar link de pagamento
- [ ] Confirmar recebimento do pagamento
- [ ] Enviar e-mail com próximos passos

### Template: Roteiro de call de vendas (15-20 min)

```
ABERTURA (2 min)
─────────────────
"Oi [Nome]! Como vai? Obrigado por separar esse tempo.
Vou te fazer algumas perguntas pra entender sua situação e ver se
faz sentido pra você. Pode ser?"

DIAGNÓSTICO (5-7 min)
─────────────────────
1. "Me conta, como você resolve [PROBLEMA] hoje?"
2. "Quanto tempo você gasta com isso por semana/mês?"
3. "Qual a parte mais frustrante?"
4. "Já tentou outras soluções? O que aconteceu?"
5. "O que mudaria na sua rotina se isso fosse resolvido?"

PROPOSTA (5 min)
────────────────
"Pelo que você me contou, acho que posso te ajudar.
Deixa eu explicar como funciona..."

[Explicar o processo, prazos, entregáveis]

"O investimento pro teste piloto é R$ [X].
Isso inclui [listar o que está incluído].

Como é piloto, são só 3 vagas e você tem suporte direto comigo."

ALINHAMENTO (3-5 min)
─────────────────────
"Faz sentido pra você?"

[Escutar objeções e responder]

"Quer que eu reserve uma vaga pra você?
Te mando o link de pagamento agora."

PRÓXIMOS PASSOS (1 min)
───────────────────────
"Assim que o pagamento confirmar, eu te envio um e-mail com
algumas perguntas e já começamos. Ok?"
```

### Tratamento de objeções comuns

| Objeção | Resposta |
|---------|----------|
| "Está caro" | "Entendo. Qual valor faria sentido pra você? Lembrando que é teste piloto com suporte direto." |
| "Preciso pensar" | "Sem problema! O que especificamente você precisa avaliar? Posso te ajudar com alguma informação?" |
| "Não tenho tempo agora" | "Quando seria um momento melhor? Posso te chamar na semana que vem?" |
| "Não sei se funciona" | "Por isso é teste piloto! Se não funcionar, a gente ajusta. O que te deixaria mais seguro?" |
| "Preciso aprovar com X" | "Claro! Quer que eu prepare um resumo pra você mostrar pra [X]?" |

### Tarefas - Dia 2: Entrega

- [ ] Enviar e-mail de onboarding (Etapa 4)
- [ ] Coletar informações necessárias via formulário/e-mail
- [ ] Executar processo de entrega (seguir checklist Etapa 4)
- [ ] Entregar resultado no prazo prometido
- [ ] Agendar check-in 24-48h após entrega
- [ ] Realizar check-in (call ou WhatsApp)
- [ ] Validar que cliente percebeu valor
- [ ] Solicitar depoimento (template abaixo)

### Template: Solicitação de depoimento

```
Assunto: Pode me ajudar com um depoimento?

Oi [Nome]!

Fico muito feliz que o [resultado] tenha sido útil pra você!

Você poderia gravar um áudio/vídeo rápido de 30-60 segundos contando:

1. Qual era seu problema antes?
2. Como foi trabalhar comigo?
3. O que mudou depois?

Ou se preferir, pode escrever mesmo!

Vou usar esse depoimento pra mostrar pra outras pessoas
que estão com o mesmo problema que você tinha.

Pode ser?

Muito obrigado!
[Seu nome]
```

### Critério de aceite

- [ ] Call de vendas realizada
- [ ] Pagamento confirmado
- [ ] Entrega realizada no prazo prometido
- [ ] Cliente percebeu valor (confirmado no check-in)
- [ ] Depoimento coletado com autorização de uso
- [ ] Caso documentado na pasta do cliente

### Output gerado

- Dossiê do cliente em `cliente-001/`
  - Gravação da call (se autorizado)
  - Briefing e informações coletadas
  - Comprovante de pagamento
  - Entregáveis enviados
  - Depoimento (áudio/vídeo/texto)
- `metricas-entrega.txt` com tempo gasto em cada etapa

---

## Etapa 7: Aprendizado e iteração (contínuo)

**Owner:** ________________
**Frequência:** A cada 2 semanas
**Próxima retrospectiva:** ___/___/___

### Tarefas de retrospectiva (a cada 2 semanas)

- [ ] Compilar métricas do período (usar template abaixo)
- [ ] Analisar feedback dos clientes
- [ ] Identificar motivo real das compras
- [ ] Listar objeções mais comuns
- [ ] Classificar aprendizados (funcionou / não funcionou / testar)
- [ ] Priorizar máximo 3 melhorias para próximo ciclo
- [ ] Atualizar hipótese de negócio
- [ ] Documentar lições aprendidas
- [ ] Compartilhar retrospectiva com time (se tiver)
- [ ] Agendar próxima retrospectiva

### Template: Métricas do período

```
RETROSPECTIVA - [DATA INÍCIO] a [DATA FIM]

TRÁFEGO E CONVERSÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━
Visitas na landing: [X]
Taxa de conversão landing: [X%]
Leads gerados: [X]
Taxa leads → venda: [X%]

PROSPECÇÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━
Abordagens enviadas: [X]
Respostas recebidas: [X] ([X%])
Conversas qualificadas: [X]
Calls realizadas: [X]

VENDAS
━━━━━━━━━━━━━━━━━━━━━━━━━━
Vendas fechadas: [X]
Receita gerada: R$ [X]
Ticket médio: R$ [X]

ENTREGA
━━━━━━━━━━━━━━━━━━━━━━━━━━
Clientes atendidos: [X]
Tempo médio de entrega: [X] dias
NPS médio: [X]/10
Depoimentos coletados: [X]

APRENDIZADOS
━━━━━━━━━━━━━━━━━━━━━━━━━━
[Listar 3-5 principais aprendizados]

PRÓXIMAS AÇÕES (máx 3)
━━━━━━━━━━━━━━━━━━━━━━━━━━
1. [Ação específica] - Owner: [Nome] - Prazo: [Data]
2. [Ação específica] - Owner: [Nome] - Prazo: [Data]
3. [Ação específica] - Owner: [Nome] - Prazo: [Data]
```

### Matriz de decisão de melhorias

| Situação | Métrica observada | Ação recomendada |
|----------|-------------------|------------------|
| Tráfego baixo | < 50 visitas/semana | Intensificar prospecção ativa (Etapa 5) |
| Conversão baixa | < 3% na landing | Revisar copy, testar nova headline |
| Lead não converte | < 5% lead→venda | Ajustar preço ou validar fit produto-mercado |
| Entrega lenta | > 7 dias | Simplificar processo ou automatizar gargalo |
| Preço sem objeção | 90%+ aceitam preço | Testar aumento de 30-50% |
| Muito trabalho manual | > 10h por cliente | Priorizar automação da etapa mais demorada |
| NPS baixo | < 7/10 | Revisar qualidade da entrega |

### Tarefas de melhoria contínua

- [ ] Identificar etapa que consome mais tempo
- [ ] Pesquisar ferramentas de automação viáveis
- [ ] Testar variação de copy na landing (A/B test)
- [ ] Revisar preço baseado em feedback
- [ ] Criar FAQ com objeções mais comuns
- [ ] Desenvolver caso de uso com cliente de sucesso
- [ ] Planejar transição de manual para automatizado

### Critério de aceite

- [ ] Retrospectiva realizada a cada 2 semanas
- [ ] Todas as métricas documentadas
- [ ] Máximo 3 melhorias priorizadas por ciclo
- [ ] Ações têm owner e prazo definidos
- [ ] Lições documentadas para referência futura

### Output gerado

- `retrospectiva-[data].md` com análise completa
- `metricas-historico.xlsx` atualizado
- `roadmap-proximas-acoes.md` com 3 prioridades

---

## Resumo executivo: Checklist completo

Use esta visão consolidada para acompanhar progresso geral:

### Fase 1: Validação (Dias 1-4)
- [ ] Etapa 0: Frase de proposta de valor validada
- [ ] Etapa 1: 10 entrevistas realizadas e dor confirmada

### Fase 2: Infraestrutura (Dias 5-6)
- [ ] Etapa 2: Landing page publicada
- [ ] Etapa 3: Checkout funcionando

### Fase 3: Preparação (Dias 7-10)
- [ ] Etapa 4: Processo de entrega documentado
- [ ] Etapa 5: Prospecção iniciada (50 abordagens)

### Fase 4: Primeira venda (Dias 11-14)
- [ ] Etapa 6: Primeiro cliente pagante e satisfeito
- [ ] Etapa 7: Retrospectiva realizada e próximos passos definidos

---

## Recursos adicionais

### Planilhas recomendadas

1. **master-zeroum.xlsx** (consolidado)
   - Aba 1: Entrevistas
   - Aba 2: Métricas landing
   - Aba 3: Leads
   - Aba 4: Pagamentos
   - Aba 5: Entregas
   - Aba 6: Retrospectivas

### Estrutura de pastas

```
zeroum-projeto/
├── 00-proposta/
│   └── proposta-de-valor.txt
├── 01-validacao/
│   ├── personas.md
│   ├── hipoteses.md
│   ├── entrevistas.xlsx
│   └── linguagem-cliente.txt
├── 02-landing/
│   ├── url.txt
│   ├── screenshots/
│   └── landing-metrics.xlsx
├── 03-checkout/
│   ├── link-pagamento.txt
│   └── pagamentos.xlsx
├── 04-mvp/
│   ├── processo-entrega.md
│   ├── checklist-entrega.md
│   └── templates-email/
├── 05-tracao/
│   ├── leads.xlsx
│   └── objecoes.md
├── 06-clientes/
│   ├── cliente-001/
│   ├── cliente-002/
│   └── [...]
└── 07-aprendizados/
    ├── retrospectivas/
    └── metricas-historico.xlsx
```

---

**Próximo passo:** Comece pela Etapa 0 e marque cada checkbox conforme avança!
