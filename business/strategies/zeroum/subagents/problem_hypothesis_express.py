"""
Subagente: Problem Hypothesis Express (00-ProblemHypothesisExpress)

Baseado em: process/ZeroUm/00-ProblemHypothesisExpress/process.MD

Propósito:
Guiar a execução da Etapa 0 da Estratégia ZeroUm em 30 minutos, gerando
uma frase clara de proposta de valor validada com alguém do público-alvo
e registrada para iterações futuras.

Etapas:
1. Preparar foco da sessão (3 min)
2. Mapear usuários-alvo imediatos (5 min)
3. Identificar a dor central (7 min)
4. Redigir e testar variações (10 min)
5. Validar com pessoa do público-alvo (5 min)

Total: 30 minutos (time-box rígido)
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from business.strategies.zeroum.subagents.base import SubagentBase
from business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

logger = logging.getLogger(__name__)

class ProblemHypothesisExpressAgent(SubagentBase):
    """
    Subagente especializado em criar e validar hipóteses de problema rapidamente.

    Implementa o processo express de 30 minutos para gerar uma frase de
    proposta de valor clara e validada.

    Template:
    "Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"
    """

    process_name = "00-ProblemHypothesisExpress"
    strategy_name = "ZeroUm"

    def __init__(
        self,
        workspace_root: Path,
        idea_context: str,
        target_audience: Optional[str] = None,
        enable_tools: bool = True,
    ):
        """
        Args:
            workspace_root: Diretório raiz do workspace
            idea_context: Contexto da ideia (2-3 frases sobre o problema e solução)
            target_audience: Público-alvo inicial (opcional)
            enable_tools: Habilitar ferramentas do framework (padrão: True)
        """
        self.workspace_root = workspace_root
        self.idea_context = idea_context
        self.target_audience = target_audience
        self.llm = build_llm()

        # Obter tools do framework (filesystem operations)
        self.tools = get_tools(AgentType.PROCESS) if enable_tools else []
        if self.tools:
            logger.info(f"Tools habilitadas: {[tool.name for tool in self.tools]}")

        # Criar estrutura de diretórios
        self.process_dir = workspace_root / "00-ProblemHypothesisExpress"
        self.data_dir = self.process_dir / "_DATA"
        self.setup_directories(["assets", "evidencias"])
        self.template_filler = ProcessTemplateFiller(
            process_code="00-ProblemHypothesisExpress",
            output_dir=self.data_dir,
            llm=self.llm,
        )

    def execute_express_session(self) -> Dict[str, Any]:
        """
        Executa sessão express completa de 30 minutos.

        Returns:
            Dicionário com resultados de todas as etapas
        """
        logger.info("Iniciando sessão express Problem Hypothesis (30 min)")

        results = {
            "idea_context": self.idea_context,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        # Etapa 1: Preparar foco (3 min)
        logger.info("Etapa 1/5: Preparar foco da sessão (3 min)")
        results["stages"]["focus"] = self._stage_1_prepare_focus()

        # Etapa 2: Mapear usuários-alvo (5 min)
        logger.info("Etapa 2/5: Mapear usuários-alvo imediatos (5 min)")
        results["stages"]["target_users"] = self._stage_2_map_target_users()

        # Etapa 3: Identificar dor central (7 min)
        logger.info("Etapa 3/5: Identificar a dor central (7 min)")
        results["stages"]["pain_point"] = self._stage_3_identify_pain()

        # Etapa 4: Redigir variações (10 min)
        logger.info("Etapa 4/5: Redigir e testar variações (10 min)")
        results["stages"]["variations"] = self._stage_4_create_variations()

        # Etapa 5: Preparar validação (5 min)
        logger.info("Etapa 5/5: Preparar validação (5 min)")
        results["stages"]["validation"] = self._stage_5_prepare_validation()

        results["completed_at"] = datetime.now().isoformat()

        # Criar documento consolidado
        self._create_consolidated_document(results)
        self._fill_data_templates(results)

        logger.info("Sessão express concluída com sucesso")

        return results

    def _stage_1_prepare_focus(self) -> Dict[str, Any]:
        """
        Etapa 1: Preparar foco da sessão (3 min).

        Confirma a ideia e define métricas de sucesso.
        """
        logger.info("Preparando foco da sessão")

        prompt = f"""
Você é um especialista em validação de ideias usando a metodologia ZeroUm.

Contexto da ideia fornecido:
{self.idea_context}

Crie um DOCUMENTO DE FOCO DA SESSÃO que estruture o seguinte:

# Foco da Sessão - Problem Hypothesis Express

**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Duração prevista:** 30 minutos

## 1. Contexto da Ideia

Baseado no contexto fornecido, resuma em 2-3 frases:
- Qual problema você acredita resolver?
- Para quem?
- Por que isso é importante agora?

## 2. Objetivo da Sessão

O que você precisa alcançar ao final dos 30 minutos:
- [ ] Lista de 3-5 usuários-alvo com canais de acesso
- [ ] Dor central identificada e documentada
- [ ] 3 variações da frase de proposta de valor
- [ ] Frase validada com pelo menos 1 pessoa do público-alvo
- [ ] Log de feedback e versões registrado

## 3. Resultado Esperado

Ao final desta sessão, você deve ter uma frase clara no formato:

**"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"**

Essa frase será:
- Compreensível em ≤ 10 segundos
- Validada com pessoa real do público-alvo
- Pronta para usar em landing page ou outreach

## 4. Contato para Validação

**CRÍTICO**: Antes de continuar, identifique:
- Nome/Perfil de quem pode validar (alguém que vive o problema)
- Canal de contato (WhatsApp, Telegram, Slack, etc.)
- Disponibilidade (quando pode responder hoje)

Se não tem ninguém disponível AGORA, pause a sessão e reagende.

## 5. Timer e Disciplina

- Etapa 1 (Foco): 3 min ⏱️
- Etapa 2 (Usuários): 5 min ⏱️
- Etapa 3 (Dor): 7 min ⏱️
- Etapa 4 (Variações): 10 min ⏱️
- Etapa 5 (Validação): 5 min ⏱️

**Total: 30 minutos (time-box rígido)**

---

**Próximo passo:** Mapear usuários-alvo imediatos (5 min)
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        # Salvar foco
        focus_file = self.data_dir / "01-foco-sessao.MD"
        focus_file.write_text(content, encoding="utf-8")
        logger.info(f"Foco da sessão salvo em {focus_file}")

        return {
            "focus_file": str(focus_file),
            "status": "completed",
            "duration_target": "3 min",
        }

    def _stage_2_map_target_users(self) -> Dict[str, Any]:
        """
        Etapa 2: Mapear usuários-alvo imediatos (5 min).

        Lista quem sente o problema e onde pode ser encontrado.
        """
        logger.info("Mapeando usuários-alvo imediatos")

        audience_hint = f"\n\nPúblico-alvo sugerido: {self.target_audience}" if self.target_audience else ""

        prompt = f"""
Contexto da ideia:
{self.idea_context}{audience_hint}

Crie um MAPEAMENTO DE USUÁRIOS-ALVO IMEDIATOS:

# Mapeamento de Usuários-Alvo Imediatos

**Objetivo:** Identificar quem sente o problema AGORA e onde pode ser encontrado.

## Perfis de Usuários-Alvo (3-5 perfis)

Para cada perfil, inclua:
- **Profissão/Descrição**: Quem é essa pessoa?
- **Momento crítico**: Quando/por que o problema fica urgente?
- **Onde encontrar**: Grupos, comunidades, eventos, contatos diretos
- **Por que é prioritário**: O que torna esse perfil relevante agora?

### Perfil 1: [Nome do perfil]
- **Profissão/Descrição:** [Ex: Fundadores de startups B2B em estágio seed]
- **Momento crítico:** [Ex: Quando precisam validar ideia antes de investir 6 meses]
- **Onde encontrar:** [Ex: Grupos de Slack de founders, aceleradoras, Y Combinator]
- **Por que é prioritário:** [Ex: Têm orçamento limitado e urgência de validar rápido]

### Perfil 2: [Nome do perfil]
[Repetir estrutura]

### Perfil 3: [Nome do perfil]
[Repetir estrutura]

## Perfil Priorizado para Validação

**Perfil selecionado:** [Qual dos perfis acima é o mais acessível AGORA?]

**Justificativa:** [Por que esse perfil é a melhor escolha para validação imediata?]

**Contato disponível:**
- Nome/Perfil: [Ex: João, founder de SaaS B2B]
- Canal: [Ex: WhatsApp, Telegram]
- Disponibilidade: [Ex: Responde rápido entre 9h-18h]

## Hipótese de Urgência

Por que esses perfis têm o problema AGORA?
- [Razão 1: Ex: Mercado aquecido para validação de produto]
- [Razão 2: Ex: Alto custo de erro ao construir produto errado]
- [Razão 3: Ex: Acesso limitado a metodologias práticas]

---

**Próximo passo:** Identificar a dor central (7 min)

Baseie-se no contexto fornecido e crie 3-5 perfis bem específicos.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        # Salvar mapeamento
        users_file = self.data_dir / "02-usuarios-alvo.MD"
        users_file.write_text(content, encoding="utf-8")
        logger.info(f"Usuários-alvo salvos em {users_file}")

        return {
            "users_file": str(users_file),
            "status": "completed",
            "duration_target": "5 min",
        }

    def _stage_3_identify_pain(self) -> Dict[str, Any]:
        """
        Etapa 3: Identificar a dor central (7 min).

        Entende qual fricção impede o público de alcançar o resultado.
        """
        logger.info("Identificando dor central")

        prompt = f"""
Contexto da ideia:
{self.idea_context}

Crie uma ANÁLISE DE DOR CENTRAL:

# Identificação da Dor Central

**Objetivo:** Entender qual fricção principal impede o público de alcançar o resultado desejado.

## 1. Como o Público Resolve Hoje

Descreva passo a passo como o público-alvo tenta resolver o problema atualmente:

**Solução atual (passo a passo):**
1. [Passo 1: Ex: Busca artigos e tutoriais no Google]
2. [Passo 2: Ex: Tenta implementar sozinho sem framework]
3. [Passo 3: Ex: Gasta semanas testando e ajustando]
4. [Passo 4: Ex: Ainda fica inseguro se validou corretamente]

## 2. Frustração Principal

O que mais frustra o público nessa jornada atual?

**Frustração #1:** [Ex: Tempo desperdiçado - leva semanas para validar]
- **Impacto:** [Ex: Atrasa lançamento do produto em 2-3 meses]

**Frustração #2:** [Ex: Incerteza - nunca sabe se validou de verdade]
- **Impacto:** [Ex: Risco de construir produto que ninguém quer]

**Frustração #3:** [Ex: Complexidade - processos muito teóricos]
- **Impacto:** [Ex: Paralisia por análise, não começa a executar]

## 3. Custos Reais

Quanto o problema custa em:

**Tempo:**
- [Ex: 3-6 meses desperdiçados construindo produto errado]

**Dinheiro:**
- [Ex: R$ 50-100k gastos em desenvolvimento antes de validar]

**Oportunidade:**
- [Ex: Janela de mercado fecha enquanto tenta validar]

**Emocional:**
- [Ex: Frustração de ver concorrente lançar primeiro]

## 4. Evidências e Observações

Baseie a dor em evidências concretas:

**Evidência 1:** [Ex: 70% das startups falham por construir produto que ninguém quer (CB Insights)]
**Evidência 2:** [Ex: Founders relatam gastar 6+ meses antes de primeira validação real]
**Evidência 3:** [Ex: Metodologias tradicionais (Lean Startup) são muito teóricas e longas]

## 5. Dor Selecionada (Crítica)

**Dor principal identificada:**

[Descreva em 2-3 frases a dor mais crítica e urgente]

**Por que essa dor é crítica:**
- É significativa o suficiente para motivar ação
- Impacta resultado de negócio diretamente
- Solução atual é inadequada ou inexistente
- Público está ativamente buscando alternativa

## 6. Teste de Validação da Dor

Para confirmar que essa dor é real:

- [ ] Você já ouviu pessoas reclamarem disso?
- [ ] Existem soluções alternativas tentando resolver?
- [ ] A dor tem custo mensurável (tempo/dinheiro)?
- [ ] É um problema recorrente, não pontual?
- [ ] Pessoas pagariam para evitar essa dor?

Meta: Pelo menos 4 de 5 marcados ✅

---

**Próximo passo:** Redigir variações da frase (10 min)

Baseie toda análise no contexto fornecido e em evidências reais quando possível.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        # Salvar análise de dor
        pain_file = self.data_dir / "03-dor-central.MD"
        pain_file.write_text(content, encoding="utf-8")
        logger.info(f"Dor central salva em {pain_file}")

        return {
            "pain_file": str(pain_file),
            "status": "completed",
            "duration_target": "7 min",
        }

    def _stage_4_create_variations(self) -> Dict[str, Any]:
        """
        Etapa 4: Redigir e testar variações (10 min).

        Cria três versões da frase de proposta de valor.
        """
        logger.info("Criando variações da frase de proposta de valor")

        prompt = f"""
Contexto da ideia:
{self.idea_context}

Crie TRÊS VARIAÇÕES da frase de proposta de valor seguindo o template:

**"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"**

# Variações da Proposta de Valor

## Template Base

```
Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]
```

**Componentes:**
- **[QUEM]**: Usuário-alvo específico (profissão + contexto)
- **[RESULTADO]**: Objetivo final desejado (mensurável)
- **[DOR]**: Principal obstáculo ou fricção

## Variação 1: Formato Clássico

**Frase:**
"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"

**Exemplo aplicado:**
[Gere a frase completa baseada no contexto]

**Análise da variação:**
- ✅ Pontos fortes: [Ex: Estrutura clara, fácil de entender]
- ⚠️ Pontos fracos: [Ex: Um pouco formal]
- ⏱️ Tempo de leitura: [Testar: ~8-10 segundos]
- 🎯 Clareza: [1-10, sendo 10 muito claro]

## Variação 2: Formato Direto

**Frase:**
"[QUEM] agora pode [RESULTADO] sem precisar [DOR]"

**Exemplo aplicado:**
[Gere a frase completa]

**Análise da variação:**
- ✅ Pontos fortes: [Ex: Mais conversacional]
- ⚠️ Pontos fracos: [Ex: Menos estruturado]
- ⏱️ Tempo de leitura: [~8-10 segundos]
- 🎯 Clareza: [1-10]

## Variação 3: Formato de Capacitação

**Frase:**
"Meu produto permite que [QUEM] consiga [RESULTADO] eliminando [DOR]"

**Exemplo aplicado:**
[Gere a frase completa]

**Análise da variação:**
- ✅ Pontos fortes: [Ex: Enfatiza eliminação da dor]
- ⚠️ Pontos fracos: [Ex: Pode soar corporativo]
- ⏱️ Tempo de leitura: [~8-10 segundos]
- 🎯 Clareza: [1-10]

## Teste de Voz Alta

Para cada variação, leia em voz alta e avalie:

| Variação | Fluência | Natural | Compreensível | Memorável | Score Total |
|----------|----------|---------|---------------|-----------|-------------|
| 1        | [1-10]   | [1-10]  | [1-10]        | [1-10]    | [Soma/40]   |
| 2        | [1-10]   | [1-10]  | [1-10]        | [1-10]    | [Soma/40]   |
| 3        | [1-10]   | [1-10]  | [1-10]        | [1-10]    | [Soma/40]   |

## Variação Preferida (Pré-Validação)

**Variação selecionada para validação:** [1, 2 ou 3]

**Justificativa:**
[Por que essa variação é a melhor para testar com o público?]

## Checklist Rápido

Antes de validar, confirme que a frase escolhida:

- [ ] Menciona explicitamente QUEM, RESULTADO e DOR
- [ ] NÃO menciona funcionalidades técnicas
- [ ] Foca no resultado, não no produto
- [ ] Pode ser compreendida em ≤ 10 segundos
- [ ] Está livre de jargões técnicos
- [ ] É específica, não genérica

Se algum item estiver faltando, revise a frase antes de validar!

---

**Próximo passo:** Validar com pessoa do público-alvo (5 min)

**IMPORTANTE:** A frase final só estará pronta APÓS validação real.

Gere as 3 variações completas baseadas no contexto fornecido.
Seja específico e acionável em cada frase.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        # Salvar variações
        variations_file = self.data_dir / "04-variacoes-proposta.MD"
        variations_file.write_text(content, encoding="utf-8")
        logger.info(f"Variações salvas em {variations_file}")

        return {
            "variations_file": str(variations_file),
            "status": "completed",
            "duration_target": "10 min",
        }

    def _stage_5_prepare_validation(self) -> Dict[str, Any]:
        """
        Etapa 5: Preparar validação (5 min).

        Cria roteiro e template para validar com pessoa real.
        """
        logger.info("Preparando materiais de validação")

        prompt = f"""
Contexto da ideia:
{self.idea_context}

Crie um GUIA DE VALIDAÇÃO completo para testar a frase com pessoa real:

# Guia de Validação - Problem Hypothesis Express

**Objetivo:** Coletar feedback real e ajustar a frase final com base na linguagem do público.

## 1. Roteiro de Validação (Máx. 3 minutos)

### Preparação

Antes de enviar mensagem/fazer chamada:
- [ ] Frase preferida selecionada (da Etapa 4)
- [ ] Contato do público-alvo disponível
- [ ] Canal de comunicação definido (WhatsApp, ligação, etc.)
- [ ] Timer de 3 minutos preparado

### Script da Validação

**Abertura (30 segundos):**

> "Oi [Nome]! Tudo bem? Estou trabalhando em uma ideia e preciso da sua ajuda rápida. Você tem 2-3 minutos agora?"

**Contexto (30 segundos):**

> "Estou criando algo para [público-alvo] e queria testar se a forma como descrevo faz sentido para você. Posso ler uma frase e pedir seu feedback?"

**Apresentação da Frase (10 segundos):**

> [Ler a variação preferida escolhida]

**Pergunta 1 - Compreensão (60 segundos):**

> "Com suas palavras, o que você entendeu que isso faz?"

**Pergunta 2 - Relevância (60 segundos):**

> "Isso descreve um problema que você ou alguém que você conhece enfrenta?"

**Pergunta 3 - Linguagem (30 segundos):**

> "Tem alguma palavra ou parte que ficou confusa? Como você diria isso de forma mais natural?"

**Fechamento (10 segundos):**

> "Perfeito! Muito obrigado pelo feedback. Vou ajustar e te mostro o resultado final!"

## 2. Template de Registro de Feedback

Use este template para documentar a validação:

### Validação #1

**Data/Hora:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

**Perfil do Validador:**
- Nome/Apelido: [Ex: João]
- Profissão: [Ex: Founder de SaaS B2B]
- Por que representa o público: [Ex: Está validando ideia agora]

**Frase Apresentada:**
[Cole a variação testada]

**Resposta à Pergunta 1 (Compreensão):**
"[Citação literal do que a pessoa disse]"

**Resposta à Pergunta 2 (Relevância):**
"[Citação literal]"

**Resposta à Pergunta 3 (Linguagem):**
"[Citação literal]"

**Observações:**
- Reação inicial: [Ex: Pareceu interessado, fez mais perguntas]
- Palavras que usou: [Ex: Usou "rápido" em vez de "ágil"]
- Confusão identificada: [Ex: Não entendeu termo "framework"]
- Sugestões diretas: [Ex: Sugeriu focar mais na economia de tempo]

**Score de Clareza:**
- Entendeu em ≤ 10 segundos? [Sim/Não]
- Conseguiu explicar de volta? [Sim/Não]
- Identificou-se com o problema? [Sim/Não]
- Usaria essas palavras? [Sim/Não]

## 3. Ajuste da Frase Final

Baseado no feedback coletado:

**Frase Original (testada):**
[Cole aqui]

**Ajustes Necessários:**
1. [Ex: Substituir "framework" por "passo a passo"]
2. [Ex: Enfatizar "economia de tempo" em vez de "eficiência"]
3. [Ex: Tornar QUEM mais específico]

**Frase Final (ajustada):**
[Versão final depois dos ajustes]

**Validação da Frase Final:**
- [ ] Incorpora feedback do validador
- [ ] Usa linguagem natural do público
- [ ] Mantém estrutura [QUEM] + [RESULTADO] + [DOR]
- [ ] Compreensível em ≤ 10 segundos
- [ ] Livre de jargões

## 4. Próximos Passos

Após validação:

**Se feedback foi positivo:**
- [ ] Usar frase em landing page
- [ ] Testar com 2-3 pessoas adicionais
- [ ] Avançar para processo [01-ProblemHypothesisDefinition] (validação rigorosa)

**Se feedback revelou confusão:**
- [ ] Ajustar frase baseado nos pontos citados
- [ ] Validar novamente com outra pessoa
- [ ] Considerar revisar público-alvo ou dor

**Sempre:**
- [ ] Documentar aprendizados no log
- [ ] Atualizar frase em todos os materiais
- [ ] Agendar próximas validações

## 5. Critérios de Sucesso

A validação foi bem-sucedida se:

✅ A pessoa entendeu o que você faz em ≤ 10 segundos
✅ Conseguiu explicar de volta com as próprias palavras
✅ Identificou-se com o problema mencionado
✅ Sugeriu linguagem mais natural (se necessário)
✅ Você tem citações literais documentadas

## 6. Avisos Importantes

⚠️ **Validar com colega interno NÃO CONTA** - Precisa ser alguém que vive a dor
⚠️ **Se pessoa não responder dentro da sessão** - Encerre sem frase final e reagende
⚠️ **Se feedback for muito negativo** - Volte à Etapa 3 (Dor Central) e revise

---

**Tempo total da sessão:** 30 minutos
**Status:** Pronto para validação

**LEMBRE-SE:** A frase só está finalizada APÓS validação real!
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        # Salvar guia de validação
        validation_file = self.data_dir / "05-guia-validacao.MD"
        validation_file.write_text(content, encoding="utf-8")
        logger.info(f"Guia de validação salvo em {validation_file}")

        # Criar template de log de versões
        log_template = self._create_version_log_template()

        return {
            "validation_file": str(validation_file),
            "log_file": str(self.data_dir / "06-log-versoes-feedback.MD"),
            "status": "ready_for_validation",
            "duration_target": "5 min",
        }

    def _create_version_log_template(self) -> str:
        """Cria template de log de versões e feedback."""
        content = f"""# Log de Versões e Feedback - Problem Hypothesis Express

**Data da sessão:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Duração:** 30 minutos (time-box)

---

## Objetivo da Sessão

Gerar uma frase clara de proposta de valor no formato:

**"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"**

Validada com pelo menos uma pessoa do público-alvo.

---

## Contexto da Ideia

{self.idea_context}

---

## Perfis de Usuários-Alvo Identificados

[Copie aqui os 3-5 perfis do arquivo 02-usuarios-alvo.MD]

---

## Dor Central Identificada

[Copie aqui a dor principal do arquivo 03-dor-central.MD]

---

## Variações Criadas

### Variação 1
[Copie da Etapa 4]

### Variação 2
[Copie da Etapa 4]

### Variação 3
[Copie da Etapa 4]

**Variação preferida para validação:** [1, 2 ou 3]

---

## Validações Realizadas

### Validação #1

**Data/Hora:** [Preencher após validação]
**Perfil:** [Nome e contexto da pessoa]
**Canal:** [WhatsApp, ligação, etc.]

**Frase apresentada:**
[Frase testada]

**Feedback (citações literais):**
- Compreensão: "[O que a pessoa disse que entendeu]"
- Relevância: "[Se identificou com o problema]"
- Linguagem: "[Sugestões de ajuste]"

**Ajustes feitos:**
- [Ajuste 1]
- [Ajuste 2]

---

## Frase Final (Validada)

**Versão final:**
[Frase ajustada após validação]

**Por que essa versão:**
- Incorpora feedback real
- Linguagem natural do público
- Compreensível em ≤ 10 segundos
- Testada e aprovada

---

## Próximos Passos

- [ ] Usar frase em landing page
- [ ] Validar com 2-3 pessoas adicionais
- [ ] Avançar para processo 01-ProblemHypothesisDefinition (validação rigorosa)
- [ ] Documentar aprendizados

---

## Aprendizados da Sessão

**O que funcionou bem:**
- [Aprendizado 1]
- [Aprendizado 2]

**O que precisa melhorar:**
- [Ponto 1]
- [Ponto 2]

**Insights sobre o público:**
- [Insight 1]
- [Insight 2]

---

**Status:** ✅ Sessão concluída | ⏱️ Tempo: 30 minutos
**Próximo processo:** [01-ProblemHypothesisDefinition ou continuar validação]
"""

        log_file = self.data_dir / "06-log-versoes-feedback.MD"
        log_file.write_text(content, encoding="utf-8")
        logger.info(f"Template de log criado em {log_file}")

        return content

    def _create_consolidated_document(self, results: Dict[str, Any]) -> None:
        """Cria documento consolidado de toda a sessão."""
        logger.info("Gerando documento consolidado")

        content = f"""# Sessão Consolidada: Problem Hypothesis Express

**Data de início:** {results['started_at']}
**Data de conclusão:** {results['completed_at']}
**Contexto da ideia:** {self.idea_context}

---

## Resumo Executivo

Esta sessão express de 30 minutos gerou uma proposta de valor estruturada
seguindo a metodologia ZeroUm.

**Formato da frase:**
"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"

---

## Etapas Executadas

### ✅ Etapa 1: Foco da Sessão (3 min)
- Contexto documentado
- Objetivos definidos
- Timer configurado
- Arquivo gerado: {results['stages']['focus']['focus_file']}

### ✅ Etapa 2: Usuários-Alvo Imediatos (5 min)
- 3-5 perfis mapeados
- Canais de acesso identificados
- Perfil prioritário selecionado
- Arquivo gerado: {results['stages']['target_users']['users_file']}

### ✅ Etapa 3: Dor Central (7 min)
- Solução atual analisada
- Frustração principal identificada
- Custos documentados
- Arquivo gerado: {results['stages']['pain_point']['pain_file']}

### ✅ Etapa 4: Variações da Proposta (10 min)
- 3 variações criadas
- Teste de voz alta realizado
- Variação preferida selecionada
- Arquivo gerado: {results['stages']['variations']['variations_file']}

### ✅ Etapa 5: Preparação para Validação (5 min)
- Roteiro de validação criado
- Template de feedback preparado
- Log de versões iniciado
- Arquivos gerados:
  - {results['stages']['validation']['validation_file']}
  - {results['stages']['validation']['log_file']}

---

## Próximos Passos CRÍTICOS

⚠️ **IMPORTANTE:** A frase só estará finalizada APÓS validação real!

### Ação Imediata (Hoje)
1. **Executar validação** com pessoa do público-alvo
2. **Documentar feedback** no log de versões
3. **Ajustar frase** baseado no feedback
4. **Registrar versão final** validada

### Próximas 48 Horas
- Validar com 2-3 pessoas adicionais
- Refinar frase se necessário
- Usar em materiais (landing, outreach)

### Próxima Semana
- Executar processo [01-ProblemHypothesisDefinition] para validação rigorosa
- Documentar aprendizados e iterar

---

## Arquivos Gerados

Todos os materiais estão organizados em:
`{self.process_dir}/_DATA/`

**Documentos criados:**
1. 01-foco-sessao.MD - Contexto e objetivos
2. 02-usuarios-alvo.MD - Perfis e canais
3. 03-dor-central.MD - Análise da dor
4. 04-variacoes-proposta.MD - 3 variações da frase
5. 05-guia-validacao.MD - Roteiro de validação
6. 06-log-versoes-feedback.MD - Template de log

**Total:** 6 documentos estruturados

---

## KPIs da Sessão

- ⏱️ **Tempo total:** 30 minutos (target)
- 📄 **Documentos gerados:** 6 arquivos
- 🎯 **Variações criadas:** 3 frases
- ✅ **Validações planejadas:** 1 pessoa (mínimo)

---

## Template da Frase Final

Após validação, sua frase estará pronta no formato:

**"Meu produto ajuda [QUEM] a [RESULTADO] sem [DOR]"**

Essa frase será:
- ✅ Compreensível em ≤ 10 segundos
- ✅ Validada com pessoa real do público-alvo
- ✅ Livre de jargões técnicos
- ✅ Focada em resultado, não em solução
- ✅ Pronta para usar em materiais

---

**Processo executado por:** ProblemHypothesisExpressAgent (ZeroUm Framework)
**Versão:** 2.0.1
**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

**Status:** ⚠️ PENDENTE DE VALIDAÇÃO REAL
**Próxima ação:** Executar roteiro de validação com público-alvo
"""

        report_file = self.process_dir / "00-sessao-consolidada.MD"
        report_file.write_text(content, encoding="utf-8")
        logger.info(f"Documento consolidado salvo em {report_file}")

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        """Preenche templates oficiais do processo usando os materiais gerados."""
        context = self._build_template_context(results)
        tasks = [
            TemplateTask(
                template="log-versoes-feedback.MD",
                instructions=(
                    "Complete cada seção do log com os dados coletados nas etapas da sessão express. "
                    "Inclua datas, perfis, dores e feedbacks mencionados nos arquivos gerados."
                ),
                output_name="06-log-versoes-feedback.MD",
            )
        ]
        self.template_filler.fill_templates(tasks, context)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        """Gera resumo textual para auxiliar no preenchimento dos templates."""
        lines: List[str] = [
            f"Contexto da ideia: {self.idea_context}",
            f"Público sugerido: {self.target_audience or 'Não informado'}",
        ]
        stages = results.get("stages", {})
        for stage_name, data in stages.items():
            lines.append(f"\n### Etapa executada: {stage_name}")
            for key, value in data.items():
                if key.endswith("_file") and isinstance(value, str):
                    path = Path(value)
                    if path.exists():
                        try:
                            lines.append(path.read_text(encoding="utf-8"))
                        except OSError:
                            continue
        return "\n".join(lines)
