# Template Compartilhado – Checklist de Qualidade

Use este checklist como base para validar entregáveis digitais (landing pages, checkouts, fluxos de entrega e materiais enviados ao cliente). Duplique para a pasta `_DATA/` do processo correspondente e marque módulos relevantes conforme o tipo de entregável.

## Informações Gerais

- Entregável verificado:
- Link / local do arquivo:
- Data do QA:
- Responsável pela validação:
- Versão / sprint:

## Módulo A – Conteúdo e Comunicação

- [ ] Ortografia e gramática revisadas.
- [ ] Mensagem principal alinhada ao briefing ou hipótese.
- [ ] CTA(s) coerentes com o próximo passo esperado.
- [ ] Provas sociais citam fonte e autorização.
- [ ] Linguagem consistente com a persona (`../_SHARED/templates/persona.MD`).

## Módulo B – Funcionalidade e Experiência

- [ ] Links, formulários ou botões testados (inclui erro e sucesso).
- [ ] Redirecionamentos configurados corretamente.
- [ ] Campos obrigatórios validados e mensagens de erro claras.
- [ ] Sequências automatizadas (e-mails, webhooks) disparando como previsto.
- [ ] Confirmações visíveis ao usuário final (tela de obrigado, recibo, notificação).

## Módulo C – Responsividade e Acessibilidade

- [ ] Visual conferido em desktop (≥1280px), tablet (~768px) e mobile (~375px).
- [ ] CTA visível e clicável em todas as resoluções.
- [ ] Hierarquia de títulos (H1, H2, H3) preservada.
- [ ] Texto alternativo inserido em imagens críticas.
- [ ] Contraste adequado entre texto e fundo (WCAG básico).

## Módulo D – Performance e Confiabilidade

- [ ] Teste de velocidade executado (ex: PageSpeed) e registrado.
- [ ] Tamanho de imagens e assets otimizado (≤ 300 KB quando aplicável).
- [ ] Sem erros críticos no console ou logs.
- [ ] Monitoramento configurado (analytics, UTM, alertas).
- [ ] Backup/export do entregável salvo (se aplicável).

## Módulo E – Operação e Handoff

- [ ] Documentação atualizada em `_DATA/` (briefings, logs, evidências).
- [ ] Responsáveis por monitoramento definidos com cadência.
- [ ] Próximo processo avisado e ciente dos insumos.
- [ ] Checklist foi revisado em dupla ou aprovado por stakeholder.
- [ ] Pendências registradas com owner e prazo.

## Observações e Pendências

- Pendência 1 (owner + prazo):
- Pendência 2:
- Observações gerais:

## Decisão Final

- ( ) Aprovado sem ajustes
- ( ) Aprovado com ajustes menores (anexar lista)
- ( ) Reprovado – refazer antes do go-live
