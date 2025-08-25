from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# Essa chave será usada pelo Wix para autenticar
SECRET_KEY = "minha_chave_teste_123"

# Endpoint de teste
@app.get("/contatos")
def listar_contatos(authorization: str = Header(None)):
    if authorization != f"Bearer {SECRET_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return [
        {"nome": "Ana", "sobrenome": "Silva", "documento": "123456789", "telefone": "11999999999"},
        {"nome": "Carlos", "sobrenome": "Souza", "documento": "987654321", "telefone": "21988888888"}
    ]
