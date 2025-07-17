from pydantic import ValidationError
import pytest
from pprint import pprint
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import pytest
import asyncio

from automoveis.casoDeuso.FichaTecnica_Interface import RepositoryFichaTecnicaInterface
from automoveis.entidade.FichaTecnica import FichaTecnica
from automoveis.casoDeuso.FichaTecnicaDTO import (FichaTecnicaDTO,
                                                 FichaTecnicaInput,
                                                 FichaTecnicaOutput)

from automoveis.casoDeuso.FichaTecnicaManager import FichaTecnicaManager

class FichaTecnicaRepositoryDemo(RepositoryFichaTecnicaInterface):
    def __init__(self):
        self._db = {}
        self._next_id = 1

    async def salvar(self, ficha: FichaTecnica):
        ficha.id_ = self._next_id
        self._db[self._next_id] = ficha
        self._next_id += 1

    async def listar(self):
        return list(self._db.values())

    async def buscar(self, id_: int):
        return self._db.get(id_)

    async def filtragem(self, filtros):
        return list(self._db.values())

    async def deletar(self, id_: int):
        if id_ in self._db:
            del self._db[id_]


async def main():
    repository = FichaTecnicaRepositoryDemo()
    manager = FichaTecnicaManager(repository)

  
    ficha_dto = FichaTecnicaDTO.model_validate({
    "ficha_id": 22,
    "marca": "Fiat",
    "modelo": "Touro",
    "cor": "Vinho",
    "ano": 2023,
    "crm": "222-23-32-3-3333",
    "combustivel": "Gasolina",
    "km": 5500,
    "motor": 2.0
})

    input_dto = FichaTecnicaInput(fichaTecnica=ficha_dto)
    await manager.criar_ficha(input_dto)
    fichas = await manager.listar()
    for ficha in fichas:
        pprint(ficha.model_dump_json(by_alias=True))

if __name__ == "__main__":
    asyncio.run(main())