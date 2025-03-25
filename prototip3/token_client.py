import requests

url = "http://127.0.0.1:5000/sumar"

# Dades JSON de la petició
dades = {
    "num1": 10,
    "num2": 20
}

# Headers amb el token d'autenticació
headers = {
    "Authorization": "Bearer secret123"
}

# Enviar petició POST amb headers i dades
resposta = requests.post(url, json=dades, headers=headers)

# Mostrar la resposta del servidor
if resposta.status_code == 200:
    print("Resposta:", resposta.json())  # {'resultat': 30}
else:
    print("Error:", resposta.status_code, resposta.text)
