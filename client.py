import requests

auth_token = "3c0143435c55ec2af2f62791fceaf00f4e603027"
hed = {"Authorization": "token " + auth_token}
data = {
    "id": "1",
    "Lote": "OSGWE1125",
    "Empresa": "Movicreto SAC",
    "Fecha": "20:19 02/01/21",
    "Cantidad": "50",
    "T_Producción": "00:45:00",
    "RUC": "20212522155",
    "Cemento": "20",
    "Agregado_1": "20",
    "Agregado_2": "20",
    "Agua": "80",
    "Aditivo_1": "0",
    "owner": "tamalitux",
}

# url = "http://garciajeri.pythonanywhere.com/app_data/"
# url = "http://127.0.0.1:8000/myConcreteREST/"
url = "http://wyvernys.pythonanywhere.com/myConcreteREST/"
response = requests.post(url, json=data, headers=hed)
print(response)
print(response.json())
