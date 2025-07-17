from typing import Optional

class FichaTecnica:
    def __init__(self, ficha_id, marca, modelo, cor, ano, crm, combustivel, km, motor):
       
        self.ficha_id: Optional[int] = ficha_id
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.crm = crm
        self.combustivel = combustivel
        self.km = km
        self.motor = motor

        self.validar()

    def validar(self):
        if self.marca == "" and self.modelo == "":
            raise Exception("Campos 'marca' e 'modelo' obrigatórios")
        if not isinstance(self.marca, str) or not isinstance(self.modelo, str):
            raise Exception(f"Campos 'marca' e 'modelo' devem ser strings")

        if self.cor == "":
            raise Exception("Campo 'cor' é obrigatório")
        if not isinstance(self.cor, str):
            raise Exception(f"Campo 'cor' deve ser string")

        if self.combustivel == "":
            raise Exception("Campo 'combustível' é obrigatório")
        if not isinstance(self.combustivel, str):
            raise Exception("Campo 'combustível' deve ser string")

        if not self.ano:
            raise Exception("Campo 'ano' é obrigatório")
        if not isinstance(self.ano, int):
            raise Exception("Campo 'ano' deve ser inteiro")

        if not self.crm:
            raise Exception("Campo 'crm' é obrigatório")
        if not isinstance(self.crm, str):
            raise Exception("Campo 'crm' deve ser string")

        if self.km is None:
            raise Exception("Campo 'km' é obrigatório")
        if not isinstance(self.km, float):
            raise Exception("Campo 'km' deve ser float")

        if not self.motor:
            raise Exception("Campo 'motor' é obrigatório")
        if not isinstance(self.motor, float):
            raise Exception("Campo 'motor' deve ser float")
