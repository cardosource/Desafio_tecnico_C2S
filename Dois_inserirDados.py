#sudo -u postgres psql -d ficatecnica
#sudo -u postgres psql -d ficatecnica

from automoveis.casoDeuso.FichaTecnicaDTO import FichaTecnicaInput,FichaTecnicaOutput, FichaTecnicaDTO
from automoveis.casoDeuso.FichaTecnicaManager import FichaTecnicaManager
from automoveis.casoDeuso.FichaTecnicaRepository import FichaTecnicaRepository
from conteudo import registros
async def main():
    repository = FichaTecnicaRepository()
    manager = FichaTecnicaManager(repository=repository)

    for registro in registros:
        
            partes = registro.split(" - ")
            
            if len(partes) < 8:
                print(f"Registro incompleto: {registro}")
                continue

            dto = FichaTecnicaInput(
                fichaTecnica=FichaTecnicaDTO(
                    marca=partes[0].strip(),
                    modelo=partes[1].strip(),
                    cor=partes[2].strip(),
                    ano=int(partes[3].strip()), 
                    crm=partes[4].strip(),
                    combustivel=partes[5].replace("combustivel-", "").strip(),
                    km=float(partes[6].replace("km", "").strip()),
                    motor=float(partes[7].strip())
                )
            )

            result = await manager.criar_ficha(dto)
            print(registro)
    print("\nRegistros inseridos com sucesso!")
            
       

'''
    repository = FichaTecnicaRepository()
    manager = FichaTecnicaManager(repository=repository)
    filtros = {"marca": "Fiat"}

    try:
        resultados = await manager.filtragem(filtros)
        for ficha in resultados:
            dto = ficha.fichaTecnica
            print(dto.marca)
            print(dto.modelo)
            print(dto.motor)
            print(dto.cor)
            print(dto.ano)
            print(dto.combustivel)
            print(dto.km)
            print(dto.crm)
          
    except ValueError as e:
        print(f"Erro ao buscar com filtros: {str(e)}")


    repository = FichaTecnicaRepository()
    manager = FichaTecnicaManager(repository=repository)

    id_para_buscar = 1  # exemplo

    try:
        ficha = await manager.buscar(id_para_buscar)
        print(f"Encontrado: Modelo: {ficha.fichaTecnica.modelo}, Motor: {ficha.fichaTecnica.motor}")
    except ValueError as e:
        print(str(e))

    repo = FichaTecnicaRepository()
    manager = FichaTecnicaManager(repo)

    fichas = await manager.listar()

    for ficha in fichas:
        print(
            
            f"Modelo: {ficha.fichaTecnica.modelo}, "
            f"Motor: {ficha.fichaTecnica.motor}, "
            f"KM: {ficha.fichaTecnica.km}"
        )
'''
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
