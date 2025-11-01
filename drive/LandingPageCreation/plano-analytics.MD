# Plano de Analytics e Monitoramento

## Identificação

- Produto/Oferta: Controle Diário de Caixa para Micro Varejo (piloto manual)
- URL da landing: https://controlecaixa.zeroum.carrd.co
- Data de publicação: 12/11/2025
- Owner de métricas: Ana Souza

## Configuração de Tags e Pixels

- Google Analytics / GA4:
  - ID: G-LPILOTO7CA
  - Local de inserção (Tag Manager, direto na ferramenta): Via Google Tag Manager
  - Responsável: Ana Souza
- Meta Pixel:
  - ID: 457812345678901
  - Eventos configurados: PageView, ViewContent, Lead
  - Responsável: Felipe Ramos (suporte técnico)
- Outras ferramentas (LinkedIn, TikTok, etc.):
  - Nome: LinkedIn Insight Tag
  - Detalhes: Inserida pelo Tag Manager para monitorar visitas vindas de outreach B2B; responsável Douglas Prado.

## Eventos e Conversões

- Evento primário (nome + finalidade): lead_piloto – disparado no envio do formulário Carrd e usado como métrica principal de conversão.
- Eventos secundários (scroll, clique, etc.): scroll_75 (profundidade mínima de leitura), cta_whatsapp (clique no botão "Quero falar com o time antes"), faq_toggle (interações nos acordeões de FAQ).
- Conversões configuradas em plataformas de anúncio:
  - Plataforma: Meta Ads
  - Evento: Lead (sincronizado com lead_piloto)
  - Observações: Otimização inicialmente para visitas (ViewContent) até atingir 50 leads semanais.

## UTMs e Parâmetros

- Padrão de UTM Source: whatsapp, email, sebrae, contador-parceiro, organico
- Padrão de UTM Medium: cpc, outreach, referral, organic
- Padrão de UTM Campaign: piloto-controle-caixa-q4-2025
- Padrões adicionais (content, term): content variando por responsável (douglas, ana, felipe); term reservado para palavras-chave caso iniciarmos tráfego pago.
- Tabela de campanhas previstas:
  - Campanha 1: Outreach WhatsApp lista piloto → UTM `whatsapp/outreach/piloto-controle-caixa-q4-2025?content=douglas`
  - Campanha 2: E-mail de contadores parceiros → UTM `email/referral/piloto-controle-caixa-q4-2025?content=carla`
  - Campanha 3: Post LinkedIn Sebrae → UTM `sebrae/organic/piloto-controle-caixa-q4-2025?content=anuncio`

## Dashboards / Relatórios

- Ferramenta utilizada (GA, Data Studio, planilha): GA4 explorations + Looker Studio resumido.
- Frequência de atualização: Tempo real no GA4 e consolidação diária às 9h no Looker Studio.
- Responsável por enviar relatório: Ana Souza (e-mail diário nos três primeiros dias, depois relatório semanal às segundas).
- Destinatários: Douglas Prado, Letícia Martins, Felipe Ramos.

## Monitoramento Inicial (primeiras 72h)

- Check 1 (data/hora): 13/11/2025 09h00
  - Visitas: meta 50 (registrar número real)
  - Conversões: meta 4 leads
  - Observações: Validar disparo de lead_piloto e cta_whatsapp.
- Check 2: 14/11/2025 09h00
  - Visitas: meta acumulada 100
  - Conversões: meta acumulada 8
  - Observações: Revisar fontes de tráfego e taxa por canal.
- Check 3: 15/11/2025 09h00
  - Visitas: meta acumulada 150
  - Conversões: meta acumulada 12
  - Observações: Caso conversão < 8%, revisar hero e CTA primário.

## Alertas e Contingência

- Evento crítico (ex: formulário inoperante):
  - Ação imediata: Publicar aviso na página, direcionar CTA para WhatsApp direto e abrir chamado com suporte Carrd.
  - Contato: Douglas Prado (telefone 11 98888-1111)
- Queda de conversão abaixo da meta:
  - Checklist de auditoria: Revisar copy do hero, confirmar funcionamento do formulário, validar UTMs, analisar gravações de sessão (Hotjar) e coletar feedback dos leads.
- Falha em scripts/pixels:
  - Procedimento: Verificar console, reinstalar container do Tag Manager, testar disparo com modo debug, notificar Felipe Ramos.

## Próximas Ações

- Ajuste planejado:
  - Descrição: Criar variação B do hero com foco em redução de juros e testar após atingir 200 visitas.
  - Owner: Douglas Prado
  - Prazo: 20/11/2025
- Teste A/B considerado:
  - Hipótese: Falar sobre "economizar até R$800 por mês em juros" aumenta cliques no CTA principal.
  - Métrica alvo: Taxa de cliques no CTA principal (CTR do botão).
- Observações adicionais: Configurar gravações de sessão (Hotjar) antes do lançamento e armazenar prints de disparos no diretório `_DATA/evidencias/`.
