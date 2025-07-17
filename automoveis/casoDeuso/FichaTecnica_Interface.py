from typing import Dict, List,Any
from automoveis.entidade.FichaTecnica import FichaTecnica
from abc import ABC, abstractmethod

class RepositoryFichaTecnicaInterface(ABC):
    @abstractmethod
    async def salvar(self, fichaTecnica: FichaTecnica) -> None:
        pass

    @abstractmethod
    async def listar(self) -> List[FichaTecnica]:
        pass

    @abstractmethod
    async def buscar(self, ficha_id: int) -> FichaTecnica:
        pass

    @abstractmethod
    async def filtragem(self, filtros: Dict[str, Any]) -> List[FichaTecnica]:
        pass

    @abstractmethod
    async def deletar(self, ficha_id: int) -> None:
        pass
