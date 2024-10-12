import requests
import sys

base_url = "http://127.0.0.1:8080"  # Assicurati di usare l'URL corretto
id_utente = ""
pwd_utente = ""
max_attempts = 3

def GetDatiCittadino():
    nome = input("Qual è il nome? ")
    cognome = input("Qual è il cognome? ")
    codF = input("Qual è il codice fiscale? ")

    return nome, cognome, codF  # Restituisce i dati come tuple

def GetFi():
    codF = input("Qual è il codice fiscale? ")
    return codF  # Restituisce solo il codice fiscale

def operatore(codop: str):
    passop = input("Inserisci la password: ")
    return codop, passop  # Restituisce ID e password come tuple

def validate_operatore(id_utente, pwd_utente):
    api_url = base_url + "/operatore"
    try:
        response = requests.post(api_url, data={'ID': id_utente, 'Password': pwd_utente}, verify=False)
        return response.status_code == 200 and response.text == "Buon lavoro"  # Controlla il messaggio di successo
    except requests.exceptions.RequestException:
        print("Problemi di comunicazione con il server, riprova più tardi")
        return False

def perform_operation(api_url, data, method="post"):
    try:
        if method == "post":
            response = requests.post(api_url, data=data, verify=False)
        elif method == "get":
            response = requests.get(api_url, data=data, verify=False)
        elif method == "put":
            response = requests.put(api_url, data=data, verify=False)
        elif method == "delete":
            response = requests.delete(api_url, data=data, verify=False)

        return response.status_code == 200 and "successo" in response.text  # Controlla la risposta
    except requests.exceptions.RequestException as e:
        print(f"Problemi di comunicazione con il server: {e}")
        return False

def main():
    global id_utente, pwd_utente
    attempts = 0
    access = True

    while access:
        if attempts >= max_attempts:
            print("Troppi tentativi falliti. Uscita dal programma.")
            sys.exit()

        print("Benvenuto operatore\nInserisci i dati per iniziare la tua attività.")
        codop = input("Inserisci il codice: ")

        if codop:
            id_utente, pwd_utente = operatore(codop)  # Ottieni ID e password
            if validate_operatore(id_utente, pwd_utente):
                print("Operatore autenticato con successo.")
                adim = id_utente == "01"

                if adim:
                    print("Operazioni disponibili:")
                    print("1. Inserisci cittadino (es. atto di nascita)")
                    print("2. Richiedi cittadino (es. cert. residenza)")
                    print("3. Modifica cittadino (es. cambio residenza)")
                    print("4. Elimina cittadino (es. trasferim altro comune)")
                    print("5. Termina lavoro")
                    sOper = input("Cosa vuoi fare? ")

                    if sOper == "1":
                        api_url = base_url + "/add_cittadino"
                        nome, cognome, codice_fiscale = GetDatiCittadino()
                        data = {'nome': nome, 'cognome': cognome, 'codice_fiscale': codice_fiscale}
                        perform_operation(api_url, data)

                    elif sOper == "2":
                        api_url = base_url + "/cerca_cittadino"
                        codice_fiscale = GetFi()
                        data = {'codice_fiscale': codice_fiscale}
                        perform_operation(api_url, data, "get")

                    elif sOper == "3":
                        api_url = base_url + "/modifica"
                        nome, cognome, codice_fiscale = GetDatiCittadino()
                        data = {'nome': nome, 'cognome': cognome, 'codice_fiscale': codice_fiscale}
                        perform_operation(api_url, data, "put")

                    elif sOper == "4":
                        api_url = base_url + "/elimina"
                        codice_fiscale = GetFi()
                        data = {'codice_fiscale': codice_fiscale}
                        perform_operation(api_url, data, "delete")

                    elif sOper == "5":
                        print("Fine lavoro")
                        access = False
                        sys.exit()
                else:
                    print("Richiedi cittadino (es. cert. residenza)")
                    api_url = base_url + "/cerca_cittadino"
                    codice_fiscale = GetFi()
                    data = {'codice_fiscale': codice_fiscale}
                    perform_operation(api_url, data, "get")
            else:
                print("Operatore non trovato")
                attempts += 1

        attempts += 1

if __name__ == "__main__":
    main()
