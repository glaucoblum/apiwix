from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# 🔹 Substitua pelos dados de conexão do Neon
DB_HOST = "ep-dawn-cake-adu3355z-pooler.c-2.us-east-1.aws.neon.tech"
DB_NAME = "neondb"
DB_USER = "neondb_owner"
DB_PASS = "npg_7uKmlk0DMZXt"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )

@app.get("/")
def root():
    return {"status": "API rodando 🚀"}

@app.get("/contatos")
def listar_contatos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, sobrenome, documento, telefone FROM contatos;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    contatos = []
    for row in rows:
        contatos.append({
            "id": row[0],
            "nome": row[1],
            "sobrenome": row[2],
            "documento": row[3],
            "telefone": row[4]
        })

    return contatos
