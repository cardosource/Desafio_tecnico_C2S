import asyncio
import json
from classes.mcp_client import McpClient

banner = """
* Pesquisa individual:
Forma de pesquisa:  chave:valor 

marca:Fiat
motor:1.0

atributo e valor separado por dois pontos ":" 
-------------------------------------
marca        | modelo     |  motor
cor          | cor        |  ano
combustivel  | km         |  crm
-------------------------------------

* Listar toda a tabela:
digite: todos
"""
tipos = {
    "motor": float,
    "km": float,
    "ano": int
}

print(banner)
buscar = input("digite ::> ").strip()

async def main():
    client = McpClient()
    try:
        await client.initialize_with_sse("http://localhost:8000/sse")

        if buscar.lower() == "todos":
            resp = await client.call_tool("listar_todos", {})
        else:
            try:
                chave, valor = buscar.split(":")
                chave = chave.strip()
                valor = valor.strip()
                if chave in tipos:
                    try:
                        valor = tipos[chave](valor)
                    except ValueError:
                        print("Valor inválido para o tipo esperado.")
                        return

                filtros = {chave: valor}

            except ValueError:
                print("Formato esperado: chave:valor")
                return

            resp = await client.call_tool("filtro", {"filtros": filtros})

        if not resp.content:
            print("Resposta vazia.")
            return

        conteudo = ''.join([c.text for c in resp.content if c.type == "text"]).strip()

        if not conteudo:
            print("Conteúdo retornado está vazio.")
            return

        try:
            fichas = json.loads(conteudo)
        except json.JSONDecodeError as e:
            print("Erro ao decodificar JSON:", e)
            print("Conteúdo bruto:", conteudo)
            return

    
        if isinstance(fichas, dict):
            fichas = [fichas]
        elif isinstance(fichas, str):
            print("Resposta inesperada: string em vez de lista.")
            print("Conteúdo:", fichas)
            return
        elif not isinstance(fichas, list):
            print("Resposta não é uma lista de fichas.")
            print("Tipo:", type(fichas))
            return

        for i, ficha in enumerate(fichas, 1):
            if not isinstance(ficha, dict):
                print(f"Item {i} não é um dicionário:", ficha)
                continue

            print(f"\nFicha {i}:")
            for chave, valor in ficha.items():
                print(f"{chave.capitalize()}: {valor}")

    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
