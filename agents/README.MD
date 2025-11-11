# agents – Implementação baseada em LANGCHAIN.MD

## Propósito

- Consolidar toda a automação descrita em `LANGCHAIN.MD` dentro de uma camada isolada
- Reutilizar as regras de `AGENTS.MD` para orquestrar processos via subagentes especializados
- Facilitar a evolução incremental (adição de novas estratégias, processos e utilitários)

## Estrutura Atual

- `base.py`: classes genéricas para orquestradores (`StrategyAgent`) e subagentes (`ProcessAgent`)
- `utils/`: helpers para carregar estratégias/processos, escrever em `drive/`, lidar com manifestos e empacotar outputs
- `generic/`: orquestrador padrão para estratégias que ainda não possuem subagentes dedicados
- `zero_um/`: primeira estratégia com subagentes reais em `subagents/`
- `registry.py`: mapeia nomes das estratégias (`ZeroUm`, `Branding`, `MVPBuilder`, `Naming`) para seus orquestradores
- `scripts/run_strategy_agent.py`: CLI que consome o registry (`python agents/scripts/run_strategy_agent.py ZeroUm NomeDoContexto -d "Contexto completo"`)
- `tests/`: cobertura inicial para `drive_writer`, manifestos e empacotamento
- `deepagents/`: stub local utilizado apenas quando o pacote oficial ainda não está disponível

> Convenção: **qualquer arquivo relacionado aos agentes (scripts, utilitários, dependências, testes ou stubs)** deve permanecer dentro desta pasta `agents/`. Evite duplicar lógica em outros diretórios do repositório.

> Integração de IA: `agents/deepagents/` tenta usar `langchain_openai.ChatOpenAI` sempre que `OPENAI_API_KEY` estiver configurada. Caso a chave não exista, gera um resumo sintético a partir das instruções (incluindo o contexto completo passado via `-d`) sem copiar o texto integral dos processos.

## Fluxo Operacional

1. `ZeroUmOrchestrator` lê `strategies/ZeroUm`, prepara `drive/<Contexto>/ZeroUm` e `_pipeline`
2. Cada processo listado ganha um subagente dedicado (por enquanto `ProblemHypothesisExpress`)
3. Subagentes precisam ler `process/<Estratégia>/<NN-Processo>/` antes de produzir artefatos numerados em `drive/<Contexto>/<Processo>/`
4. Manifestos JSON são gravados em `drive/<Contexto>/_pipeline/`, permitindo que o orquestrador acompanhe o status
5. Ao final, o orquestrador gera `00-consolidado.MD` e chama `package_artifacts` para montar o `.zip`

### Contexto detalhado

- Passe a descrição completa do projeto pelo parâmetro `-d/--context-description` do CLI. Esse texto alimenta o orquestrador e todos os subagentes, orientando como aplicar o processo.
- Exemplo: `python agents/scripts/run_strategy_agent.py ZeroUm AutomarticlesAutomacaoBlog -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS."`
- O contexto completo será registrado no consolidado da estratégia e embutido em cada prompt enviado aos subagentes.
- Durante a execução, o CLI exibe logs detalhando cada tarefa (`INFO`). Use `--quiet` caso queira reduzir o ruído e mostrar apenas avisos/erros.
- O nome da pasta em `drive/` é automaticamente normalizado via IA (quando `OPENAI_API_KEY` estiver configurada). Sem a chave, aplica-se a heurística local. Defina `AGENTS_DISABLE_CONTEXT_AI=1` para forçar a heurística mesmo com IA ativa.

## Como Usar

### Opção 1: Com OPENAI_API_KEY (modo completo)

```bash
source agents/.venv/bin/activate
export OPENAI_API_KEY="sk-proj-sua-chave"
python agents/scripts/run_strategy_agent.py ZeroUm AutomarticlesAutomacaoBlog -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS."
```

### Opção 2: Modo offline (sem IA, usa fallback)

```bash
source agents/.venv/bin/activate
AGENTS_SKIP_SECRET_CHECK=1 python agents/scripts/run_strategy_agent.py ZeroUm AutomarticlesAutomacaoBlog -d "Automarticles é uma plataforma que automatiza blogs para PMEs usando IA e integrações com CMS."
```

## Modo de Reflexão (Thinking)

O sistema suporta raciocínio estendido através de um padrão de reflexão em 3 estágios que melhora significativamente a qualidade dos artefatos gerados.

### Arquivos Implementados

- [`agents/deepagents/reasoning.py`](agents/deepagents/reasoning.py) - Módulo com funções de reflexão
- [`agents/deepagents/__init__.py`](agents/deepagents/__init__.py) - Adicionado método `run_with_reflection()`
- [`agents/zero_um/subagents/problem_hypothesis_express.py`](agents/zero_um/subagents/problem_hypothesis_express.py) - Suporte a reflexão

### Comparação de Resultados

#### Métricas de Performance

| Métrica | Modo Simples | Modo Reflexão | Diferença |
| ------- | ------------ | ------------- | --------- |
| Tokens  | 484          | 1,779         | **3.67x** |
| Tempo   | 15.77s       | 60.61s        | **3.84x** |
| Linhas  | 52           | 49            | Similar   |

#### Análise Qualitativa

**Modo Simples:**

- ✅ Estrutura básica completa
- ✅ Todas as seções presentes
- ⚠️ Conteúdo mais genérico
- ⚠️ Menos contextualização
- ⚠️ Dor principal superficial

**Modo Reflexão:**

- ✅ Título profissional ("Artefato Final - ProblemHypothesisExpress")
- ✅ Contexto mais rico - explicação da diferenciação da proposta
- ✅ Dor principal detalhada - inclui consequências específicas (atrasos, impostos, erros)
- ✅ Evidências concretas - menciona relatos de freelancers
- ✅ Notas de leitura incluídas - timing e fluência das frases
- ✅ Mais estruturado - formatação markdown aprimorada

### Como Ativar o Modo Reflexão

**Modo Simples (padrão):**

```bash
source agents/.venv/bin/activate
export OPENAI_API_KEY="sua-chave"
python agents/scripts/run_strategy_agent.py ZeroUm ContextoNome -d "Descrição"
```

**Modo Reflexão (thinking):**

```bash
source agents/.venv/bin/activate
export OPENAI_API_KEY="sua-chave"
AGENTS_REASONING_MODE=reflection AGENTS_TODO_VERBOSE=true python agents/scripts/run_strategy_agent.py ZeroUm ContextoNome -d "Descrição"
```

### Configurações Disponíveis

```bash
# Modo de raciocínio
AGENTS_REASONING_MODE=simple|reflection|thinking|extended

# Modelo LLM (opcional)
AGENTS_REASONING_MODEL=gpt-4o-mini|gpt-4o|gpt-5

# Habilitar traces detalhados (futuro)
AGENTS_ENABLE_THINKING_TRACES=true
```

### Processo de Reflexão (3 Estágios)

#### 1. Draft (Rascunho)

- **Temperatura**: 0.3
- **Max tokens**: 4096
- **Objetivo**: Gera estrutura completa do artefato com todo o conteúdo principal

#### 2. Reflection (Crítica)

- **Temperatura**: 0.2
- **Max tokens**: 2048
- **Referência**: Usa `validator.MD` como critério de qualidade
- **Identifica**: Pontos fortes, lacunas e melhorias necessárias

#### 3. Refinement (Refinamento)

- **Temperatura**: 0.25
- **Max tokens**: 5000
- **Objetivo**: Incorpora crítica no rascunho e produz versão final refinada

### ROI e Recomendação

**Custo**: ~3.7x mais tokens (de $0.002 para $0.007 por processo)

**Benefício**: Conteúdo significativamente mais rico, contextualizado e aderente ao `validator.MD`

**Use reflexão para:**

- ✅ Processos críticos (ProblemHypothesisExpress, TargetUserIdentification)
- ✅ Artefatos que serão apresentados a clientes
- ✅ Quando a qualidade é mais importante que velocidade

**Evite reflexão para:**

- ❌ Processos simples ou operacionais
- ❌ Quando budget de tokens é limitado
- ❌ Execuções em massa onde velocidade é prioridade

## Próximos Passos

- Adicionar os demais subagentes da estratégia ZeroUm seguindo o padrão de `subagents/base.py`
- Validar o fluxo ponta a ponta com `deepagents` instalado, garantindo que os artefatos sejam gerados automaticamente
- Criar orquestradores específicos para Branding, Naming e MVPBuilder para substituir o modo genérico
- Expandir modo de reflexão para outros subagentes da estratégia ZeroUm
