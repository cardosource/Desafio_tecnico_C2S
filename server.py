from automoveis.casoDeuso.FichaTecnicaDTO import FichaTecnicaInput, FichaTecnicaDTO
from automoveis.casoDeuso.FichaTecnicaManager import FichaTecnicaManager
from automoveis.casoDeuso.FichaTecnicaRepository import FichaTecnicaRepository
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
from json import dumps

mcp = FastMCP("Pesquisa")
repository = FichaTecnicaRepository()
manager = FichaTecnicaManager(repository=repository)

@mcp.tool()
async def filtro(filtros: Dict) -> Any:
    """
    Buscar a partir de filtro  específico.

    """
    

    try:
        resultados = await manager.filtragem(filtros)
        ficha_completa = []

        for ficha in resultados:
            dto = ficha.fichaTecnica
            ficha_completa.append({
                "id": dto.id_,
                "marca": dto.marca,
                "modelo": dto.modelo,
                "motor": dto.motor,
                "cor": dto.cor,
                "ano": dto.ano,
                "combustivel": dto.combustivel,
                "km": dto.km,
                "crm": dto.crm,
            })

        return dumps(ficha_completa, ensure_ascii=False)

    except ValueError as e:
        return dumps({"erro": str(e)})


@mcp.tool()
async def listar_todos() -> Any:
    """
    Lista todas as fichas técnicas cadastradas 
    """
    try:
        fichas = await manager.listar()
        resultado = []

        for ficha in fichas:
            dto = ficha.fichaTecnica
            resultado.append({
                "id": dto.id_,
                "marca": dto.marca,
                "modelo": dto.modelo,
                "motor": dto.motor,
                "cor": dto.cor,
                "ano": dto.ano,
                "combustivel": dto.combustivel,
                "km": dto.km,
                "crm": dto.crm,
            })

        return dumps(resultado, ensure_ascii=False)

    except ValueError as e:
        return dumps({"erro": str(e)})
