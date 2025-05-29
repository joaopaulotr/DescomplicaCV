# DescomplicaCV

Uma ferramenta para converter currículos em diferentes formatos para um formato PDF padronizado usando processamento de linguagem natural.

## Visão Geral do Projeto

Este projeto consiste em duas partes principais:
- **Backend API (Python/FastAPI)**: Processa arquivos de currículo e extrai informações relevantes usando NLP
- **Frontend (Vue.js)**: Interface para enviar currículos e visualizar os resultados processados

## Instalação e Configuração

### Backend (Python)

1. Navegue até a pasta do backend:
   ```
   cd backend-python
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - No Windows:
     ```
     .\venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

5. Instale o modelo de linguagem para português:
   ```
   python -m spacy download pt_core_news_sm
   ```

6. Execute o servidor:
   ```
   uvicorn main:app --reload
   ```

### Frontend (Vue.js)

1. Navegue até a pasta do frontend:
   ```
   cd frontend-vue
   ```

2. Instale as dependências:
   ```
   npm install
   ```

3. Execute o servidor de desenvolvimento:
   ```
   npm run dev
   ```

## Uso

1. Acesse o frontend (geralmente em http://localhost:5173)
2. Faça o upload de um currículo (PDF, DOCX ou TXT)
3. Aguarde o processamento
4. Visualize as informações extraídas

## Tecnologias Utilizadas

- **Backend**: Python, FastAPI, spaCy, PyMuPDF, python-docx
- **Frontend**: Vue.js 3, Vite, Axios

## Estrutura do Projeto

```
DescomplicaCV/
├── backend-python/       # Backend da aplicação em Python
│   ├── main.py           # Arquivo principal com endpoints FastAPI
│   └── requirements.txt  # Dependências do Python
│
└── frontend-vue/         # Frontend da aplicação em Vue.js
    ├── public/           # Arquivos públicos do Vue
    ├── src/              # Código-fonte do Vue
    │   ├── assets/       # Recursos estáticos (CSS, imagens)
    │   ├── components/   # Componentes Vue reutilizáveis
    │   ├── router/       # Configuração de rotas
    │   ├── services/     # Serviços para API
    │   ├── stores/       # Store Pinia/Vuex
    │   ├── utils/        # Utilitários
    │   └── views/        # Páginas/visualizações Vue
    └── package.json      # Dependências do Node.js
```

## Contribuições

Contribuições são sempre bem-vindas! Se você deseja contribuir com este projeto, por favor siga estas etapas:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Envie para a branch (`git push origin feature/nova-funcionalidade`)
5. Crie um novo Pull Request

Para mais detalhes, veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md).

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.