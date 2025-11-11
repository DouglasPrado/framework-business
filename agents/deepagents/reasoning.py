"""Módulo de raciocínio estendido (thinking) para DeepAgent."""

from __future__ import annotations

from typing import Any, Dict, Optional

from agents.config import get_settings


def create_draft_prompt(
    system_prompt: str,
    instructions: str,
    tools: list[str] | None = None,
) -> str:
    """
    Cria prompt para geração do rascunho inicial.

    Args:
        system_prompt: Prompt base do sistema
        instructions: Instruções específicas do processo
        tools: Lista de ferramentas disponíveis

    Returns:
        Prompt formatado para geração de draft
    """
    tool_list = ", ".join(tools) if tools else "ls, read_file, write_file"

    return f"""
{system_prompt.strip()}

Ferramentas virtuais disponíveis: {tool_list}.

## Fase 1: RASCUNHO INICIAL

Você está na fase de geração de rascunho. Seu objetivo é:
1. Produzir a estrutura completa do artefato
2. Incluir todo o conteúdo principal
3. Garantir que todas as seções obrigatórias estejam presentes
4. Não se preocupe com perfeição - foque em completude

Regras obrigatórias:
- Escreva em português claro e direto
- NÃO use tabelas markdown
- NÃO use emojis
- Siga AGENTS.MD rigorosamente

### Instruções do processo
{instructions.strip()}

### Saída esperada
Produza o rascunho completo do artefato em markdown, pronto para ser revisado.
""".strip()


def create_reflection_prompt(
    draft: str,
    validator_content: str,
    instructions: str,
    process_code: str,
) -> str:
    """
    Cria prompt para reflexão crítica sobre o rascunho.

    Args:
        draft: Rascunho gerado na fase anterior
        validator_content: Conteúdo do arquivo validator.MD
        instructions: Instruções originais do processo
        process_code: Código do processo (ex: 00-ProblemHypothesisExpress)

    Returns:
        Prompt formatado para crítica
    """
    return f"""
Você é um REVISOR CRÍTICO especializado em {process_code}.

## Fase 2: REFLEXÃO E CRÍTICA

Seu papel é analisar o rascunho abaixo e fornecer uma crítica construtiva e específica.

### Rascunho para revisar
```
{draft.strip()}
```

### Critérios de validação (validator.MD)
{validator_content.strip() if validator_content else "Nenhum critério específico fornecido."}

### Instruções originais do processo
{instructions.strip()}

### Sua tarefa
Analise o rascunho e produza uma crítica estruturada com:

#### 1. Pontos fortes
Liste o que está bem feito no rascunho (2-3 pontos específicos)

#### 2. Lacunas identificadas
O que está faltando ou incompleto? Seja específico sobre:
- Seções ausentes
- Informações superficiais
- Contexto insuficiente

#### 3. Melhorias necessárias
O que precisa ser refinado? Indique:
- Clareza de comunicação
- Aderência às instruções
- Conformidade com validator.MD

#### 4. Conformidade com regras
Verifique se o rascunho:
- Está em português ✓/✗
- NÃO usa tabelas markdown ✓/✗
- NÃO usa emojis ✓/✗
- Segue estrutura do processo ✓/✗

### Formato de saída
Produza a crítica em formato markdown estruturado, clara e acionável.
""".strip()


def create_refinement_prompt(
    draft: str,
    critique: str,
    instructions: str,
) -> str:
    """
    Cria prompt para refinamento baseado na crítica.

    Args:
        draft: Rascunho original
        critique: Crítica gerada na fase de reflexão
        instructions: Instruções originais do processo

    Returns:
        Prompt formatado para refinamento
    """
    return f"""
## Fase 3: REFINAMENTO

Você recebeu um rascunho e uma crítica construtiva.
Seu objetivo é produzir a VERSÃO FINAL refinada e melhorada do artefato.

### Rascunho original
```
{draft.strip()}
```

### Crítica recebida
```
{critique.strip()}
```

### Instruções originais
{instructions.strip()}

### Sua tarefa
Produza a versão final do artefato incorporando:
1. Todos os pontos fortes do rascunho original
2. Correção de todas as lacunas identificadas
3. Implementação de todas as melhorias sugeridas
4. Garantia de conformidade com todas as regras

### Regras obrigatórias (lembre-se!)
- Escreva em português claro e direto
- NÃO use tabelas markdown
- NÃO use emojis
- Siga AGENTS.MD rigorosamente

### Saída esperada
Produza o artefato final completo, refinado e pronto para publicação.
Não inclua meta-comentários sobre as mudanças - apenas o artefato final.
""".strip()


def get_reasoning_config(stage: str) -> Dict[str, Any]:
    """
    Retorna configuração de LLM otimizada para cada estágio de reasoning.

    Args:
        stage: Estágio do reasoning (draft, reflection, refinement)

    Returns:
        Dicionário com configuração de LLM
    """
    settings = get_settings(validate=False)
    base_config = {
        "model": settings.reasoning_model,
    }

    if stage == "draft":
        return {
            **base_config,
            "temperature": 0.3,  # Criatividade moderada para draft
            "max_tokens": 4096,  # Espaço para rascunho completo
        }
    elif stage == "reflection":
        return {
            **base_config,
            "temperature": 0.2,  # Mais focado para crítica
            "max_tokens": 2048,  # Crítica geralmente menor
        }
    elif stage == "refinement":
        return {
            **base_config,
            "temperature": 0.25,  # Balanceado para refinamento
            "max_tokens": 5000,   # Espaço para versão final expandida
        }
    else:
        return base_config


def is_reflection_enabled() -> bool:
    """
    Verifica se o modo de reflexão está habilitado via variável de ambiente.

    Returns:
        True se reflection estiver habilitado
    """
    settings = get_settings(validate=False)
    return settings.reasoning_mode.lower() in ("reflection", "thinking", "extended")


def format_thinking_traces(
    draft_tokens: int,
    critique_tokens: int,
    refined_tokens: int,
    draft_length: int,
    critique_length: int,
    refined_length: int,
) -> Dict[str, Any]:
    """
    Formata traces de thinking para inclusão no manifesto.

    Args:
        draft_tokens: Tokens usados no draft
        critique_tokens: Tokens usados na crítica
        refined_tokens: Tokens usados no refinamento
        draft_length: Caracteres no draft
        critique_length: Caracteres na crítica
        refined_length: Caracteres no refinamento

    Returns:
        Dicionário com traces formatados
    """
    return {
        "reasoning_mode": "reflection",
        "stages": {
            "draft": {
                "tokens": draft_tokens,
                "characters": draft_length,
            },
            "reflection": {
                "tokens": critique_tokens,
                "characters": critique_length,
            },
            "refinement": {
                "tokens": refined_tokens,
                "characters": refined_length,
            },
        },
        "total_reasoning_tokens": draft_tokens + critique_tokens + refined_tokens,
        "improvement_ratio": round(refined_length / draft_length, 2) if draft_length > 0 else 1.0,
    }
