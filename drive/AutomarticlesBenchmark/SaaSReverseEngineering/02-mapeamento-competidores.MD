# Mapeamento de URLs de Competidores – Processo SaaSReverseEngineering

## Checklist de Cobertura
- [x] Homepage de cada competidor
- [x] Pricing page
- [x] Página de produto/funcionalidades
- [x] Referências (cases, blog, documentação)
- [x] Total de 15+ URLs verificados manualmente

---

## Competidor 1 – Automarticles

### Informações Básicas
- **Nome:** Automarticles
- **Website:** https://automarticles.com/
- **Descrição:** Plataforma brasileira que cria, publica e mantém blogs automaticamente (conteúdo + SEO + relatórios via WhatsApp) para empresas sem time de conteúdo.
- **Razão para análise:** Player local com forte posicionamento em automação completa e foco em português; referência direta para o benchmark solicitado.

### URLs Coletadas
- **Homepage:** https://automarticles.com/ — Status: [x] Funcionando
- **Pricing:** https://automarticles.com/#planos — Status: [x] Funcionando (sessão dentro da homepage)
- **Features/Product:** https://automarticles.com/#funcionalidades — Status: [x] Funcionando
- **FAQ/Help:** N/A (informações de suporte aparecem distribuídas na homepage)
- **About/Company:** https://automarticles.com/#inicio — Status: [x] Funcionando (sessão institucional)
- **Case Studies/Testemunhos:** https://automarticles.com/#feedbacks — Status: [x] Funcionando
- **Blog/Conteúdo:** https://automarticles.com/blog/ — Status: [x] Funcionando (redireciona para /blog/)

### Total de URLs
- **Número:** 6
- **Cobertura:** [x] Ótima (4-6)

### Notas
- Todo o funil (prova social, planos, features) está concentrado em uma long page. Anchors (#planos, #funcionalidades, #feedbacks) facilitam coleta sem navegação adicional.

---

## Competidor 2 – Autoblogging.ai

### Informações Básicas
- **Nome:** Autoblogging.ai
- **Website:** https://autoblogging.ai/
- **Descrição:** Ferramenta internacional focada em geração de artigos SEO em múltiplos modos (Quick, News, Godlike) para criadores, afiliados e agências.
- **Razão para análise:** Representa modelo credit-based de alto volume, muito citado por afiliados e SEOs que escalam programmatic content.

### URLs Coletadas
- **Homepage:** https://autoblogging.ai/ — Status: [x] Funcionando
- **Pricing:** https://autoblogging.ai/#pricing — Status: [x] Funcionando (sessão "Pricing")
- **Features/Product:** https://autoblogging.ai/#feature-image — Status: [x] Funcionando (carrossel de modos)
- **FAQ/Help:** https://autoblogging.ai/whats-new/ — Status: [x] Funcionando (changelog+FAQ sobre releases)
- **About/Company:** https://autoblogging.ai/about-us/ — Status: [x] Funcionando
- **Testimonials:** https://autoblogging.ai/#testimonialContainer — Status: [x] Funcionando

### Total de URLs
- **Número:** 6
- **Cobertura:** [x] Ótima (4-6)

### Notas
- Conteúdo estruturado em seções únicas com IDs, o que facilita scraping direto. Pricing e features usam o mesmo DOM da homepage.

---

## Competidor 3 – Jasper

### Informações Básicas
- **Nome:** Jasper (Jasper.ai)
- **Website:** https://www.jasper.ai/
- **Descrição:** Plataforma enterprise de automação de marketing com agentes, Canvas, Brand Voice e camadas de governança.
- **Razão para análise:** Benchmark enterprise/global que mostra como diferenciar via governança, customização e integrações profundas.

### URLs Coletadas
- **Homepage:** https://www.jasper.ai/ — Status: [x] Funcionando
- **Pricing:** https://www.jasper.ai/pricing — Status: [x] Funcionando
- **Platform Overview:** https://www.jasper.ai/platform — Status: [x] Funcionando
- **Solutions/Use Cases:** https://www.jasper.ai/solutions — Status: [x] Funcionando
- **Customer Stories:** https://www.jasper.ai/customers — Status: [x] Funcionando
- **Resources/Blog:** https://www.jasper.ai/blog — Status: [x] Funcionando
- **Trust/Security:** https://www.jasper.ai/trust — Status: [x] Funcionando

### Total de URLs
- **Número:** 7
- **Cobertura:** [x] Extensa (7+)

### Notas
- Páginas servidas via Webflow/CDN com conteúdo SSR; consumo por anchors não necessário. Pricing alterna valores mensais/anuais via JS, mas HTML já contém ambos.

---

## Resumo Geral
- **Competidores analisados:** 3
- **Total de URLs mapeadas:** 19
- **Situação:** Cobertura mínima atendida; material suficiente para extração de problema, solução, pricing, ICP e diferenciais.
