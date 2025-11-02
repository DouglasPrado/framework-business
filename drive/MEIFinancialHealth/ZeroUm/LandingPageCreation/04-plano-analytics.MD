# Plano de Analytics e Monitoramento – LucroSeparado

## Identificação

- Produto/Oferta: Programa Beta LucroSeparado
- URL da landing: https://lucroseparado.carrd.co (slug temporário)
- Data de publicação: 03/11/2025 (prevista)
- Owner de métricas: Douglas Prado

## Configuração de Tags e Pixels

- Google Analytics / GA4:
  - ID: G-2MEI4LUCRO
  - Local de inserção: Google Tag Manager (contêiner GTM-MEI123) embutido no Carrd
  - Responsável: Douglas Prado
- Meta Pixel:
  - ID: 123456789012345
  - Eventos configurados: PageView, Lead (via evento personalizado), CTAClick (btn hero)
  - Responsável: Douglas Prado
- Outras ferramentas:
  - Hotjar (heatmap) – ID HJ-889922 – instalar somente após meta de conversões iniciais

## Eventos e Conversões

- Evento primário: lead_submit (Typeform submission + redirect com parâmetro ?status=lead)
- Eventos secundários:
  - cta_click_hero (clique botão hero)
  - faq_toggle (interação com FAQ – evento GTM)
  - scroll_75 (usuário chegou a 75% da página)
- Conversões configuradas:
  - Plataforma: Google Ads (caso tráfego pago) – conversão “Lead LucroSeparado Beta”
  - Plataforma: Meta Ads – evento Lead otimizado via API de conversões (se campanha ativa)

## UTMs e Parâmetros

- Padrão de UTM Source: instagram, whatsapp, feira, telegram, email
- Padrão de UTM Medium: organic, paid, referral
- Padrão de UTM Campaign: lp-lucroseparado-beta-nov2025
- Padrões adicionais:
  - utm_content: hero-botao, prova-social, faq-link
  - utm_term: (usar apenas em campanhas pagas)
- Tabela de campanhas previstas:
  - Campanha | Fonte | UTM completa | Responsável | Data início
  - Lista Beta WhatsApp | whatsapp | lp-lucroseparado-beta-nov2025&utm_source=whatsapp&utm_medium=organic&utm_content=lista-grupo | Douglas | 03/11
  - Stories Instagram | instagram | lp-lucroseparado-beta-nov2025&utm_source=instagram&utm_medium=organic&utm_content=stories-cta | Douglas | 04/11
  - Feira Lavradio QR | feira | lp-lucroseparado-beta-nov2025&utm_source=feira&utm_medium=referral&utm_content=qr-code | Douglas | 09/11

## Dashboards / Relatórios

- Ferramenta: Looker Studio conectado ao GA4 + planilha de leads (Google Sheets)
- Frequência de atualização: automática (GA4 em tempo real) + revisão manual diária nas primeiras 72h
- Responsável por enviar relatório: Douglas Prado
- Destinatários: Squad ZeroUm (Douglas + stakeholders)

## Monitoramento Inicial (primeiras 72h)

- Check 1 (04/11 12h):
  - Visitas: ______
  - Conversões: ______
  - Observações: ______
- Check 2 (05/11 12h):
  - Visitas: ______
  - Conversões: ______
  - Observações: ______
- Check 3 (06/11 12h):
  - Visitas: ______
  - Conversões: ______
  - Observações: ______

## Alertas e Contingência

- Evento crítico: Formulário Typeform fora do ar
  - Ação: Ativar fallback com formulário Google Forms (link alternativo), comunicar via banner na landing
  - Contato: support@lucroseparado.com (Douglas)
- Conversão abaixo da meta (<25% após 120 visitas):
  - Checklist: Revisar copy hero, confirmar funcionamento do Typeform, analisar mapa de calor, testar CTA secundário
- Falha em scripts/pixels:
  - Procedimento: Usar Tag Assistant / Pixel Helper, revisar contêiner GTM, disparar teste manual com hits de debug

## Próximas Ações

- Ajuste planejado:
  - Descrição: Implementar evento de clique no botão “Ver como funciona” para medir interesse na seção de solução.
  - Owner: Douglas Prado
  - Prazo: 05/11/2025
- Teste A/B considerado:
  - Hipótese: Headline com “retirada ideal” converte mais que “lucro claro”
  - Métrica alvo: Taxa de clique no CTA hero
- Observações adicionais:
  - Registrar prints do GA4 e Pixel Helper em `_DATA/evidencias` após publicação.
