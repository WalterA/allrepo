import requests,json
import sys

base_url = "http://127.0.0.1:8080"

def GetDatiCittadino():
    nome = input("Qual'è il nome?")
    cognome = input("Qual'è il cognome")
    dataN = input("Qual'è la data di nascita?")
    codF = input("Qual'è il codice fiscale?")

    datiCittadino = {"nome":nome, "cognome": cognome, "data nascita":dataN, "codice fiscale":codF}
    return datiCittadino

def GetFi():
    codF = input("Qual'è il codice fiscale?")
    fi={"codice fiscale":codF}
    return fi

def operatore(codop:str):
    print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
    passop =  input("Inserisci la password")
    operatore = {"ID":codop , "Password" : passop}
    return operatore

access=True
while access:
    print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
    codop = input("Inserisci il codice")
    if codop:
        api_url = base_url + "/operatore"
        jsonDataRequest = operatore(codop)
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprovapiù tardi")
    if data1["Msg"] == "Buon lavoro":
                print("Operazioni disponibili:")
                print("1. Inserisci cittadino (es. atto di nascita)")
                print("2. Richiedi cittadino (es. cert. residenza)")
                print("3. Modifica cittadino (es. cambio residenza)")
                print("4. Elimina cittadino (es. trasferim altro comune)")
                print("5. termina lavoro")
                sOper = input("Cosa vuoi fare?")
    else:
        print("Dati errati, riprovare")
    if sOper == "1":
        print("Richiesto nuovo cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        try:
            response = requests.post(api_url,json=jsonDataRequest)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprovapiù tardi")
    if sOper == "2":
        print("Richiesto codice fiscale cittadino")
        api_url = base_url + "/cerca_cittadino"
        jsonDataRequest = GetFi()
        try:
            response = requests.get(api_url, json=jsonDataRequest)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
        except requests.exceptions.RequestException as e:
            print(f"Problemi di comunicazione con il server: {e}")
    if sOper == "3":
        print("Richiesto atto di nascita")
        api_url = base_url + "/modifica"
        jsonDataRequest = GetDatiCittadino()
        try:
            response = requests.put(api_url, json=jsonDataRequest)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
        except requests.exceptions.RequestException as e:
            print(f"Problemi di comunicazione con il server: {e}")
    if sOper == "4":
        print("Richiesto atto di nascita")
        api_url = base_url + "/elimina"
        jsonDataRequest = GetFi()
        try:
            response = requests.delete(api_url, json=jsonDataRequest)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
        except requests.exceptions.RequestException as e:
            print(f"Problemi di comunicazione con il server: {e}")
    if sOper == "5":
        print("Fine lavoro")
        access=True
        sys.exit()

    print("Operazioni disponibili:")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi cittadino (es. cert. residenza)")
    print("3. Modifica cittadino (es. cambio residenza)")
    print("4. Elimina cittadino (es. trasferim altro comune)")
    print("5. Esci")
    sOper = input("Cosa vuoi fare?")