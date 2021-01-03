import requests

auth_token = "1858750d52d79d24a64bad85a75d3de7313f6956"
hed = {"Authorization": "token " + auth_token}
data = {
    "id": "1",
    "Fecha": "17:19 pm 02/01/21",
    "Cantidad": "50",
    "Empresa": "Movicreto SAC",
    "RUC": "20212522155",
    "Cemento": "20",
    "Agregado_1": "20",
    "Agregado_2": "20",
    "Agua": "80",
    "Aditivo_1": "0",
    "T_Producción": "00:45:00",
    "owner": "tamalitux",
}

# url = "http://garciajeri.pythonanywhere.com/app_data/"
url = "http://127.0.0.1:8000/myConcreteREST/"
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())
