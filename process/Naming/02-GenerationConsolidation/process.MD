# Processo de Execução - Generation and Consolidation (Naming)

Este processo guia as sessões criativas e a consolidação da long list de nomes alinhada ao briefing.

## Visão geral do fluxo

```
PREPARAÇÃO → GERAÇÃO DIVERGENTE → DEPURAÇÃO INICIAL → PRIORIZAÇÃO → HANDOFF
```

## Entradas obrigatórias

- Briefing aprovado (`ContextBriefing`)
- Insumos de pesquisa (`ResearchInputs`: matriz, banco de palavras, alertas)
- Critérios e pesos de avaliação
- Ferramentas para brainstorm (docs compartilhados, whiteboard, geradores controlados)

## GenerationConsolidation.1: Preparação das sessões

### Objetivo
Planejar rodadas criativas, definir participantes e materiais de apoio.

### Sequência de ações
- Revisar briefing, critérios e insights da pesquisa.
- Selecionar participantes (times estratégicos, criativos, produto, jurídico).
- Definir técnicas que serão usadas em cada rodada (brainwriting, SCAMPER, combinações linguísticas etc.).
- Preparar planilhas/documentos para registrar nomes em tempo real.
- Agendar sessões (solo e coletivas) e compartilhar materiais prévios.

### Pontos de decisão
1. **Participantes confirmados e materiais distribuídos?**
   - ✅ Sim → iniciar geração.
   - ❌ Não → reagendar ou remover bloqueios.
2. **Técnicas definidas atendem à diversidade desejada?**
   - ✅ Sim → prosseguir.
   - ❌ Não → adicionar técnicas complementares.

### Outputs
- `_DATA/GenerationConsolidation/plano-sessoes-criativas.MD`
- `_DATA/GenerationConsolidation/log-sessoes-criativas.MD` (estrutura preparada)

## GenerationConsolidation.2: Geração divergente (rodadas criativas)

### Objetivo
Gerar o máximo de alternativas com diversidade de estilos e categorias.

### Sequência de ações
- Conduzir sessões solo (brain dump, combos automáticos) e coletivas (brainwriting, mapa semântico).
- Aplicar gatilhos: sufixos/prefixos, metáforas, acrônimos, empréstimos linguísticos.
- Registrar cada opção em `longlist-naming.MD` com categoria, racional, notas fonéticas iniciais.
- Sinalizar origem (rodada, responsável, técnica) no log.
- Pausar para avaliar energia criativa e planejar nova rodada se necessário.

### Pontos de decisão
1. **Volume mínimo alcançado?** (meta > 30 opções brutas)
   - ✅ Sim → seguir para depuração.
   - ❌ Não → rodar nova sessão ou explorar técnica diferente.
2. **Categorias variadas presentes?**
   - ✅ Sim → prosseguir.
   - ❌ Não → incluir participantes adicionais ou nova abordagem.

### Outputs
- `_DATA/GenerationConsolidation/longlist-naming.MD` (versão bruta)
- `_DATA/GenerationConsolidation/log-sessoes-criativas.MD`

## GenerationConsolidation.3: Depuração inicial

### Objetivo
Eliminar opções que violam critérios obrigatórios ou alertas críticos.

### Sequência de ações
- Revisar alternativas aplicando critérios must-have do briefing.
- Remover nomes com pronúncia impraticável, significados negativos evidentes, conflitos imediatos.
- Registrar cada descarte em `descartes-naming.MD` com motivo (critério violado, alerta linguístico, duplicidade).
- Atualizar `longlist-naming.MD` marcando status (ativo, descartado).
- Garantir que cada nome restante possua racional claro e observações relevantes.

### Pontos de decisão
1. **Critérios obrigatórios aplicados a todos os nomes?**
   - ✅ Sim → avançar.
   - ❌ Não → revisar novamente.
2. **Long list mantém diversidade mínima (≥ 20 opções)?**
   - ✅ Sim → prosseguir.
   - ❌ Não → rodar nova rodada criativa focada nas lacunas.

### Outputs
- `_DATA/GenerationConsolidation/descartes-naming.MD`
- `_DATA/GenerationConsolidation/longlist-naming.MD` atualizado com status

## GenerationConsolidation.4: Priorização

### Objetivo
Aplicar pesos do briefing para ranquear opções e formar lista priorizada.

### Sequência de ações
- Criar planilha ou tabela com cada nome e critérios ponderados.
- Atribuir notas (1-5) para cada critério com base no racional registrado.
- Calcular pontuação total ponderada.
- Destacar top opções por categoria (evocativo, inventado, híbrido, descritivo) para manter variedade.
- Documentar insights em `priorizacao-longlist.MD` e sinalizar opções de backup.

### Pontos de decisão
1. **Top opções refletem critérios e equilíbrio?**
   - ✅ Sim → compartilhar com stakeholders.
   - ❌ Não → revisar notas ou ajustes nos pesos.
2. **Existe material suficiente para filtros de viabilidade?** (ideal 15-20 opções)
   - ✅ Sim → preparar handoff.
   - ❌ Não → retornar a geração ou ajustar critérios.

### Outputs
- `_DATA/GenerationConsolidation/priorizacao-longlist.MD`
- Atualização em `longlist-naming.MD` com ranking/pontuação

## GenerationConsolidation.5: Handoff para filtros

### Objetivo
Compartilhar long list priorizada, decisões e próximos passos com stakeholders e equipe de Filtros de Viabilidade.

### Sequência de ações
- Revisar documentação para garantir registros completos (racional, categoria, status, pontuação).
- Compartilhar arquivos com sponsor, jurídico, digital e equipe responsável pela etapa seguinte.
- Registrar decisões em `handoff-generation.MD` (contexto, destaques, recomendações).
- Atualizar cronograma com datas da próxima etapa e responsáveis.

### Pontos de decisão
1. **Sponsor/ stakeholders aprovaram long list?**
   - ✅ Sim → concluir etapa.
   - ❌ Não → registrar feedback e ajustar.
2. **Materiais acessíveis e versionados?**
   - ✅ Sim → handoff completo.
   - ❌ Não → corrigir permissões/links.

### Outputs
- `_DATA/GenerationConsolidation/handoff-generation.MD`
- `_DATA/GenerationConsolidation/cronograma-naming.MD` (atualizado se necessário)

## Indicadores de acompanhamento

- Volume total de nomes gerados (bruto e após depuração).
- Distribuição por categoria de nome.
- Percentual de nomes que atendem aos critérios must-have.
- Tempo gasto entre primeira sessão e handoff.

## Documentação e governança

- Todos os arquivos devem permanecer em `_DATA/GenerationConsolidation/`.
- Versione `longlist-naming.MD` e `priorizacao-longlist.MD` para rastrear mudanças.
- Registrar aprendizados e ajustes no processo para melhorar próximas rodadas.
