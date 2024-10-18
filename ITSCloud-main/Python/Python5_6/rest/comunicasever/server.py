#from crypt import methods
from flask import Flask, jsonify, request
from configparser import ConfigParser
import psycopg2
import sys
import os
import os.path
import time

api = Flask(__name__)

import psycopg2

# Configurazione della connessione al database
conn = psycopg2.connect(
    host="localhost",      # indirizzo del server PostgreSQL (localhost per locale)
    database="postgres",       # nome del database
    user="postgres",         # nome utente del database
    password="postgres"  # password dell'utente
)

# Creare un cursore per eseguire le query
#cur = conn.cursor()

# Eseguire una query SQL
#cur.execute("SELECT version();")

# Recuperare e stampare il risultato della query
#db_version = cur.fetchone()
#print(f"PostgreSQL version: {db_version}")

# Chiudere la connessione e il cursore
# cur.close()
# conn.close()
"""
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

conn = None


def connect():
    Connect to the PostgreSQL database server 
    print('Connecting to the PostgreSQL database 0...')
    global conn
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        return cur

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

def write_in_db(cur,sql_insert):
    global conn
    try:
        cur.execute(sql_insert)
        # commit the changes to the database
        conn.commit()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
    #except Exception as error:
        #print("Inizio:")
        #print(error)
        sError = str(error)
        #print("Fine:")
        if sError.startswith("duplicate key value "):
            print("Duplicate key, vado avanti")
            conn.rollback()
            return -2
        cur = None
        conn = None
        print(sError)
        return -1

#La funzione torna -1 se è andata male e numero di righe se va bene
def read_in_db(cur,sql_select):
    try:
        cur.execute(sql_select)
        print("The number of parts: ", cur.rowcount)
        return cur.rowcount
        #row = cur.fetchone()

        #while row is not None:
        #    print(row)
        #    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:

        cur = None
        conn = None
        return -1

def read_next_row(cur):
    try:
        row = cur.fetchone()
        return True,row
    except:
        cur = None
        conn = None
        return False,None

def close(cur):
    global conn
    try:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur = None
        conn = None
"""       
@api.route('/login', methods=['POST'])
def login():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        id = jsonReq.get('id_utente')
        pwd = jsonReq.get('pwd_utente')
        
        cur = conn.cursor()
        if cur is None:
            return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
        query=("SELECT id,password from operatori where id = %s and password = %s")
        cur.execute(query, (id, pwd))
        result = cur.fetchone()
        operatore={"id":id,"password":pwd}
        if result:
            query = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW(), %s , %s);"
            cur.execute(query, (id,"Login"))
            conn.commit()
            print("Operazione inserita con successo.")
            return jsonify({"Esito": "200", "Msg": "Dati corretti","operatore":operatore}), 200
        else:
            return jsonify({"Esito": "403", "Msg": "ID errato"}), 403
        

        
@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        jsonReq = request.json
        codice_fiscale = jsonReq.get('codFiscale')
        if codice_fiscale in cittadini:
            return jsonify({"Esito": "200", "Msg": "Cittadino già esistente"}), 200
        else:
            cittadini[codice_fiscale] = jsonReq
            JsonSerialize(cittadini, file_path) 
            return jsonify({"Esito": "200", "Msg": "Cittadino aggiunto con successo"}), 200
    else:
        return 'Content-Type non supportato!'

@api.route('/read_cittadino', methods=['POST'])
def read_cittadino():
    try:
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            jsonReq = request.json
            cf = jsonReq.get('codFiscale')
            op = jsonReq.get("operatore")
            id = op.get("id")
        if int(id) > 1:
            cur = conn.cursor()
            if cur is None:
                return jsonify({"Esito": "500", "Msg": "Errore connessione al DB"}), 500
            query=("SELECT * from cittadini where codice_fiscale = %s")
            cur.execute(query, (cf,))
            result = cur.fetchone()
            if result:
                query = "INSERT INTO operazioni (data, operatori, op) VALUES (NOW(), %s , %s);"
                cur.execute(query, (id,"Cerca cittadino"))
                conn.commit()
                return jsonify({"Esito": "200", "Msg": "Cittadino trovato","operatore":op,"cittadino":result}), 200
            else:
                return jsonify({"Esito": "403", "Msg": "cittadino non trovato"}), 404
        else:
            return jsonify({"Esito": "403", "Msg": "Operatore non ha i permessi"}), 403
    except Exception as e:
        print(f"Errore: {e}")  # Stampa l'errore nel terminale
        return jsonify({"Esito": "500", "Msg": "Errore interno del server"}), 500

# @api.route('/update_cittadino', methods=['POST'])
# def update_cittadino():
#     content_type = request.headers.get('Content-Type')
#     if content_type == 'application/json':
#         jsonReq = request.json
#         codice_fiscale = jsonReq.get('codFiscale')
#         if codice_fiscale in cittadini:
#             cittadini[codice_fiscale] = jsonReq
#             JsonSerialize(cittadini, file_path)  
#             return jsonify({"Esito": "200", "Msg": "Cittadino aggiornato con successo"}), 200
#         else:
#             return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
#     else:
#         return 'Content-Type non supportato!'

# @api.route('/elimina_cittadino', methods=['POST'])
# def elimina_cittadino():
#     content_type = request.headers.get('Content-Type')
#     if content_type == 'application/json':
#         cod = request.json.get('codFiscale')
#         if cod in cittadini:
#             del cittadini[cod]
#             JsonSerialize(cittadini, file_path)  
#             return jsonify({"Esito": "200", "Msg": "Cittadino rimosso con successo"}), 200
#         else:
#             return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
#     else:
#         return 'Content-Type non supportato!'

api.run(host="127.0.0.1", port=8080, ssl_context="adhoc")

