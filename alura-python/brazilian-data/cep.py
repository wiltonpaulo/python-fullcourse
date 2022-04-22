import requests

url = "https://viacep.com.br/ws/"

cep = "04468000"
data = requests.get(f"{url}/{cep}/json/").json()

for name, value in data.items():
    print(f"{name} => {value}")


print(f"Your CEP is in {data['localidade']}")
