import requests
import sys

id_utente = ""
pwd_utente = ""
base_url = "https://127.0.0.1:8080"
operatore= None
def GetDatiCittadino():
    nome = input("Qual è il nome? ")
    cognome = input("Qual è il cognome? ")
    codF = input("Qual è il codice fiscale? ")
    return nome , cognome , codF

def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ').upper()
    return cod

access = False
print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
conta=3
while access == False:
    codop = input("Inserisci l'ID operatore: ")
    if conta == 1:
        print("Raggiunto il massimo di errori, arrivederci")
        access = False
        sys.exit()
    if codop.isdigit():
        while not access:
            api_url = base_url + "/login"
            id_utente = input("Inserisci ID operatore: ")
            pwd_utente = input("Inserisci Password dell'operatore: ")
            jsonDataRequest = {'id_utente': id_utente, 'pwd_utente': pwd_utente}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                data1 = response.json()
                if data1.get("Esito") == "200":
                    access = True
                    dResponse = response.json()
                    operatore = dResponse["operatore"]
                    print(dResponse["Msg"])
                else:
                    print("Dati errati, riprova.")
            else:
                print(f"Errore nella richiesta: {response.status_code}")
    else:
        conta-=1
        print(f"ID operatore non valido. Inserisci solo numeri. Tentativi rimasti {conta}")

while access:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")
    sOper = input("Cosa vuoi fare?")
    if int(operatore["id"]) > 1:
        if sOper == "2":
            print("Richiesta dati cittadino")
            api_url = base_url + "/read_cittadino"
            jsonDataRequest = {"codFiscale" : GetCodicefiscale(),"operatore":operatore}
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            if response.status_code == 200:
                response=response.json()
                cittadino = response["cittadino"]
                id_operatore = response["operatore"]["id"] 
                print(f"Cittadino: {cittadino}, ID Operatore: {id_operatore}")
            else:
                print(f"Errore nella richiesta: {response.status_code}, {response.text}")
        else:
            print("Operazione non consentita")
        if sOper == "5":
            print("Fine lavoro")
            access = False
            sys.exit()
    else:
        if sOper == "1":
            print("Nuovo cittadino")
            api_url = base_url + "/add_cittadino"
            jsonDataRequest = GetDatiCittadino()
            try:
                response = requests.post(api_url, json=jsonDataRequest, verify=False)
                data1 = response.json()
                print(response.status_code)
                print(response.headers["Content-Type"])
                
                if data1["Esito"] == "000" and data1["ID"] == id_utente and data1["Password"] == pwd_utente:
                    print("Cittadino inserito con successo")
                    print(data1)
                else:
                    print("Dati errati")      
            except:
                print("Problemi di comunicazione con il server, riprova più tardi")
        else:
            print("Operazione non consentita")
        
    # if operatore["id"] == 1:
    #         print("Richiesto nuovo cittadino")
            
"""
#         elif sOper == "2":
#             print("Richiesto codice fiscale cittadino")
#             api_url = base_url + "/cerca_cittadino"
#             jsonDataRequest = GetFi()
#             try:
#                 response = requests.get(api_url, json=jsonDataRequest, verify=False)
#                 data1 = response.json()
#                 print(response.status_code)
#                 print(response.headers["Content-Type"])
                
#                 if data1["Esito"] == "000" and data1["ID"] == id_utente and data1["Password"] == pwd_utente:
#                     print(data1["Cittadino"])
#                 else:
#                     print("Dati errati")      
#             except requests.exceptions.RequestException as e:
#                 print(f"Problemi di comunicazione con il server: {e}")
        
#         elif sOper == "3":
#             print("Richiesto atto di nascita")
#             api_url = base_url + "/modifica"
#             jsonDataRequest = GetDatiCittadino()
#             try:
#                 response = requests.put(api_url, json=jsonDataRequest, verify=False)
#                 data1 = response.json()
#                 print(response.status_code)
#                 print(response.headers["Content-Type"])
                
#                 if data1["Esito"] == "000":
#                     print(data1)
#                 else:
#                     print("Dati errati")
#             except requests.exceptions.RequestException as e:
#                 print(f"Problemi di comunicazione con il server: {e}")
        
#         elif sOper == "4":
#             print("Richiesto atto di nascita")
#             api_url = base_url + "/elimina"
#             jsonDataRequest = GetFi()
#             try:
#                 response = requests.delete(api_url, json=jsonDataRequest, verify=False)
#                 data1 = response.json()
#                 print(response.status_code)
#                 print(response.headers["Content-Type"])
                
#                 if data1["Esito"] == "000":
#                     print(data1)
#                 else:
#                     print("Dati errati")
#             except requests.exceptions.RequestException as e:
#                 print(f"Problemi di comunicazione con il server: {e}")
        
#         elif sOper == "5":
#             print("Fine lavoro")
#             access = False
#             sys.exit()

#     else:
#         print("Operatore non trovato o credenziali errate.")
# """