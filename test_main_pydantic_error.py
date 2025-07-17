
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#pytest --cov  --cov-report=term-missin


import pytest
import asyncio
from pydantic import ValidationError
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
        ficha.ficha_id = self._next_id
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


@pytest.mark.parametrize("campo, valor", [
    ("id", None),            # espera o tipo int
    ("marca", 123),          # espera o tipo string
    ("modelo", None),        # espera o tipo string
    ("cor", True),           # espera o tipo string
    ("moto", int(22)),       # espera o tipo float
    ("crm",999),             # espera o tipo string
    

])
def test_validacao_pydantic(campo, valor):
    dados_validos = {
        "ficha_id": 1,
        "marca": "Fiat",
        "modelo": "Uno",
        "cor": "Prata",
        "ano": 2018,
        "crm": "ABC-2939-2999",
        "combustivel": "Gasolina",
        "km": 300,
        "motor": 2.0
    }

    dados_validos[campo] = valor

    with pytest.raises(ValidationError):
        FichaTecnicaDTO.model_validate(dados_validos,by_alias=True)