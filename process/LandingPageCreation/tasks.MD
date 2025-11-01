# Checklist Operacional - LandingPageCreation

Este checklist orienta a criação e publicação de uma landing page de pré-venda em até 8 horas. Use-o para controlar owners, datas, evidências e garantir que todos os requisitos sejam cumpridos antes de direcionar tráfego.

## Informações do Projeto

- Nome do produto/Oferta:
- Owner responsável:
- Data planejada de publicação:
- Objetivo principal (lead, pré-venda, inscrição):
- Meta de conversão inicial:

---

## Etapa 1 – Consolidar insumos e briefing (45 min)

Owner:
Data início: ___/___/___
Data conclusão: ___/___/___

### Tarefas
- [ ] Revisar declaração de hipótese ([Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md))
- [ ] Analisar biblioteca de linguagem do cliente (citações, bullets)
- [ ] Definir objetivo da landing (lead, venda, lista de espera)
- [ ] Escolher ferramenta aprovada (Carrd/Webflow/Wix/Netlify ou outra listada em `tools/`)
- [ ] Consolidar materiais necessários (logos, imagens, links para checkout)
- [ ] Preencher `_DATA/briefing-landing.MD` com metas, público, oferta e métricas
- [ ] Registrar pendências de acesso (domínio, conta da ferramenta, analytics)

### Output
- [ ] `briefing-landing.MD` salvo em `_DATA/`
- [ ] Checklist de pendências pré-produção atualizado

---

## Etapa 2 – Definir estrutura da página (60 min)

Owner:
Data início:
Data conclusão:

### Tarefas
- [ ] Selecionar layout base/template dentro da ferramenta escolhida
- [ ] Mapear seções obrigatórias (Hero, Problema, Solução, Benefícios, Prova Social, Oferta, FAQ, CTA)
- [ ] Organizar ordem das seções e CTAs intermediários
- [ ] Esboçar wireframe textual utilizando `_DATA/estrutura-secoes.MD`
- [ ] Identificar assets adicionais necessários (imagens, ícones, vídeos) e responsáveis
- [ ] Validar estrutura com stakeholders (se necessário)

### Output
- [ ] `estrutura-secoes.MD` preenchido com narrativa completa
- [ ] Lista de assets pendentes com owners e prazos

---

## Etapa 3 – Produzir copy e selecionar prova social (90 min)

Owner:
Data início:
Data conclusão:

### Tarefas
- [ ] Redigir headline e subheadline com linguagem validada
- [ ] Criar 3 bullets de benefícios (dor → benefício → prova)
- [ ] Escrever seções de problema e solução utilizando citações reais
- [ ] Selecionar quotes da biblioteca de linguagem com autorização
- [ ] Montar FAQ com 3-5 objeções e respostas
- [ ] Definir CTA principal e microcopy do botão
- [ ] Registrar copy final em `_DATA/copy-draft.MD`
- [ ] Revisar ortografia e consistência de tom

### Output
- [ ] `copy-draft.MD` completo com textos prontos para implementação
- [ ] Lista de citações aprovadas com referências às entrevistas

---

## Etapa 4 – Construir landing na ferramenta (120 min)

Owner:
Ferramenta utilizada:

### Tarefas
- [ ] Criar projeto/página na ferramenta selecionada
- [ ] Implementar seções seguindo wireframe e copy aprovados
- [ ] Ajustar identidade visual (cores, tipografia, espaçamento) conforme disponível
- [ ] Inserir provas sociais e seção de FAQ
- [ ] Configurar CTA(s) e links internos/externos
- [ ] Gerar link de pré-visualização (staging) para QA
- [ ] Registrar ajustes pendentes e tempo gasto

### Output
- [ ] Link de preview salvo em `_DATA/`
- [ ] Lista de pendências identificadas antes do QA final

---

## Etapa 5 – Configurar formulário, integrações e analytics (60 min)

Owner:

### Tarefas
- [ ] Configurar formulário (campos obrigatórios, mensagem de sucesso, redirecionamento)
- [ ] Integrar formulário a CRM, planilha ou e-mail (verificar ferramentas aprovadas)
- [ ] Inserir scripts/pixels (Google Analytics, Meta Pixel, outros conforme briefing)
- [ ] Configurar eventos principais (PageView, Lead, Purchase, clique de CTA)
- [ ] Testar formulário e eventos com dados fictícios (registrar evidências)
- [ ] Preencher `_DATA/plano-analytics.MD` com responsáveis, UTMs e cadência de análise
- [ ] Documentar fallback caso ferramentas fiquem offline

### Output
- [ ] Plano de analytics completo em `_DATA/`
- [ ] Evidências de eventos disparando (prints ou logs)

---

## Etapa 6 – QA, otimização e publicação (75 min)

Owner:
Data publicação:
URL final:

### Tarefas
- [ ] Executar `_DATA/checklist-qa.MD` (responsividade, links, ortografia, tempo de carregamento)
- [ ] Ajustar imagens (compressão ≤ 300 KB) e verificar contraste de cores
- [ ] Validar tempo de carregamento (PageSpeed / GTmetrix) em desktop e mobile
- [ ] Revisar copy final com stakeholder (se necessário)
- [ ] Publicar no domínio final ou subdomínio aprovado
- [ ] Registrar URL final e compartilhar com stakeholders
- [ ] Criar backlog de otimizações pós-lançamento
- [ ] Salvar evidências (prints, relatórios de performance inicial) em `_DATA/`

### Output
- [ ] `checklist-qa.MD` marcado como concluído
- [ ] Página publicada e acessível em URL final
- [ ] Registro de métricas iniciais e pendências

---

## Checklist Final de Qualidade

- [ ] Briefing, estrutura, copy, plano de analytics e checklist de QA armazenados em `_DATA/`
- [ ] Ferramenta utilizada está aprovada em `tools/`
- [ ] Landing publicada com CTA funcional testado
- [ ] Eventos de analytics e formulário verificados com evidências
- [ ] Tempo de carregamento ≤ 3s desktop e ≤ 4s mobile (registrar resultado)
- [ ] Provas sociais com autorização documentada
- [ ] Planilha ou relatório de métricas configurado para monitoramento contínuo
- [ ] Validador executado (ver [validator.MD](validator.MD))

---

## Estrutura Recomendada de Arquivos em `_DATA/`

```
_DATA/
├── briefing-landing.MD
├── estrutura-secoes.MD
├── copy-draft.MD
├── plano-analytics.MD
├── checklist-qa.MD
├── evidencias/
│   ├── preview.png
│   ├── testes-formulario.png
│   └── pagespeed.txt
└── backlog-ajustes.MD (opcional)
```

Organize evidências e métricas adicionais nesta estrutura para facilitar auditorias e iterações futuras.
