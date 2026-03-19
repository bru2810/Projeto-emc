# Documentação do Projeto - Espaço Mulher Campesina (EMC)

## Visão Geral

O projeto é um site institucional para a clínica de estética **Espaço Mulher Campesina**, localizada em Osasco - SP. O site foi desenvolvido usando Flask (Python) como backend e HTML/CSS/JavaScript para o frontend. Esta documentação detalha a estrutura e funcionalidades da página inicial (`index.html`) e seus estilos (`inicio.css`).

---

## 📄 Arquivo: `index.html`

### Estrutura Geral

A página inicial (`index.html`) é um template Jinja2 que estende `base.html` e contém todas as seções principais do site.

#### Localização
```
espaco-mulher-app/templates/index.html
```

### Estrutura do Documento

#### 1. **Head Section** (Linhas 1-53)

**Meta Tags SEO:**
- Título otimizado: "Espaço Mulher Campesina | Dra. Tânia Silva | Clínica de Estética em Osasco"
- Descrição focada em tratamentos estéticos
- Keywords relevantes para SEO local
- Open Graph tags para compartilhamento em redes sociais
- Twitter Cards configurados

**Recursos Externos:**
- CSS: `/static/css/inicio.css`
- Favicon: `/static/img/favicon.png`

**Estilos Inline:**
- Animação de corações (`heart-animation`) - efeito visual na página inicial

#### 2. **Script de Animação de Corações** (Linhas 59-102)

**Funcionalidade:**
- Cria animação de corações flutuantes na página inicial
- Executa apenas na rota `/` ou `/home`
- Cria 15 corações inicialmente com delay escalonado
- Continua criando corações por 3 segundos
- Remove elementos após 5 segundos

**Características:**
- Posição aleatória horizontal
- Tamanho aleatório (10px a 35px)
- Animação de subida com rotação
- Fade out automático

#### 3. **Seções da Página**

##### 3.1. **Hero Section - EMC Identidade** (Linhas 105-156)

**Classe CSS:** `.emc-identidade`

**Estrutura:**
- Container principal: `.emc-moldura` (grid de 2 colunas)
- Conteúdo textual: `.emc-conteudo`
- Imagem desktop: `.emc-imagem-container`
- Imagem mobile: `.emc-imagem-mobile`

**Elementos:**
- Subtítulo: "Bem-vinda ao"
- Título principal: "Espaço Mulher" e "Campesina"
- Texto de chamada com destaques em `<strong>`
- Dois botões de ação:
  - Botão primário: "Agendar consulta" (link para `/whatsapp`)
  - Botão secundário: "Conheça nossa essência" (link para `/sobre`)

**Imagens:**
- Desktop: `static/img/capa_outubrorosa2025.jpg`
- Mobile: mesma imagem, mas com layout diferente

##### 3.2. **Seção de Promoções** (Linhas 175-185)

**Classe CSS:** `.faixas_promo`

**Estrutura:**
- Container flexbox vertical
- 3 banners promocionais com links para WhatsApp
- Cada banner tem mensagem pré-formatada para WhatsApp

**Promoções:**
1. Drenagem Linfática (`NovaPromocao01.png`)
2. Limpeza de Pele (`NovaPromocao02.png`)
3. Limpeza de Pele (`NovaPromocao03.png`)

**Funcionalidade:**
- Links diretos para WhatsApp com mensagens pré-formatadas
- Número: `5511945717295`

##### 3.3. **Seção Sobre a Clínica** (Linhas 188-242)

**Classe CSS:** `.about-clinica`

**Estrutura:**
- Texto sobre a clínica (`.about-text`)
- Carrossel de resultados (`.carrossel_section`)

**Carrossel de Resultados:**
- 8 slides de imagens de resultados
- Navegação via radio buttons
- Imagens:
  1. `emb_facial_esp.jpg`
  2. `emb_facial_esp2.jpg`
  3. `olheiras_esp2.jpg`
  4. `preenc_labial_esp.JPG`
  5. `botox2_esp.png`
  6. `result_detox7.JPG`
  7. `result_corporal.jpg`
  8. `result_C30(1).JPG`

**Funcionalidade:**
- Transição automática entre slides
- Controle via CSS (radio buttons ocultos)

##### 3.4. **Seção de Especialidades** (Linhas 245-295)

**Classe CSS:** `.inicio-procedimentos`

**Estrutura:**
- Título com decoração (círculo + linha)
- Grid de 6 especialidades
- Botão "Ver mais +"

**Especialidades:**
1. **Corporal** - `corporal_banheira.jpg`
2. **Tratamentos** - `rosto.png`
3. **Procedimentos Faciais** - `bot0x1.JPG`
4. **Epilação** - `epilacao.jpg`
5. **Secagem de vasos** - `varises.jpg`
6. **SPA** - `spa2.png`

**Funcionalidade:**
- Grid responsivo (1 coluna mobile, 3 colunas desktop)
- Efeito hover com escala
- Filtro grayscale em desktop que remove no hover

##### 3.5. **Seção de Depoimentos** (Linhas 297-505)

**Classe CSS:** `.reviews-section`

**Estrutura:**
- Cabeçalho com título e avaliação de 5 estrelas
- Carrossel de depoimentos (`.reviews-carousel`)
- Controles de navegação (anterior/próximo)

**Depoimentos:**
- 12 depoimentos de clientes
- Cada card contém:
  - Ícone de aspas
  - Nome do autor
  - Texto do depoimento
  - Ícone de coração

**Funcionalidade:**
- Navegação via JavaScript (arquivo `comentarios.js`)
- Transição suave entre cards
- Scrollbar customizada para textos longos

##### 3.6. **Seção Dra. Tânia Silva** (Linhas 507-600)

**Classe CSS:** `.dr-tania-section`

**Estrutura:**
- Container de perfil (`.profile-container`)
- Grid de 2 colunas:
  - Coluna visual: foto, nome, CRBM, redes sociais
  - Coluna de conteúdo: introdução + cards de qualificação

**Cards de Qualificação:**
1. **Formação Acadêmica**
   - Biomedicina
   - Estética e Cosméticos

2. **Pós-Graduações**
   - Estética Avançada
   - Harmonização Facial e Corporal
   - Procedimentos Injetáveis Estéticos
   - Nutrição Estética
   - Saúde da Mulher
   - Emagrecimento e Obesidade

3. **Especializações**
   - Plasma Rico em Plaquetas (PRP)
   - CrioliPólise
   - Bioquímica
   - Fisiologia Humana
   - Psicanálise Clínica
   - Hidrolipoclasia não aspirativa
   - Mestre em Reiki

4. **Abordagens**
   - Medicina Preventiva
   - Cuidado Centrado na Paciente
   - Estética Integrativa e Natural
   - Promoção da Autoestima Feminina
   - Atenção ao Bem-estar Emocional

**Redes Sociais:**
- Instagram: `https://www.instagram.com/tania_espacomulher/`
- WhatsApp: `https://wa.me//5511945717295`

##### 3.7. **Seção Blog** (Linhas 602-648)

**Classe CSS:** `.section-blog`

**Estrutura:**
- Título com decoração
- Container de cards (`.container-blog`)
- 3 artigos em destaque
- Botão "Ver mais"

**Artigos:**
1. **Celulite: Impactos na Autoestima Feminina** (`/artigo?id=1`)
2. **Preenchimento Íntimo com PRP** (`/artigo?id=2`)
3. **10 Dicas para Manter a Pele Hidratada** (`/artigo?id=3`)

**Estrutura dos Cards:**
- Imagem de capa
- Categoria
- Título
- Resumo

##### 3.8. **Seção Localização** (Linhas 650-672)

**Classe CSS:** `.location`

**Estrutura:**
- Endereço com ícone
- Informações de horário
- Mapa interativo

**Informações:**
- Endereço: R. Nico Branco, 64 Vila Campesina, Osasco - SP
- Horário: Ter - Sáb, 9h - 18h
- Mapa: Folium (via JavaScript)

#### 4. **Scripts Externos** (Linhas 677-680)

**Arquivos JavaScript:**
1. `/static/js/inicio.js` - Funcionalidades da página inicial
2. `/static/js/index.js` - Scripts gerais
3. `/static/js/comentarios.js` - Controle do carrossel de depoimentos
4. `/static/js/popup.js` - Funcionalidade de popups (comentado no HTML)

---

## 🎨 Arquivo: `inicio.css`

### Estrutura Geral

O arquivo CSS contém todos os estilos para a página inicial, organizados por seções e componentes.

#### Localização
```
espaco-mulher-app/static/css/inicio.css
```

### Paleta de Cores

#### Cores Principais
- **Verde Primário:** `#96AC60` / `#576D49`
- **Verde Claro:** `#83ac6a` / `#B7CD7F`
- **Rosa:** `#F28482` / `#D1898E` / `#BC6066` / `#FFCDD4`
- **Terroso:** `#D4A373` / `#FAEDCD`
- **Marrom:** `#5E503F` / `#31470B`

#### Variáveis CSS (Root)
```css
--primary-color: #96AC60
--primary-dark: #31470B
--text-color: #555
--light-gray: #f9f9f9
--white: #ffffff
--shadow: 0 5px 15px rgba(0, 0, 0, 0.05)
--transition: all 0.3s ease
```

### Seções CSS

#### 1. **Estilos Legados** (Linhas 1-101)

**Classes:**
- `.mentoria` - Seção de mentoria (não utilizada na versão atual)
- `.barrasInicioCima` / `.barrasInicioBaixo` - Barras decorativas

#### 2. **Seção Sobre a Clínica** (Linhas 103-118)

**Classes:**
- `.about-text h1` - Título da seção (cor verde)
- `.about-text button` - Botão estilizado com borda verde

#### 3. **Seção de Promoções** (Linhas 120-137)

**Classes:**
- `.faixas_promo` - Container flexbox vertical
- `.faixa_img` - Imagens dos banners promocionais

**Características:**
- Layout vertical em mobile
- Bordas arredondadas (20px)
- Espaçamento entre banners

#### 4. **Seção de Especialidades** (Linhas 140-207)

**Classes:**
- `.inicio-procedimentos` - Container principal com fundo verde claro
- `.grid-procedimentos` - Grid responsivo
- `.grid-procedimentos .item` - Itens do grid

**Características:**
- Fundo: `#b7cd7f67` (verde claro transparente)
- Bordas inferiores arredondadas (100px)
- Grid: 1 coluna (mobile) → 3 colunas (desktop)
- Efeito hover: escala 1.05
- Filtro grayscale em desktop (remove no hover)

#### 5. **Seção de Depoimentos** (Linhas 509-822)

**Classes Principais:**
- `.reviews-section` - Container principal
- `.review-card` - Cards individuais de depoimento
- `.carousel-controls` - Controles de navegação

**Características:**
- Cards com sombra e borda superior colorida
- Scrollbar customizada para textos longos
- Transições suaves (0.6s)
- Botões circulares de navegação
- Responsivo: 70% largura desktop, 90% mobile

**Animações:**
- `fadeIn` - Entrada suave dos cards

#### 6. **Seção EMC Identidade (Hero)** (Linhas 1288-1716)

**Variáveis CSS:**
```css
--cor-terra-1: #D4A373
--cor-terra-2: #FAEDCD
--cor-rosa: #F28482
--cor-texto: #5E503F
--cor-fundo: #FFF9F2
```

**Classes Principais:**
- `.emc-identidade` - Container principal
- `.emc-moldura` - Grid de 2 colunas (conteúdo + imagem)
- `.emc-conteudo` - Área textual
- `.emc-imagem-container` - Imagem desktop
- `.emc-imagem-mobile` - Imagem mobile (oculta em desktop)

**Características:**
- Layout grid responsivo
- Imagem com sombra destacada (15px offset)
- Botões com gradiente e hover effects
- Animações de entrada (fadeInUp)

**Responsividade:**
- Mobile: layout vertical, fundo com gradiente verde
- Desktop: layout horizontal (2 colunas)

#### 7. **Seção Dra. Tânia Silva** (Linhas 1720-1990)

**Classes Principais:**
- `.dr-tania-section` - Container com gradiente de fundo
- `.profile-grid` - Grid de 2 colunas (foto + conteúdo)
- `.qualification-cards` - Grid de cards de qualificação
- `.q-card` - Cards individuais

**Características:**
- Foto com efeito 3D (perspective + rotateY)
- Cards com hover effect (elevação + sombra)
- Barra lateral que cresce no hover
- Ícones de redes sociais com hover

**Responsividade:**
- Desktop: 2 colunas (foto + conteúdo)
- Tablet/Mobile: 1 coluna (stack vertical)

#### 8. **Seção Blog** (Linhas 1072-1160)

**Classes:**
- `.section-blog` - Container principal
- `.container-blog` - Grid de cards
- `.card` - Cards individuais de artigo

**Características:**
- Grid flexível (3 colunas desktop, 2 tablet, 1 mobile)
- Cards com hover (escala 1.05)
- Categoria destacada com fundo rosa claro
- Botão com borda arredondada

#### 9. **Seção Localização** (Linhas 286-339)

**Classes:**
- `.location` - Grid de 2 colunas (endereço + mapa)
- `.endereco` - Informações de endereço
- `#mapa` - Container do mapa

**Características:**
- Mapa com sombra destacada (20px offset)
- Efeito hover que inverte a sombra
- Ícones grandes para horário e dias

#### 10. **Carrossel de Resultados** (Linhas 862-1006)

**Classes:**
- `.carrossel_section` - Container do carrossel
- `.carousel_article` - Container dos slides
- `.slide-proc` - Slides individuais

**Características:**
- Largura: 80vw (mobile) → 45vw (desktop)
- Transição suave (2s)
- Bordas arredondadas assimétricas
- Navegação via CSS (radio buttons)

**Lógica de Navegação:**
- Cada radio button move o container em -12.5% (8 slides)
- `#radio1-result` → 0%
- `#radio2-result` → -12.5%
- `#radio3-result` → -25%
- ... até `#radio8-result` → -87.5%

#### 11. **Popup** (Linhas 1192-1287)

**Classes:**
- `.popup` - Overlay fixo
- `.popup-content` - Conteúdo do popup
- `.popup-image` - Imagem do popup

**Características:**
- Overlay escuro (rgba(0, 0, 0, 0.6))
- Animação de entrada (fadeInUp)
- Botão de fechar
- Responsivo (largura 90% em mobile)

**Nota:** Popup está comentado no HTML (linhas 159-173)

### Media Queries

#### Breakpoints Principais

1. **Mobile First (< 600px)**
   - Grid de especialidades: 1 coluna
   - Layout vertical para todas as seções
   - Fontes reduzidas

2. **Tablet (600px - 768px)**
   - Grid de especialidades: 3 colunas
   - Layout híbrido
   - Ajustes de espaçamento

3. **Desktop (768px - 992px)**
   - Layout completo de 2 colunas
   - Grid de blog: 3 colunas
   - Efeitos hover ativos

4. **Large Desktop (> 992px)**
   - Espaçamentos aumentados
   - Fontes maiores
   - Cards de qualificação: grid flexível

5. **Extra Large (> 1200px)**
   - Container máximo: 1230px
   - Otimizações de espaçamento

### Animações CSS

#### 1. **fadeInUp**
```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```
**Uso:** Entrada de elementos (títulos, cards, popups)

#### 2. **fadeIn**
```css
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
```
**Uso:** Aparição suave de elementos

#### 3. **rise** (inline no HTML)
```css
@keyframes rise {
    to {
        transform: translateY(-100vh) rotate(360deg);
    }
}
```
**Uso:** Animação de corações flutuantes

#### 4. **fadeOut** (inline no HTML)
```css
@keyframes fadeOut {
    to {
        opacity: 0;
        visibility: hidden;
    }
}
```
**Uso:** Desaparecimento de corações

### Efeitos Hover

#### Principais Efeitos

1. **Cards de Especialidades:**
   - Escala: `transform: scale(1.05)`
   - Remoção de grayscale
   - Mudança de sombra

2. **Botões:**
   - Elevação: `translateY(-3px)`
   - Sombra aumentada
   - Mudança de cor de borda

3. **Cards de Qualificação:**
   - Elevação: `translateY(-5px)`
   - Barra lateral cresce
   - Sombra aumentada

4. **Imagens:**
   - Zoom suave: `scale(1.03)`
   - Transição de 1s

5. **Mapa:**
   - Inversão de sombra (direção oposta)

### Acessibilidade

#### Recursos Implementados

1. **Alt Text:** Todas as imagens possuem texto alternativo
2. **ARIA Labels:** Botões de navegação com `aria-label`
3. **Semântica HTML:** Uso de `<section>`, `<article>`, `<h1-h3>`
4. **Contraste:** Cores com bom contraste para leitura
5. **Navegação por Teclado:** Elementos interativos acessíveis

### Performance

#### Otimizações

1. **Lazy Loading:** Imagens com `loading="lazy"`
2. **CSS Variables:** Uso de variáveis para cores reutilizáveis
3. **Transitions:** Uso de `will-change` em animações
4. **Scrollbar Customizada:** Estilização leve para textos longos

### Dependências Externas

#### Bibliotecas/Fontes

1. **Bootstrap Icons:** Usado para ícones (`.bi-*`)
   - Estrelas, setas, corações, calendário, etc.

2. **Fontes:**
   - Poppins (para seção EMC Identidade)
   - System fonts (fallback)

3. **Folium:** Biblioteca Python para mapas (via JavaScript)

---

## 🔧 Funcionalidades JavaScript

Para documentação completa e detalhada de todos os arquivos JavaScript, consulte a seção **[📜 Documentação JavaScript](#-documentação-javascript)** abaixo.

**Resumo das Funcionalidades:**
1. **Carrossel de Resultados** - Alternância automática de slides (inicio.js)
2. **Mapa Interativo** - Localização da clínica com Leaflet (inicio.js)
3. **Animações de Entrada** - Fade-in em scroll usando Intersection Observer (index.js)
4. **Carrossel de Depoimentos** - Navegação manual de reviews (comentarios.js)
5. **Animação de Corações** - Efeito visual na página inicial (inline no HTML)
6. **Header Dinâmico** - Mudança de estilo no scroll (header.js)
7. **Menu Mobile** - Toggle de ícone hambúrguer (header.js)

---

## 📱 Responsividade

### Estratégia Mobile-First

O CSS foi desenvolvido com abordagem mobile-first, com media queries para telas maiores.

#### Breakpoints

| Dispositivo | Largura | Características |
|------------|---------|----------------|
| Mobile | < 600px | Layout vertical, fontes reduzidas |
| Tablet | 600px - 768px | Layout híbrido, grid 2-3 colunas |
| Desktop | 768px - 992px | Layout completo, 2 colunas |
| Large | 992px - 1200px | Espaçamentos aumentados |
| XL | > 1200px | Container máximo, otimizações |

### Adaptações por Seção

#### Hero Section (EMC Identidade)
- **Mobile:** Layout vertical, fundo com gradiente verde
- **Desktop:** Grid 2 colunas, imagem lateral

#### Especialidades
- **Mobile:** 1 coluna
- **Desktop:** 3 colunas

#### Depoimentos
- **Mobile:** Cards 90% largura
- **Desktop:** Cards 70% largura

#### Dra. Tânia
- **Mobile:** Stack vertical
- **Desktop:** Grid 2 colunas

#### Blog
- **Mobile:** 1 coluna (90% largura)
- **Tablet:** 2 colunas (45% cada)
- **Desktop:** 3 colunas (30% cada)

---

## 🎯 SEO e Meta Tags

### Otimizações Implementadas

1. **Meta Tags Completas:**
   - Title otimizado
   - Description focada
   - Keywords relevantes
   - Open Graph tags
   - Twitter Cards

2. **Estrutura Semântica:**
   - Uso correto de headings (h1, h2, h3)
   - Sections e articles
   - Alt text em todas as imagens

3. **Performance:**
   - Lazy loading de imagens
   - CSS otimizado
   - Scripts no final do body

---

## 🐛 Observações e Melhorias Futuras

### Problemas Identificados

1. **Tag `</head>` Duplicada:**
   - Linha 52 e 53 têm `</head>` duplicado
   - **Solução:** Remover uma das tags

2. **Popup Comentado:**
   - Popup de eventos está comentado (linhas 159-173)
   - **Decisão:** Manter comentado ou remover completamente

3. **CSS Legado:**
   - Classes `.mentoria` não são utilizadas
   - **Sugestão:** Remover código não utilizado

4. **Media Query Duplicada:**
   - Media query para `.emc-moldura` duplicada (linhas 1543 e 1552)
   - **Solução:** Consolidar em uma única query

### Melhorias Sugeridas

1. **Performance:**
   - Minificar CSS em produção
   - Otimizar imagens (WebP)
   - Implementar lazy loading mais agressivo

2. **Acessibilidade:**
   - Adicionar skip links
   - Melhorar contraste em alguns elementos
   - Adicionar focus states mais visíveis

3. **Manutenibilidade:**
   - Organizar CSS em módulos
   - Documentar classes customizadas
   - Padronizar nomenclatura

4. **Funcionalidades:**
   - Implementar autoplay no carrossel de resultados
   - Adicionar indicadores de slide
   - Melhorar feedback visual em interações

---

## 📜 Documentação JavaScript

### Visão Geral

Os arquivos JavaScript são responsáveis pela interatividade e funcionalidades dinâmicas da página inicial. Todos os scripts são carregados no final do `body` para garantir melhor performance.

### Arquivos JavaScript Utilizados em `index.html`

#### 1. **`inicio.js`** - Funcionalidades da Página Inicial

**Localização:** `/static/js/inicio.js`  
**Tamanho:** 1.2KB (39 linhas)

##### Funcionalidades

###### 1.1. **Carrossel de Resultados Automático** (Linhas 1-10)

**Descrição:**  
Controla o carrossel de resultados da clínica, alternando automaticamente entre os 8 slides.

**Código:**
```javascript
document.addEventListener("DOMContentLoaded", function () {
  let count = 1;
  const total = 8;

  setInterval(function () {
    document.getElementById("radio" + count + "-result").checked = true;
    count++;
    if (count > total) count = 1;
  }, 5000); // troca a imagem a cada 5 segundos
});
```

**Funcionalidade:**
- Aguarda o carregamento do DOM
- Inicializa contador em 1
- Define total de slides: 8
- Alterna automaticamente a cada 5 segundos
- Retorna ao primeiro slide após o último

**Elementos HTML Relacionados:**
- Radio buttons: `#radio1-result` até `#radio8-result`
- Slides: `.slide-proc`

**Dependências:**
- CSS: `.carousel_article` e `.slide-proc`
- HTML: Radio buttons ocultos no carrossel

---

###### 1.2. **Mapa Interativo (Leaflet)** (Linhas 12-39)

**Descrição:**  
Inicializa e configura o mapa interativo da clínica usando a biblioteca Leaflet.

**Código:**
```javascript
var mapa = L.map("mapa", {
    center: [-23.540853, -46.771263],
    crs: L.CRS.EPSG3857,
    zoom: 15,
    zoomControl: true,
    preferCanvas: false,
});

var title_layer = L.tileLayer(
    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
    { 
        "attribution": "&copy; <a href=\"https://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors", 
        "detectRetina": false, 
        "maxNativeZoom": 19, 
        "maxZoom": 19, 
        "minZoom": 0, 
        "noWrap": false, 
        "opacity": 1, 
        "subdomains": "abc", 
        "tms": false 
    }
);

title_layer.addTo(mapa);

var marker = L.marker([-23.540853, -46.771263], {}).addTo(mapa);

var popup = L.popup({ "maxWidth": "100%" });
var html = $(`<div id="html" style="width: 100.0%; height: 100.0%;">Espaço Mulher Campesina - Estética Avançada</div>`)[0];
popup.setContent(html);
marker.bindPopup(popup);
```

**Configurações:**
- **Coordenadas:** -23.540853, -46.771263 (Osasco, SP)
- **Zoom:** 15 (nível de zoom inicial)
- **Tile Layer:** OpenStreetMap
- **Marker:** Marcador na localização da clínica
- **Popup:** Informação da clínica ao clicar no marcador

**Elementos HTML Relacionados:**
- Container: `#mapa` (div com classe `.folium-map`)

**Dependências:**
- Biblioteca Leaflet (L)
- jQuery ($) - para criação do popup HTML

**Nota:**  
O código parece ter sido gerado pelo Folium (biblioteca Python) e exportado para JavaScript. O uso de jQuery pode ser substituído por JavaScript vanilla.

---

#### 2. **`index.js`** - Animações de Scroll e Intersection Observer

**Localização:** `/static/js/index.js`  
**Tamanho:** 443B (18 linhas)

##### Funcionalidades

###### 2.1. **Animações de Entrada (Intersection Observer)** (Linhas 1-16)

**Descrição:**  
Implementa animações de fade-in para elementos quando entram na viewport usando Intersection Observer API.

**Código:**
```javascript
const fadein = document.querySelectorAll('.hidden');

const myObserver = new IntersectionObserver((response) => {
    console.log(response);
    response.forEach((intersect) => {
        if (intersect.isIntersecting) {
            intersect.target.classList.add('show')
        } else {
            intersect.target.classList.remove('show')
        }
    })
})

fadein.forEach((element) => {
    myObserver.observe(element)
})
```

**Funcionalidade:**
- Seleciona todos os elementos com classe `.hidden`
- Cria um Intersection Observer para detectar quando elementos entram na viewport
- Adiciona classe `.show` quando elemento está visível
- Remove classe `.show` quando elemento sai da viewport

**Elementos HTML Relacionados:**
- Elementos com classe `.hidden` (ex: `.item.hidden` na seção de especialidades)

**CSS Relacionado:**
- Classe `.hidden` - elemento inicialmente oculto
- Classe `.show` - deve ser definida no CSS para animação de entrada

**Observações:**
- `console.log(response)` pode ser removido em produção
- A remoção da classe `.show` quando o elemento sai da viewport pode causar animação repetida ao scrollar para cima

**Melhorias Sugeridas:**
- Remover `console.log` em produção
- Adicionar opções ao Intersection Observer (threshold, rootMargin)
- Considerar manter a classe `.show` após primeira visualização

---

#### 3. **`comentarios.js`** - Carrossel de Depoimentos

**Localização:** `/static/js/comentarios.js`  
**Tamanho:** 836B (27 linhas)

##### Funcionalidades

###### 3.1. **Navegação do Carrossel de Depoimentos** (Linhas 1-26)

**Descrição:**  
Controla a navegação manual do carrossel de depoimentos com botões anterior/próximo.

**Código:**
```javascript
document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.review-card');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');

    let currentIndex = 0;

    function updateCarousel() {
        cards.forEach((card, i) => {
            card.classList.remove('active');
        });
        cards[currentIndex].classList.add('active');
    }

    prevBtn.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + cards.length) % cards.length;
        updateCarousel();
    });

    nextBtn.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % cards.length;
        updateCarousel();
    });

    updateCarousel(); // inicia com o primeiro review
});
```

**Funcionalidade:**
- Aguarda o carregamento do DOM
- Seleciona todos os cards de depoimento (`.review-card`)
- Seleciona botões de navegação (`.carousel-prev` e `.carousel-next`)
- Mantém índice do card atual
- Função `updateCarousel()`:
  - Remove classe `.active` de todos os cards
  - Adiciona classe `.active` ao card atual
- Botão anterior: decrementa índice (com loop circular)
- Botão próximo: incrementa índice (com loop circular)
- Inicializa mostrando o primeiro card

**Elementos HTML Relacionados:**
- Cards: `.review-card` (12 cards no total)
- Botão anterior: `.carousel-prev`
- Botão próximo: `.carousel-next`

**CSS Relacionado:**
- `.review-card` - estilização dos cards
- `.review-card.active` - card visível (display: block, opacity: 1)

**Características:**
- Navegação circular (último → primeiro, primeiro → último)
- Transições suaves via CSS (0.6s ease)
- Loop infinito em ambas as direções

**Melhorias Sugeridas:**
- Adicionar autoplay opcional
- Adicionar indicadores de slide (dots)
- Adicionar suporte a teclado (setas esquerda/direita)
- Adicionar touch/swipe para mobile

---

#### 4. **`popup.js`** - Funcionalidade de Popup

**Localização:** `/static/js/popup.js`  
**Tamanho:** 337B (12 linhas)

##### Funcionalidades

###### 4.1. **Abertura e Fechamento de Popup** (Linhas 1-11)

**Descrição:**  
Controla a exibição de popup de eventos/promoções na página inicial.

**Código:**
```javascript
window.onload = function() {
    const popup = document.getElementById("event-popup");
    popup.style.visibility = "visible";
    popup.style.opacity = "1";
};

function closePopup() {
    const popup = document.getElementById("event-popup");
    popup.style.opacity = "1";
    popup.style.visibility = "hidden";
}
```

**Funcionalidade:**
- **Abertura:** Ao carregar a página (`window.onload`), torna o popup visível
- **Fechamento:** Função `closePopup()` oculta o popup

**Elementos HTML Relacionados:**
- Popup: `#event-popup` (atualmente comentado no HTML)

**CSS Relacionado:**
- `.popup` - overlay fixo com fundo escuro
- `.popup-content` - conteúdo do popup

**Observações:**
- O popup está comentado no HTML (linhas 159-173)
- Bug: Na função `closePopup()`, `opacity` está sendo definido como "1" quando deveria ser "0"
- A função `closePopup()` é chamada via `onclick` no HTML

**Correção Sugerida:**
```javascript
function closePopup() {
    const popup = document.getElementById("event-popup");
    popup.style.opacity = "0";  // Corrigido: era "1"
    popup.style.visibility = "hidden";
}
```

**Status:**  
⚠️ **Não está ativo** - Popup comentado no HTML

---

#### 5. **`header.js`** - Funcionalidades do Header

**Localização:** `/static/js/header.js`  
**Tamanho:** 857B (32 linhas)

##### Funcionalidades

###### 5.1. **Mudança de Background no Scroll** (Linhas 2-10)

**Descrição:**  
Adiciona classe ao body quando o usuário scrolla mais de 50px, permitindo mudança de estilo do header.

**Código:**
```javascript
window.addEventListener('scroll', () => {
    var scrollPosition = window.scrollY;

    if (scrollPosition > 50) {
        document.body.classList.add('scrolled');
    } else {
        document.body.classList.remove('scrolled');
    }
});
```

**Funcionalidade:**
- Monitora evento de scroll
- Adiciona classe `.scrolled` ao body quando scroll > 50px
- Remove classe quando scroll <= 50px

**CSS Relacionado:**
- `.scrolled` - classe adicionada ao body
- Pode ser usado para estilizar header: `.header.scrolled` ou `body.scrolled .header`

**Uso Típico:**
- Mudar cor de fundo do header
- Adicionar sombra ao header
- Mudar cor do texto do header

---

###### 5.2. **Toggle do Menu Mobile** (Linhas 13-28)

**Descrição:**  
Altera o ícone do menu hambúrguer entre aberto e fechado.

**Código:**
```javascript
document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('menu-btn');
    const menuIcon = document.querySelector('.icon-hamburguer');

    // Ícones personalizados
    const hamburguerIcon = '/static/img/logo_menu.png';
    const closeIcon = '/static/img/logo_menu_close.png';

    menuBtn.addEventListener('change', () => {
        if (menuBtn.checked) {
            menuIcon.src = closeIcon;
        } else {
            menuIcon.src = hamburguerIcon;
        }
    });
});
```

**Funcionalidade:**
- Aguarda o carregamento do DOM
- Seleciona checkbox do menu (`#menu-btn`)
- Seleciona ícone do menu (`.icon-hamburguer`)
- Define caminhos dos ícones (hambúrguer e fechado)
- Monitora mudança no checkbox
- Se marcado: mostra ícone de fechar
- Se desmarcado: mostra ícone de hambúrguer

**Elementos HTML Relacionados:**
- Checkbox: `#menu-btn` (input type="checkbox")
- Ícone: `.icon-hamburguer` (img)

**Imagens:**
- Hambúrguer: `/static/img/logo_menu.png`
- Fechar: `/static/img/logo_menu_close.png`

**Características:**
- Usa checkbox para controlar estado (padrão para menus mobile)
- Alterna entre dois ícones diferentes
- Funciona com CSS que controla visibilidade do menu

---

### Scripts Inline no HTML

#### Animação de Corações (Linhas 59-102 do `index.html`)

**Descrição:**  
Cria animação de corações flutuantes na página inicial.

**Código:**
```javascript
if (window.location.pathname === '/' || window.location.pathname === '/home') {
    function createHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart-animation');
        heart.innerHTML = '💗';
        
        // Posição aleatória
        const left = Math.random() * window.innerWidth;
        heart.style.left = `${left}px`;
        
        // Tamanho aleatório
        const size = Math.random() * 25 + 10;
        heart.style.fontSize = `${size}px`;
        
        document.body.appendChild(heart);
        
        // Remover após a animação terminar
        setTimeout(() => {
            heart.remove();
        }, 5000);
    }
    
    // Criar vários corações no início
    function startHeartAnimation() {
        // Primeira explosão de corações
        for (let i = 0; i < 15; i++) {
            setTimeout(createHeart, i * 100);
        }
        
        // Continuar criando por 3 segundos
        const heartInterval = setInterval(createHeart, 150);
        
        // Parar após 3 segundos
        setTimeout(() => {
            clearInterval(heartInterval);
        }, 3000);
    }
    
    // Iniciar quando a página carregar
    window.addEventListener('load', startHeartAnimation);
}
```

**Funcionalidade:**
- Executa apenas na página inicial (`/` ou `/home`)
- Cria 15 corações inicialmente com delay escalonado (100ms entre cada)
- Continua criando corações a cada 150ms por 3 segundos
- Cada coração:
  - Posição horizontal aleatória
  - Tamanho aleatório (10px a 35px)
  - Animação CSS de subida com rotação
  - Removido após 5 segundos

**CSS Relacionado:**
- `.heart-animation` - definido inline no HTML (linhas 25-51)
- Animações: `rise` e `fadeOut`

**Características:**
- Efeito visual de boas-vindas
- Não interfere na usabilidade
- Performance otimizada (remove elementos automaticamente)

---

### Dependências JavaScript

#### Bibliotecas Externas

1. **Leaflet** (para mapas)
   - **Versão:** Não especificada
   - **Uso:** Mapa interativo da clínica
   - **CDN:** Não visível no código (provavelmente carregado via base.html)

2. **jQuery** (para manipulação DOM)
   - **Versão:** Não especificada
   - **Uso:** Criação de popup HTML no mapa
   - **Nota:** Pode ser substituído por JavaScript vanilla

#### APIs Nativas Utilizadas

1. **Intersection Observer API**
   - Uso: Animações de entrada em scroll
   - Suporte: Navegadores modernos

2. **DOM API**
   - Uso: Manipulação de elementos HTML
   - Métodos: `querySelector`, `addEventListener`, `classList`

---

### Ordem de Carregamento dos Scripts

Os scripts são carregados no final do `body` na seguinte ordem:

```html
<script src="/static/js/inicio.js"></script>
<script src="/static/js/index.js"></script>
<script src="/static/js/comentarios.js"></script>
<script src="/static/js/popup.js"></script>
```

**Ordem de Execução:**
1. `inicio.js` - Carrossel e mapa (aguarda DOMContentLoaded)
2. `index.js` - Intersection Observer (executa imediatamente)
3. `comentarios.js` - Carrossel de depoimentos (aguarda DOMContentLoaded)
4. `popup.js` - Popup (aguarda window.onload)

**Observação:**  
A ordem de carregamento não é crítica, pois todos usam event listeners apropriados.

---

### Problemas Identificados e Correções

#### 1. **Bug no `popup.js`**
**Problema:** Na função `closePopup()`, `opacity` está sendo definido como "1" quando deveria ser "0".

**Correção:**
```javascript
function closePopup() {
    const popup = document.getElementById("event-popup");
    popup.style.opacity = "0";  // Corrigido
    popup.style.visibility = "hidden";
}
```

#### 2. **Console.log em Produção**
**Problema:** `index.js` contém `console.log(response)` que deve ser removido em produção.

**Correção:**
```javascript
const myObserver = new IntersectionObserver((response) => {
    // console.log(response); // Removido
    response.forEach((intersect) => {
        // ...
    })
})
```

#### 3. **Uso de jQuery no `inicio.js`**
**Problema:** Uso de jQuery apenas para criar elemento HTML simples.

**Correção (JavaScript Vanilla):**
```javascript
var html = document.createElement('div');
html.id = "html";
html.style.width = "100.0%";
html.style.height = "100.0%";
html.textContent = "Espaço Mulher Campesina - Estética Avançada";
popup.setContent(html);
```

#### 4. **Remoção de Classe `.show` no Scroll**
**Problema:** `index.js` remove a classe `.show` quando elemento sai da viewport, causando animação repetida.

**Solução Sugerida:**
```javascript
const myObserver = new IntersectionObserver((response) => {
    response.forEach((intersect) => {
        if (intersect.isIntersecting) {
            intersect.target.classList.add('show');
            // Opcional: parar de observar após primeira visualização
            // myObserver.unobserve(intersect.target);
        }
        // Remover else para manter animação após primeira visualização
    })
}, {
    threshold: 0.1  // Adicionar opções
});
```

---

### Melhorias Sugeridas

#### 1. **Performance**
- Lazy load do mapa (carregar apenas quando visível)
- Debounce no scroll event do header
- Throttle no Intersection Observer

#### 2. **Acessibilidade**
- Adicionar suporte a teclado no carrossel (setas)
- Adicionar ARIA labels nos botões
- Melhorar foco visual

#### 3. **Funcionalidades**
- Autoplay no carrossel de depoimentos (opcional)
- Indicadores de slide (dots)
- Touch/swipe para mobile
- Pausar autoplay ao interagir

#### 4. **Código**
- Modularizar funções
- Adicionar comentários JSDoc
- Remover dependência de jQuery
- Usar const/let consistentemente
- Adicionar tratamento de erros

---

## 📚 Referências e Dependências

### Tecnologias Utilizadas

- **HTML5** - Estrutura semântica
- **CSS3** - Estilização e animações
- **JavaScript (ES6+)** - Interatividade
- **Jinja2** - Template engine (Flask)
- **Bootstrap Icons** - Ícones
- **Folium** - Mapas interativos

### Estrutura de Arquivos

```
espaco-mulher-app/
├── templates/
│   └── index.html          # Página inicial
├── static/
│   ├── css/
│   │   └── inicio.css      # Estilos da página inicial
│   ├── js/
│   │   ├── inicio.js        # Scripts da página inicial (carrossel + mapa)
│   │   ├── index.js         # Animações de scroll (Intersection Observer)
│   │   ├── comentarios.js   # Carrossel de depoimentos
│   │   ├── popup.js         # Funcionalidade de popups (não ativo)
│   │   └── header.js       # Funcionalidades do header (scroll + menu mobile)
│   └── img/                 # Imagens e assets
```

---

## 📝 Changelog

### Versão Atual
- Hero section com design moderno (EMC Identidade)
- Carrossel de resultados com 8 slides
- Seção de depoimentos com 12 reviews
- Perfil completo da Dra. Tânia Silva
- Seção de blog com 3 artigos em destaque
- Localização com mapa interativo
- Animações de corações na página inicial
- Design totalmente responsivo

---

## 👥 Contato e Suporte

Para questões sobre o código ou documentação, consulte:
- Repositório do projeto
- Documentação do Flask
- Documentação do Bootstrap Icons

---

**Última atualização:** 2025
**Versão da documentação:** 1.0

