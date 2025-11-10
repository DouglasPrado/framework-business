# Processo: Mapeamento de Issues para MVP

## Visão Geral

O processo de Mapeamento de Issues transforma o Briefing de MVP em backlog técnico executável, criando issues detalhadas, configurando repositório e definindo timeline de desenvolvimento.

**Objetivo:** Criar backlog técnico completo com issues priorizadas, estimadas e organizadas em milestones, pronto para execução.

**Duração:** 3-4 dias

**Responsável típico:** Tech Lead ou Desenvolvedor Senior

---

## Quando Usar Este Processo

Use este processo quando:
- Briefing de MVP está aprovado e completo
- Escopo de funcionalidades está claro
- Time técnico está identificado
- Precisa transformar escopo de produto em tarefas técnicas executáveis

Não use este processo quando:
- Briefing de MVP ainda não existe (execute MVPScopeDefinition primeiro)
- Escopo ainda está sendo debatido
- Não há clareza sobre funcionalidades

---

## Estrutura de Arquivos

```
MVPIssuesMapping/
├── README.MD (este arquivo)
├── process.MD (fluxo de 5 etapas)
├── tasks.MD (checklist de 25 tarefas)
└── _DATA/
    └── template-issue-github.md
```

---

## Como Executar Este Processo

### Passo 1: Prepare as Entradas
- [ ] Briefing de MVP aprovado
- [ ] Template de Funcionalidades preenchido
- [ ] Acesso a GitHub/GitLab
- [ ] Node.js instalado localmente

### Passo 2: Leia os Documentos
1. [process.MD](process.MD) - Entenda as 5 etapas
2. [tasks.MD](tasks.MD) - Familiarize-se com as 25 tarefas

### Passo 3: Execute as Tarefas
- Etapa 1: Setup de Repositório (Tarefas 1-6)
- Etapa 2: Mapeamento de Funcionalidades (Tarefas 7-10)
- Etapa 3: Issues de Setup Técnico (Tarefas 11-16)
- Etapa 4: Priorização e Estimativa (Tarefas 17-20)
- Etapa 5: Milestones e Board (Tarefas 21-25)

### Passo 4: Valide o Resultado
- [ ] Mínimo 15-20 issues criadas
- [ ] Timeline validada em 6-8 semanas
- [ ] Board kanban funcionando
- [ ] Time alinhado

---

## Principais Entregas

1. **Repositório Git configurado** com projeto Next.js rodando
2. **15-20 issues técnicas** seguindo template padrão
3. **Issues priorizadas** (P0, P1, P2) e estimadas
4. **4 Milestones** organizando entregas incrementais
5. **Board kanban** configurado para acompanhamento
6. **Timeline validada** de 6-8 semanas

---

## Métricas de Sucesso

- Tempo: 3-4 dias
- Issues criadas: mínimo 15, ideal 20-25
- Clareza: desenvolvedor consegue executar sem perguntas
- Timeline: validada em 6-8 semanas
- Cobertura: 100% das funcionalidades mapeadas

---

## Integrações com Outros Processos

**Processo anterior:**
- MVPScopeDefinition (fornece Briefing de MVP)

**Próximo processo:**
- MVPInfrastructureSetup (execução das issues P0)

**Posição na estratégia:** Etapa 2 de 7 do MVPBuilder

---

## Template Disponível

**Template de Issue GitHub**
- Arquivo: _DATA/template-issue-github.md
- Uso: Criar todas as issues de desenvolvimento
- Contém: Estrutura padrão + 4 exemplos completos

---

## FAQ Rápido

**P: Quantas issues devo criar?**
R: Mínimo 15, ideal 20-25. Funcionalidade core: 3-5 issues. Cada secundária: 2-3 issues. Setup: 7-8 issues.

**P: Como estimar se nunca usei essa stack?**
R: Use referências de projetos similares. Adicione 50% de buffer. Valide com desenvolvedor experiente.

**P: E se timeline exceder 8 semanas?**
R: Corte funcionalidades P2 ou P3. Revise estimativas. Considere adicionar desenvolvedores.

**P: Preciso criar todas as issues de uma vez?**
R: Sim para issues P0 e P1 (setup + core). Issues P2 podem ser refinadas depois.

---

**Criado em:** 2025-11-05
**Versão:** 1.0
**Parte da estratégia:** MVPBuilder (Etapa 2 de 7)
