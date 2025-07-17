
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
     
@pytest.mark.parametrize("campo, valor, mensagem_erro", [
    ("marca", "", "Campos 'marca' e 'modelo' obrigatórios"),
    ("modelo", "", "Campos 'marca' e 'modelo' obrigatórios"),
    ("modelo", False, "Campos 'marca' e 'modelo' devem ser strings"),
    ("marca", 123, "Campos 'marca' e 'modelo' devem ser strings"),

])
def test_ficha_tecnica_entidade_validacao(campo, valor, mensagem_erro):
    dados = {
        "ficha_id": 1,
        "marca": "Chevrolet",
        "modelo": "S-10",
        "cor": "grafite",
        "ano": 2020,
        "crm": "11111-1222-44-ffff-33",
        "combustivel": "Diesel",
        "km": 35000.0,
        "motor": 2.0
    }

    dados[campo] = valor

    with pytest.raises(ValidationError) as pydanticErro:
        FichaTecnica(**dados)
    with pytest.raises(Exception) as campoErro:
        FichaTecnica(**dados)

    assert mensagem_erro in str(pydanticErro.value)
    assert mensagem_erro in str(campoErro.value)

