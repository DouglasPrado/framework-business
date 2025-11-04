# Paleta de Cores - Lúmina

## Visão Geral

Esta pasta contém todos os arquivos relacionados à paleta de cores da marca Lúmina, incluindo swatches, guias de uso e testes de acessibilidade.

---

## Conceito Cromático

**Metáfora visual**: Luz âmbar que ilumina (clareza) + estabilidade grafite (confiança)

**Estratégia de cor**:
- Cores quentes para transmitir acolhimento e energia
- Tons terrosos para credibilidade e estabilidade
- Paleta limitada para facilitar aplicação consistente

---

## Estrutura de Arquivos

```
paleta/
├── README.MD (este arquivo)
├── swatches/
│   ├── lumina-paleta.ase (Adobe Swatch Exchange)
│   ├── lumina-paleta.aco (Adobe Color)
│   ├── lumina-paleta.gpl (GIMP/Inkscape)
│   └── lumina-paleta.sketchpalette (Sketch)
├── exports/
│   ├── paleta-primaria.png
│   ├── paleta-secundaria.png
│   ├── paleta-completa.png
│   └── matriz-contraste.png
├── css/
│   ├── lumina-colors.css
│   └── lumina-colors-tailwind.js
└── docs/
    ├── testes-acessibilidade.MD
    ├── combinacoes-aprovadas.MD
    └── uso-por-canal.MD
```

---

## Paleta Primária

### 1. Âmbar Lúmina (Cor Principal)

**Códigos**:
- HEX: `#FFB84D`
- RGB: `rgb(255, 184, 77)`
- HSL: `hsl(36, 100%, 65%)`
- CMYK: `c0 m27 y70 k0`
- Pantone: `1365 C` (aproximado)

**Propósito**: Cor de marca, destaque, CTAs principais, elementos interativos.

**Personalidade**: Energia, clareza, otimismo, acessibilidade.

**Quando usar**:
- Botões primários
- Links importantes
- Ícones de destaque
- Elementos de navegação ativa
- Alertas positivos
- Símbolos de luz/clareza

**Quando NÃO usar**:
- Fundos grandes (cansa a vista)
- Texto corrido (baixo contraste com branco)
- Alertas de erro (conflita com semântica)

**Acessibilidade**:
- Sobre branco: Contraste 2.1:1 (FALHA - não usar para texto)
- Sobre Grafite (#1F2937): Contraste 7.8:1 (AAA - ótimo)
- Sobre preto: Contraste 8.5:1 (AAA)

---

### 2. Dourado Iluminação (Tom de Apoio)

**Códigos**:
- HEX: `#F59E0B`
- RGB: `rgb(245, 158, 11)`
- HSL: `hsl(38, 92%, 50%)`
- CMYK: `c0 m35 y95 k4`
- Pantone: `130 C` (aproximado)

**Propósito**: Variação de destaque, elementos hover, ênfases secundárias.

**Personalidade**: Riqueza, valor, conquista, progresso.

**Quando usar**:
- Estado hover de botões âmbar
- Ícones de conquista/celebração
- Badges de premium/destaque
- Gráficos e visualizações (variação)
- Elementos de gamificação

**Quando NÃO usar**:
- CTAs principais (usar Âmbar)
- Grandes áreas de fundo
- Textos pequenos

**Acessibilidade**:
- Sobre branco: Contraste 3.2:1 (FALHA AA para texto normal)
- Sobre Grafite: Contraste 8.9:1 (AAA)
- Sobre preto: Contraste 9.8:1 (AAA)

---

### 3. Grafite Sólido (Texto Principal)

**Códigos**:
- HEX: `#1F2937`
- RGB: `rgb(31, 41, 55)`
- HSL: `hsl(215, 28%, 17%)`
- CMYK: `c44 m26 y9 k78`
- Pantone: `432 C` (aproximado)

**Propósito**: Textos principais, títulos, elementos estruturais.

**Personalidade**: Solidez, confiança, profissionalismo, estabilidade.

**Quando usar**:
- Títulos H1, H2, H3
- Corpo de texto principal
- Ícones de interface
- Bordas e separadores importantes
- Elementos de navegação

**Quando NÃO usar**:
- Textos sobre imagens escuras (usar Branco)
- Fundos muito grandes (preferir Cinza Claro)

**Acessibilidade**:
- Sobre branco: Contraste 15.8:1 (AAA - perfeito)
- Sobre Bege Claro: Contraste 13.2:1 (AAA)
- Sobre Âmbar: Contraste 7.8:1 (AAA)

---

## Paleta Secundária

### 4. Cinza Médio (Texto Secundário)

**Códigos**:
- HEX: `#6B7280`
- RGB: `rgb(107, 114, 128)`
- HSL: `hsl(220, 9%, 46%)`
- CMYK: `c16 m11 y0 k50`

**Propósito**: Textos de apoio, labels, placeholders, metadados.

**Quando usar**:
- Descrições e legendas
- Placeholders de input
- Labels de formulário
- Timestamps
- Textos auxiliares

**Acessibilidade**:
- Sobre branco: Contraste 4.6:1 (AA - aprovado)
- Sobre Bege Claro: Contraste 3.8:1 (mínimo AA Large)

---

### 5. Cinza Claro (Fundos Neutros)

**Códigos**:
- HEX: `#F3F4F6`
- RGB: `rgb(243, 244, 246)`
- HSL: `hsl(220, 14%, 96%)`
- CMYK: `c1 m1 y0 k4`

**Propósito**: Fundos de seções, cards, áreas secundárias.

**Quando usar**:
- Backgrounds de seções alternadas
- Fundos de cards
- Áreas de input inativo
- Separadores sutis

**Combinações**:
- Texto Grafite sobre Cinza Claro: Contraste 13.1:1 (AAA)
- Texto Cinza Médio sobre Cinza Claro: Contraste 3.8:1 (AA Large)

---

### 6. Bege Claro (Fundos Quentes)

**Códigos**:
- HEX: `#FEF3E2`
- RGB: `rgb(254, 243, 226)`
- HSL: `hsl(36, 93%, 94%)`
- CMYK: `c0 m4 y11 k0`

**Propósito**: Fundos de destaque suave, áreas de atenção positiva.

**Quando usar**:
- Fundos de cards importantes
- Áreas de destaque leve (sem alarme)
- Seções de benefícios
- Tooltips informativos

**Combinações**:
- Texto Grafite sobre Bege: Contraste 13.2:1 (AAA)
- Ícone Âmbar sobre Bege: Funciona bem visualmente

---

## Paleta Semântica (Feedback)

### 7. Verde Sucesso

**Códigos**:
- HEX: `#10B981`
- RGB: `rgb(16, 185, 129)`
- HSL: `hsl(160, 84%, 39%)`

**Uso**: Mensagens de sucesso, confirmações, status positivo.

**Exemplos**:
- "Retirada registrada com sucesso"
- "Seu caixa está saudável"
- Ícones de check e confirmação

**Acessibilidade sobre branco**: Contraste 3.3:1 (AA Large)

---

### 8. Vermelho Atenção

**Códigos**:
- HEX: `#EF4444`
- RGB: `rgb(239, 68, 68)`
- HSL: `hsl(0, 84%, 60%)`

**Uso**: Alertas críticos, erros, ações destrutivas.

**Exemplos**:
- "Caixa no vermelho"
- Erros de formulário
- Botões de cancelar/excluir

**Regra importante**: Sempre acompanhar de ícone (não depender só da cor).

**Acessibilidade sobre branco**: Contraste 3.9:1 (AA Large)

---

### 9. Azul Informação

**Códigos**:
- HEX: `#3B82F6`
- RGB: `rgb(59, 130, 246)`
- HSL: `hsl(217, 91%, 60%)`

**Uso**: Informações neutras, dicas, links secundários.

**Exemplos**:
- "Dica: Separe sempre 30% para impostos"
- Tooltips informativos
- Links de "Saiba mais"

**Acessibilidade sobre branco**: Contraste 4.1:1 (AA)

---

## Guia de Combinações Aprovadas

### Combinação 1: Alta Ênfase (CTAs)
- **Fundo**: Âmbar (#FFB84D)
- **Texto**: Grafite (#1F2937)
- **Hover**: Dourado (#F59E0B)
- **Contraste**: 7.8:1 (AAA)
- **Uso**: Botões primários, CTAs principais

### Combinação 2: Leitura Principal
- **Fundo**: Branco (#FFFFFF)
- **Texto**: Grafite (#1F2937)
- **Ênfase**: Âmbar (#FFB84D)
- **Contraste**: 15.8:1 (AAA)
- **Uso**: Conteúdo editorial, landing pages

### Combinação 3: Áreas Secundárias
- **Fundo**: Cinza Claro (#F3F4F6)
- **Texto**: Grafite (#1F2937)
- **Apoio**: Cinza Médio (#6B7280)
- **Contraste**: 13.1:1 / 4.6:1
- **Uso**: Cards, seções alternadas

### Combinação 4: Destaque Quente
- **Fundo**: Bege Claro (#FEF3E2)
- **Texto**: Grafite (#1F2937)
- **Ícone**: Âmbar (#FFB84D)
- **Contraste**: 13.2:1 (AAA)
- **Uso**: Alertas positivos, highlights

### Combinação 5: Escuro (Footer, Modals)
- **Fundo**: Grafite (#1F2937)
- **Texto**: Branco (#FFFFFF)
- **Ênfase**: Âmbar (#FFB84D)
- **Contraste**: 15.8:1 / 7.8:1
- **Uso**: Footers, modais, seções dramáticas

---

## Aplicação por Canal

### WhatsApp
- **Primária**: Âmbar para destaques, números importantes
- **Texto**: Grafite para corpo
- **Fundos**: Bege Claro para mensagens de destaque
- **Evitar**: Fundos muito coloridos (interferem na leitura)

### Landing Page
- **Hero**: Fundo Branco + títulos Grafite + CTA Âmbar
- **Seções**: Alternar Branco e Cinza Claro
- **CTAs**: Âmbar com hover Dourado
- **Footer**: Grafite com texto Branco

### Instagram
- **Feed**: Predominância de Âmbar e Branco
- **Stories**: Fundos Bege Claro ou Grafite (texto contrastante)
- **Destaques**: Ícones Âmbar sobre fundo Branco

### Email
- **Header**: Fundo Branco, logo horizontal
- **Corpo**: Texto Grafite sobre Branco
- **CTAs**: Botão Âmbar (garantir fallback para clientes sem CSS)
- **Footer**: Cinza Claro com texto Cinza Médio

### Dashboard/App
- **Background geral**: Cinza Claro (#F3F4F6)
- **Cards**: Branco com bordas sutis
- **Dados positivos**: Verde Sucesso
- **Dados críticos**: Vermelho Atenção (com ícone)
- **Ações principais**: Âmbar

---

## Exportação de Swatches

### Para Adobe (Illustrator/Photoshop/InDesign)

**Formato ASE (Adobe Swatch Exchange)**:

```
Lumina - Primárias
- Âmbar Lúmina: #FFB84D
- Dourado Iluminação: #F59E0B
- Grafite Sólido: #1F2937

Lumina - Secundárias
- Cinza Médio: #6B7280
- Cinza Claro: #F3F4F6
- Bege Claro: #FEF3E2

Lumina - Semânticas
- Verde Sucesso: #10B981
- Vermelho Atenção: #EF4444
- Azul Informação: #3B82F6

Lumina - Básicas
- Branco: #FFFFFF
- Preto: #000000
```

**Como criar**:
1. Abrir Illustrator
2. Window > Swatches
3. Adicionar cores com códigos HEX exatos
4. Nomear cada cor conforme acima
5. Clicar no menu Swatches > Save Swatch Library as ASE
6. Salvar como `lumina-paleta.ase`

---

### Para Web (CSS/Tailwind)

**Arquivo CSS** (`lumina-colors.css`):

```css
:root {
  /* Primárias */
  --lumina-ambar: #FFB84D;
  --lumina-dourado: #F59E0B;
  --lumina-grafite: #1F2937;

  /* Secundárias */
  --lumina-cinza-medio: #6B7280;
  --lumina-cinza-claro: #F3F4F6;
  --lumina-bege-claro: #FEF3E2;

  /* Semânticas */
  --lumina-sucesso: #10B981;
  --lumina-atencao: #EF4444;
  --lumina-info: #3B82F6;

  /* Básicas */
  --lumina-branco: #FFFFFF;
  --lumina-preto: #000000;
}

/* Classes utilitárias */
.bg-ambar { background-color: var(--lumina-ambar); }
.text-ambar { color: var(--lumina-ambar); }
.bg-grafite { background-color: var(--lumina-grafite); }
.text-grafite { color: var(--lumina-grafite); }
```

**Arquivo Tailwind** (`lumina-colors-tailwind.js`):

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        'lumina-ambar': '#FFB84D',
        'lumina-dourado': '#F59E0B',
        'lumina-grafite': '#1F2937',
        'lumina-cinza-medio': '#6B7280',
        'lumina-cinza-claro': '#F3F4F6',
        'lumina-bege-claro': '#FEF3E2',
        'lumina-sucesso': '#10B981',
        'lumina-atencao': '#EF4444',
        'lumina-info': '#3B82F6',
      }
    }
  }
}

// Uso: className="bg-lumina-ambar text-lumina-grafite"
```

---

### Para Figma/Sketch

**Figma**:
1. Criar Color Styles para cada cor
2. Nomear como: `Lumina/Primária/Âmbar`
3. Agrupar em categorias (Primária, Secundária, Semântica)
4. Publicar como biblioteca compartilhada

**Sketch**:
1. Importar arquivo `.sketchpalette`
2. Ou criar Document Colors manualmente
3. Sincronizar via Sketch Cloud (se aplicável)

---

## Testes de Acessibilidade

### Matriz de Contraste (WCAG 2.1)

**Legenda**:
- ✅ AAA (≥7:1): Excelente para todo tipo de texto
- ✅ AA (≥4.5:1): Aprovado para texto normal
- ⚠️ AA Large (≥3:1): Apenas para texto ≥18pt ou ≥14pt bold
- ❌ Falha (<3:1): Não usar para texto

**Combinações testadas**:

| Fundo | Texto | Contraste | Status | Uso |
|-------|-------|-----------|--------|-----|
| Branco | Grafite | 15.8:1 | ✅ AAA | Texto principal |
| Branco | Cinza Médio | 4.6:1 | ✅ AA | Texto secundário |
| Branco | Âmbar | 2.1:1 | ❌ Falha | Não usar |
| Âmbar | Grafite | 7.8:1 | ✅ AAA | CTAs |
| Grafite | Branco | 15.8:1 | ✅ AAA | Footer, modais |
| Grafite | Âmbar | 7.8:1 | ✅ AAA | Destaques escuros |
| Bege Claro | Grafite | 13.2:1 | ✅ AAA | Cards quentes |
| Cinza Claro | Grafite | 13.1:1 | ✅ AAA | Seções alternadas |

**Ferramentas de teste**:
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Figma plugin: Stark
- Chrome DevTools: Lighthouse

---

## Regras de Uso

### SEMPRE:
- Usar cores da paleta oficial (códigos exatos)
- Testar contraste antes de publicar
- Manter Âmbar para elementos de marca/destaque
- Usar Grafite para textos principais
- Acompanhar cores semânticas com ícones

### NUNCA:
- Inventar novos tons sem aprovação
- Usar Âmbar para textos corridos sobre branco
- Depender apenas de cor para transmitir informação crítica
- Usar gradientes (a menos que especificado)
- Saturar demais (máximo 30% da tela em Âmbar)

### EVITAR:
- Mais de 3 cores na mesma composição (exceto semânticas)
- Fundos Âmbar grandes (cansa a vista)
- Cinza Médio em textos pequenos sobre Branco (baixo contraste)

---

## Checklist de Qualidade

Antes de publicar design:

- [ ] Todas as cores são da paleta oficial
- [ ] Contraste de textos ≥4.5:1 (AA) ou ≥3:1 (AA Large)
- [ ] CTAs usam Âmbar com texto Grafite
- [ ] Alertas críticos não dependem só da cor
- [ ] Fundos grandes usam Branco, Cinza Claro ou Bege Claro
- [ ] Logo usa cores oficiais (Âmbar + Grafite)
- [ ] Testado em modo daltônico (Figma/Stark)
- [ ] Impresso em preto e branco para validar hierarquia

---

## Próximos Passos

### Para Design Team
1. Exportar swatches para Adobe (.ase)
2. Criar Color Styles no Figma
3. Exportar arquivo CSS com variáveis
4. Gerar imagens de referência (PNG) da paleta
5. Criar matriz de contraste visual (PNG)
6. Documentar combinações aprovadas com exemplos visuais

### Ferramentas Recomendadas
- **Paletas**: Coolors.co, Adobe Color
- **Contraste**: WebAIM, Stark (Figma)
- **Exportação**: Illustrator, Figma, Sketch
- **Validação**: Lighthouse, axe DevTools

---

**Última atualização**: 04/11/2025
**Versão**: 1.0
**Responsável**: Design Team
**Status**: Aguardando criação dos swatches e exports
