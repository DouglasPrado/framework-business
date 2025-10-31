# Base de Conhecimento - LandingPageCreation

## Visão Geral

Landing pages de pré-venda transformam hipóteses validadas em propostas claras, mensuráveis e acionáveis. Esta base de conhecimento reúne princípios, boas práticas, materiais de apoio e respostas para dúvidas frequentes ao construir páginas em ferramentas no-code aprovadas.

## Objetivo Central

Garantir que cada landing publicada:
- Traduza a proposta de valor de forma objetiva usando linguagem real do cliente.
- Colete dados confiáveis (leads, pré-vendas, métricas de engajamento).
- Permita ajustes rápidos com base em indicadores de performance.

## Princípios Fundamentais

1. **Narrativa contínua:** conduza o visitante do problema à oferta de forma lógica e sem fricções.
2. **Linguagem do cliente:** reutilize citações e expressões capturadas em entrevistas para copy.
3. **CTA único e claro:** uma ação principal por página (capturar lead ou direcionar para checkout).
4. **Prova social contextualizada:** destaque evidências alinhadas à dor e ao benefício priorizados.
5. **Mensuração desde o início:** configure analytics antes do lançamento oficial.

## Conceitos-Chave

### Hero
Primeira dobra da página. Deve apresentar headline clara (baseada na [Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md)), subheadline explicativa e CTA principal. Recomenda-se complementar com bullet que introduza o benefício central.

### Prova social
Depoimentos, números ou logos que validam a proposta. Priorize citações provenientes de [UserInterviewValidation](../UserInterviewValidation/process.MD) com contexto (nome, cargo ou segmento, quando autorizado).

### CTA (Call to Action)
Botão ou formulário principal da página. Deve usar verbos de ação e alinhar expectativa de tempo e benefício (“Garantir minha vaga”, “Quero acessar a lista beta”). Utilize microcopy de suporte para remover objeções (“Sem cartão de crédito”).

### Métricas primárias e secundárias
- **Primárias:** conversão (leads, cliques, pré-vendas).
- **Secundárias:** taxa de rejeição, tempo na página, scroll depth. Use-as para identificar pontos de fricção.

### Responsividade
Garantir experiência fluida em mobile é obrigatório. Estruture seções com hierarquia clara e teste em diferentes resoluções (desktop, tablet, smartphone).

## Perguntas Frequentes

### Qual ferramenta devo usar?
Verifique em `tools/` as plataformas aprovadas (ex: Carrd, Webflow, Wix, Netlify). Escolha com base em velocidade de implementação, integrações disponíveis e familiaridade do time. Se precisar de nova ferramenta, documente solicitação conforme governança.

### Como selecionar citações para prova social?
Escolha frases que:
- descrevem claramente o problema ou benefício já validado;
- são específicas (evite elogios genéricos);
- possuem autorização explícita para divulgação (capturada no processo de entrevistas).

### Qual o tamanho ideal da landing?
Foque em uma página enxuta com as seções obrigatórias. Adicione seções extras (ex: processo passo a passo, tabela de planos) apenas se contribuírem diretamente para conversão. Priorize clareza em vez de volume.

### Como priorizar métricas?
Defina conversão principal no briefing (`briefing-landing.MD`). Analise diariamente nas primeiras 72 horas após o lançamento para identificar ajustes rápidos (copy, CTA, hero). Utilize `_DATA/plano-analytics.MD` para registrar responsáveis e cadência.

### Quando atualizar a página?
Considere ajustes quando:
- taxa de conversão abaixo da meta após volume mínimo de visitas;
- feedbacks qualitativos indicarem objeções não tratadas;
- novas evidências surgirem em entrevistas ou testes subsequentes.

## Checkpoints de Qualidade

1. **Narrativa completa:** a página responde a “O que é?”, “Para quem?”, “Qual problema resolve?”, “Por que acreditar?”, “O que acontece depois do CTA?”.
2. **Copy aderente:** headlines e bullets refletem linguagem validada. Compare com notas da biblioteca de linguagem.
3. **Provas em destaque:** pelo menos uma citação, número ou caso real.
4. **CTA funcional:** formulario ou botão testado com dados fictícios.
5. **Mensuração ativa:** pixel/eventos verificáveis em tempo real.
6. **Performance adequada:** tempo de carregamento ≤ 3s em desktop, ≤ 4s em mobile (PageSpeed ou GTmetrix).

## Boas Práticas de Estrutura

- Hero com headline impactante, subheadline e CTA único.
- Seção de problema usando frases reais das entrevistas.
- Seção de solução com lista de benefícios (3 bullets).
- Prova social com citação, nome e contexto.
- Seção de oferta (preço, bônus, urgência).
- FAQ com 3-5 perguntas frequentes (objeções + respostas).
- CTA final reforçando benefício e ação próxima.

## Ferramentas e Integrações Comuns *(verificar catálogo `tools/`)*

- **Construtores:** Carrd, Webflow, Wix, Dorik, Framer (quando aprovados).
- **Formulários/CRM:** Google Forms, Typeform, HubSpot, Mailchimp.
- **Analytics:** Google Analytics, Meta Pixel, Tag Manager.
- **Performance:** PageSpeed Insights, GTmetrix, WebPageTest.
- **Compressão de imagens:** Squoosh, TinyPNG (usar antes de subir assets).

## Materiais de Apoio

- Artigos sobre copywriting orientado por entrevistas (Jobs To Be Done).
- Guias de CRO (Conversion Rate Optimization) para landing pages.
- Estudos de caso internos (quando disponíveis) armazenados em `_DATA/`.
- Modelos de copy adaptados a partir de rodadas anteriores.

## Riscos e Mitigações

### Copy genérica
- **Sintoma:** headlines vagas, baixa conversão.
- **Mitigação:** revisar biblioteca de linguagem e inserir citações diretas.

### Formulário quebrado
- **Sintoma:** leads não chegam ao CRM ou e-mail.
- **Mitigação:** teste real antes do lançamento; configure alertas.

### Analytics sem eventos
- **Sintoma:** ausência de dados em dashboards.
- **Mitigação:** usar modo debug (GA/Meta), registrar prints de disparo.

### Performance lenta
- **Sintoma:** tempo de carregamento > 3s, alta taxa de rejeição.
- **Mitigação:** comprimir imagens, remover scripts desnecessários, usar CDN da plataforma.

### Falta de responsividade
- **Sintoma:** layout quebrado em mobile, CTAs fora de tela.
- **Mitigação:** testar diferentes resoluções, ajustar spacing e tamanho de fonte.

## Integrações com Outros Processos

### Processos anteriores
- [ProblemHypothesisDefinition](../ProblemHypothesisDefinition/process.MD)
- [TargetUserIdentification](../TargetUserIdentification/process.MD)
- [UserInterviewValidation](../UserInterviewValidation/process.MD)

### Processos posteriores
- [CheckoutSetup] (a criar) – conecta com fluxo de pagamento
- [OutreachCampaign] (a criar) – direciona tráfego
- [ContentPublication] (a criar) – sustenta mensagens em canais orgânicos

## Próximos Passos Sugeridos Após Publicação

1. Monitorar métricas definidas no plano de analytics (primeiras 72h).
2. Coletar feedback qualitativo (ex: gravação de sessão, comentários de usuários).
3. Planejar teste A/B ou variações de copy quando volume permitir.
4. Alimentar backlog com objeções ou insights novos para processos seguintes.
5. Atualizar `strategies/ZeroUm` com métricas iniciais e decisões.

## Referências Internas

- [process.MD](process.MD)
- [tasks.MD](tasks.MD)
- [validator.MD](validator.MD)
- [_DATA/briefing-landing.MD](\_DATA/briefing-landing.MD)
- [_DATA/copy-draft.MD](\_DATA/copy-draft.MD)
- [_DATA/checklist-qa.MD](\_DATA/checklist-qa.MD)
