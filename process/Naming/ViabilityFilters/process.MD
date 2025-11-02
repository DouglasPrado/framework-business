# Processo de Execução - Viability Filters (Naming)

Este processo avalia a long list priorizada aplicando verificações linguísticas, digitais e jurídicas, produzindo uma short list segura.

## Visão geral do fluxo

```
REVISÃO DA LONG LIST → VERIFICAÇÕES LINGUÍSTICAS → DISPONIBILIDADE DIGITAL → BUSCAS JURÍDICAS → MATRIZ DE AVALIAÇÃO → SHORT LIST & HANDOFF
```

## Entradas obrigatórias

- `longlist-naming.MD` e `priorizacao-longlist.MD` (GenerationConsolidation)
- Critérios e pesos (`criterios-avaliacao.MD`)
- Alertas linguísticos (`alertas-linguisticos.MD`)
- Acesso às bases de domínios, redes sociais, registros de marca

## ViabilityFilters.1: Revisão da long list e plano de checagens

### Objetivo
Planejar verificações e distribuir responsabilidades.

### Sequência de ações
- Revisar nomes priorizados, notas e categorias.
- Definir quais verificações serão executadas (linguística, domínio, social, app, jurídico).
- Mapear responsáveis, prazos e ferramentas.
- Registrar plano em `plano-checagens.MD`.

### Pontos de decisão
1. **Recursos e acessos disponíveis?**
   - ✅ Sim → iniciar verificações.
   - ❌ Não → solicitar suporte (jurídico, TI, marketing).
2. **Cronograma compatível com próximos marcos?**
   - ✅ Sim → prosseguir.
   - ❌ Não → ajustar antes de avançar.

### Outputs
- `_DATA/ViabilityFilters/plano-checagens.MD`

## ViabilityFilters.2: Verificações linguísticas e culturais

### Objetivo
Garantir que nomes sejam pronunciáveis e não apresentem significados negativos.

### Sequência de ações
- Avaliar pronúncia e legibilidade em idiomas/mercados relevantes.
- Consultar dicionários, tradutores e falantes nativos (quando necessário).
- Registrar achados em `alertas-riscos-remanescentes.MD` com classificação de risco.
- Atualizar `matriz-avaliacao.MD` com notas/pesos referentes a critérios linguísticos.

### Pontos de decisão
1. **Nomes com risco linguístico alto?**
   - ✅ Sim → marcar como vermelho e sinalizar sponsor.
   - ❌ Não → continuar.
2. **Mitigações possíveis para riscos médios?**
   - Registrar plano (adaptação, disclaimers, treinamento) ou descartar.

### Outputs
- `_DATA/ViabilityFilters/alertas-riscos-remanescentes.MD`
- Atualização em `_DATA/ViabilityFilters/matriz-avaliacao.MD`

## ViabilityFilters.3: Disponibilidade digital

### Objetivo
Checar disponibilidade de domínios, handles sociais e nomes em app stores.

### Sequência de ações
- Verificar domínios prioritários (TLDs relevantes, variações regionais).
- Checar disponibilidade em redes sociais e plataformas-chave.
- Registrar status (disponível, ocupado, negociável) em `disponibilidade-dominios.MD` e `disponibilidade-social.MD`.
- Anexar evidências (prints, links) na pasta `evidencias/`.
- Atualizar `matriz-avaliacao.MD` com pontuação digital.

### Pontos de decisão
1. **Domínios essenciais disponíveis?**
   - ✅ Sim → pontuação positiva.
   - ❌ Não → avaliar alternativas (variações, negociação) ou sinalizar.
2. **Handles sociais críticos disponíveis?**
   - ✅ Sim → prosseguir.
   - ❌ Não → registrar plano de mitigação.

### Outputs
- `_DATA/ViabilityFilters/disponibilidade-dominios.MD`
- `_DATA/ViabilityFilters/disponibilidade-social.MD`
- Evidências salvas em `_DATA/ViabilityFilters/evidencias/`

## ViabilityFilters.4: Busca jurídica preliminar

### Objetivo
Identificar conflitos em registros de marca e avaliar riscos legais.

### Sequência de ações
- Consultar bases oficiais (INPI, USPTO, EUIPO etc.) e registradores locais.
- Registrar resultados com classes relevantes, status e observações.
- Envolver jurídico para parecer preliminar (`parecer-juridico.MD`).
- Atualizar `matriz-avaliacao.MD` com notas de risco legal.

### Pontos de decisão
1. **Existem conflitos diretos (mesma classe/segmento)?**
   - ✅ Sim → marcar como vermelho ou solicitar parecer jurídico detalhado.
   - ❌ Não → classificar conforme risco residual.
2. **Riscos médios requerem ações?**
   - Documentar mitigação (negociação, variação ortográfica, classe alternativa).

### Outputs
- `_DATA/ViabilityFilters/parecer-juridico.MD`
- Atualização em `_DATA/ViabilityFilters/matriz-avaliacao.MD`

## ViabilityFilters.5: Consolidação e short list

### Objetivo
Pontuar e classificar opções, entregando short list final.

### Sequência de ações
- Consolidar notas (linguística, digital, jurídica) na matriz.
- Calcular pontuação total ponderada.
- Classificar risco (verde, amarelo, vermelho) para cada nome.
- Selecionar short list (3-5 nomes) e documentar status em `shortlist-naming.MD`.
- Atualizar `alertas-riscos-remanescentes.MD` com riscos e planos.

### Pontos de decisão
1. **Short list atende critérios e metas?**
   - ✅ Sim → compartilhar com stakeholders.
   - ❌ Não → reavaliar long list ou ajustar critérios.
2. **Riscos remanescentes aceitáveis?**
   - ✅ Sim → registrar e seguir para testes.
   - ❌ Não → retornar à geração.

### Outputs
- `_DATA/ViabilityFilters/matriz-avaliacao.MD` (versão final)
- `_DATA/ViabilityFilters/shortlist-naming.MD`
- `_DATA/ViabilityFilters/alertas-riscos-remanescentes.MD`

## Indicadores de acompanhamento

- Quantidade de nomes classificados como baixo/médio/alto risco.
- Tempo médio por verificação (linguística, digital, jurídica).
- Percentual de opções descartadas por categoria de risco.
- Número de riscos remanescentes levados para a etapa de testes.

## Documentação e governança

- Todos os arquivos e evidências devem estar em `_DATA/ViabilityFilters/`.
- Versione documentos críticos (matriz, shortlist) e registre aprovação formal.
- Alinhe cronograma com jurídico e marketing para evitar atrasos nos testes.
