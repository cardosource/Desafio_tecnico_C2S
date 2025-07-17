from pydantic  import BaseModel,ConfigDict,Field
from automoveis.entidade.FichaTecnica import FichaTecnica
from typing import Optional

class FichaTecnicaDTO(BaseModel):
        model_config = ConfigDict(extra='forbid',frozen=True )
        
        id_:Optional[int] = Field(default=None,alias='ficha_id')
        marca: str 
        modelo: str 
        cor: str 
        ano: int 
        crm: str
        combustivel: str 
        km: float 
        motor: float 

class FichaTecnicaInput(BaseModel):
    #model_config = ConfigDict(extra='forbid')
    fichaTecnica: FichaTecnicaDTO

class FichaTecnicaOutput(BaseModel):
    #model_config = ConfigDict(extra='forbid')
    fichaTecnica: FichaTecnicaDTO
