"""
Subagente: Client Delivery (10-ClientDelivery)

Baseado em: process/ZeroUm/10-ClientDelivery/process.MD

Propósito:
Garantir que cada cliente receba a entrega contratada com clareza,
previsibilidade e padronização, desde o onboarding até o acompanhamento
pós-entrega, assegurando satisfação, documentação completa e geração
de depoimentos reutilizáveis.

Etapas:
1. Preparar handoff e plano de entrega (60 min)
2. Executar onboarding e alinhamento com o cliente (45 min)
3. Planejar execução detalhada e alocar recursos (120 min)
4. Produzir, revisar e homologar entregáveis (variável)
5. Realizar entrega oficial e garantir entendimento (60 min)
6. Executar pós-entrega e capturar depoimentos (45 min + follow-up)
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from framework.agents import BaseAgent
from business.strategies.zeroum.subagents.template_filler import (
    ProcessTemplateFiller,
    TemplateTask,
)

logger = logging.getLogger(__name__)

class ClientDeliveryAgent(BaseAgent):
    """
    Subagente especializado em gerenciar todo o processo de entrega ao cliente.

    Implementa as 6 etapas do processo ClientDelivery:
    - Handoff e planejamento
    - Onboarding e alinhamento
    - Planejamento detalhado
    - Produção e QA
    - Entrega oficial
    - Pós-entrega e depoimentos
    """

    process_name = "10-ClientDelivery"
    strategy_name = "ZeroUm"

    def __init__(
        self,
        workspace_root: Path,
        client_name: str,
        delivery_scope: str,
        deadline: Optional[str] = None,
        enable_tools: bool = True,
    ):
        """
        Args:
            workspace_root: Diretório raiz do workspace
            client_name: Nome do cliente
            delivery_scope: Escopo resumido da entrega
            deadline: Prazo de entrega (formato: YYYY-MM-DD)
            enable_tools: Habilitar ferramentas do framework (padrão: True)
        """
        # Inicializar BaseAgent (configura workspace_root, llm, tools, process_dir, data_dir)
        super().__init__(workspace_root=workspace_root, enable_tools=enable_tools)

        # Atributos específicos do negócio
        self.client_name = client_name
        self.delivery_scope = delivery_scope
        self.deadline = deadline or "A definir"

        # Criar estrutura de diretórios específica
        self.setup_directories(["assets", "evidencias"])

        # Template filler usa self.llm (já configurado pelo BaseAgent)
        self.template_filler = ProcessTemplateFiller(
            process_code="10-ClientDelivery",
            output_dir=self.data_dir,
            llm=self.llm,
        )

        # Alias para compatibilidade (process_dir = delivery_dir)
        self.delivery_dir = self.process_dir

    def execute_full_delivery(self) -> Dict[str, Any]:
        """
        Executa o processo completo de entrega ao cliente.

        Returns:
            Dicionário com resultados de todas as etapas
        """
        logger.info(f"Iniciando processo de entrega para cliente: {self.client_name}")

        results = {
            "client_name": self.client_name,
            "delivery_scope": self.delivery_scope,
            "deadline": self.deadline,
            "started_at": datetime.now().isoformat(),
            "stages": {},
        }

        # Etapa 1: Handoff e planejamento
        logger.info("Etapa 1/6: Preparar handoff e plano de entrega")
        results["stages"]["handoff"] = self._stage_1_handoff()

        # Etapa 2: Onboarding
        logger.info("Etapa 2/6: Onboarding e alinhamento")
        results["stages"]["onboarding"] = self._stage_2_onboarding()

        # Etapa 3: Planejamento detalhado
        logger.info("Etapa 3/6: Planejamento detalhado")
        results["stages"]["planning"] = self._stage_3_planning()

        # Etapa 4: Produção (placeholder - depende do escopo)
        logger.info("Etapa 4/6: Produção e QA")
        results["stages"]["production"] = self._stage_4_production()

        # Etapa 5: Entrega oficial
        logger.info("Etapa 5/6: Entrega oficial")
        results["stages"]["official_delivery"] = self._stage_5_delivery()

        # Etapa 6: Pós-entrega
        logger.info("Etapa 6/6: Pós-entrega e depoimentos")
        results["stages"]["post_delivery"] = self._stage_6_post_delivery()

        results["completed_at"] = datetime.now().isoformat()

        # Criar documento consolidado e preencher templates oficiais
        self._create_consolidated_report(results)
        # TEMPORÁRIO: Comentado até corrigir path dos templates
        # self._fill_data_templates(results)

        logger.info("Processo de entrega concluído com sucesso")

        return results

    def _stage_1_handoff(self) -> Dict[str, Any]:
        """
        Etapa 1: Preparar handoff e plano de entrega (60 min).

        Consolida informações, verifica pagamento e define plano macro.
        """
        logger.info("Gerando brief de entrega com LLM")

        prompt = f"""
Você é um gerente de entrega experiente. Crie um BRIEF DE ENTREGA completo para:

**Cliente:** {self.client_name}
**Escopo:** {self.delivery_scope}
**Prazo:** {self.deadline}

Estruture o brief seguindo este formato:

# Brief de Entrega - {self.client_name}

## 1. Resumo da Oferta
- Produto/Serviço contratado
- Valor e forma de pagamento
- Prazo acordado

## 2. Escopo Detalhado
### O que está incluído:
- [Liste 3-5 entregáveis principais]

### O que NÃO está incluído (limites):
- [Liste 3-5 itens fora do escopo]

## 3. Expectativas do Cliente
- Resultado esperado pelo cliente
- Critérios de sucesso
- Preocupações ou restrições mencionadas

## 4. Responsáveis e Prazos
- Responsável pela entrega: [Nome]
- Data de início: {datetime.now().strftime('%Y-%m-%d')}
- Data de entrega: {self.deadline}
- Milestones intermediários: [Sugestão de 2-3 marcos]

## 5. Riscos e Dependências
- Riscos identificados
- Dependências críticas (acessos, aprovações, etc.)
- Plano de contingência

## 6. Indicadores de Sucesso
- Entrega no prazo
- Satisfação do cliente (NPS ≥ 8)
- Zero ajustes críticos pós-entrega
"""

        response = self.llm.invoke(prompt)
        brief_content = response.content if hasattr(response, "content") else str(response)

        # Salvar brief
        brief_file = self.data_dir / "01-brief-entrega.MD"
        brief_file.write_text(brief_content, encoding="utf-8")
        logger.info(f"Brief salvo em {brief_file}")

        # Criar diagnóstico de pendências
        diagnostico = self._generate_diagnostico_pendencias()

        return {
            "brief_file": str(brief_file),
            "diagnostico_file": str(self.data_dir / "02-diagnostico-pendencias.MD"),
            "status": "completed",
        }

    def _generate_diagnostico_pendencias(self) -> str:
        """Gera diagnóstico de pendências."""
        prompt = f"""
Crie um DIAGNÓSTICO DE PENDÊNCIAS para a entrega do cliente {self.client_name}.

Liste potenciais pendências críticas que podem bloquear a entrega:

# Diagnóstico de Pendências - {self.client_name}

## Pendências Identificadas

### 1. Financeiro
- [ ] Pagamento confirmado
- [ ] Nota fiscal emitida
- [ ] Forma de pagamento validada

### 2. Acesso e Recursos
- [ ] Acessos necessários fornecidos pelo cliente
- [ ] Credenciais e permissões configuradas
- [ ] Recursos externos disponíveis (APIs, serviços)

### 3. Informações e Conteúdo
- [ ] Briefing completo recebido
- [ ] Materiais e assets fornecidos
- [ ] Aprovações necessárias identificadas

### 4. Capacidade Interna
- [ ] Time alocado
- [ ] Ferramentas disponíveis
- [ ] Conhecimento técnico necessário presente

## Ações Requeridas
[Para cada pendência, liste responsável e prazo]

## Status: 🟡 Aguardando validação
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        diagnostico_file = self.data_dir / "02-diagnostico-pendencias.MD"
        diagnostico_file.write_text(content, encoding="utf-8")

        return content

    def _stage_2_onboarding(self) -> Dict[str, Any]:
        """
        Etapa 2: Onboarding e alinhamento (45 min).

        Cria materiais de boas-vindas e roteiro de alinhamento.
        """
        logger.info("Gerando materiais de onboarding")

        # E-mail de boas-vindas
        email_content = self._generate_onboarding_email()

        # Formulário de coleta
        formulario_content = self._generate_formulario_onboarding()

        # Roteiro de reunião
        roteiro_content = self._generate_roteiro_onboarding()

        return {
            "email_file": str(self.data_dir / "onboarding" / "01-email-boas-vindas.MD"),
            "formulario_file": str(self.data_dir / "onboarding" / "02-formulario-onboarding.MD"),
            "roteiro_file": str(self.data_dir / "onboarding" / "03-roteiro-reuniao.MD"),
            "status": "completed",
        }

    def _generate_onboarding_email(self) -> str:
        """Gera e-mail de boas-vindas personalizado."""
        prompt = f"""
Escreva um e-mail profissional de BOAS-VINDAS para o cliente {self.client_name}.

O e-mail deve:
1. Dar boas-vindas calorosas
2. Confirmar o escopo: {self.delivery_scope}
3. Apresentar o processo e próximos passos
4. Solicitar informações necessárias
5. Passar confiança e profissionalismo

Formato:
**Assunto:** Bem-vindo(a)! Vamos começar sua entrega - {self.client_name}

Olá [Nome do Cliente],

[Corpo do e-mail - 3-4 parágrafos]

Próximos passos:
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

Estou à disposição para qualquer dúvida!

Atenciosamente,
[Seu Nome]
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        email_file = self.data_dir / "onboarding" / "01-email-boas-vindas.MD"
        email_file.write_text(content, encoding="utf-8")

        return content

    def _generate_formulario_onboarding(self) -> str:
        """Gera formulário de coleta de informações."""
        prompt = f"""
Crie um FORMULÁRIO DE ONBOARDING para coletar informações do cliente {self.client_name}.

Escopo da entrega: {self.delivery_scope}

O formulário deve ter 10-15 perguntas organizadas em seções:

# Formulário de Onboarding - {self.client_name}

## Seção 1: Informações Gerais
1. Nome completo e cargo
2. E-mail principal para contato
3. Telefone/WhatsApp

## Seção 2: Contexto do Negócio
4. [Pergunta contextual relevante]
5. [Pergunta sobre objetivo]

## Seção 3: Especificações da Entrega
6. [Pergunta sobre requisitos]
7. [Pergunta sobre preferências]

## Seção 4: Acessos e Recursos
8. [Pergunta sobre acessos]
9. [Pergunta sobre materiais]

## Seção 5: Alinhamento de Expectativas
10. [Pergunta sobre expectativa]

Personalize as perguntas para o escopo específico.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        form_file = self.data_dir / "onboarding" / "02-formulario-onboarding.MD"
        form_file.write_text(content, encoding="utf-8")

        return content

    def _generate_roteiro_onboarding(self) -> str:
        """Gera roteiro de reunião de onboarding."""
        prompt = f"""
Crie um ROTEIRO DE REUNIÃO DE ONBOARDING (45 minutos) para {self.client_name}.

# Roteiro: Reunião de Onboarding - {self.client_name}

**Duração:** 45 minutos
**Objetivo:** Alinhar expectativas e coletar informações críticas

## Agenda

### 1. Abertura (5 min)
- Boas-vindas
- Apresentação do time
- Objetivo da reunião

### 2. Revisão do Escopo (10 min)
- Confirmar entregáveis: {self.delivery_scope}
- Esclarecer limites (o que NÃO está incluído)
- Tirar dúvidas iniciais

### 3. Cronograma e Milestones (10 min)
- Apresentar timeline
- Definir checkpoints de aprovação
- Alinhar disponibilidade do cliente

### 4. Coleta de Informações (15 min)
- Revisar formulário de onboarding
- Esclarecer pontos críticos
- Listar acessos e recursos necessários

### 5. Próximos Passos e Encerramento (5 min)
- Resumir decisões tomadas
- Definir canal de comunicação preferido
- Marcar próximo check-in

## Perguntas-Chave a Fazer:
1. [Pergunta 1]
2. [Pergunta 2]
3. [Pergunta 3]

## Checklist Pós-Reunião:
- [ ] Ata registrada
- [ ] Decisões documentadas
- [ ] Próximas ações agendadas
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        roteiro_file = self.data_dir / "onboarding" / "03-roteiro-reuniao.MD"
        roteiro_file.write_text(content, encoding="utf-8")

        return content

    def _stage_3_planning(self) -> Dict[str, Any]:
        """
        Etapa 3: Planejamento detalhado (120 min).

        Quebra a entrega em tarefas com responsáveis e cronograma.
        """
        logger.info("Gerando plano de execução detalhado")

        plano_content = self._generate_plano_execucao()
        cronograma_content = self._generate_cronograma_detalhado()

        return {
            "plano_file": str(self.data_dir / "03-plano-execucao.MD"),
            "cronograma_file": str(self.data_dir / "04-cronograma-detalhado.MD"),
            "status": "completed",
        }

    def _generate_plano_execucao(self) -> str:
        """Gera plano de execução detalhado."""
        prompt = f"""
Crie um PLANO DE EXECUÇÃO DETALHADO para a entrega do cliente {self.client_name}.

Escopo: {self.delivery_scope}
Prazo: {self.deadline}

# Plano de Execução - {self.client_name}

## Visão Geral
- **Objetivo:** [Descrever objetivo principal]
- **Prazo:** {self.deadline}
- **Responsável:** [Nome]

## Entregáveis e Tarefas

### Entregável 1: [Nome]
**Descrição:** [Descrição breve]
**Responsável:** [Nome]
**Prazo:** [Data]

Tarefas:
- [ ] Tarefa 1.1 - [Descrição] (Estimativa: Xh)
- [ ] Tarefa 1.2 - [Descrição] (Estimativa: Xh)
- [ ] Tarefa 1.3 - [Descrição] (Estimativa: Xh)

### Entregável 2: [Nome]
[Repetir estrutura]

## Checkpoints de Revisão
- **Checkpoint 1:** [Data] - Revisão interna inicial
- **Checkpoint 2:** [Data] - Validação com cliente
- **Checkpoint 3:** [Data] - QA final

## Recursos Necessários
- Ferramentas: [Listar]
- Acessos: [Listar]
- Conhecimento: [Listar]

## Critérios de Qualidade
- [ ] Critério 1
- [ ] Critério 2
- [ ] Critério 3

Quebre em 3-5 entregáveis principais, cada um com 3-5 tarefas específicas.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        plano_file = self.data_dir / "03-plano-execucao.MD"
        plano_file.write_text(content, encoding="utf-8")

        return content

    def _generate_cronograma_detalhado(self) -> str:
        """Gera cronograma detalhado."""
        prompt = f"""
Crie um CRONOGRAMA DETALHADO para a entrega do cliente {self.client_name}.

Data de início: {datetime.now().strftime('%Y-%m-%d')}
Data de entrega: {self.deadline}

# Cronograma Detalhado - {self.client_name}

## Timeline Visual

```
Início: {datetime.now().strftime('%Y-%m-%d')}
   |
   |--- Semana 1: [Atividades principais]
   |
   |--- Semana 2: [Atividades principais]
   |
   |--- Semana 3: [Atividades principais]
   |
Final: {self.deadline}
```

## Marcos Principais

| Data | Marco | Responsável | Status |
|------|-------|-------------|--------|
| [Data] | Onboarding concluído | [Nome] | 🟢 |
| [Data] | Primeira versão pronta | [Nome] | 🟡 |
| [Data] | Revisão do cliente | [Nome] | ⚪ |
| [Data] | QA finalizado | [Nome] | ⚪ |
| {self.deadline} | Entrega oficial | [Nome] | ⚪ |

## Distribuição de Esforço

- **Planejamento e setup:** X horas
- **Produção:** X horas
- **Revisão e ajustes:** X horas
- **QA e testes:** X horas
- **Entrega e documentação:** X horas

**Total estimado:** X horas

## Cadência de Updates ao Cliente
- Check-in semanal: Toda [dia da semana] às [horário]
- Status report: Enviado toda [dia da semana]
- Disponibilidade para dúvidas: [Horário de atendimento]

Distribua as atividades de forma realista considerando o prazo.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        cronograma_file = self.data_dir / "04-cronograma-detalhado.MD"
        cronograma_file.write_text(content, encoding="utf-8")

        return content

    def _stage_4_production(self) -> Dict[str, Any]:
        """
        Etapa 4: Produção e QA (tempo variável).

        Placeholder para execução da produção.
        """
        logger.info("Gerando checklist de execução e QA")

        # Checklist de execução
        checklist_content = self._generate_checklist_execucao()

        # Checklist de QA
        qa_content = self._generate_checklist_qa()

        return {
            "checklist_file": str(self.data_dir / "05-checklist-execucao.MD"),
            "qa_file": str(self.data_dir / "06-checklist-qa.MD"),
            "status": "pending_execution",
            "note": "Produção deve ser executada manualmente seguindo os checklists",
        }

    def _generate_checklist_execucao(self) -> str:
        """Gera checklist de execução."""
        prompt = f"""
Crie um CHECKLIST DE EXECUÇÃO para a produção da entrega do cliente {self.client_name}.

Escopo: {self.delivery_scope}

# Checklist de Execução - {self.client_name}

## Antes de Começar
- [ ] Brief de entrega revisado
- [ ] Plano de execução validado
- [ ] Recursos e acessos disponíveis
- [ ] Ferramentas configuradas

## Durante a Produção

### Fase 1: Setup Inicial
- [ ] Item 1.1
- [ ] Item 1.2
- [ ] Item 1.3

### Fase 2: Desenvolvimento
- [ ] Item 2.1
- [ ] Item 2.2
- [ ] Item 2.3

### Fase 3: Refinamento
- [ ] Item 3.1
- [ ] Item 3.2
- [ ] Item 3.3

## Documentação Contínua
- [ ] Log de decisões atualizado
- [ ] Registro de alterações mantido
- [ ] Status report enviado ao cliente

## Checkpoints de Qualidade
- [ ] Revisão interna realizada
- [ ] Feedback do cliente incorporado
- [ ] Padrões de qualidade seguidos

Crie 15-20 itens específicos para o escopo da entrega.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        checklist_file = self.data_dir / "05-checklist-execucao.MD"
        checklist_file.write_text(content, encoding="utf-8")

        return content

    def _generate_checklist_qa(self) -> str:
        """Gera checklist de QA."""
        prompt = f"""
Crie um CHECKLIST DE QA (Quality Assurance) rigoroso para a entrega do cliente {self.client_name}.

# Checklist de QA - {self.client_name}

**IMPORTANTE:** Todos os itens devem estar marcados antes da entrega oficial.

## 1. Completude
- [ ] Todos os entregáveis prometidos estão presentes
- [ ] Escopo acordado foi 100% atendido
- [ ] Nenhum item crítico pendente

## 2. Qualidade Técnica
- [ ] Funcionalidades testadas (quando aplicável)
- [ ] Código revisado (quando aplicável)
- [ ] Performance adequada
- [ ] Compatibilidade verificada

## 3. Qualidade de Conteúdo
- [ ] Textos revisados (ortografia, gramática)
- [ ] Consistência de linguagem e tom
- [ ] Informações precisas e atualizadas

## 4. Experiência do Usuário
- [ ] Intuitividade testada
- [ ] Instruções claras incluídas
- [ ] Casos de uso principais validados

## 5. Documentação
- [ ] Manual de uso criado (se aplicável)
- [ ] Instruções de configuração incluídas
- [ ] FAQ ou troubleshooting preparado

## 6. Alinhamento com Cliente
- [ ] Expectativas do brief atendidas
- [ ] Preferências do cliente respeitadas
- [ ] Feedback anterior incorporado

## 7. Entrega e Suporte
- [ ] Pacote de entrega organizado
- [ ] Materiais acessíveis ao cliente
- [ ] Plano de suporte pós-entrega definido

## Status Final: ⚪ Aguardando revisão

**Responsável pelo QA:** [Nome]
**Data da revisão:** [Data]

Personalize para o escopo: {self.delivery_scope}
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        qa_file = self.data_dir / "06-checklist-qa.MD"
        qa_file.write_text(content, encoding="utf-8")

        return content

    def _stage_5_delivery(self) -> Dict[str, Any]:
        """
        Etapa 5: Entrega oficial (60 min).

        Prepara materiais para reunião de entrega.
        """
        logger.info("Gerando materiais de entrega oficial")

        roteiro_content = self._generate_roteiro_apresentacao()
        instrucoes_content = self._generate_pacote_instrucoes()

        return {
            "roteiro_file": str(self.data_dir / "07-roteiro-apresentacao.MD"),
            "instrucoes_file": str(self.data_dir / "08-pacote-instrucoes.MD"),
            "status": "ready_for_presentation",
        }

    def _generate_roteiro_apresentacao(self) -> str:
        """Gera roteiro de apresentação da entrega."""
        prompt = f"""
Crie um ROTEIRO DE APRESENTAÇÃO (60 minutos) para a entrega oficial ao cliente {self.client_name}.

# Roteiro de Apresentação - {self.client_name}

**Duração:** 60 minutos
**Objetivo:** Apresentar solução, transferir conhecimento e confirmar satisfação

## Agenda

### 1. Abertura (5 min)
- Recapitular jornada desde o onboarding
- Relembrar objetivos e expectativas iniciais
- Apresentar agenda da reunião

### 2. Demonstração da Solução (25 min)
- Visão geral do que foi entregue
- Demonstração prática dos principais recursos
- Destacar diferenciais e atenção aos detalhes
- Responder dúvidas em tempo real

### 3. Transferência de Conhecimento (15 min)
- Como usar no dia a dia
- Boas práticas e recomendações
- Troubleshooting básico
- Onde encontrar documentação adicional

### 4. Próximos Passos e Suporte (10 min)
- Período de garantia e suporte incluído
- Como solicitar ajustes (se aplicável)
- Check-in pós-entrega agendado
- Materiais disponibilizados

### 5. Feedback e Encerramento (5 min)
- Coletar impressões iniciais
- Confirmar satisfação
- Agradecer pela confiança
- Solicitar depoimento (se momento apropriado)

## Materiais Necessários
- [ ] Acesso/link para demonstração
- [ ] Pacote de instruções preparado
- [ ] Documentação de suporte
- [ ] Formulário de confirmação de recebimento

## Checklist Pré-Apresentação
- [ ] QA 100% concluído
- [ ] Demo environment testado
- [ ] Materiais enviados com antecedência
- [ ] Backup preparado (se aplicável)

Adapte para o escopo: {self.delivery_scope}
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        roteiro_file = self.data_dir / "07-roteiro-apresentacao.MD"
        roteiro_file.write_text(content, encoding="utf-8")

        return content

    def _generate_pacote_instrucoes(self) -> str:
        """Gera pacote de instruções para o cliente."""
        prompt = f"""
Crie um PACOTE DE INSTRUÇÕES completo para o cliente {self.client_name}.

# Pacote de Instruções - {self.client_name}

## Bem-vindo(a) à sua entrega!

Parabéns! Sua solução está pronta. Este documento contém tudo que você precisa saber para começar a usar.

---

## 📦 O Que Você Recebeu

### Entregáveis
1. [Entregável 1] - [Descrição breve]
2. [Entregável 2] - [Descrição breve]
3. [Entregável 3] - [Descrição breve]

### Acessos e Recursos
- **Link principal:** [URL]
- **Credenciais:** [Informações ou referência]
- **Documentação adicional:** [Links]

---

## 🚀 Primeiros Passos

### Passo 1: [Ação inicial]
[Instruções detalhadas]

### Passo 2: [Próxima ação]
[Instruções detalhadas]

### Passo 3: [Configuração]
[Instruções detalhadas]

---

## 💡 Como Usar no Dia a Dia

### Caso de Uso 1: [Cenário comum]
**Objetivo:** [O que você quer fazer]
**Como fazer:**
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

### Caso de Uso 2: [Outro cenário]
[Repetir estrutura]

---

## 🔧 Solução de Problemas

### Problema: [Situação comum]
**Solução:** [Como resolver]

### Problema: [Outra situação]
**Solução:** [Como resolver]

---

## 📞 Suporte e Próximos Passos

### Período de Garantia
- **Duração:** [X dias/semanas]
- **O que está coberto:** [Detalhes]
- **Como solicitar:** [Canal e processo]

### Check-in Agendado
- **Data:** [Data do follow-up]
- **Objetivo:** Verificar se está tudo funcionando bem

### Contato para Dúvidas
- **E-mail:** [Seu e-mail]
- **Horário de atendimento:** [Horário]
- **Prazo de resposta:** [Tempo esperado]

---

## 🌟 Ajude Outros a Encontrar Esta Solução

Se você está satisfeito(a) com a entrega, adoraríamos receber um depoimento!

**O que incluir no depoimento:**
- Qual era o seu desafio inicial?
- Como a solução ajudou?
- Qual foi o resultado ou benefício percebido?

[Link para formulário de depoimento ou instruções]

---

**Data da entrega:** {datetime.now().strftime('%d/%m/%Y')}
**Responsável:** [Seu nome]

Personalize completamente para: {self.delivery_scope}
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        instrucoes_file = self.data_dir / "08-pacote-instrucoes.MD"
        instrucoes_file.write_text(content, encoding="utf-8")

        return content

    def _stage_6_post_delivery(self) -> Dict[str, Any]:
        """
        Etapa 6: Pós-entrega e depoimentos (45 min + follow-up).

        Prepara materiais de follow-up e coleta de depoimentos.
        """
        logger.info("Gerando materiais de pós-entrega")

        followup_content = self._generate_followup_email()
        depoimento_content = self._generate_template_depoimento()

        return {
            "followup_file": str(self.data_dir / "09-followup-pos-entrega.MD"),
            "depoimento_file": str(self.data_dir / "10-template-depoimento.MD"),
            "status": "ready_for_followup",
        }

    def _generate_followup_email(self) -> str:
        """Gera e-mail de follow-up pós-entrega."""
        prompt = f"""
Escreva um E-MAIL DE FOLLOW-UP para enviar 24-48h após a entrega ao cliente {self.client_name}.

**Assunto:** Como está sendo a experiência? - {self.client_name}

Olá [Nome do Cliente],

[Corpo do e-mail - 3-4 parágrafos]

Perguntas importantes:
1. Você conseguiu [usar/acessar/implementar] a solução sem dificuldades?
2. Há algo que não ficou claro ou precisa de ajuste?
3. O resultado está alinhado com suas expectativas?

Estou à disposição para qualquer dúvida ou ajuste!

Aproveito para solicitar um pequeno favor: se você está satisfeito(a) com a entrega, adoraria receber um breve depoimento sobre a experiência. Isso nos ajuda muito a melhorar e atrair mais clientes como você!

[Link para depoimento ou instruções]

Atenciosamente,
[Seu Nome]

---

# Checklist de Follow-up

## 24-48h após entrega:
- [ ] Enviar este e-mail
- [ ] Aguardar resposta (prazo: 48h)

## Se resposta positiva:
- [ ] Agradecer feedback
- [ ] Solicitar depoimento (se ainda não enviado)
- [ ] Registrar caso de sucesso

## Se houver problemas:
- [ ] Identificar natureza do problema
- [ ] Priorizar resolução
- [ ] Manter cliente atualizado
- [ ] Resolver dentro do período de garantia

## 7 dias após entrega:
- [ ] Check-in final
- [ ] Confirmar satisfação
- [ ] Coletar métricas (NPS, satisfação)
- [ ] Fechar caso

Personalize para o contexto do cliente {self.client_name}.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        followup_file = self.data_dir / "09-followup-pos-entrega.MD"
        followup_file.write_text(content, encoding="utf-8")

        return content

    def _generate_template_depoimento(self) -> str:
        """Gera template para solicitar depoimento."""
        prompt = f"""
Crie um TEMPLATE para solicitar DEPOIMENTO do cliente {self.client_name}.

# Template de Solicitação de Depoimento - {self.client_name}

## E-mail/Mensagem de Solicitação

**Assunto:** [Nome], você poderia compartilhar sua experiência?

Olá [Nome],

Fico muito feliz que a entrega tenha atendido suas expectativas!

Para nos ajudar a crescer e continuar entregando valor, adoraria se você pudesse compartilhar brevemente sua experiência. Não precisa ser longo - um parágrafo curto já ajuda muito!

**Sugestão de estrutura para seu depoimento:**

1. **Contexto:** Qual era o seu desafio ou objetivo inicial?
2. **Solução:** O que foi entregue e como ajudou?
3. **Resultado:** Qual benefício ou resultado você percebeu?

**Formatos aceitos:**
- ✍️ Texto (e-mail, mensagem ou formulário)
- 🎤 Áudio (WhatsApp ou gravação)
- 🎥 Vídeo curto (30-60 segundos)

[Link para formulário ou instruções de envio]

Muito obrigado pela confiança!

Atenciosamente,
[Seu Nome]

---

## Guia de Edição do Depoimento

Quando receber o depoimento do cliente:

### 1. Revisar e Formatar
- Corrigir erros gramaticais (manter autenticidade)
- Destacar trechos-chave
- Adicionar contexto se necessário

### 2. Estrutura Ideal
**[Nome do Cliente] - [Cargo/Empresa]**

"[Depoimento com 2-3 parágrafos destacando contexto, solução e resultado]"

**Projeto:** {self.delivery_scope}
**Data:** {datetime.now().strftime('%B %Y')}

### 3. Uso do Depoimento
- [ ] Adicionar ao portfólio
- [ ] Incluir em materiais de venda
- [ ] Compartilhar em redes sociais (com permissão)
- [ ] Usar em estudos de caso

---

## Exemplos de Bons Depoimentos

**Exemplo 1 (Texto):**
"Eu precisava [desafio]. A solução entregue [o que foi feito] e o resultado foi [benefício]. Recomendo muito o trabalho do [seu nome]!"

**Exemplo 2 (Estruturado):**
**Contexto:** Minha empresa tinha dificuldade em [problema].
**Solução:** Recebi [entregável] que [característica].
**Resultado:** Agora conseguimos [benefício] e isso gerou [impacto].

Personalize completamente para o contexto do cliente.
"""

        response = self.llm.invoke(prompt)
        content = response.content if hasattr(response, "content") else str(response)

        depoimento_file = self.data_dir / "10-template-depoimento.MD"
        depoimento_file.write_text(content, encoding="utf-8")

        return content

    def _create_consolidated_report(self, results: Dict[str, Any]) -> None:
        """Cria relatório consolidado de toda a entrega."""
        logger.info("Gerando relatório consolidado")

        content = f"""# Relatório Consolidado: Client Delivery - {self.client_name}

**Data de início:** {results['started_at']}
**Data de conclusão:** {results['completed_at']}
**Escopo:** {self.delivery_scope}
**Prazo acordado:** {self.deadline}

---

## Resumo Executivo

Este relatório documenta o processo completo de entrega ao cliente {self.client_name},
seguindo as 6 etapas do processo ClientDelivery do framework ZeroUm.

---

## Etapas Executadas

### ✅ Etapa 1: Handoff e Planejamento
- Brief de entrega criado
- Diagnóstico de pendências realizado
- Arquivos gerados:
  - {results['stages']['handoff']['brief_file']}
  - {results['stages']['handoff']['diagnostico_file']}

### ✅ Etapa 2: Onboarding e Alinhamento
- Materiais de boas-vindas preparados
- Formulário de coleta criado
- Roteiro de reunião estruturado
- Arquivos gerados:
  - {results['stages']['onboarding']['email_file']}
  - {results['stages']['onboarding']['formulario_file']}
  - {results['stages']['onboarding']['roteiro_file']}

### ✅ Etapa 3: Planejamento Detalhado
- Plano de execução definido
- Cronograma criado
- Arquivos gerados:
  - {results['stages']['planning']['plano_file']}
  - {results['stages']['planning']['cronograma_file']}

### 🟡 Etapa 4: Produção e QA
- Checklists preparados
- **Status:** {results['stages']['production']['status']}
- **Nota:** {results['stages']['production']['note']}
- Arquivos gerados:
  - {results['stages']['production']['checklist_file']}
  - {results['stages']['production']['qa_file']}

### ✅ Etapa 5: Entrega Oficial
- Roteiro de apresentação preparado
- Pacote de instruções criado
- Arquivos gerados:
  - {results['stages']['official_delivery']['roteiro_file']}
  - {results['stages']['official_delivery']['instrucoes_file']}

### ✅ Etapa 6: Pós-Entrega
- Follow-up estruturado
- Template de depoimento preparado
- Arquivos gerados:
  - {results['stages']['post_delivery']['followup_file']}
  - {results['stages']['post_delivery']['depoimento_file']}

---

## Próximas Ações Manuais

1. **Executar produção:** Seguir checklist em `{results['stages']['production']['checklist_file']}`
2. **Realizar QA:** Completar checklist em `{results['stages']['production']['qa_file']}`
3. **Agendar reunião de entrega:** Usar roteiro em `{results['stages']['official_delivery']['roteiro_file']}`
4. **Enviar follow-up:** 24-48h após entrega
5. **Coletar depoimento:** Usar template em `{results['stages']['post_delivery']['depoimento_file']}`

---

## Indicadores de Sucesso (Meta)

- [ ] Entrega no prazo: ✅ (Prazo: {self.deadline})
- [ ] QA 100% concluído: ⚪ (Aguardando)
- [ ] Cliente satisfeito (NPS ≥ 8): ⚪ (Verificar no follow-up)
- [ ] Depoimento coletado: ⚪ (Verificar em 7 dias)
- [ ] Ajustes pós-entrega ≤ 2: ⚪ (Monitorar)

---

## Arquivos Gerados

Todos os materiais estão organizados em:
`{self.delivery_dir}/_DATA/`

Total de arquivos: 10 documentos estruturados

---

**Processo executado por:** ClientDeliveryAgent (ZeroUm Framework)
**Versão:** 2.0.1
**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

        report_file = self.delivery_dir / "00-relatorio-consolidado.MD"
        report_file.write_text(content, encoding="utf-8")
        logger.info(f"Relatório consolidado salvo em {report_file}")

    def _fill_data_templates(self, results: Dict[str, Any]) -> None:
        """Preenche os templates oficiais de `_DATA` com base nos materiais gerados."""
        context = self._build_template_context(results)
        tasks: List[TemplateTask] = [
            TemplateTask(
                template="brief-entrega.MD",
                instructions="Complete o brief com dados reais do cliente, escopo, limites e riscos identificados.",
                output_name="01-brief-entrega.MD",
            ),
            TemplateTask(
                template="diagnostico-pendencias.MD",
                instructions="Liste pendências críticas com responsáveis e prazos, conforme o diagnóstico e checklists.",
                output_name="02-diagnostico-pendencias.MD",
            ),
            TemplateTask(
                template="mensagem-confirmacao.MD",
                instructions="Escreva a mensagem enviada ao cliente confirmando o kickoff e os próximos passos imediatos.",
                output_name="03-mensagem-confirmacao.MD",
            ),
            TemplateTask(
                template="onboarding-email.MD",
                instructions="Personalize o e-mail de boas-vindas com tom profissional e próximos passos claros.",
                output_name="onboarding/01-email-boas-vindas.MD",
            ),
            TemplateTask(
                template="formulario-onboarding.MD",
                instructions="Adapte o formulário para o contexto do cliente e preencha respostas conhecidas; indique 'Aguardando cliente' quando necessário.",
                output_name="onboarding/02-formulario-onboarding.MD",
            ),
            TemplateTask(
                template="roteiro-onboarding.MD",
                instructions="Detalhe a pauta da reunião de onboarding com perguntas específicas e checkpoints.",
                output_name="onboarding/03-roteiro-reuniao.MD",
            ),
            TemplateTask(
                template="ata-onboarding.MD",
                instructions="Registre participantes, decisões e pendências extraídas do onboarding.",
                output_name="onboarding/04-ata-onboarding.MD",
            ),
            TemplateTask(
                template="plano-execucao.MD",
                instructions="Estruture o plano de execução citando entregáveis, responsáveis e critérios de sucesso.",
                output_name="03-plano-execucao.MD",
            ),
            TemplateTask(
                template="cronograma-detalhado.MD",
                instructions="Monte o cronograma semanal com marcos e cadência de comunicação.",
                output_name="04-cronograma-detalhado.MD",
            ),
            TemplateTask(
                template="checklist-execucao.MD",
                instructions="Liste as tarefas de produção passo a passo, vinculando responsáveis e status.",
                output_name="05-checklist-execucao.MD",
            ),
            TemplateTask(
                template="checklist-qa-entrega.MD",
                instructions="Detalhe verificações de QA obrigatórias antes da entrega.",
                output_name="06-checklist-qa.MD",
            ),
            TemplateTask(
                template="roteiro-apresentacao.MD",
                instructions="Descreva o roteiro da reunião de entrega com tempo estimado e tópicos.",
                output_name="07-roteiro-apresentacao.MD",
            ),
            TemplateTask(
                template="pacote-instrucoes.MD",
                instructions="Explique os entregáveis disponibilizados e como utilizá-los após a reunião.",
                output_name="08-pacote-instrucoes.MD",
            ),
            TemplateTask(
                template="ata-entrega.MD",
                instructions="Registre participantes, dúvidas e próximos passos alinhados na reunião oficial de entrega.",
                output_name="entregas/ata-entrega.MD",
            ),
            TemplateTask(
                template="followup-pos-entrega.MD",
                instructions="Planeje o acompanhamento pós-entrega com agenda, indicadores e perguntas de satisfação.",
                output_name="09-followup-pos-entrega.MD",
            ),
            TemplateTask(
                template="template-depoimento.MD",
                instructions="Personalize o pedido de depoimento com foco no resultado obtido pelo cliente.",
                output_name="10-template-depoimento.MD",
            ),
            TemplateTask(
                template="registro-feedback.MD",
                instructions="Prepare o log para registrar feedbacks contínuos do cliente pós-entrega.",
                output_name="relatos/registro-feedback.MD",
            ),
            TemplateTask(
                template="relato-caso.MD",
                instructions="Documente um estudo de caso resumindo contexto, solução e impacto.",
                output_name="relatos/relato-caso.MD",
            ),
            TemplateTask(
                template="tracker-tempo.MD",
                instructions="Distribua o tempo investido por etapa para facilitar controle interno.",
                output_name="tracker-tempo.MD",
            ),
        ]
        self.template_filler.fill_templates(tasks, context)

    def _build_template_context(self, results: Dict[str, Any]) -> str:
        """Compila contexto textual para orientar o preenchimento dos templates."""
        lines: List[str] = [
            f"Cliente: {self.client_name}",
            f"Escopo: {self.delivery_scope}",
            f"Prazo: {self.deadline}",
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
