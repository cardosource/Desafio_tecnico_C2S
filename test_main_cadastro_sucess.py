
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

@pytest.mark.asyncio
@pytest.mark.parametrize("marca, modelo, cor, ano, crm, combustivel, km, motor", [
    ("Toyota", "Corolla", "Prata", 2020, "ABC1234", "Gasolina", 35000, 2.0),
    ("Honda", "Civic", "Preto", 2018, "DEF5678", "Flex", 45000, 1.8),
    ("Ford", "Focus", "Branco", 2019, "GHI9101", "Diesel", 40000, 2.0)
])
async def test_criar_e_listar_ficha(marca, modelo, cor, ano, crm, combustivel, km, motor):
    repository = FichaTecnicaRepositoryDemo()
    manager = FichaTecnicaManager(repository)

    ficha_dto = FichaTecnicaDTO.model_validate({
        "marca": marca,
        "modelo": modelo,
        "cor": cor,
        "ano": ano,
        "crm": crm,
        "combustivel": combustivel,
        "km": km,
        "motor": motor
    })

    input_dto = FichaTecnicaInput(fichaTecnica=ficha_dto)
    await manager.criar_ficha(input_dto)

    resultado = await manager.listar()
    assert len(resultado) == 1
    ficha_resultado = resultado[0].fichaTecnica

    assert ficha_resultado.marca == marca
    assert ficha_resultado.modelo == modelo
    assert ficha_resultado.cor == cor
    assert ficha_resultado.ano == ano
    assert ficha_resultado.crm == crm
    assert ficha_resultado.combustivel == combustivel
    assert ficha_resultado.km == km
    assert ficha_resultado.motor == motor

