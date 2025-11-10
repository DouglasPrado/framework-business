# Especificação Técnica - [Nome da Funcionalidade]

Data: [YYYY-MM-DD]
Desenvolvedor: [Nome]
Projeto: [Nome do MVP]

---

## 1. Descrição da Funcionalidade

### Resumo
[Descreva em 2-3 parágrafos o que esta funcionalidade faz e por que é importante para o MVP]

### Proposta de Valor
[Como esta funcionalidade demonstra a proposta de valor do MVP?]

### Contexto
[Contexto adicional sobre esta funcionalidade - de onde vem a necessidade, qual problema resolve]

---

## 2. Critérios de Aceite

Baseado no Briefing de MVP:

1. [ ] [Critério de aceite 1]
2. [ ] [Critério de aceite 2]
3. [ ] [Critério de aceite 3]
4. [ ] [Critério de aceite 4]
5. [ ] [Critério de aceite 5]

---

## 3. Fluxo do Usuário

### Fluxo Principal

1. Usuário [ação inicial]
2. Sistema [resposta do sistema]
3. Usuário [próxima ação]
4. Sistema [resposta]
5. [Continue descrevendo o fluxo completo]

### Fluxos Alternativos

**Fluxo Alternativo 1: [Nome]**
- [Descrever quando este fluxo acontece]
- [Passos do fluxo alternativo]

**Fluxo de Erro 1: [Nome do Erro]**
- [Quando este erro acontece]
- [Como o sistema responde]

---

## 4. Componentes React Necessários

### Páginas (Rotas)

#### Página: [Nome da Página]
- **Rota:** `/[caminho]`
- **Proteção:** [ ] Pública  [ ] Requer autenticação
- **Descrição:** [O que esta página faz]
- **Componentes principais:** [Lista de componentes usados]

#### Página: [Nome da Página 2]
- **Rota:** `/[caminho]`
- **Proteção:** [ ] Pública  [ ] Requer autenticação
- **Descrição:** [O que esta página faz]
- **Componentes principais:** [Lista de componentes usados]

### Componentes Específicos da Feature

#### Componente: [NomeDoComponente]
- **Arquivo:** `src/components/feature/[NomeDoComponente].tsx`
- **Propósito:** [O que este componente faz]
- **Props:**
  ```typescript
  interface Props {
    prop1: string;
    prop2: number;
    onAction?: () => void;
  }
  ```
- **Estado interno:** [Descrever estados se houver]
- **Usa componentes base:** [Lista se aplicável]

#### Componente: [OutroComponente]
- **Arquivo:** `src/components/feature/[OutroComponente].tsx`
- **Propósito:** [O que este componente faz]
- **Props:**
  ```typescript
  interface Props {
    // definir props
  }
  ```

### Hooks Customizados (se aplicável)

#### Hook: use[NomeDoHook]
- **Arquivo:** `src/hooks/use[NomeDoHook].ts`
- **Propósito:** [O que este hook faz]
- **Retorna:**
  ```typescript
  {
    data: DataType;
    isLoading: boolean;
    error: Error | null;
  }
  ```

### Componentes Base Reutilizados

- [ ] Button (de `components/ui/`)
- [ ] Card (de `components/ui/`)
- [ ] Input (de `components/ui/`)
- [ ] Modal (de `components/ui/`)
- [ ] [Outros componentes base]

---

## 5. API Routes Necessárias

### Endpoint: [Nome do Endpoint]

**Método:** `GET` | `POST` | `PUT` | `DELETE`
**Rota:** `/api/[caminho]`
**Autenticação:** [ ] Sim  [ ] Não

**Descrição:**
[O que este endpoint faz]

**Parâmetros de Entrada:**

Query params:
```typescript
{
  param1?: string;
  param2?: number;
}
```

Body (se POST/PUT):
```typescript
{
  field1: string;
  field2: number;
  field3?: boolean;
}
```

**Validação (Zod Schema):**
```typescript
const schema = z.object({
  field1: z.string().min(1).max(100),
  field2: z.number().positive(),
  field3: z.boolean().optional(),
});
```

**Resposta de Sucesso:**
Status: `200` | `201`
```typescript
{
  id: string;
  field1: string;
  field2: number;
  createdAt: string;
}
```

**Respostas de Erro:**
- `400 Bad Request`: Dados inválidos
- `401 Unauthorized`: Não autenticado
- `403 Forbidden`: Não autorizado
- `404 Not Found`: Recurso não encontrado
- `500 Internal Server Error`: Erro no servidor

**Lógica de Negócio:**
1. [Passo 1 da lógica]
2. [Passo 2 da lógica]
3. [Passo 3 da lógica]

---

### Endpoint: [Outro Endpoint]

[Repetir estrutura acima para cada endpoint]

---

## 6. Models Prisma Necessários

### Model: [NomeDoModel]

**Arquivo:** `prisma/schema.prisma`

**Schema:**
```prisma
model NomeDoModel {
  id          String   @id @default(cuid())
  field1      String
  field2      Int
  field3      Boolean  @default(false)
  userId      String
  user        User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt

  @@index([userId])
  @@index([field1])
}
```

**Descrição dos Campos:**
- `id`: Identificador único
- `field1`: [Descrição do campo]
- `field2`: [Descrição do campo]
- `field3`: [Descrição do campo]
- `userId`: Referência ao usuário dono do recurso
- `createdAt`: Data de criação
- `updatedAt`: Data da última atualização

**Relacionamentos:**
- Pertence a `User` (many-to-one)
- [Outros relacionamentos]

**Índices:**
- `userId`: Para filtrar recursos por usuário (performance)
- `field1`: Para buscar por [campo] (performance)

---

### Model: [OutroModel]

[Repetir estrutura acima para cada model]

---

### Models Existentes a Atualizar

#### Model: [ModelExistente]

**Campos a adicionar:**
```prisma
// Adicionar ao model existente
newField1  String?
newField2  Int?
```

**Relacionamentos a adicionar:**
```prisma
// Adicionar ao model existente
relatedItems  RelatedItem[]
```

---

## 7. Fluxo de Dados

### Diagrama de Fluxo

[Inserir link para diagrama criado em Miro, Excalidraw, Figma, ou desenhar em ASCII]

```
Usuário → Frontend (React) → API Route → Validação (Zod) → Lógica de Negócio → Prisma → PostgreSQL
                  ↑                                                                        |
                  |                                                                        |
                  +------------------------------------------------------------------------+
                                              Resposta
```

### Descrição Detalhada do Fluxo

**1. Ação do Usuário:**
- Usuário [descreve ação, ex: clica em "Criar Item"]
- Frontend mostra estado de loading

**2. Request para API:**
- Frontend faz `POST /api/items` com dados do formulário
- Headers incluem cookie de sessão (autenticação)

**3. Validação no Backend:**
- API route valida sessão (NextAuth)
- Valida dados com schema Zod
- Retorna 400 se dados inválidos

**4. Lógica de Negócio:**
- [Descrever lógica específica da feature]
- Verificar autorização se necessário
- Processar dados

**5. Persistência no Banco:**
- Usar Prisma Client para criar/atualizar registro
- Relacionamentos são conectados
- Dados salvos no PostgreSQL

**6. Resposta para Frontend:**
- API retorna status 201 com dados criados
- Frontend atualiza estado
- Mostra toast de sucesso
- Redireciona ou atualiza UI

---

## 8. Dependências Técnicas

### Bibliotecas NPM Necessárias

- [ ] `react-hook-form` - Formulários
- [ ] `zod` - Validação
- [ ] `@stripe/stripe-js` - Stripe (se aplicável)
- [ ] `react-hot-toast` ou `sonner` - Toasts
- [ ] `swr` ou `@tanstack/react-query` - Data fetching (opcional)
- [ ] [Outras dependências]

### Serviços Externos

- [ ] Stripe (pagamento) - se aplicável
- [ ] [Outros serviços]

### Variáveis de Ambiente Necessárias

```env
# Adicionar ao .env
DATABASE_URL="postgresql://..."
NEXTAUTH_SECRET="..."
NEXTAUTH_URL="http://localhost:3000"
STRIPE_SECRET_KEY="sk_test_..." # se aplicável
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY="pk_test_..." # se aplicável
```

---

## 9. Considerações de Segurança

### Validação
- [ ] Validação no frontend (UX)
- [ ] Validação no backend (segurança)
- [ ] Sanitização de inputs (prevenir XSS)

### Autenticação e Autorização
- [ ] Rotas protegidas verificam sessão
- [ ] API routes verificam autenticação
- [ ] Ownership de recursos verificado (usuário só acessa seus recursos)

### Dados Sensíveis
- [ ] Secrets em variáveis de ambiente
- [ ] Dados de pagamento não armazenados (apenas tokens)
- [ ] Erros não vazam informações sensíveis

---

## 10. Considerações de Performance

### Frontend
- [ ] Debounce em inputs de busca (se aplicável)
- [ ] Lazy loading de imagens
- [ ] Code splitting por rota (automático no Next.js)

### Backend
- [ ] Queries Prisma com `select` específico
- [ ] `include` de relacionamentos limitado
- [ ] Índices em campos filtrados frequentemente
- [ ] Cache de dados se aplicável (SWR faz automático)

### Metas de Performance
- Tempo de carregamento inicial: < 3s
- Tempo de resposta de API: < 1s
- Tempo de ações principais: < 2s

---

## 11. Casos de Teste Principais

### Casos de Sucesso

1. **Teste: [Nome do Teste]**
   - Pré-condição: [Estado inicial]
   - Passos: [Ações do usuário]
   - Resultado esperado: [O que deve acontecer]

2. **Teste: [Outro Teste]**
   - Pré-condição: [Estado inicial]
   - Passos: [Ações do usuário]
   - Resultado esperado: [O que deve acontecer]

### Casos de Erro

1. **Teste: [Cenário de Erro]**
   - Pré-condição: [Estado inicial]
   - Trigger: [O que causa o erro]
   - Resultado esperado: [Como sistema responde]

2. **Teste: [Outro Cenário de Erro]**
   - Pré-condição: [Estado inicial]
   - Trigger: [O que causa o erro]
   - Resultado esperado: [Como sistema responde]

### Edge Cases

1. **Teste: [Edge Case]**
   - Cenário: [Situação incomum]
   - Resultado esperado: [Como sistema lida]

---

## 12. Riscos Técnicos Identificados

### Risco 1: [Nome do Risco]
- **Probabilidade:** Alta | Média | Baixa
- **Impacto:** Alto | Médio | Baixo
- **Descrição:** [O que pode dar errado]
- **Mitigação:** [Como prevenir ou lidar]

### Risco 2: [Outro Risco]
- **Probabilidade:** Alta | Média | Baixa
- **Impacto:** Alto | Médio | Baixo
- **Descrição:** [O que pode dar errado]
- **Mitigação:** [Como prevenir ou lidar]

---

## 13. Estimativa de Esforço

### Por Componente

- Planejamento detalhado: 0.5 dia
- Frontend (componentes + páginas): 4-5 dias
- Backend (API routes + lógica): 4-5 dias
- Integração: 2-3 dias
- Testes e refinamento: 2-3 dias
- Documentação: 0.5 dia

**Total estimado:** 10-14 dias

### Tarefas Críticas (Caminho Crítico)

1. [Tarefa que bloqueia outras]
2. [Outra tarefa crítica]
3. [Tarefa que tudo depende]

---

## 14. Notas Adicionais

### Decisões de Design
[Documentar decisões importantes tomadas e razões]

### Alternativas Consideradas
[Listar abordagens alternativas que foram consideradas mas não escolhidas, e por quê]

### Melhorias Futuras
[Ideias de como melhorar esta funcionalidade no futuro, mas que não cabem no MVP]

### Referências
[Links úteis, documentação consultada, etc]

---

## 15. Aprovações

### Revisado por:
- [ ] [Nome] - [Função] - [Data]
- [ ] [Nome] - [Função] - [Data]

### Aprovado por:
- [ ] [Nome do Stakeholder] - [Data]

---

**Criado em:** [Data]
**Última atualização:** [Data]
**Versão:** 1.0
