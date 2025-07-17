from automoveis.casoDeuso.FichaTecnicaDTO import FichaTecnicaInput, FichaTecnicaOutput,FichaTecnicaDTO
from automoveis.entidade.FichaTecnica import FichaTecnica
from automoveis.casoDeuso.FichaTecnica_Interface import RepositoryFichaTecnicaInterface
from typing import Dict,Any,List
from automoveis.casoDeuso.FichaTecnicaDTO import FichaTecnicaInput, FichaTecnicaOutput
from automoveis.entidade.FichaTecnica import FichaTecnica

class FichaTecnicaManager:
    def __init__(self, repository: RepositoryFichaTecnicaInterface):
        self.repository = repository

    async def criar_ficha(self, dto: FichaTecnicaInput) -> str:

        data = dto.fichaTecnica

        ficha = FichaTecnica(
            ficha_id=data.id_,
            marca=data.marca,
            modelo=data.modelo,
            cor=data.cor,
            ano=data.ano,
            crm=data.crm,
            combustivel=data.combustivel,
            km=data.km,
            motor=data.motor,
        )

        await self.repository.salvar(ficha)
        return "salvo"

    async def listar(self) -> list[FichaTecnicaOutput]:
        fichas = await self.repository.listar()
        return [
            FichaTecnicaOutput(fichaTecnica=FichaTecnicaDTO(
                ficha_id=f.ficha_id,
                marca=f.marca,
                modelo=f.modelo,
                cor=f.cor,
                ano=f.ano,
                crm=f.crm,
                combustivel=f.combustivel,
                km=f.km,
                motor=f.motor,
            )) for f in fichas
        ]

    async def buscar(self, id_: int) -> FichaTecnicaOutput:
        f = await self.repository.buscar(id_)
        return FichaTecnicaOutput(fichaTecnica=FichaTecnicaDTO(
            ficha_id=f.ficha_id,
            marca=f.marca,
            modelo=f.modelo,
            cor=f.cor,
            ano=f.ano,
            crm=f.crm,
            combustivel=f.combustivel,
            km=f.km,
            motor=f.motor,
        ))

    async def filtragem(self, filtros: Dict[str, Any]) -> List[FichaTecnicaOutput]:
        fichas = await self.repository.filtragem(filtros)
        return [
            FichaTecnicaOutput(fichaTecnica=FichaTecnicaDTO(
                ficha_id=f.ficha_id,
                marca=f.marca,
                modelo=f.modelo,
                cor=f.cor,
                ano=f.ano,
                crm=f.crm,
                combustivel=f.combustivel,
                km=f.km,
                motor=f.motor,
            )) for f in fichas
        ]

    async def deletar(self, id_: int) -> None:
        await self.repository.deletar(id_)
        '''não implementado'''
