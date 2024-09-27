import requests,json

base_url = "http://127.0.0.1:8080"

def GetDatiCittadino():
    nome = "Mario"
    cognome = "Garibaldi"
    dataN = "07/11/1890"
    codF = "dcfvfg70b34h501u"
    datiCittadino = {"nome":nome, "cognome": cognome, "dataNascita":dataN, "codFiscale":codF}
    return datiCittadino


api_url = base_url + "/add_cittadino"
jsonDataRequest = GetDatiCittadino()
response = requests.post(api_url,json=jsonDataRequest)
#print(response.json())
print(response.status_code)
print(response.headers["Content-Type"])
data1 = response.json()
print(data1)