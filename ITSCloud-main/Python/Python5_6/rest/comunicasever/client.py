import requests
import sys

id_utente = ""
pwd_utente = ""
base_url = "https://127.0.0.1:8080"

def GetDatiCittadino():
    nome = input("Qual è il nome? ")
    cognome = input("Qual è il cognome? ")
    codF = input("Qual è il codice fiscale? ")
    datiCittadino = {"nome": nome, "cognome": cognome, "codice_fiscale": codF}
    return datiCittadino

def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codFiscale": cod}

access = False
print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
codop = input("Inserisci l'ID operatore: ")

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
                print(dResponse["Msg"])
            else:
                print("Dati errati, riprova.")
        else:
            print(f"Errore nella richiesta: {response.status_code}")
else:
    print("ID operatore non valido. Inserisci solo numeri.")

       
# while access:
#     sOper = input("Cosa vuoi fare?\nOperazioni disponibili:\n1. Inserisci cittadino (es. atto di nascita)\n2. Richiedi cittadino (es. cert. residenza)\n3. Modifica cittadino (es. cambio residenza)\n4. Elimina cittadino (es. trasferim altro comune)\n5. Termina lavoro")
#     if sOper == "1":
#         while access:
#             operatore = verifica_operatore(conn, id_utente, pwd_utente)
#             if operatore:
#                 print("Operatore trovato:", operatore)
#             else:
#                  print("Operatore non trovato o dati non validi")
#                  access=False

#             print("Richiesto nuovo cittadino")
#             api_url = base_url + "/add_cittadino"
#             jsonDataRequest = GetDatiCittadino()
#             try:
#                 response = requests.post(api_url, json=jsonDataRequest, verify=False)
#                 data1 = response.json()
#                 print(response.status_code)
#                 print(response.headers["Content-Type"])
                
#                 if data1["Esito"] == "000" and data1["ID"] == id_utente and data1["Password"] == pwd_utente:
#                     print("Cittadino inserito con successo")
#                     print(data1)
#                 else:
#                     print("Dati errati")      
#             except:
#                 print("Problemi di comunicazione con il server, riprova più tardi")
# """
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