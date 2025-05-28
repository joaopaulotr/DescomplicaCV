# Como usar o DescomplicaCV

Este documento explica como este projeto foi estruturado para funcionar como uma aplicação de página única (SPA).

## Estrutura do Projeto

O projeto foi simplificado para ter apenas uma única página que contém toda a funcionalidade:

```
src/
├── App.vue                # Container principal da aplicação
├── views/
│   └── HomeView.vue       # Única página com todo o conversor de CV
├── router/
│   └── index.js           # Configuração simplificada de rota
├── assets/                # Arquivos CSS e outros recursos
└── services/api/          # Para futura conexão com o backend
```

## Funcionamento

1. O usuário acessa a página inicial que contém:
   - Um formulário para upload do currículo
   - Botão para converter
   - Feedback visual do processo

2. Todo o processo ocorre na mesma página:
   - Upload do arquivo
   - Processamento
   - Download automático do PDF convertido

## Configuração Técnica

O router foi configurado para:
- Renderizar apenas o `HomeView.vue` na rota principal (/)
- Redirecionar qualquer outra rota para a página principal

O componente `App.vue` foi simplificado para:
- Um cabeçalho simples com o título da aplicação
- A área de conteúdo principal que renderiza o HomeView
- Um rodapé com informações básicas
