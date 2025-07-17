from automoveis.casoDeuso.FichaTecnica_Interface import RepositoryFichaTecnicaInterface
from automoveis.entidade.FichaTecnica  import FichaTecnica
from bancodados.models.FichaTecnicaORM import ModelFichaTecnica
from bancodados.config.db_session import create_session
from sqlalchemy.future import select

from sqlalchemy import and_
class FichaTecnicaRepository(RepositoryFichaTecnicaInterface):

    async def salvar(self, ficha: FichaTecnica) -> None:
        async with create_session() as session:
            orm_ficha = ModelFichaTecnica(
                marca=ficha.marca,
                modelo=ficha.modelo,
                cor=ficha.cor,
                ano=ficha.ano,
                crm=ficha.crm,
                combustivel=ficha.combustivel,
                km=ficha.km,
                motor=ficha.motor,
            )
            session.add(orm_ficha)
            await session.commit()

    async def listar(self) -> list[FichaTecnica]:
        async with create_session() as session:
            result = await session.execute(select(ModelFichaTecnica))
            rows = result.scalars().all()
            return [FichaTecnica(
                ficha_id=row.ficha_id,
                marca=row.marca,
                modelo=row.modelo,
                cor=row.cor,
                ano=row.ano,
                crm=row.crm,
                combustivel=row.combustivel,
                km=row.km,
                motor=row.motor,
            ) for row in rows]

    async def buscar(self, ficha_id: int) -> FichaTecnica:
        async with create_session() as session:
            result = await session.get(ModelFichaTecnica, ficha_id)
            if result is None:
                raise ValueError(f"Ficha com ID {ficha_id} não encontrada.")
            return FichaTecnica(
                ficha_id=result.ficha_id,
                marca=result.marca,
                modelo=result.modelo,
                cor=result.cor,
                ano=result.ano,
                crm=result.crm,
                combustivel=result.combustivel,
                km=result.km,
                motor=result.motor,
            )

    async def filtragem(self, filtros: dict) -> list[FichaTecnica]:
        async with create_session() as session:
            query = select(ModelFichaTecnica)

            condicoes = []
            for chave, valor in filtros.items():
                attr = getattr(ModelFichaTecnica, chave, None)
                if attr is not None:
                    condicoes.append(attr == valor)

            if condicoes:
                query = query.where(and_(*condicoes))

            result = await session.execute(query)
            rows = result.scalars().all()

            return [
                FichaTecnica(
                    ficha_id=row.ficha_id,
                    marca=row.marca,
                    modelo=row.modelo,
                    cor=row.cor,
                    ano=row.ano,
                    crm=row.crm,
                    combustivel=row.combustivel,
                    km=row.km,
                    motor=row.motor,
                ) for row in rows
            ]
    async def deletar(self, ficha_id: int) -> None:
        async with create_session() as session:
            result = await session.get(ModelFichaTecnica, ficha_id)
            if result is None:
                raise ValueError(f"Ficha com ID {ficha_id} não encontrada.")
            await session.delete(result)
            await session.commit()