from flask import Flask, json, request
from configparser import ConfigParser
import psycopg2

# Funzione per leggere la configurazione del database
def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

# Connessione al database
conn = None

def connect():
    print('Connecting to the PostgreSQL database...')
    global conn
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        return cur
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

# Funzione per chiudere la connessione
def close(cur):
    global conn
    if cur:
        cur.close()
    if conn:
        conn.close()

api = Flask(__name__)

# Autenticazione dell'operatore
@api.route('/operatore', methods=['POST'])
def verop():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sId = jsonReq["ID"]
            sPass = jsonReq["Password"]
            
            cur = connect()
            query = f"SELECT id, password FROM operatori WHERE id = '{sId}'"
            cur.execute(query)
            operatore = cur.fetchone()

            if operatore and sPass == operatore[1]:
                jsonResp = {"Esito": "000", "Msg": "Buon lavoro", "ID": operatore[0], "Password": operatore[1]}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Operatore non trovato o password errata"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
        finally:
            close(cur)
    else:
        return 'Content-Type not supported!', 401

# Aggiungi cittadino
@api.route('/add_cittadino', methods=['POST'])
def controlla_cittadino(conn, codF):
    """Controlla se il cittadino è già presente nel database."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM cittadini WHERE codice_fiscale = %s;", (codF,))
        row = cur.fetchone()
        cur.close()
        return row is not None  # Restituisce True se il cittadino esiste, altrimenti False
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def GestisciAddCittadino(conn):
    global nome
    global cognome
    global codf
    
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/json':
        jsonReq = request.json
        nome = jsonReq["nome"]
        cognome= jsonReq["cognome"]
        codF = jsonReq["codice_fiscale"]
    else:
        print("error")
    # Controlla se il cittadino è già presente
    if controlla_cittadino(conn, codF):
        print("Cittadino già presente nel database.")
    else:
        # Inserisce il cittadino nel database
        try:
            cur = conn.cursor()
            sql_insert = "INSERT INTO cittadini (nome, cognome, codice_fiscale) VALUES (%s, %s, %s);"
            cur.execute(sql_insert, (nome, cognome, codF))
            conn.commit()
            print("Cittadino aggiunto con successo.")
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()


# Cerca cittadino
@api.route('/cerca_cittadino', methods=['GET'])
def CercaCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            sId = jsonReq["ID"]
            sPass = jsonReq["Password"]

            cur = connect()
            # Verifica che l'operatore esista
            query = f"SELECT id FROM operatori WHERE id = '{sId}' AND password = '{sPass}'"
            cur.execute(query)
            operatore = cur.fetchone()

            if operatore:
                # Cerca il cittadino
                query = f"SELECT * FROM anagrafe WHERE codice_fiscale = '{sCodiceFiscale}'"
                cur.execute(query)
                cittadino = cur.fetchone()

                if cittadino:
                    jsonResp = {"Esito": "000", "Msg": "Cittadino trovato", "Cittadino": cittadino}
                    return json.dumps(jsonResp), 200
                else:
                    jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
                    return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Operatore non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
        finally:
            close(cur)
    else:
        return 'Content-Type not supported!', 401

# Modifica cittadino
@api.route('/modifica', methods=['PUT'])
def ModificaCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            cur = connect()

            # Verifica se il cittadino esiste
            query = f"SELECT * FROM anagrafe WHERE codice_fiscale = '{sCodiceFiscale}'"
            cur.execute(query)
            cittadino = cur.fetchone()

            if cittadino:
                query = f"UPDATE anagrafe SET nome = '{jsonReq['nome']}', cognome = '{jsonReq['cognome']}' WHERE codice_fiscale = '{sCodiceFiscale}'"
                cur.execute(query)
                conn.commit()

                jsonResp = {"Esito": "000", "Msg": "Cittadino modificato con successo"}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
        finally:
            close(cur)
    else:
        return 'Content-Type not supported!', 401

# Elimina cittadino
@api.route('/elimina', methods=['DELETE'])
def eliminaCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            cur = connect()

            # Verifica se il cittadino esiste
            query = f"SELECT * FROM anagrafe WHERE codice_fiscale = '{sCodiceFiscale}'"
            cur.execute(query)
            cittadino = cur.fetchone()

            if cittadino:
                query = f"DELETE FROM anagrafe WHERE codice_fiscale = '{sCodiceFiscale}'"
                cur.execute(query)
                conn.commit()

                jsonResp = {"Esito": "000", "Msg": "Cittadino eliminato con successo"}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
        finally:
            close(cur)
    else:
        return 'Content-Type not supported!', 401

# Avvia l'API
api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
