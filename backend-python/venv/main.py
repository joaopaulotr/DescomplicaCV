from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importe para CORS

app = FastAPI(title="API DescomplicaCV", version="0.1.0")

# Configuração do CORS (Cross-Origin Resource Sharing)
# Permite que seu frontend Vue (rodando em outra porta) acesse esta API
origins = [
    "http://localhost:5173",  # Endereço comum do Vue com Vite em desenvolvimento
    "http://localhost:8080",  # Endereço comum do Vue CLI mais antigo
    # Adicione o endereço do seu frontend em produção aqui, se souber
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos HTTP
)

@app.get("/")
async def health_check():
    return {"status": "API DescomplicaCV está funcionando!", "message": "Bem-vindo(a)!"}

# Aqui você adicionará seus endpoints para upload, parsing e geração de PDF
# Exemplo de endpoint que você vai construir:
# from fastapi import File, UploadFile, HTTPException
# @app.post("/api/gerar-curriculo-pdf/")
# async def gerar_curriculo_endpoint(file: UploadFile = File(...)):
#     # Sua lógica de processamento aqui
#     # raise HTTPException(status_code=501, detail="Endpoint ainda não implementado.")
#     return {"filename": file.filename, "message": "Arquivo recebido, processamento pendente."}

print("FastAPI app inicializado. Rode com: uvicorn main:app --reload --port 8000")