import random
import string
import requests
import re



def gerar_crm(digitos: int = 20) -> str:
    caracteres = string.ascii_uppercase + string.digits  
    valor = ''.join(random.choice(caracteres) for _ in range(digitos))
    return valor

def gerar_modelos():
    carros_urls = [
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Renault",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Volvo",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Fiat",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Chevrolet"
    ]

    carros_encontrados = set()
    regex_carro = re.compile(r'<a[^>]+href="\/wiki\/[^"]+"[^>]+title="([^"]+)"')
    
    for url in carros_urls:
        response = requests.get(url)
        html = response.text
    
        matches = regex_carro.findall(html)
    
        for titulo in matches:
            if re.match(r'^[A-Z][a-z]+(?:\s+[A-Z0-9][\w\-áéíóúãõç]+)+$', titulo):
                carros_encontrados.add(titulo)
    
    return sorted(carros_encontrados)

def gerar_marcas():
    marcas_encontradas = set()
    regex_href = re.compile(r'<a[^>]+href="\/wiki\/([A-Z][a-zA-Z]+)_[^"]+"')
    response = requests.get("https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil")
    html = response.text
    matches = regex_href.findall(html)
    
    for marca in matches:
        marcas_encontradas.add(marca)
    
    return sorted(marcas_encontradas)
def gerar_anos():
    carros_urls = [
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Renault",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Volvo",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Fiat",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Chevrolet"
    ]
    
    anos_encontrados = set()
    regex_anos = re.compile(r'</a>\s*(\d{4}(?:[-–](?:\d{4}|presente))?)')
    
    for url in carros_urls:
        response = requests.get(url)
        html = response.text
        matches = regex_anos.findall(html)
        for ano in matches:
            if '-' in ano or '–' in ano:
                primeiro_ano = re.split(r'[-–]', ano)[0]
                try:
                    anos_encontrados.add(int(primeiro_ano.strip()))
                except ValueError:
                    continue
            else:
                try:
                    anos_encontrados.add(int(ano.strip()))
                except ValueError:
                    continue
    
    return sorted(anos_encontrados)

    carros_urls = [
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Renault",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Volvo",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Fiat",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Chevrolet"
    ]
    
    anos_encontrados = set()
    regex_anos = re.compile(r'</a>\s*(\d{4}(?:[-–](?:\d{4}|presente))?)')
    
    for url in carros_urls:
        response = requests.get(url)
        html = response.text
        matches = regex_anos.findall(html)
        for ano in matches:
            if '-' in ano or '–' in ano:
                primeiro_ano = re.split(r'[-–]', ano)[0]
                try:
                    anos_encontrados.add(int(primeiro_ano.strip()))
                except ValueError:
                    continue
            else:
                try:
                    anos_encontrados.add(int(ano.strip()))
                except ValueError:
                    continue
    
    return sorted(anos_encontrados)

    
    carros_urls = [
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Renault",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Volvo",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Fiat",
        "https://pt.wikipedia.org/wiki/Lista_de_autom%C3%B3veis_do_Brasil#Chevrolet"
    ]
    
    anos_encontrados = set()
    regex_anos = re.compile(r'</a>\s*(\d{4}(?:[-–](?:\d{4}|presente))?)')
    
    for url in carros_urls:
        response = requests.get(url)
        html = response.text
        matches = regex_anos.findall(html)
        for ano in matches:
            if '-' in ano or '–' in ano:
                primeiro_ano = re.split(r'[-–]', ano)[0]
                anos_encontrados.add(ano)
                return  sorted(int(primeiro_ano.strip()))    

    return sorted(anos_encontrados)

def gerar_combustivel(existentes):
    while True:
        letras = random.choices(string.ascii_uppercase, k=2)
        numero = random.choice(string.digits)
        codigo = f"{letras[0]}{letras[1].lower()}{numero}"
        if codigo not in existentes:
            existentes.add(codigo)
            return codigo

gerar_cores = [
    "vermelho", "azul", "verde", "amarelo", "roxo", "laranja", 
    "rosa", "marrom", "cinza", "preto", "branco", "prata",
    "bege",  "dourado", "prata", "vinho", "salmão"
]

motores = ["1.0", "1.4", "1.6", "1.8", "2.0", "2.4", "3.0", "3.5"]


marcas = gerar_marcas()[:100]
modelos = gerar_modelos()[:100]
anos = gerar_anos()[:100]

codigos_combustivel = set()
registros = []

for i in range(100):
    marca = marcas[i % len(marcas)]
    modelo = modelos[i % len(modelos)]
    cor = random.choice(gerar_cores)
    ano = anos[i % len(anos)]
    cod_crm = gerar_crm()
    combustivel = gerar_combustivel(codigos_combustivel)
    km = random.randint(0, 200000)
    motor = random.choice(motores)
    
    registros.append(f"{marca} -  {modelo} -  {cor} -  {ano} - {cod_crm} - combustivel-{combustivel} - {km}km - {motor}")

'''
if __name__ == '__main__':
    for registro in registros:
        print(registro)
'''
