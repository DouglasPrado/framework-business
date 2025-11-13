# ClientDeliveryAgent - Exemplo de Uso

## Visão Geral

O **ClientDeliveryAgent** é um subagente especializado que automatiza todo o processo de entrega ao cliente, desde o handoff até o pós-entrega e coleta de depoimentos.

Baseado no processo: [process/ZeroUm/10-ClientDelivery/process.MD](../../../process/ZeroUm/10-ClientDelivery/process.MD)

## O Que o Subagente Faz

### Gera Automaticamente (com LLM):

1. **Etapa 1 - Handoff** (60 min)
   - Brief de entrega detalhado
   - Diagnóstico de pendências

2. **Etapa 2 - Onboarding** (45 min)
   - E-mail de boas-vindas personalizado
   - Formulário de coleta de informações
   - Roteiro de reunião de onboarding

3. **Etapa 3 - Planejamento** (120 min)
   - Plano de execução com tarefas
   - Cronograma detalhado com marcos

4. **Etapa 4 - Produção** (variável)
   - Checklist de execução
   - Checklist de QA rigoroso

5. **Etapa 5 - Entrega Oficial** (60 min)
   - Roteiro de apresentação
   - Pacote de instruções completo

6. **Etapa 6 - Pós-Entrega** (45 min + follow-up)
   - E-mail de follow-up
   - Template de solicitação de depoimento

**Total:** ~10 documentos estruturados prontos para uso

## Como Usar

### Uso Básico

```python
from pathlib import Path
from agents.business.strategies.zeroum.subagents.client_delivery import ClientDeliveryAgent

# Configurar
agent = ClientDeliveryAgent(
    workspace_root=Path("drive/MeuCliente"),
    client_name="Empresa XYZ",
    delivery_scope="Website + Landing page + Dashboard",
    deadline="2025-12-31"
)

# Executar processo completo
results = agent.execute_full_delivery()

# Resultado: 10 documentos gerados em drive/MeuCliente/10-ClientDelivery/
```

### Executar Exemplo

```bash
# Ativar ambiente
source agents/.venv/bin/activate

# Executar exemplo
python3 agents/business/examples/client_delivery_example.py
```

### Resultado Esperado

```
drive/ExemploClientDelivery/
└── 10-ClientDelivery/
    ├── 00-relatorio-consolidado.MD        # Relatório final
    └── _DATA/
        ├── 01-brief-entrega.MD            # Etapa 1
        ├── 02-diagnostico-pendencias.MD   # Etapa 1
        ├── onboarding/
        │   ├── 01-email-boas-vindas.MD    # Etapa 2
        │   ├── 02-formulario-onboarding.MD # Etapa 2
        │   └── 03-roteiro-reuniao.MD      # Etapa 2
        ├── 03-plano-execucao.MD           # Etapa 3
        ├── 04-cronograma-detalhado.MD     # Etapa 3
        ├── 05-checklist-execucao.MD       # Etapa 4
        ├── 06-checklist-qa.MD             # Etapa 4
        ├── 07-roteiro-apresentacao.MD     # Etapa 5
        ├── 08-pacote-instrucoes.MD        # Etapa 5
        ├── 09-followup-pos-entrega.MD     # Etapa 6
        └── 10-template-depoimento.MD      # Etapa 6
```

## Integração com Orchestrator

### Opção 1: Node Direto (Simples)

```python
# agents/business/strategies/zeroum/orchestrator.py

def _client_delivery(self, state: Dict[str, Any]) -> Dict[str, Any]:
    """Node: Executa processo de entrega ao cliente."""
    from agents.business.strategies.zeroum.subagents.client_delivery import ClientDeliveryAgent

    # Criar subagente
    agent = ClientDeliveryAgent(
        workspace_root=self.context.workspace_root,
        client_name=state.get('client_name', self.context.context_name),
        delivery_scope=state.get('delivery_scope', self.context.context_description),
        deadline=state.get('deadline', 'A definir')
    )

    # Executar
    results = agent.execute_full_delivery()

    # Atualizar estado
    state['client_delivery_results'] = results

    return state

# Adicionar ao graph
graph = OrchestrationGraph.from_handlers({
    "coletar_contexto": self._coletar_contexto,
    "gerar_hipotese": self._gerar_hipotese,
    "client_delivery": self._client_delivery,  # ← NOVO
    "validar_resultado": self._validar_resultado,
})
```

### Opção 2: Execução Independente

```python
# Script separado ou CLI
from agents.business.strategies.zeroum.subagents.client_delivery import ClientDeliveryAgent

agent = ClientDeliveryAgent(...)
results = agent.execute_full_delivery()
```

## Personalização

### Executar Apenas Etapas Específicas

```python
agent = ClientDeliveryAgent(...)

# Apenas handoff
agent._stage_1_handoff()

# Apenas onboarding
agent._stage_2_onboarding()

# Apenas planejamento
agent._stage_3_planning()

# E assim por diante...
```

### Customizar Prompts

Edite os métodos `_generate_*()` no arquivo `client_delivery.py` para ajustar os prompts do LLM conforme suas necessidades.

## Métricas e KPIs

O processo ClientDelivery tem os seguintes KPIs (definidos no process.MD):

- **Tempo total de entrega** ≤ prazo acordado
- **QA aprovado na primeira rodada** ≥ 90%
- **Satisfação do cliente (NPS)** ≥ 8
- **Depoimentos capturados em 7 dias** ≥ 70%
- **Ajustes pós-entrega** ≤ 2 ajustes menores
- **Tempo de resposta ao cliente** ≤ 12h úteis

## Próximos Passos Após Execução

1. **Revisar documentos gerados** - Ajustar conforme necessário
2. **Executar onboarding** - Usar materiais gerados
3. **Produzir entregáveis** - Seguir checklist
4. **Realizar QA** - Completar checklist antes da entrega
5. **Apresentar ao cliente** - Usar roteiro preparado
6. **Follow-up** - Enviar e-mail 24-48h após entrega
7. **Coletar depoimento** - Usar template preparado

## Avisos Importantes

⚠️ **Atenção:**
- O subagente gera **documentos estruturados**, não executa a produção real
- **QA deve ser 100% concluído** antes da entrega oficial
- **Expectativas devem ser alinhadas** por escrito no onboarding
- **Follow-up é crítico** - não deixe passar de 48h

## Troubleshooting

### Erro: LLM não configurado
```bash
# Verifique se OPENAI_API_KEY está no .env
cat agents/.env | grep OPENAI_API_KEY

# Configure se necessário
echo "OPENAI_API_KEY=sk-sua-chave" >> agents/.env
```

### Erro: Diretório não encontrado
```bash
# Certifique-se de que o workspace existe
mkdir -p drive/MeuCliente
```

### Documentos genéricos
- **Solução:** Forneça `delivery_scope` detalhado
- **Exemplo:** "Landing page responsiva com formulário de lead, integração com CRM e dashboard de métricas em tempo real"

## Documentação Relacionada

- [GUIA_CRIAR_SUBAGENTES.md](../../../GUIA_CRIAR_SUBAGENTES.md) - Como criar subagentes
- [process/ZeroUm/10-ClientDelivery/](../../../process/ZeroUm/10-ClientDelivery/) - Processo original
- [FIX_DOTENV_LOADING.md](../../../FIX_DOTENV_LOADING.md) - Setup do .env

## Exemplo de Output Real

Ver: `drive/ExemploClientDelivery/10-ClientDelivery/00-relatorio-consolidado.MD`

---

**Versão:** 2.0.1
**Status:** Pronto para uso
**LLM:** Obrigatório (gpt-4o-mini por padrão)
