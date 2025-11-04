# Iconografia - Lúmina

## Visão Geral

Esta pasta contém todos os arquivos relacionados ao sistema de ícones da marca Lúmina, incluindo biblioteca de ícones, especificações de criação e guias de uso.

---

## Conceito de Iconografia

**Estilo**: Outline (contorno), minimalista, amigável.

**Valores refletidos**:
- Clareza Radical (formas simples e diretas)
- Simplicidade Prática (sem ornamentos desnecessários)
- Proximidade Humana (cantos arredondados, não geométrico rígido)

**Metáfora visual**: Assim como Lúmina ilumina o caminho financeiro, os ícones devem iluminar a interface.

---

## Estrutura de Arquivos

```
iconografia/
├── README.MD (este arquivo)
├── library/
│   ├── svg/
│   │   ├── financeiro/
│   │   │   ├── money-light.svg
│   │   │   ├── wallet-two.svg
│   │   │   ├── cash-flow.svg
│   │   │   ├── calculator.svg
│   │   │   └── ...
│   │   ├── acoes/
│   │   │   ├── check-circle.svg
│   │   │   ├── alert-triangle.svg
│   │   │   ├── info-circle.svg
│   │   │   └── ...
│   │   ├── navegacao/
│   │   │   ├── home.svg
│   │   │   ├── menu.svg
│   │   │   ├── search.svg
│   │   │   └── ...
│   │   └── comunicacao/
│   │       ├── whatsapp.svg
│   │       ├── email.svg
│   │       ├── bell.svg
│   │       └── ...
│   └── png/
│       └── (versões rasterizadas para email/fallback)
├── specs/
│   ├── grid-sistema.png
│   ├── anatomia-icone.png
│   └── tamanhos-contextos.png
└── docs/
    ├── lista-completa-icones.MD
    └── diretrizes-criacao.MD
```

---

## Especificações Técnicas

### Tamanho Base
- **Grid**: 24x24px (base padrão)
- **Área útil**: 20x20px (margem de 2px em cada lado)
- **Stroke (contorno)**: 2px (1.5px para detalhes internos)

**Por quê 24px?**
- Padrão da indústria (Material Design, Heroicons)
- Fácil escalabilidade (12px, 24px, 48px, 96px)
- Alinhamento perfeito em grids de 8px

---

### Estilo Visual

#### Tipo: Outline (Contorno)
- Apenas contornos, sem preenchimento sólido
- Exceção: Elementos de destaque podem ter fill pontual

**Vantagens**:
- Leveza visual
- Clareza em pequenos tamanhos
- Alinhamento com estética moderna e clean
- Flexibilidade de cor

---

#### Cantos: Arredondados
- **Raio**: 2px nos cantos externos
- **Raio interno**: 1px (quando aplicável)

**Por quê arredondado?**
- Transmite proximidade e humanização
- Mais amigável que ícones geométricos rígidos
- Alinha com personalidade "Sábia Cuidadora"

---

#### Peso do Traço
- **Padrão**: 2px (stroke-width)
- **Detalhes internos**: 1.5px (quando necessário)
- **Nunca menos que**: 1px (perde legibilidade)

---

#### Estilo de Linhas
- **Line cap**: Round (pontas arredondadas)
- **Line join**: Round (junções arredondadas)
- **Consistência**: Todas as linhas seguem mesmo padrão

---

### Cores

#### Cor Padrão (Interface)
- **HEX**: #1F2937 (Grafite)
- **Uso**: Ícones de navegação, interface geral

#### Cor de Destaque
- **HEX**: #FFB84D (Âmbar)
- **Uso**: Ícones ativos, destaques, estados selecionados

#### Cor Secundária
- **HEX**: #6B7280 (Cinza Médio)
- **Uso**: Ícones inativos, estados desabilitados

#### Cores Semânticas
- **Sucesso**: #10B981 (Verde)
- **Atenção**: #EF4444 (Vermelho)
- **Informação**: #3B82F6 (Azul)

**Regra**: Ícones devem funcionar em versão monocromática (não depender de cor para significado).

---

## Tamanhos e Contextos

### 16x16px - Inline/Compacto
**Uso**: Dentro de textos, badges pequenos, ícones de status.

**Ajustes**:
- Simplificar detalhes internos
- Aumentar peso do traço para 2.5px (melhor legibilidade)
- Testar visibilidade antes de usar

**Exemplo**: Ícone ao lado de link "Saiba mais →"

---

### 20x20px - UI Compacto
**Uso**: Botões pequenos, inputs, navegação secundária.

**Ajustes**:
- Manter detalhes essenciais
- Stroke 2px funciona bem

**Exemplo**: Ícone em botão de filtro, ícone de campo de busca.

---

### 24x24px - Padrão (Base)
**Uso**: Maioria dos casos - navegação, cards, listas, CTAs.

**Ajustes**:
- Tamanho ideal (sem ajustes necessários)
- Usar design base criado neste tamanho

**Exemplo**: Menu de navegação, ícones de features, ícones de cards.

---

### 32x32px - Destaque Médio
**Uso**: Ícones de features, benefits, seções importantes.

**Ajustes**:
- Pode adicionar detalhes extras
- Stroke 2px mantém proporção

**Exemplo**: Ícones de benefícios na landing page.

---

### 48x48px - Grande Destaque
**Uso**: Hero sections, ilustrações, estados vazios (empty states).

**Ajustes**:
- Adicionar detalhes visuais
- Stroke 2-3px (testar qual fica melhor)

**Exemplo**: Ícone principal na hero section, ilustração de erro 404.

---

### 64x64px+ - Ilustrativo
**Uso**: Ilustrações grandes, onboarding, páginas de status.

**Ajustes**:
- Pode adicionar elementos gráficos extras
- Considerar adicionar cor (fill) em elementos pontuais

**Exemplo**: Ilustração de sucesso após cadastro, tela de carregamento.

---

## Biblioteca de Ícones Recomendada: Heroicons

### Por quê Heroicons?

**Vantagens**:
- Outline style (perfeito para Lúmina)
- Open source (grátis)
- Alta qualidade
- Consistência visual
- 24x24px base (nosso padrão)
- Cantos arredondados
- Atualizada e mantida (by Tailwind Labs)

**Download**: https://heroicons.com/

**Licença**: MIT (livre para uso comercial)

---

### Categorias de Ícones Necessários

#### 1. Financeiro (Prioritário)
Ícones relacionados ao core business de Lúmina.

**Ícones necessários**:
- `banknotes` - Dinheiro/notas
- `currency-dollar` - Cifrão/valor monetário
- `wallet` - Carteira
- `calculator` - Calculadora
- `chart-bar` - Gráficos/relatórios
- `arrow-trending-up` - Crescimento
- `arrow-trending-down` - Queda
- `credit-card` - Cartão/pagamento
- `receipt-percent` - Nota fiscal/porcentagem
- `scale` - Balança/equilíbrio (duas caixas)

**Customização**: Considerar criar ícone único de "duas caixas separadas" (conceito central de Lúmina).

---

#### 2. Ações e Estados
Ícones de interface para ações do usuário.

**Ícones necessários**:
- `check-circle` - Sucesso/confirmação
- `x-circle` - Erro/cancelar
- `exclamation-triangle` - Alerta/atenção
- `information-circle` - Informação/ajuda
- `light-bulb` - Ideia/dica (relacionado a Lúmina!)
- `bell` - Notificação
- `eye` - Visualizar
- `eye-slash` - Ocultar
- `lock-closed` - Bloqueado/privado
- `lock-open` - Desbloqueado

---

#### 3. Navegação
Ícones de menu e navegação de interface.

**Ícones necessários**:
- `home` - Início
- `chart-pie` - Dashboard
- `document-text` - Documentos/relatórios
- `cog-6-tooth` - Configurações
- `user-circle` - Perfil
- `question-mark-circle` - Ajuda/FAQ
- `arrow-left` - Voltar
- `arrow-right` - Avançar
- `chevron-down` - Dropdown aberto
- `chevron-up` - Dropdown fechado
- `bars-3` - Menu hamburger (mobile)

---

#### 4. Comunicação
Ícones para canais e interações.

**Ícones necessários**:
- `chat-bubble-left-right` - Chat/conversa
- `envelope` - Email
- `phone` - Telefone
- `device-phone-mobile` - WhatsApp/celular
- `paper-airplane` - Enviar mensagem
- `share` - Compartilhar
- `link` - Link/conexão
- `at-symbol` - Menção/@

**Social**:
- WhatsApp (buscar logo oficial)
- Instagram (buscar logo oficial)
- LinkedIn (buscar logo oficial)

---

#### 5. Temporais
Ícones relacionados a tempo e frequência.

**Ícones necessários**:
- `calendar` - Calendário
- `clock` - Horário
- `calendar-days` - Múltiplos dias
- `arrow-path` - Atualização/recorrência

---

#### 6. Dados e Documentos

**Ícones necessários**:
- `document-chart-bar` - Relatório
- `document-arrow-down` - Download
- `document-plus` - Novo documento
- `clipboard-document-check` - Checklist
- `folder` - Pasta
- `archive-box` - Arquivar

---

## Ícones Customizados (Criar Internamente)

Ícones que não existem em bibliotecas e precisam ser criados:

### 1. Duas Caixas Separadas
**Conceito**: Representação visual do core value de Lúmina (separação pessoal/empresarial).

**Design**:
- Dois retângulos lado a lado
- Linha divisória central sutil
- Luz/brilho no topo (opcional)
- Stroke 2px, cantos arredondados 2px

**Tamanho**: 24x24px base

**Uso**: Feature principal, explicações de como funciona, onboarding.

---

### 2. Luz de Lanterna
**Conceito**: Variação do símbolo de Lúmina para uso em ícones.

**Design**:
- Ponto central de luz
- Feixes divergindo (versão simplificada do logo)
- Outline style

**Uso**: Ícone de "insight", "clareza", "alerta positivo".

---

### 3. Retirada Ideal
**Conceito**: Dinheiro saindo da carteira de forma segura.

**Design**:
- Carteira base
- Notas saindo com seta para cima
- Checkmark pequeno (indicando segurança)

**Uso**: Feature "retirada ideal", CTAs de calcular valor.

---

## Diretrizes de Criação

### Criando Novos Ícones (Passo a Passo)

#### 1. Setup no Figma/Illustrator
- Criar artboard 24x24px
- Ativar grid de 1px
- Criar guias em 2px de margem (área útil 20x20px)
- Configurar stroke: 2px, round cap, round join

#### 2. Sketch do Conceito
- Desenhar forma básica em 5-10 minutos
- Focar na clareza do símbolo
- Testar legibilidade em 24px (zoom out)

#### 3. Refinar Geometria
- Alinhar ao grid de 1px
- Arredondar cantos (2px)
- Simplificar formas complexas
- Garantir simetria (quando aplicável)

#### 4. Testar em Contexto
- Reduzir para 16px (ainda legível?)
- Ampliar para 48px (proporções ok?)
- Testar em fundo claro e escuro
- Testar com cores semânticas

#### 5. Exportar
- **SVG otimizado**: Expandir strokes, simplificar paths
- **PNG transparente**: 24px, 48px, 96px
- Nomear descritivamente: `nome-do-icone.svg`

---

### Checklist de Qualidade para Ícones

Antes de aprovar um ícone:

- [ ] Baseado em grid 24x24px
- [ ] Área útil 20x20px respeitada (2px margem)
- [ ] Stroke 2px (ou 1.5px em detalhes)
- [ ] Cantos arredondados (2px)
- [ ] Line cap e join = round
- [ ] Funciona em 16px (legível)
- [ ] Funciona em 48px (proporcional)
- [ ] Funciona em preto e branco
- [ ] Funciona sobre fundo claro E escuro
- [ ] SVG otimizado (sem elementos desnecessários)
- [ ] Nomeado descritivamente

---

## Aplicação por Canal

### WhatsApp
**Limitação**: WhatsApp não renderiza ícones customizados em mensagens de texto.

**Solução**:
- Usar emojis nativos quando possível
- Criar imagens com texto + ícone quando crítico
- Evitar depender de ícones para clareza

**Emojis recomendados**:
- 💡 (Lâmpada) - Representa Lúmina
- 💰 (Dinheiro)
- 📊 (Gráfico)
- ✅ (Check)
- ⚠️ (Alerta)
- 📅 (Calendário)

---

### Landing Page
**Uso**: Ícones de features, benefits, navegação.

**Especificações**:
- Features/benefits: 32-48px
- Navegação: 24px
- Footer: 20px
- Cor: Âmbar (#FFB84D) para destaques, Grafite para demais

**Exemplo**:
```html
<div class="feature">
  <img src="/icons/light-bulb.svg" alt="Clareza" width="48" height="48">
  <h3>Clareza Absoluta</h3>
  <p>Saiba exatamente quanto retirar</p>
</div>
```

---

### Dashboard/App
**Uso**: Navegação, ações, status, dados.

**Especificações**:
- Navegação principal: 24px
- Ações (botões): 20px
- Status inline: 16px
- Gráficos/dados: 32px

**Estados**:
- Ativo: Âmbar (#FFB84D)
- Inativo: Cinza Médio (#6B7280)
- Hover: Dourado (#F59E0B)

---

### Instagram
**Uso**: Stories, posts, destaques.

**Especificações**:
- Stories: 48-64px (alta visibilidade)
- Posts: 32-48px
- Destaques (highlights): 64px

**Dica**: Criar versão com fundo circular/quadrado colorido para melhor destaque visual.

---

### Email
**Uso**: CTAs, listas, separadores visuais.

**Especificações**:
- Tamanho: 24-32px
- Formato: PNG (melhor compatibilidade que SVG)
- Alt text: Sempre incluir (clientes bloqueiam imagens)

**Exemplo**:
```html
<img src="check-circle.png" alt="Confirmado" width="24" height="24" style="vertical-align: middle;">
```

---

## Otimização de SVG

### Antes de Usar em Produção

**Ferramentas**:
- SVGOMG: https://jakearchibald.github.io/svgomg/
- Figma export otimizado
- Illustrator "Export for Screens"

**Otimizações essenciais**:
- Remover metadados
- Remover comentários
- Simplificar paths
- Arredondar decimais (2 casas)
- Remover atributos desnecessários (width/height pode ficar em CSS)

**Exemplo de SVG otimizado**:
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="12" cy="12" r="10"/>
  <path d="M9 12l2 2 4-4"/>
</svg>
```

**Vantagens**:
- Arquivo menor (carregamento rápido)
- Escalável sem perda de qualidade
- Cor controlável via CSS (`stroke="currentColor"`)

---

## Implementação Web

### SVG Inline

```html
<!-- Vantagem: Controle total via CSS -->
<svg class="icon icon-check" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
  <circle cx="12" cy="12" r="10"/>
  <path d="M9 12l2 2 4-4"/>
</svg>

<style>
.icon {
  stroke: #1F2937; /* Grafite */
  transition: stroke 0.2s;
}
.icon:hover {
  stroke: #FFB84D; /* Âmbar */
}
</style>
```

---

### SVG como Imagem

```html
<!-- Vantagem: Cache do navegador -->
<img src="/icons/check-circle.svg" alt="Confirmado" width="24" height="24">
```

---

### Sprite SVG (Otimização Avançada)

```html
<!-- sprite.svg -->
<svg xmlns="http://www.w3.org/2000/svg">
  <symbol id="icon-check" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="10"/>
    <path d="M9 12l2 2 4-4"/>
  </symbol>
  <symbol id="icon-alert" viewBox="0 0 24 24">
    <path d="M12 2L2 20h20L12 2z"/>
  </symbol>
</svg>

<!-- Uso -->
<svg width="24" height="24">
  <use href="/sprite.svg#icon-check"/>
</svg>
```

**Vantagem**: Um único arquivo, múltiplos ícones, cache eficiente.

---

## Regras de Uso

### SEMPRE:
- Usar ícones da biblioteca oficial (Heroicons ou customizados aprovados)
- Manter proporções (não distorcer)
- Incluir alt text descritivo
- Testar legibilidade em 16px mínimo
- Usar cores da paleta oficial

### NUNCA:
- Misturar estilos (outline + solid na mesma interface)
- Usar ícones menores que 16px
- Depender apenas de cor para significado
- Rotacionar ícones de forma aleatória
- Adicionar sombras ou efeitos 3D

### EVITAR:
- Mais de 1 ícone ilustrativo grande por seção
- Ícones decorativos sem propósito funcional
- Excesso de detalhes (simplicidade é chave)

---

## Acessibilidade

### Alt Text

**Ícones decorativos** (não transmitem informação essencial):
```html
<img src="decorative-icon.svg" alt="" role="presentation">
```

**Ícones funcionais** (transmitem significado):
```html
<img src="check-circle.svg" alt="Confirmado">
<img src="alert-triangle.svg" alt="Atenção: Saldo baixo">
```

**Botões com ícone**:
```html
<button aria-label="Fechar menu">
  <svg>...</svg>
</button>
```

---

### Cor e Contraste

**Regra**: Não depender apenas de cor para transmitir informação.

**Exemplo errado**:
- Ícone vermelho = erro (daltônicos não veem)

**Exemplo correto**:
- Ícone de "X" vermelho = erro (forma + cor)
- Label de texto "Erro: Campo obrigatório"

---

## Próximos Passos

### Para Design Team
1. Baixar Heroicons (biblioteca completa)
2. Selecionar ícones da lista de necessários
3. Criar ícones customizados (Duas Caixas, Luz, Retirada)
4. Organizar em pastas por categoria
5. Exportar SVG otimizados
6. Criar PNG para email (24px, 48px)
7. Documentar lista completa com previews

### Para Dev Team
1. Hospedar ícones em `/icons/` ou CDN
2. Implementar sistema de carregamento (sprite ou individual)
3. Criar componente React/Vue reutilizável (se aplicável)
4. Testar performance de carregamento
5. Validar acessibilidade (alt text, aria-labels)

### Ferramentas Recomendadas
- **Biblioteca**: Heroicons.com
- **Edição**: Figma, Illustrator
- **Otimização**: SVGOMG, Figma plugin "SVG Export"
- **Sprite**: svg-sprite (npm)
- **Preview**: iconmonstr.com, icomoon.io

---

**Última atualização**: 04/11/2025
**Versão**: 1.0
**Responsável**: Design Team
**Status**: Aguardando download de Heroicons e criação de ícones customizados
