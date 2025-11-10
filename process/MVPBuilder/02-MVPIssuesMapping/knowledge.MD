# Base de Conhecimento - Mapeamento de Issues para MVP

## Propósito

Este documento fornece contexto teórico, boas práticas e referências sobre mapeamento de issues técnicas para desenvolvimento de MVP.

## Fundamentos

### O que são Issues Técnicas

Issues técnicas são tarefas específicas e executáveis que descrevem trabalho de desenvolvimento. Uma boa issue deve ter:
- Título claro e descritivo
- Descrição do que precisa ser feito
- Critérios de aceite testáveis
- Estimativa de tempo
- Dependências mapeadas

### Priorização de Issues

**P0 (Bloqueante):** Setup técnico que bloqueia todo desenvolvimento
**P1 (Core):** Funcionalidade principal do MVP
**P2 (Secundário):** Funcionalidades complementares
**P3 (Nice to have):** Pode ser cortado

## Boas Práticas

### Ao Criar Issues

- Seja específico no título: "Criar página de login" > "Login"
- Critérios de aceite testáveis: "Usuário consegue fazer login" > "Login funciona"
- Adicione 20-30% de buffer nas estimativas
- Issues > 8h considere quebrar em menores
- Sempre mapeie dependências explícitas

### Estimativas Realistas

- Considere tempo de code review
- Inclua tempo de testes
- Adicione buffer para imprevistos
- Valide com desenvolvedores que executarão

## FAQ

**P: Quantas issues criar?**
R: Mínimo 15, ideal 20-25 para MVP completo.

**P: Como estimar sem conhecer a stack?**
R: Use referências de projetos similares + 50% de buffer.

**P: E se timeline exceder 8 semanas?**
R: Corte funcionalidades P2/P3 ou adicione desenvolvedores.

---

**Criado em:** 2025-11-05
**Versão:** 1.0
