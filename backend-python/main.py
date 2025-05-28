"""
DescomplicaCV - API Backend em Python com FastAPI

Esta API fornece endpoints para:
1. Receber arquivos de currículo em diferentes formatos (PDF, DOCX, TXT)
2. Processar estes arquivos e extrair informações relevantes
3. Gerar um novo currículo em formato PDF padronizado

Desenvolvido como parte do projeto DescomplicaCV.

Requisitos:
- Python 3.7+
- FastAPI
- Uvicorn (servidor ASGI)
- PyMuPDF (manipulação de PDFs)
- python-docx (manipulação de DOCXs)

Instalação:
pip install fastapi uvicorn python-multipart pymupdf python-docx
"""

import os
import io
from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
import fitz  # PyMuPDF - Biblioteca para manipulação de PDFs
from docx import Document  # python-docx - Biblioteca para manipulação de arquivos DOCX


# Criando a instância do FastAPI com metadados
app = FastAPI(
    title="API DescomplicaCV", 
    version="0.1.0",
    description="API para conversão de currículos para o formato PDF padronizado"
)

# Configuração do CORS (Cross-Origin Resource Sharing)
# Permite que o frontend Vue.js (rodando em outra porta) acesse esta API
origins = [
    "http://localhost:5173",  # Endereço comum do Vue com Vite em desenvolvimento
    "http://localhost:3000",  # Porta alternativa comum para desenvolvimento
    # Adicione aqui o endereço do seu frontend em produção quando souber
]

# Adicionando o middleware CORS à aplicação
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos HTTP
)


@app.get("/")
def home():
    """
    Endpoint raiz da API.
    
    Returns:
        dict: Mensagem de boas-vindas e informações básicas sobre a API
    """
    return {"message": "Bem-vindo à API DescomplicaCV!"}


@app.post("/convert-cv")
async def convert_cv(file: UploadFile = File(...)):
    """
    Endpoint para receber e processar arquivos de currículo em diferentes formatos.
    
    Aceita arquivos PDF, DOCX e TXT, processando-os de acordo com o tipo.
    Não salva nada em disco, apenas analisa o conteúdo e retorna informações.
    
    Parameters:
        file (UploadFile): O arquivo de currículo enviado pelo cliente
        
    Returns:
        dict: Mensagem indicando o sucesso do processamento e informações do arquivo
        FileResponse: No futuro, um PDF convertido
        
    Raises:
        HTTPException: Em caso de erro no processamento do arquivo
    """
    filename = file.filename
    content = await file.read()
    
    # Determina a extensão do arquivo
    ext = os.path.splitext(filename)[1].lower()
    
    # Processa baseado no tipo de arquivo
    if ext == ".pdf":
        try:
            # Abre o PDF usando PyMuPDF (fitz) para validação
            # stream=content carrega o PDF a partir do conteúdo em memória
            pdf = fitz.open(stream=content, filetype="pdf")
            num_pages = len(pdf)
            
            # Em uma versão futura, aqui ficaria a lógica para converter o PDF
            # Mas por enquanto, apenas extraímos algumas informações
            metadata = pdf.metadata
            
            return {
                "filename": filename,
                "format": "pdf",
                "pages": num_pages,
                "title": metadata.get("title", "Sem título"),
                "author": metadata.get("author", "Autor desconhecido"),
                "message": "PDF analisado com sucesso!"
            }
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Arquivo PDF inválido ou corrompido: {str(e)}")
    
    elif ext == ".docx":
        try:
            # Cria um objeto BytesIO para trabalhar com o arquivo em memória
            docx_bytes = io.BytesIO(content)
            
            # Carrega o documento DOCX na memória
            doc = Document(docx_bytes)
            
            # Extrai informações do documento
            paragraphs_count = len(doc.paragraphs)
            text_sample = doc.paragraphs[0].text if doc.paragraphs else ""
            
            return {
                "filename": filename,
                "format": "docx",
                "paragraphs": paragraphs_count,
                "text_sample": text_sample[:100] + "..." if len(text_sample) > 100 else text_sample,
                "message": "DOCX analisado com sucesso!"
            }
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao processar DOCX: {str(e)}")
    
    elif ext == ".txt":
        try:
            # Converte o conteúdo binário para texto com codificação UTF-8
            texto = content.decode("utf-8")
            lines = texto.count("\n") + 1
            
            return {
                "filename": filename,
                "format": "txt",
                "lines": lines,
                "text_sample": texto[:100] + "..." if len(texto) > 100 else texto,
                "message": "Arquivo TXT analisado com sucesso!"
            }
            
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Erro ao processar TXT: {str(e)}")
    
    else:
        # Se o formato não for suportado, retorna erro 415 (Unsupported Media Type)
        raise HTTPException(
            status_code=415, 
            detail=f"Tipo de arquivo {ext} não suportado. Por favor, envie um arquivo PDF, DOCX ou TXT."
        )


# Rota temporária para testes - será substituída pela implementação real no futuro
@app.post("/return-pdf")
async def return_pdf(file: UploadFile = File(...)):
    """
    Endpoint temporário para testes que recebe um arquivo e simplesmente retorna um PDF de exemplo.
    
    No futuro, este endpoint será substituído pelo endpoint real de conversão
    que gerará um PDF formatado a partir do conteúdo do currículo.
    
    Parameters:
        file (UploadFile): O arquivo de currículo enviado pelo cliente
        
    Returns:
        FileResponse: Um arquivo PDF fixo para testes
    """
    # Este é apenas um endpoint de mockup que retorna um PDF de exemplo
    # Na implementação real, você usaria os dados do currículo para gerar um PDF personalizado
    
    # Caminho para um PDF de exemplo - substitua pelo caminho correto em sua máquina
    # ou implemente uma geração dinâmica de PDF com uma biblioteca como ReportLab
    sample_pdf_path = "exemplo.pdf"
    
    # Verificar se o arquivo existe, caso contrário, retornar erro
    if not os.path.exists(sample_pdf_path):
        # Código para criar um PDF simples com ReportLab ou outra biblioteca poderia ir aqui
        raise HTTPException(
            status_code=501, 
            detail="Funcionalidade em desenvolvimento. Nenhum PDF de exemplo disponível."
        )
    
    # Retorna o PDF como uma resposta de arquivo
    return FileResponse(
        path=sample_pdf_path, 
        filename="curriculo_convertido.pdf", 
        media_type="application/pdf"
    )


# Para iniciar o servidor em desenvolvimento:
# cd backend-python
# uvicorn main:app --reload

# Se estiver dentro da pasta venv:
# cd venv
# uvicorn main:app --reload
