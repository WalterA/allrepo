"""import requests, json
import sys

base_url = "https://127.0.0.1:8080"
id_utente = ""
pwd_utente = ""


def GetFi():
    id = input("Inserisci ID operatore: ")
    passw = input("Inserisci Password dell'operatore: ")
    codF = input("Qual è il codice fiscale? ")
    fi = {"ID": id, "Password": passw, "codice fiscale": codF}
    return fi

def operatore(codop: str):
    passop = input("Inserisci la password: ")
    operatore = {"ID": codop, "Password": passop}
    return operatore

access = True
while access:
    print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
    codop = input("Inserisci il codice: ")
    
    if codop:
        api_url = base_url + "/operatore"
        jsonDataRequest = operatore(codop)
        data1 = None  # Definisco data1 prima del blocco try
        try:
            response = requests.post(api_url, json=jsonDataRequest, verify=False)
            data1 = response.json()  # Assegno data1 dopo aver ricevuto la risposta
            print(response.status_code)
            print(response.headers["Content-Type"])
            
            if data1["Esito"] == "000":
                id_utente = data1["ID"]
                pwd_utente = data1["Password"]
                print(data1)
            else:
                print("Operatore non trovato")
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
            continue
    
    if data1 and data1.get("Msg") == "Buon lavoro":  # Controllo che data1 sia definito e che contenga "Msg"
        print("Operazioni disponibili:")
        print("1. Inserisci cittadino (es. atto di nascita)")
        print("2. Richiedi cittadino (es. cert. residenza)")
        print("3. Modifica cittadino (es. cambio residenza)")
        print("4. Elimina cittadino (es. trasferim altro comune)")
        print("5. Termina lavoro")
        sOper = input("Cosa vuoi fare? ")
        
        
"""
from configparser import ConfigParser
import psycopg2
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

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db

def connect():
    """ Connect to the PostgreSQL database server """
    print('Connecting to the PostgreSQL database...')
    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def verifica_operatore(conn, id_utente, pwd_utente):
    """ Verifica le credenziali dell'operatore nel database """
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM operatori WHERE id = %s AND password = %s;", (id_utente, pwd_utente))
        row = cur.fetchone()
        cur.close()
        return row
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

access = False
print("Benvenuto operatore\ninserisci i dati per iniziare la tua attività.")
codop = input("Inserisci il codice operatore: ")

if codop:
    conn = connect()
    if conn:
        id_utente = input("Inserisci ID operatore: ")
        pwd_utente = input("Inserisci Password dell'operatore: ")

        # Verifica le credenziali dell'operatore
        operatore = verifica_operatore(conn, id_utente, pwd_utente)
        if operatore:
            print("Operatore trovato:", operatore)
            access = True
            # Qui puoi continuare con le altre operazioni
        else:
            print("Operatore non trovato o dati non validi")

        conn.close()
    else:
        print("Impossibile connettersi al database")
while access:
    sOper = input("Cosa vuoi fare?\nOperazioni disponibili:\n1. Inserisci cittadino (es. atto di nascita)\n2. Richiedi cittadino (es. cert. residenza)\n3. Modifica cittadino (es. cambio residenza)\n4. Elimina cittadino (es. trasferim altro comune)\n5. Termina lavoro")
    if sOper == "1":
        while access:
            operatore = verifica_operatore(conn, id_utente, pwd_utente)
            if operatore:
                print("Operatore trovato:", operatore)
            else:
                 print("Operatore non trovato o dati non validi")
                 access=False

            print("Richiesto nuovo cittadino")
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
"""
        elif sOper == "2":
            print("Richiesto codice fiscale cittadino")
            api_url = base_url + "/cerca_cittadino"
            jsonDataRequest = GetFi()
            try:
                response = requests.get(api_url, json=jsonDataRequest, verify=False)
                data1 = response.json()
                print(response.status_code)
                print(response.headers["Content-Type"])
                
                if data1["Esito"] == "000" and data1["ID"] == id_utente and data1["Password"] == pwd_utente:
                    print(data1["Cittadino"])
                else:
                    print("Dati errati")      
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
        
        elif sOper == "3":
            print("Richiesto atto di nascita")
            api_url = base_url + "/modifica"
            jsonDataRequest = GetDatiCittadino()
            try:
                response = requests.put(api_url, json=jsonDataRequest, verify=False)
                data1 = response.json()
                print(response.status_code)
                print(response.headers["Content-Type"])
                
                if data1["Esito"] == "000":
                    print(data1)
                else:
                    print("Dati errati")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
        
        elif sOper == "4":
            print("Richiesto atto di nascita")
            api_url = base_url + "/elimina"
            jsonDataRequest = GetFi()
            try:
                response = requests.delete(api_url, json=jsonDataRequest, verify=False)
                data1 = response.json()
                print(response.status_code)
                print(response.headers["Content-Type"])
                
                if data1["Esito"] == "000":
                    print(data1)
                else:
                    print("Dati errati")
            except requests.exceptions.RequestException as e:
                print(f"Problemi di comunicazione con il server: {e}")
        
        elif sOper == "5":
            print("Fine lavoro")
            access = False
            sys.exit()

    else:
        print("Operatore non trovato o credenziali errate.")
"""