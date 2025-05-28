# Estrutura da Aplicação DescomplicaCV

Este documento descreve a estrutura da aplicação frontend do DescomplicaCV, uma ferramenta para conversão de currículos em PDF com template padronizado.

## Estrutura de Pastas

```
src/
├── App.vue                  # Componente raiz da aplicação
├── main.js                  # Ponto de entrada JavaScript
├── assets/                  # Arquivos estáticos (CSS, imagens)
├── components/              # Componentes reutilizáveis menores
│   ├── ui/                  # Componentes de UI genéricos
│   │   └── StatusMessage.vue  # Componente para feedback ao usuário
│   └── cv/                  # Componentes específicos para o processamento de CV
│       └── FileUploadForm.vue # Componente para upload de arquivos
├── views/                   # Componentes de página/visão
│   ├── HomeView.vue         # Página inicial
│   ├── UploadView.vue       # Página de upload de CV
│   └── AboutView.vue        # Página sobre o projeto
├── services/                # Serviços e lógica de negócios
│   └── api/                 # Chamadas de API
│       └── index.js         # Configuração e métodos de API
├── stores/                  # Gerenciamento de estado (Pinia)
│   └── cvStore.js           # Store para gerenciar estado dos CVs
├── utils/                   # Funções utilitárias
│   └── fileUtils.js         # Utilitários para manipulação de arquivos
└── router/                  # Configuração de rotas
    └── index.js             # Definição das rotas da aplicação
```

## Fluxo da Aplicação

1. O usuário acessa a página inicial (`HomeView.vue`)
2. Clica no botão para ir para a página de upload (`UploadView.vue`)
3. Faz upload do arquivo usando o componente `FileUploadForm.vue`
4. O componente chama o serviço de API (`services/api/index.js`)
5. O status e mensagens são exibidos via `StatusMessage.vue`
6. A API retorna um PDF que é baixado pelo navegador usando `fileUtils.js`

## Tecnologias Utilizadas

- Vue.js 3 (Composition API)
- Vite como build tool
- Vue Router para navegação
- Pinia para gerenciamento de estado
- Axios para chamadas de API

## Próximos Passos

1. Implementar os componentes com a lógica de negócio
2. Conectar o frontend à API backend
3. Estilos e UI/UX
