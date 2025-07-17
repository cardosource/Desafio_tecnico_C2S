


import asyncio
import json
from datetime import date
import torch
from classes.mcp_client import McpClient
from meta_llama_core import contexto_rag, query_iniciar 

from dotenv import load_dotenv
load_dotenv()



tipos = {
    "motor": float,
    "km": float,
    "ano": int,
}

async def contexto_rag(pergunta: str) -> str:
    client = McpClient()
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")

        if pergunta.lower() == "todos":
            resp = await client.call_tool("listar_todos", {})
        else:
            try:
                chave, valor = pergunta.split(":")
                chave = chave.strip()
                if chave in tipos:
                    valor = tipos[chave](valor)
                filtros = {chave: valor}
                resp = await client.call_tool("filtro", {"filtros": filtros})
            except ValueError:
                return "Formato esperado:::: chave:valor"

        if not resp.content:
            return "Nenhum dado encontrado."

        conteudo = ''.join([c.text for c in resp.content if c.type == "text"]).strip()
        if not conteudo:
            return "Nada encontrado"

        try:
            fichas = json.loads(conteudo)
        except json.JSONDecodeError:
            return "Não foi possivel decodificar os dados."

        if not fichas:
            return "Sem resultado"

        contexto = ""
        for i, ficha in enumerate(fichas, 1):
            partes = [f"{k}: {v}" for k, v in ficha.items()]
            contexto += f"Veículo {i} -> " + ", ".join(partes) + "\n"

        return contexto

    finally:
        await client.cleanup()


async def main():
    print("Digite 'sair' para encerrar.\n")

    while True:
        pergunta = input("Perunta::> ").strip()
        if pergunta.lower() in {"sair", "exit", "quit"}:
            return

        contexto = await contexto_rag(pergunta)
        resposta = query_iniciar(pergunta, contexto, chain_rag)

        print("Resposta:\n" + resposta + "\n")

if __name__ == '__main__':
    asyncio.run(main())
