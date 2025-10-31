# Processo de Criação de Landing Page de Pré-Venda

## Propósito

Transformar hipóteses validadas e linguagem do cliente em uma landing page publicada, funcional e mensurável em até 8 horas, habilitando a medição de demanda e a coleta de leads ou pré-vendas.

## Objetivo

Publicar uma landing page com copy alinhada às dores e desejos do público, incluindo formulário/CTA funcionando, analytics configurado e checklist de qualidade concluído, garantindo que a página esteja pronta para tráfego imediato.

## Escopo

### Dentro do escopo
- Consolidar insumos de hipóteses e linguagem do cliente em briefing
- Definir estrutura de seções (Hero, Problema, Solução, Prova Social, Oferta, FAQ, CTA)
- Redigir copy completa, incluindo bullets de benefícios e prova social
- Selecionar ferramenta aprovada e construir página com assets básicos
- Configurar formulário (ou checkout) e eventos de analytics
- Realizar QA (responsividade, links, performance, ortografia) e publicar

### Fora do escopo
- Criação de identidade visual complexa ou design customizado avançado
- Desenvolvimento front-end sob medida fora das plataformas listadas
- Configuração de campanhas de tráfego ou automações de CRM
- Produção de vídeos ou sessões de fotos dedicadas
- Análises de SEO aprofundadas ou testes multivariados

## Etapas do Processo

### Etapa 1: Consolidar insumos e briefing (45 minutos)

Objetivo: reunir todos os materiais necessários para produzir a página com clareza.

Passos:
- Revisar hipóteses e objetivos comerciais (conversão desejada, público-alvo)
- Coletar citações e bullets da biblioteca de linguagem (_DATA/rodada anterior)
- Definir oferta e incentivo (preço, bônus, urgência)
- Registrar métricas-alvo (ex: conversão mínima esperada) e critérios de sucesso
- Escolher ferramenta preferencial (Carrd, Webflow, Wix, Netlify) confirmando aprovação em `tools/`

Template de apoio: `_DATA/briefing-landing.MD`

Outputs:
- Briefing preenchido e salvo em `_DATA/`
- Lista de recursos necessários (logos, imagens, domínios, integrações)
- Checklist de pendências pré-produção (acessos, DNS, scripts)

### Etapa 2: Definir estrutura da página (60 minutos)

Objetivo: desenhar o fluxo da página garantindo narrativa coerente e completa.

Passos:
- Selecionar layout base ou template na ferramenta escolhida
- Mapear seções obrigatórias: Hero, Problema, Solução, Benefícios (3 bullets), Prova Social, Oferta, FAQ, CTA final
- Definir ordem das seções e CTAs intermediários
- Esboçar wireframe textual rápido (blocos com título, subtítulo, copy principal)
- Identificar espaços para imagens, ícones ou vídeos (opcionais)

Template de apoio: `_DATA/estrutura-secoes.MD`

Outputs:
- Estrutura aprovada (wireframe textual) salva em `_DATA/`
- Lista de assets/recursos de mídia necessários com responsável e prazo

### Etapa 3: Produzir copy e selecionar prova social (90 minutos)

Objetivo: criar textos de alta conversão usando linguagem real do cliente.

Passos:
- Redigir headlines, subheadlines e CTA principal baseados na hipótese
- Escrever 3 bullets de benefícios claros (dor → benefício → prova)
- Inserir citações de entrevistas como prova social (com nome/cargo quando permitido)
- Construir seção FAQ com pelo menos 3 perguntas frequentes levantadas no UserInterviewValidation
- Revisar copy com foco em clareza, persuasão e consistência de tom

Template de apoio: `_DATA/copy-draft.MD`

Outputs:
- Documento de copy completo (incluindo microcopy de botões e placeholders)
- Lista de citações aprovadas com fonte
- Versão pronta para implementação na ferramenta

### Etapa 4: Construir landing na ferramenta escolhida (120 minutos)

Objetivo: montar a página com estrutura e copy aplicadas, garantindo usabilidade.

Passos:
- Configurar projeto na ferramenta (domínio temporário ou slug)
- Reproduzir estrutura definida adicionando copy e assets
- Ajustar estilos (cores, tipografia) conforme identidade disponível
- Implementar CTAs (botões, formulários) nas seções relevantes
- Inserir provas sociais, FAQ e seção final de CTA
- Publicar versão de staging/pré-visualização para QA inicial

Outputs:
- Página montada e acessível em ambiente de testes
- Registro de links e acessos relevantes (editor, preview)
- Notas de ajustes pendentes antes da publicação final

### Etapa 5: Configurar formulário, automações e analytics (60 minutos)

Objetivo: garantir captura de dados, mensuração e integrações necessárias.

Passos:
- Configurar formulário (campos, mensagens de sucesso, redirecionamento)
- Integrar com CRM, planilha ou e-mail (conforme ferramentas aprovadas)
- Implementar pixels/analytics: Google Analytics, Meta Pixel, outros aprovados
- Configurar eventos básicos: PageView, Lead, Purchase (se aplicável)
- Testar formulários e eventos com dados fictícios e inspecionar disparos
- Registrar UTM padrão e parâmetros obrigatórios no plano de analytics

Template de apoio: `_DATA/plano-analytics.MD`

Outputs:
- Formulário/CTA testado com evidência (screenshot, log de evento)
- Scripts de analytics inseridos e verificados
- Plano de métricas documentado com responsáveis e cadência de análise

### Etapa 6: QA, otimização rápida e publicação (75 minutos)

Objetivo: validar qualidade final antes do lançamento oficial.

Passos:
- Executar checklist de QA (responsividade, links, ortografia, tempo de carga)
- Ajustar imagens e compressão para atingir tempo alvo (< 3s desktop)
- Revisar copy final e formatação (hierarquia, espaçamento, contraste)
- Publicar página no domínio final ou subdomínio aprovado
- Registrar URL final e enviar para stakeholders
- Documentar próximos passos e backlog de otimizações

Template de apoio: `_DATA/checklist-qa.MD`

Outputs:
- Checklist de QA completo e salvo em `_DATA/`
- URL final publicada e acessível
- Relatório curto com métricas iniciais e pendências pós-lançamento

## Pontos de Decisão

1. **Após Etapa 1 (Briefing):** Ferramenta escolhida está aprovada?  
   - Se não, documentar necessidade no catálogo de ferramentas e aguardar aprovação.

2. **Após Etapa 2 (Estrutura):** Wireframe atende narrativa completa (problema → solução → prova → oferta)?  
   - Se não, iterar antes de redigir copy.

3. **Após Etapa 4 (Construção):** Página em staging reflete copy e estrutura planejadas?  
   - Se não, ajustar antes de implementar analytics.

4. **Após Etapa 5 (Configuração):** Eventos e formulários disparam corretamente?  
   - Se não, revisar integrações antes de publicar.

5. **Após Etapa 6 (QA):** Checklist sem pendências críticas?  
   - Se não, bloquear publicação até corrigir.

## Resultados Esperados

1. Briefing estruturado com metas e oferta
2. Estrutura textual validada (wireframe)
3. Copy completa com bullets e provas sociais
4. Landing montada na ferramenta aprovada
5. Formulário e analytics configurados e testados
6. Checklist de QA concluído e página publicada
7. Registro de métricas iniciais e plano de acompanhamento

## Indicadores-Chave de Desempenho

- Tempo total de criação (meta: ≤ 8 horas)
- Tempo de carregamento inicial (meta: ≤ 3s desktop, ≤ 4s mobile)
- Percentual de seções implementadas conforme estrutura (meta: 100%)
- Taxa de erro nos testes de formulário/analytics (meta: 0 falhas)
- Taxa de aprovação no checklist de QA (meta: 100% itens críticos concluídos)

## Avisos e Armadilhas Comuns

1. **Ferramenta não aprovada:** validar antes de iniciar para evitar retrabalho.
2. **Copy não aderente à linguagem:** utilize citações reais para evitar generalidades.
3. **Formulário sem teste:** sempre teste submissões antes de tráfego pago.
4. **Scripts em conflito:** verifique console do navegador para erros JS.
5. **Imagens pesadas:** comprima arquivos e utilize formatos modernos (WebP).
6. **DNS sem propagação:** se usar domínio customizado, considere janela de até 24h e plano B (subdomínio).

## Dependências

Entradas necessárias:
- Declaração de hipótese atualizada ([ProblemHypothesisDefinition](../ProblemHypothesisDefinition/process.MD))
- Perfis e linguagem do cliente ([TargetUserIdentification](../TargetUserIdentification/process.MD), [UserInterviewValidation](../UserInterviewValidation/process.MD))
- Artefatos criados em `_DATA/` (biblioteca de linguagem, citações)

Saídas habilitam:
- [CheckoutSetup](../ a definir) – integração com pagamentos
- [OutreachCampaign] – direcionamento de tráfego
- Métricas para revisões estratégicas em `strategies/ZeroUm`

## Referências

- [UserInterviewValidation/process.MD](../UserInterviewValidation/process.MD) – fonte de insights para copy
- [_SHARED/templates/declaracao-hipotese.md](../_SHARED/templates/declaracao-hipotese.md) – referência para headline
- [tasks.MD](tasks.MD) – execução operacional
- [knowledge.MD](knowledge.MD) – melhores práticas e troubleshooting
