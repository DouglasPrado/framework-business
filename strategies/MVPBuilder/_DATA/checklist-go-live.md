# Checklist de Go-Live - MVP

**Projeto**: [Nome do Produto/MVP]
**Data prevista de lancamento**: [DD/MM/AAAA]
**Responsavel**: [Nome]

---

## Objetivo deste Checklist

Este checklist garante que todos os aspectos criticos do MVP foram validados antes do lancamento em producao. Nao passe para producao ate que TODOS os itens marcados como obrigatorios estejam completos.

**Como usar**:
- [ ] = Pendente
- [x] = Completo
- [~] = Nao aplicavel (justifique)

---

## 1. Validacoes Tecnicas

### Infraestrutura e Deploy

- [ ] **Deploy de producao funcionando**
  - Aplicacao acessivel via URL de producao
  - HTTPS configurado e funcionando
  - Certificado SSL valido

- [ ] **Banco de dados de producao configurado**
  - Banco criado e acessivel
  - Migrations aplicadas com sucesso
  - Backup automatico configurado

- [ ] **Variaveis de ambiente de producao configuradas**
  - Todas as variaveis necessarias no Vercel/hosting
  - DATABASE_URL apontando para banco de producao
  - NEXTAUTH_SECRET configurado (diferente de dev)
  - NEXTAUTH_URL com URL de producao
  - STRIPE_SECRET_KEY (modo live)
  - STRIPE_WEBHOOK_SECRET (producao)
  - Email service API keys configuradas
  - Sem variaveis de teste/dev em producao

- [ ] **DNS configurado (se dominio customizado)**
  - Dominio apontando para servidor correto
  - Propagacao de DNS completa
  - Redirecionamentos (www → sem www ou vice-versa) funcionando

### Funcionalidades Core

- [ ] **Cadastro e login funcionando**
  - Usuario consegue criar conta
  - Usuario consegue fazer login
  - Sessao persiste entre reloads
  - Logout funciona corretamente
  - Recuperacao de senha funcionando

- [ ] **Funcionalidade principal funcionando end-to-end**
  - Fluxo completo testado em producao
  - Todos os passos da funcionalidade core funcionam
  - Dados sendo salvos corretamente no banco
  - Performance aceitavel (< 2s de resposta)

- [ ] **Funcionalidades secundarias funcionando**
  - Todas as funcionalidades secundarias testadas
  - Integracao com funcionalidade core funcionando
  - Sem bugs criticos (P0) conhecidos

### Sistema de Pagamento

- [ ] **Stripe em modo live configurado**
  - Conta Stripe aprovada para modo live
  - Chaves API de producao configuradas
  - Produtos/precos de producao criados
  - Webhook apontando para URL de producao
  - Webhook secret configurado no backend

- [ ] **Fluxo de pagamento funcionando**
  - Usuario consegue iniciar checkout
  - Pagamento com cartao real funciona (teste com cartao proprio)
  - Webhook recebe confirmacao de pagamento
  - Status de assinatura atualiza no banco corretamente
  - Email de confirmacao de pagamento enviado

- [ ] **Teste completo com transacao real**
  - Fazer transacao real de teste ($1-5)
  - Confirmar que dinheiro aparece no Stripe
  - Confirmar que acesso ao produto e liberado
  - Testar estorno (se aplicavel)

### Email e Notificacoes

- [ ] **Servico de email configurado em producao**
  - API keys de producao configuradas
  - Dominio verificado (se necessario)
  - SPF/DKIM configurados (reduz spam)

- [ ] **Emails transacionais funcionando**
  - Email de boas-vindas enviado apos cadastro
  - Email de recuperacao de senha funcionando
  - Email de confirmacao de pagamento enviado
  - Emails nao indo para spam (testar Gmail, Outlook)

### Performance e Responsividade

- [ ] **Performance aceitavel**
  - Tempo de carregamento inicial < 3s
  - Tempo de resposta de API < 2s
  - Paginas principais testadas com Lighthouse (score > 70)
  - Imagens otimizadas

- [ ] **Responsividade testada**
  - Funciona em desktop (Chrome, Safari, Firefox)
  - Funciona em mobile (iOS Safari, Android Chrome)
  - Funciona em tablet
  - Breakpoints principais testados (375px, 768px, 1280px)

### Monitoramento e Observabilidade

- [ ] **Analytics configurado**
  - Google Analytics 4 ou Posthog instalado
  - Eventos customizados configurados:
    - Cadastro concluido
    - Login
    - Funcionalidade core usada
    - Pagamento iniciado
    - Pagamento concluido
  - Testado que eventos estao sendo enviados

- [ ] **Error tracking configurado**
  - Sentry instalado e configurado
  - Erros sendo capturados corretamente
  - Alertas configurados para erros criticos
  - Testar erro de proposito e validar captura

- [ ] **Uptime monitoring configurado**
  - Alertas de downtime ativos (Vercel, UptimeRobot, etc)
  - Email/Slack notification configurada
  - Dashboard de status acessivel

### Testes Completos

- [ ] **Smoke test completo executado**
  - Cadastro → Login → Funcionalidade core → Pagamento → Logout
  - Fluxo executado sem erros
  - Testado por pelo menos 2 pessoas diferentes

- [ ] **Casos de erro testados**
  - Login com senha errada (mensagem amigavel)
  - Cadastro com email duplicado (erro tratado)
  - Pagamento recusado (mensagem amigavel)
  - Campos obrigatorios vazios (validacao frontend)
  - Falha de API (error handling adequado)

- [ ] **Navegadores testados**
  - Chrome (desktop)
  - Safari (desktop)
  - Firefox
  - Safari (iOS)
  - Chrome (Android)

---

## 2. Validacoes de Negocio

### Conteudo e Documentacao

- [ ] **Paginas institucionais criadas**
  - Pagina inicial (home) com proposta de valor clara
  - Pagina "Sobre" ou "Como funciona"
  - Pagina de pricing/planos clara
  - Pagina de contato ou suporte

- [ ] **Documentacao de usuario criada**
  - Getting Started / Como usar
  - FAQ com perguntas comuns
  - Guia da funcionalidade principal
  - Documentacao acessivel e facil de encontrar

- [ ] **Conteudo revisado**
  - Textos sem erros de portugues
  - Mensagens amigaveis e claras
  - Call-to-actions (CTAs) claros
  - Proposta de valor bem comunicada

### Pricing e Produtos

- [ ] **Produtos Stripe criados**
  - Produtos de producao criados no Stripe
  - Precos corretos configurados
  - Descricoes claras
  - Moeda correta (BRL, USD, etc)

- [ ] **Pricing claro e transparente**
  - Precos visiveis na pagina de pricing
  - Informacao sobre o que esta incluso
  - Politica de reembolso clara
  - Informacao sobre cancelamento (se assinatura)

### Early Adopters e Lancamento

- [ ] **Lista de early adopters identificada**
  - Minimo 20-30 pessoas identificadas
  - Contatos coletados e organizados
  - Mensagem de convite preparada

- [ ] **Incentivo para early adopters definido**
  - Desconto, acesso vip, lifetime deal ou outro incentivo
  - Incentivo comunicado claramente

- [ ] **Plano de onboarding preparado**
  - Script de onboarding 1:1 (se aplicavel)
  - Email de boas-vindas personalizado
  - Canal de suporte direto (email, Slack, WhatsApp)

- [ ] **Materiais de comunicacao preparados**
  - Email de lancamento escrito
  - Posts para redes sociais preparados
  - Mensagens para lista de espera (se houver)

---

## 3. Validacoes de Legal e Compliance

### Documentos Legais

- [ ] **Termos de uso criados**
  - Termos disponiveis e visiveis no site
  - Link no footer de todas as paginas
  - Usuario aceita termos no cadastro

- [ ] **Politica de privacidade criada**
  - Conforme LGPD (Lei Geral de Protecao de Dados)
  - Explicita quais dados sao coletados
  - Explicita como dados sao usados
  - Informacao sobre direitos do usuario
  - Link no footer de todas as paginas

- [ ] **Politica de reembolso definida (se aplicavel)**
  - Politica clara e visivel
  - Prazo de reembolso especificado
  - Processo de solicitar reembolso explicado

### LGPD e Cookies

- [ ] **Consentimento de dados no cadastro**
  - Checkbox de consentimento de tratamento de dados
  - Texto explicativo sobre uso de dados
  - Link para politica de privacidade

- [ ] **Banner de cookies (se aplicavel)**
  - Banner exibido na primeira visita
  - Usuario pode aceitar ou recusar cookies nao essenciais
  - Preferencias salvas

- [ ] **Direito de exclusao de dados implementado**
  - Usuario consegue deletar propria conta (ou solicitar)
  - Dados sao removidos do banco (ou anonimizados)

### Seguranca Basica

- [ ] **Senhas com hash**
  - Senhas armazenadas com bcrypt ou similar
  - NUNCA em texto plano

- [ ] **HTTPS obrigatorio**
  - Todo trafego em HTTPS
  - Sem conteudo mixed (http + https)

- [ ] **Protecao contra ataques basicos**
  - Rate limiting em endpoints criticos (login, cadastro)
  - Validacao de inputs (prevencao de SQL injection, XSS)
  - CORS configurado adequadamente

---

## 4. Validacoes de Experiencia do Usuario

### Usabilidade

- [ ] **Navegacao intuitiva**
  - Usuario consegue encontrar funcionalidade principal facilmente
  - Menu/navegacao claro
  - Breadcrumbs ou indicadores de localizacao (se aplicavel)

- [ ] **Feedback visual adequado**
  - Loading states em acoes assincronas
  - Mensagens de sucesso apos acoes (ex: "Projeto salvo!")
  - Mensagens de erro amigaveis e acionaveis
  - Confirmacoes antes de acoes destrutivas (deletar, cancelar)

- [ ] **Empty states implementados**
  - Mensagens quando nao ha dados ainda
  - Call-to-action para criar primeiro item
  - Nao deixar telas completamente vazias

- [ ] **Acessibilidade basica**
  - Navegacao por teclado funciona
  - Labels em formularios claros
  - Contraste adequado (texto legivel)
  - Alt text em imagens importantes

### Onboarding

- [ ] **Primeiro uso claro**
  - Usuario entende o que fazer apos login
  - Dashboard inicial nao e confuso
  - (Opcional) Tour guiado ou tooltips

- [ ] **Email de boas-vindas efetivo**
  - Email enviado imediatamente apos cadastro
  - Explica proximos passos
  - Links para documentacao e suporte

---

## 5. Validacoes de Suporte e Operacao

### Suporte ao Usuario

- [ ] **Canal de suporte definido**
  - Email de suporte configurado e monitorado
  - Ou chat, ou formulario de contato
  - Tempo de resposta esperado comunicado

- [ ] **Processo de suporte documentado**
  - Time sabe como responder perguntas comuns
  - Escalacao de bugs criticos definida
  - FAQ cobre perguntas principais

### Monitoramento Pos-Lancamento

- [ ] **Plano de monitoramento definido**
  - Quem vai monitorar metricas diariamente?
  - Quem vai responder alertas de erro?
  - Frequencia de check-ins (daily, 2x dia, etc)

- [ ] **Rituais pos-lancamento agendados**
  - Daily check nas primeiras 48h
  - Weekly review agendado
  - Retrospectiva de 2 semanas agendada

### Rollback Plan

- [ ] **Plano de rollback documentado**
  - Como reverter para versao anterior?
  - Quem tem permissao para executar rollback?
  - Backup do banco antes de lancamento

- [ ] **Comunicacao de incidentes planejada**
  - Como comunicar usuarios se houver problema critico?
  - Template de mensagem preparado
  - Canal de comunicacao definido (email, status page)

---

## 6. Validacoes de Time e Alinhamento

### Alinhamento Interno

- [ ] **Time ciente da data de lancamento**
  - Todos sabem quando e o go-live
  - Disponibilidade garantida nas primeiras 48h
  - Contatos de emergencia compartilhados

- [ ] **Demo final realizada**
  - Stakeholders viram MVP completo
  - Feedback coletado e ajustes feitos (se necessario)

- [ ] **Aprovacao formal de lancamento**
  - Product Owner aprovou
  - Tech Lead aprovou
  - Outros stakeholders necessarios aprovaram

### Comunicacao Externa

- [ ] **Plano de comunicacao de lancamento**
  - Email para lista de espera preparado
  - Posts em redes sociais agendados
  - Mensagem para early adopters enviada
  - Press release ou blog post (se aplicavel)

---

## 7. Checklist Final Pre-Lancamento

Execute estas validacoes nas ultimas 24h antes do lancamento:

- [ ] **Fazer transacao real de teste (ultima vez)**
- [ ] **Testar fluxo completo em producao (ultima vez)**
- [ ] **Validar que emails estao sendo enviados**
- [ ] **Validar que analytics esta coletando eventos**
- [ ] **Validar que Sentry esta capturando erros**
- [ ] **Confirmar que time esta disponivel para suporte**
- [ ] **Confirmar data e hora de lancamento com todos**
- [ ] **Fazer backup do banco de dados**
- [ ] **Tomar um cafe e respirar fundo**

---

## 8. Go/No-Go Decision

### Criterios para GO (Lancar)

Para aprovar o lancamento, TODOS os criterios abaixo devem ser verdadeiros:

- [ ] Todos os itens marcados como obrigatorios neste checklist estao completos
- [ ] Zero bugs criticos (P0) conhecidos que impedem uso basico
- [ ] Funcionalidade core funciona end-to-end sem erros
- [ ] Sistema de pagamento validado com transacao real
- [ ] Monitoramento (analytics + error tracking) funcionando
- [ ] Time disponivel para suporte nas proximas 48h
- [ ] Aprovacao formal de stakeholders obtida

### Criterios para NO-GO (Adiar lancamento)

Adie o lancamento se QUALQUER um dos criterios abaixo for verdadeiro:

- [ ] Bug critico (P0) impede uso da funcionalidade core
- [ ] Sistema de pagamento nao esta funcionando
- [ ] Monitoramento nao esta capturando dados
- [ ] Termos de uso ou politica de privacidade faltando
- [ ] Time nao esta disponivel para suporte pos-lancamento
- [ ] Stakeholder critico nao aprovou lancamento

---

## 9. Decisao Final

**Data desta validacao**: [DD/MM/AAAA]
**Horario**: [HH:MM]

**Decisao**:
- [ ] **GO** - Lancamento aprovado
- [ ] **NO-GO** - Lancamento adiado

**Razao (se NO-GO)**:
[Descreva o que impede o lancamento e quando pode ser reavaliado]

**Proximo review** (se NO-GO): [DD/MM/AAAA]

---

## 10. Assinaturas de Aprovacao

**Product Owner**:
- Nome: [Nome]
- Assinatura: ________________
- Data: [DD/MM/AAAA]

**Tech Lead**:
- Nome: [Nome]
- Assinatura: ________________
- Data: [DD/MM/AAAA]

**Outro Stakeholder**:
- Nome: [Nome]
- Assinatura: ________________
- Data: [DD/MM/AAAA]

---

## Pos-Lancamento

### Primeiras 24h

- [ ] Monitorar Sentry a cada 2-4 horas
- [ ] Checar metricas de cadastro e ativacao
- [ ] Responder suporte em ate 2 horas
- [ ] Fazer daily check com time

### Primeira Semana

- [ ] Monitorar metricas diariamente
- [ ] Coletar feedback de early adopters
- [ ] Corrigir bugs P0 em ate 24h
- [ ] Fazer weekly review no fim da semana

### Primeiras 4 Semanas

- [ ] Continuar monitoramento semanal
- [ ] Realizar entrevistas com usuarios
- [ ] Coletar dados para relatorio de validacao
- [ ] Preparar decisao: Pivotar, Perseverar ou Expandir

---

**Checklist criado em**: 2025-11-05
**Versao**: 1.0
**Parte de**: Estrategia MVP Builder
**Mantido por**: Framework Business Team

---

**Notas importantes**:

1. Este checklist e extenso de proposito. Nem tudo se aplica a todo MVP. Marque como [~] itens nao aplicaveis e justifique.

2. Priorize items de seguranca, legal (LGPD) e funcionalidade core. O resto pode ser refinado pos-lancamento.

3. Lancamento rapido > Perfeicao. Se funcionalidade core funciona e nao ha bugs criticos, considere lancar mesmo se pequenos detalhes faltarem.

4. Lembre-se: MVP e sobre validacao, nao perfeicao. O objetivo e aprender rapido com usuarios reais.
