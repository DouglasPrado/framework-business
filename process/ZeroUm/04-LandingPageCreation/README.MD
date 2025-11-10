# LandingPageCreation

## Visão Geral

Este processo orienta a criação e publicação de uma landing page de pré-venda em até 8 horas, desde o briefing de copy até a configuração de analytics. O foco é transformar hipóteses validadas e linguagem do cliente em uma página funcional que colete leads ou pedidos antecipados, com rastreabilidade completa.

## Quando Usar

Use este processo quando:
- Há hipóteses validadas por entrevistas (ex: [UserInterviewValidation](../03-UserInterviewValidation/process.MD))
- Existe necessidade de testar proposta de valor via tráfego pago ou orgânico
- É preciso abrir canal de aquisição antes de desenvolver o produto completo
- O time precisa coletar métricas de interesse (visitas, conversões) em curto prazo
- A estratégia ZeroUm avança para a Etapa 2 (Landing page de pré-venda)

## Pré-requisitos

- Declaração de hipótese atualizada ([Declaração de Hipótese](../_SHARED/templates/declaracao-hipotese.md))
- Biblioteca de linguagem do cliente consolidada em `_DATA/` do processo anterior
- Seleção preliminar da ferramenta de publicação (confirmar em `tools/`)
- Acesso às credenciais necessárias (domínio, conta da plataforma escolhida, analytics)
- Tempo bloqueado de 6-8 horas corridas ou distribuídas no mesmo dia

## Tempo Estimado

- Preparação e briefing: 45 minutos
- Estrutura e copy: 2 horas
- Construção na ferramenta: 2 horas
- Configuração de formulários e analytics: 1 hora
- QA (responsividade, performance, revisão final): 1h15
- Total recomendado: 6-8 horas

## Resultado Esperado

Ao final deste processo você terá:
- Landing page publicada com URL validada
- Copy completa utilizando linguagem real do cliente
- Formulário ou CTA funcional (captura de leads ou checkout)
- Analytics configurado (pixel e eventos principais)
- Checklist de QA assinado e registro de performance inicial
- Plano de monitoramento e ajustes pós-lançamento

## Arquivos Principais

- [process.MD](process.MD) – fluxo detalhado do processo
- [knowledge.MD](knowledge.MD) – conceitos, boas práticas, FAQs e riscos
- [tasks.MD](tasks.MD) – checklist operacional executável
- [validator.MD](validator.MD) – critérios para validar a entrega
- Pasta `_DATA/` – templates de briefing, estrutura de seção, copy e QA

## Como Executar

1. Leia [process.MD](process.MD) para entender etapas, entregáveis e pontos de decisão.
2. Siga [tasks.MD](tasks.MD), preenchendo o checklist e registrando evidências.
3. Utilize os templates em `_DATA/` para briefing, copy e QA.
4. Documente cada saída (copy final, prints, métricas) na pasta `_DATA/`.
5. Ao final, valide com [validator.MD](validator.MD) antes de considerar concluído.

## Critérios de Qualidade

- Landing publicada e acessível no ambiente escolhido
- Copy alinhada à linguagem validada com pelo menos 3 bullets de benefícios
- Formulário/CTA testado em desktop e mobile
- Analytics e eventos-chave verificados em tempo real
- Tempo de carregamento ≤ 3 segundos em desktop (referência GTmetrix / PageSpeed)
- Registro de evidências e checklist de QA concluído

## Próximos Processos

1. **CheckoutSetup** – integrar página com fluxo de pagamento
2. **OutreachCampaign** – direcionar tráfego qualificado para a landing
3. **ContentPublication** – suportar campanha com conteúdos derivados
4. **ManualMVPDesign** – preparar entrega mínima se conversão positiva

## Dependências

### Depende de
- [ProblemHypothesisDefinition](../01-ProblemHypothesisDefinition/process.MD)
- [TargetUserIdentification](../02-TargetUserIdentification/process.MD)
- [UserInterviewValidation](../03-UserInterviewValidation/process.MD)

### Habilita
- Processes de aquisição e vendas (Outreach, Checkout, SalesCall)
- Mensuração de demanda real via métricas de conversão
- Iterações futuras de copy e proposta de valor

## Dicas para Sucesso

- Reutilize citações literais da biblioteca de linguagem para headlines e provas sociais.
- Estabeleça versão mínima publicável: primeiro coloque a página no ar, depois refinamentos.
- Teste CTAs e formulários com dados fictícios antes de publicar.
- Padronize nomes de eventos e parâmetros para facilitar análises posteriores.
- Documente ajustes pós-lançamento na planilha de monitoramento.

## Avisos Importantes

- Confirme se a ferramenta escolhida está aprovada no catálogo `tools/`; caso contrário, documente pedido de inclusão.
- Não publique sem checklist de QA completo (responsividade, ortografia, links).
- Evite usar imagens sem direitos ou sem otimização (peso máximo recomendado: 300 KB).
- Se usar domínio personalizado, verifique propagação DNS antes de campanhas.
- Atualize stakeholders com link final e credenciais de acesso imediatamente após o lançamento.

## Métricas de Sucesso

- Tempo de criação dentro da meta (≤ 8 horas)
- Tempo de carregamento inicial (≤ 3 s desktop, ≤ 4 s mobile)
- Taxa de conversão inicial (definida no briefing) monitorada após 48h
- Integridade dos dados de analytics (eventos disparando corretamente)
- Zero erros críticos identificados no QA pós-publicação

## Suporte e Referências

- [process.MD](process.MD) – detalhes do fluxo
- [tasks.MD](tasks.MD) – checklist operacional
- [knowledge.MD](knowledge.MD) – conceitos, referências e troubleshooting
- Templates em `_DATA/` – briefing, wireframe básico, copy guide, checklist QA, plano de métricas

## Versão e Manutenção

- Versão: 1.0
- Criado em: 2025-10-31
- Responsável: Framework Business Team
- Revisar sempre que novas ferramentas aprovadas ou padrões de copy surgirem

## Estrutura de Arquivos

```
LandingPageCreation/
├── README.MD
├── process.MD
├── knowledge.MD
├── tasks.MD
├── validator.MD
└── _DATA/
    ├── briefing-landing.MD
    ├── estrutura-secoes.MD
    ├── copy-draft.MD
    ├── checklist-qa.MD
    └── plano-analytics.MD
```

Ao executar o processo, adicione versões datadas dos artefatos e evidências na pasta `_DATA/`, mantendo rastreabilidade das iterações.

> Duplique `../_SHARED/templates/estrutura-landing.MD` e `../_SHARED/templates/checklist-qualidade.MD` ao preparar `estrutura-secoes.MD` e `checklist-qa.MD`.
