# Tipografia - Lúmina

## Visão Geral

Esta pasta contém todos os arquivos relacionados ao sistema tipográfico da marca Lúmina, incluindo fontes, hierarquia, especificações técnicas e guias de uso.

---

## Conceito Tipográfico

**Estratégia**: Tipografia humanista, moderna e altamente legível que transmite proximidade sem perder profissionalismo.

**Valores refletidos**:
- Clareza Radical (alta legibilidade)
- Proximidade Humana (formas arredondadas)
- Simplicidade Prática (sem serifas ornamentais)

---

## Estrutura de Arquivos

```
tipografia/
├── README.MD (este arquivo)
├── fonts/
│   ├── Inter/
│   │   ├── Inter-Regular.woff2
│   │   ├── Inter-Medium.woff2
│   │   ├── Inter-SemiBold.woff2
│   │   ├── Inter-Bold.woff2
│   │   ├── Inter-Regular.ttf
│   │   ├── Inter-Medium.ttf
│   │   ├── Inter-SemiBold.ttf
│   │   └── Inter-Bold.ttf
│   └── Roboto-Mono/
│       ├── RobotoMono-Regular.woff2
│       └── RobotoMono-Regular.ttf
├── specs/
│   ├── hierarquia-tipografica.png
│   ├── escala-modular.png
│   └── espacamentos.png
├── css/
│   ├── lumina-typography.css
│   └── lumina-typography-tailwind.js
└── docs/
    ├── uso-por-contexto.MD
    └── testes-legibilidade.MD
```

---

## Família Tipográfica Principal: Inter

### Por que Inter?

**Características**:
- Desenhada especificamente para telas (alta legibilidade em pequenos tamanhos)
- Formas humanistas e amigáveis
- Espaçamento otimizado para leitura
- Suporte completo a português (incluindo acentuação)
- Open source e gratuita
- Excelente renderização em todos os navegadores

**Download oficial**: https://rsms.me/inter/

**Licença**: SIL Open Font License (livre para uso comercial)

---

### Pesos Utilizados

#### 1. Inter Regular (400)
**Uso**: Corpo de texto, parágrafos, descrições longas.

**Características**:
- Peso neutro, ideal para leitura prolongada
- Boa legibilidade em tamanhos pequenos (14px+)
- Não cansa a vista

**Contextos**:
- Parágrafos de landing page
- Conteúdo de blog
- Descrições de produtos
- Corpo de email

**Tamanhos recomendados**: 14-18px (web) | 10-12pt (print)

---

#### 2. Inter Medium (500)
**Uso**: Subtítulos, labels, destaques leves.

**Características**:
- Peso intermediário que cria hierarquia sem ser dramático
- Ideal para UI elements
- Mantém legibilidade em tamanhos médios

**Contextos**:
- Labels de formulário
- Subtítulos H4
- Destaques em parágrafos
- Botões secundários
- Navegação

**Tamanhos recomendados**: 14-20px (web) | 10-14pt (print)

---

#### 3. Inter SemiBold (600)
**Uso**: Subtítulos importantes, títulos H3, CTAs secundários.

**Características**:
- Peso intermediário-alto
- Cria ênfase sem ser agressivo
- Bom para títulos de seções

**Contextos**:
- Títulos H3
- Cabeçalhos de cards
- Botões de ação
- Números importantes (R$ 2.347)
- Títulos de seção

**Tamanhos recomendados**: 18-28px (web) | 14-20pt (print)

---

#### 4. Inter Bold (700)
**Uso**: Títulos principais (H1, H2), CTAs primários, destaques críticos.

**Características**:
- Peso máximo usado na marca
- Alto impacto visual
- Mantém legibilidade mesmo em bold

**Contextos**:
- Títulos H1 e H2
- CTAs principais
- Números de destaque
- Logo (texto "Lúmina")
- Chamadas de atenção

**Tamanhos recomendados**: 24-72px (web) | 18-48pt (print)

---

## Família Tipográfica Secundária: Roboto Mono

### Por que Roboto Mono?

**Uso**: Exclusivamente para dados numéricos, códigos, valores monetários.

**Características**:
- Monoespaçada (todos os caracteres têm mesma largura)
- Facilita leitura de números alinhados
- Transmite precisão e confiabilidade
- Boa legibilidade para valores monetários

**Download**: https://fonts.google.com/specimen/Roboto+Mono

**Peso utilizado**: Regular (400)

**Contextos**:
- Valores monetários: R$ 2.347,00
- Dados de dashboard
- Tabelas numéricas
- Códigos de referência
- Timestamps precisos

**Tamanhos recomendados**: 14-20px (web)

---

## Hierarquia Tipográfica

### Desktop/Web

#### H1 - Título Principal
```css
font-family: 'Inter', sans-serif;
font-weight: 700; /* Bold */
font-size: 48px;
line-height: 1.2; /* 58px */
letter-spacing: -0.02em; /* -0.96px */
color: #1F2937; /* Grafite */
```

**Uso**: Título principal da página, hero section.

**Exemplo**: "Saiba quanto retirar todo mês, sem medo de quebrar o caixa"

---

#### H2 - Título de Seção
```css
font-family: 'Inter', sans-serif;
font-weight: 700; /* Bold */
font-size: 36px;
line-height: 1.3; /* 47px */
letter-spacing: -0.01em; /* -0.36px */
color: #1F2937; /* Grafite */
```

**Uso**: Início de seções importantes, divisores de conteúdo.

**Exemplo**: "Como Lúmina funciona"

---

#### H3 - Subtítulo de Destaque
```css
font-family: 'Inter', sans-serif;
font-weight: 600; /* SemiBold */
font-size: 24px;
line-height: 1.4; /* 34px */
letter-spacing: 0;
color: #1F2937; /* Grafite */
```

**Uso**: Títulos de cards, seções secundárias, benefícios.

**Exemplo**: "Clareza Absoluta"

---

#### H4 - Subtítulo Menor
```css
font-family: 'Inter', sans-serif;
font-weight: 500; /* Medium */
font-size: 18px;
line-height: 1.5; /* 27px */
letter-spacing: 0;
color: #1F2937; /* Grafite */
```

**Uso**: Títulos menores, FAQs, listas.

**Exemplo**: "Por que MEIs perdem dinheiro?"

---

#### Body Large - Texto de Destaque
```css
font-family: 'Inter', sans-serif;
font-weight: 400; /* Regular */
font-size: 18px;
line-height: 1.6; /* 29px */
letter-spacing: 0;
color: #1F2937; /* Grafite */
```

**Uso**: Lead paragraphs, introduções, citações.

**Exemplo**: "Lúmina é a luz que mostra seu lucro real."

---

#### Body - Texto Padrão
```css
font-family: 'Inter', sans-serif;
font-weight: 400; /* Regular */
font-size: 16px;
line-height: 1.6; /* 26px */
letter-spacing: 0;
color: #1F2937; /* Grafite */
```

**Uso**: Corpo de texto principal, parágrafos, conteúdo editorial.

**Exemplo**: Textos de blog, descrições de produto.

---

#### Body Small - Texto Secundário
```css
font-family: 'Inter', sans-serif;
font-weight: 400; /* Regular */
font-size: 14px;
line-height: 1.5; /* 21px */
letter-spacing: 0;
color: #6B7280; /* Cinza Médio */
```

**Uso**: Legendas, labels, metadados, disclaimers.

**Exemplo**: "Última atualização: há 2 horas"

---

#### Caption - Texto Mínimo
```css
font-family: 'Inter', sans-serif;
font-weight: 400; /* Regular */
font-size: 12px;
line-height: 1.4; /* 17px */
letter-spacing: 0.01em;
color: #6B7280; /* Cinza Médio */
```

**Uso**: Rodapés, disclaimers legais, créditos.

**Exemplo**: "© 2025 Lúmina. Todos os direitos reservados."

---

#### Button - Botões e CTAs
```css
font-family: 'Inter', sans-serif;
font-weight: 600; /* SemiBold */
font-size: 16px;
line-height: 1.5; /* 24px */
letter-spacing: 0.01em;
text-transform: none; /* Não usar UPPERCASE */
color: #1F2937; /* Grafite sobre Âmbar */
```

**Uso**: Todos os botões e calls-to-action.

**Exemplo**: "Quero saber meu lucro real"

---

#### Numbers - Valores Monetários
```css
font-family: 'Roboto Mono', monospace;
font-weight: 400; /* Regular */
font-size: 20px;
line-height: 1.4; /* 28px */
letter-spacing: 0;
color: #1F2937; /* Grafite */
```

**Uso**: Valores monetários, dados importantes.

**Exemplo**: "R$ 2.347,00"

---

### Mobile (≤768px)

Ajustes proporcionais para mobile:

```css
/* H1 Mobile */
font-size: 32px; /* -16px */
line-height: 1.25;

/* H2 Mobile */
font-size: 28px; /* -8px */
line-height: 1.3;

/* H3 Mobile */
font-size: 20px; /* -4px */
line-height: 1.4;

/* Body Mobile */
font-size: 16px; /* Mantém */
line-height: 1.6;

/* Body Small Mobile */
font-size: 14px; /* Mantém */
line-height: 1.5;
```

**Regra geral**: Reduzir 15-30% dos títulos para mobile, manter corpo de texto.

---

## Escala Modular

**Base**: 16px (1rem)

**Razão**: 1.25 (Major Third)

**Escala resultante**:
- 12px (0.75rem) - Caption
- 14px (0.875rem) - Small
- 16px (1rem) - Base
- 18px (1.125rem) - Large
- 20px (1.25rem) - Numbers
- 24px (1.5rem) - H3
- 28px (1.75rem) - H2 Mobile
- 32px (2rem) - H1 Mobile
- 36px (2.25rem) - H2
- 48px (3rem) - H1

**Ferramenta**: https://www.modularscale.com/?16&px&1.25

---

## Especificações de Espaçamento

### Espaçamento Vertical (Line Height)

**Regra geral**:
- Títulos grandes (H1, H2): 1.2-1.3
- Títulos médios (H3, H4): 1.3-1.5
- Corpo de texto: 1.5-1.6
- Textos pequenos: 1.4-1.5

**Por quê?**:
- Títulos não precisam de muito espaço entre linhas (são curtos)
- Corpo de texto precisa de mais espaço para facilitar leitura prolongada

---

### Letter Spacing (Tracking)

**Regra geral**:
- Títulos grandes (48px+): -0.02em (compactar levemente)
- Títulos médios (24-36px): -0.01em ou 0
- Corpo de texto (14-18px): 0 (padrão da fonte)
- Textos pequenos (12px): +0.01em (expandir levemente)

**Por quê?**:
- Títulos grandes ficam melhores compactados
- Textos pequenos precisam de mais espaço para clareza

---

### Margens Entre Elementos

```css
/* Espaçamento entre título e subtítulo */
h1 + h2 { margin-top: 16px; }

/* Espaçamento entre título e parágrafo */
h2 + p { margin-top: 16px; }
h3 + p { margin-top: 12px; }

/* Espaçamento entre parágrafos */
p + p { margin-top: 16px; }

/* Espaçamento entre seções */
section + section { margin-top: 64px; }
```

---

## Implementação Web

### CSS com @font-face

```css
/* Inter Regular */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/fonts/Inter/Inter-Regular.woff2') format('woff2'),
       url('/fonts/Inter/Inter-Regular.ttf') format('truetype');
}

/* Inter Medium */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url('/fonts/Inter/Inter-Medium.woff2') format('woff2'),
       url('/fonts/Inter/Inter-Medium.ttf') format('truetype');
}

/* Inter SemiBold */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url('/fonts/Inter/Inter-SemiBold.woff2') format('woff2'),
       url('/fonts/Inter/Inter-SemiBold.ttf') format('truetype');
}

/* Inter Bold */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('/fonts/Inter/Inter-Bold.woff2') format('woff2'),
       url('/fonts/Inter/Inter-Bold.ttf') format('truetype');
}

/* Roboto Mono */
@font-face {
  font-family: 'Roboto Mono';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/fonts/Roboto-Mono/RobotoMono-Regular.woff2') format('woff2'),
       url('/fonts/Roboto-Mono/RobotoMono-Regular.ttf') format('truetype');
}

/* Base */
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #1F2937;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

---

### CSS Utility Classes

```css
/* Hierarquia */
.text-h1 {
  font-weight: 700;
  font-size: 48px;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.text-h2 {
  font-weight: 700;
  font-size: 36px;
  line-height: 1.3;
  letter-spacing: -0.01em;
}

.text-h3 {
  font-weight: 600;
  font-size: 24px;
  line-height: 1.4;
}

.text-body {
  font-weight: 400;
  font-size: 16px;
  line-height: 1.6;
}

.text-small {
  font-weight: 400;
  font-size: 14px;
  line-height: 1.5;
  color: #6B7280;
}

.text-number {
  font-family: 'Roboto Mono', monospace;
  font-size: 20px;
  line-height: 1.4;
}

/* Mobile responsive */
@media (max-width: 768px) {
  .text-h1 { font-size: 32px; }
  .text-h2 { font-size: 28px; }
  .text-h3 { font-size: 20px; }
}
```

---

### Tailwind Config

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        'mono': ['Roboto Mono', 'monospace'],
      },
      fontSize: {
        'h1': ['48px', { lineHeight: '1.2', letterSpacing: '-0.02em' }],
        'h2': ['36px', { lineHeight: '1.3', letterSpacing: '-0.01em' }],
        'h3': ['24px', { lineHeight: '1.4' }],
        'h4': ['18px', { lineHeight: '1.5' }],
        'body-lg': ['18px', { lineHeight: '1.6' }],
        'body': ['16px', { lineHeight: '1.6' }],
        'body-sm': ['14px', { lineHeight: '1.5' }],
        'caption': ['12px', { lineHeight: '1.4' }],
        'number': ['20px', { lineHeight: '1.4' }],
      },
      fontWeight: {
        'regular': 400,
        'medium': 500,
        'semibold': 600,
        'bold': 700,
      }
    }
  }
}

// Uso: className="font-sans text-h1 font-bold"
```

---

## Aplicação por Canal

### WhatsApp
- **Texto principal**: Inter Regular 16px
- **Nomes/Destaques**: Inter SemiBold 16px
- **Valores**: Roboto Mono 18px
- **Observação**: WhatsApp não suporta fontes customizadas (usar emojis e formatação nativa: *bold*, _itálico_)

### Landing Page
- **Hero H1**: Inter Bold 48px (mobile: 32px)
- **Subtítulo**: Inter Regular 18px
- **Corpo**: Inter Regular 16px
- **CTAs**: Inter SemiBold 16px

### Instagram
- **Posts (imagem)**: Inter Bold para títulos
- **Stories (texto)**: Inter SemiBold (alta legibilidade)
- **Captions**: Inter Regular
- **Observação**: Usar tamanhos grandes (≥24pt) para legibilidade mobile

### Email
- **Assunto**: 40-50 caracteres, sem bold excessivo
- **Corpo**: Inter Regular 16px (garantir fallback: Arial, sans-serif)
- **CTAs**: Inter SemiBold 16px, botão com padding

### Dashboard/App
- **Títulos de seção**: Inter SemiBold 20px
- **Dados numéricos**: Roboto Mono 18-24px
- **Labels**: Inter Medium 14px
- **Corpo**: Inter Regular 16px

---

## Acessibilidade Tipográfica

### Tamanhos Mínimos

**Web**:
- Corpo de texto: 16px mínimo (14px aceitável para secundário)
- Títulos: 18px mínimo
- Legais/disclaimers: 12px mínimo absoluto

**Mobile**:
- Corpo de texto: 16px mínimo (não reduzir)
- Títulos: 20px mínimo
- Botões: 16px mínimo (área de toque ≥44x44px)

**Impresso**:
- Corpo de texto: 10pt mínimo
- Títulos: 14pt mínimo

---

### Contraste

**WCAG 2.1 AA**:
- Texto normal (16px): Contraste ≥4.5:1
- Texto grande (18px+ ou 14px bold): Contraste ≥3:1

**Combinações aprovadas**:
- Grafite sobre Branco: 15.8:1 (AAA) ✅
- Cinza Médio sobre Branco: 4.6:1 (AA) ✅
- Grafite sobre Âmbar: 7.8:1 (AAA) ✅

**Evitar**:
- Âmbar sobre Branco para texto (2.1:1 - falha)
- Cinza Claro sobre Branco para texto (1.2:1 - falha)

---

### Legibilidade

**Comprimento de linha**:
- Ideal: 50-75 caracteres por linha
- Máximo: 90 caracteres
- Mobile: 35-50 caracteres

**Espaçamento entre parágrafos**:
- Mínimo: 1x tamanho da fonte (16px de espaço)
- Recomendado: 1.5x (24px)

**Alinhamento**:
- Preferir esquerda (left-align) para português
- Evitar justificado (cria espaços irregulares)
- Centralizado apenas para títulos curtos

---

## Regras de Uso

### SEMPRE:
- Usar Inter como fonte padrão
- Usar Roboto Mono apenas para números/códigos
- Manter hierarquia clara (H1 > H2 > H3)
- Garantir contraste mínimo 4.5:1
- Testar em mobile antes de publicar

### NUNCA:
- Usar mais de 2 famílias tipográficas
- Usar texto em UPPERCASE para frases longas
- Comprometer legibilidade por estética
- Usar tamanhos menores que 14px para texto principal
- Ignorar line-height (deixar padrão 1.0 cria texto ilegível)

### EVITAR:
- Mais de 3 pesos diferentes na mesma página
- Parágrafos com mais de 90 caracteres de largura
- Text-align: justify (cria espaçamento irregular)
- Overlays de texto sobre imagens (sem fundo/sombra)

---

## Checklist de Qualidade

Antes de publicar:

- [ ] Todas as fontes carregam corretamente (testar em navegadores)
- [ ] Fallbacks definidos (Arial, sans-serif)
- [ ] Hierarquia clara (apenas 1 H1 por página)
- [ ] Tamanhos mínimos respeitados (16px corpo, 14px secundário)
- [ ] Contraste validado (4.5:1 mínimo)
- [ ] Line-height adequado (1.5-1.6 para corpo)
- [ ] Responsivo (mobile tem tamanhos ajustados)
- [ ] Performance (WOFF2 prioritário, font-display: swap)
- [ ] Acessibilidade (legível para daltônicos, zoom 200%)

---

## Próximos Passos

### Para Dev Team
1. Baixar fontes Inter e Roboto Mono
2. Hospedar em `/fonts/` ou usar Google Fonts
3. Implementar @font-face ou link externo
4. Criar utility classes CSS
5. Testar carregamento e performance
6. Validar em Chrome, Safari, Firefox, Edge

### Para Design Team
1. Criar guia visual de hierarquia (PNG)
2. Exportar specs de tamanhos e espaçamentos
3. Criar templates de componentes (botões, cards, forms)
4. Validar legibilidade em diferentes dispositivos

### Ferramentas Recomendadas
- **Download**: Google Fonts, rsms.me/inter
- **Teste de performance**: Google PageSpeed, WebPageTest
- **Validação**: WAVE (acessibilidade), Lighthouse
- **Otimização**: Font Squirrel WebFont Generator

---

**Última atualização**: 04/11/2025
**Versão**: 1.0
**Responsável**: Design & Dev Teams
**Status**: Aguardando download e implementação das fontes
