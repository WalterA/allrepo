from flask import Flask, request
from comunicasever import dbclient as db
import sys

api = Flask(__name__)

@api.route('/operatore', methods=['POST'])
def verop():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)

    if content_type == 'application/x-www-form-urlencoded':
        try:
            sId = request.form["ID"]
            sPass = request.form["Password"]
            print(f"Ricevuto ID: {sId}, Password: {sPass}")  # Debug
            
            cur = db.connect()
            if cur is None:
                print("Errore connessione al DB")
                return "Errore interno", 500
            
            # Usa i parametri corretti
            sQuery = "SELECT id, password FROM Operatori WHERE id = %s AND password = %s;"
            cur.execute(sQuery, (sId, sPass))  # Passa i parametri come tupla
            result = cur.fetchone()
            print(f"Risultato della query: {result}")  # Debug
            
            if result:
                return "Buon lavoro", 200
            else:
                return "Credenziali non valide", 401
            
        except Exception as e:
            print("Errore: ", e)
            return "Errore interno", 500
    else:
        return "Content-Type non supportato", 400


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/x-www-form-urlencoded':
        try:
            sCodiceFiscale = request.form["codice_fiscale"]
            sNome = request.form["nome"]
            sCognome = request.form["cognome"]
            
            cur = db.connect()
            if cur is None:
                print("Errore connessione al DB")
                sys.exit()
            
            sQuery = "INSERT INTO Cittadini (codice_fiscale, nome, cognome) VALUES (%s, %s, %s);"
            result = db.write_in_db(cur, sQuery, (sCodiceFiscale, sNome, sCognome))
            
            if result == 0:
                return "Cittadino aggiunto con successo", 200
            elif result == -2:
                return "Cittadino già presente", 409
            else:
                return "Errore durante l'inserimento", 500
            
        except Exception as e:
            print("Errore: ", e)
            return "Errore interno", 500
    else:
        return "Content-Type non supportato", 400

@api.route('/cerca_cittadino', methods=['GET'])
def CercaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/x-www-form-urlencoded':
        try:
            sCodiceFiscale = request.form["codice_fiscale"]
            
            cur = db.connect()
            if cur is None:
                print("Errore connessione al DB")
                sys.exit()

            sQuery = "SELECT * FROM Cittadini WHERE codice_fiscale = %s;"
            cur.execute(sQuery, (sCodiceFiscale,))
            result = cur.fetchone()
            
            if result:
                return f"Cittadino trovato: {result}", 200
            else:
                return "Cittadino non trovato", 404
            
        except Exception as e:
            print("Errore: ", e)
            return "Errore interno", 500
    else:
        return "Content-Type non supportato", 400

@api.route('/modifica', methods=['PUT'])
def ModificaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/x-www-form-urlencoded':
        try:
            sCodiceFiscale = request.form["codice_fiscale"]
            sNome = request.form["nome"]
            sCognome = request.form["cognome"]

            cur = db.connect()
            if cur is None:
                print("Errore connessione al DB")
                sys.exit()

            sQuery = "UPDATE Cittadini SET nome = %s, cognome = %s WHERE codice_fiscale = %s;"
            result = db.write_in_db(cur, sQuery, (sNome, sCognome, sCodiceFiscale))

            if result == 0:
                return "Cittadino modificato con successo", 200
            elif result == -1:
                return "Cittadino non trovato", 404
            else:
                return "Errore durante la modifica", 500

        except Exception as e:
            print("Errore: ", e)
            return "Errore interno", 500
    else:
        return "Content-Type non supportato", 400

@api.route('/elimina', methods=['DELETE'])
def EliminaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type == 'application/x-www-form-urlencoded':
        try:
            sCodiceFiscale = request.form["codice_fiscale"]

            cur = db.connect()
            if cur is None:
                print("Errore connessione al DB")
                sys.exit()

            sQuery = "DELETE FROM Cittadini WHERE codice_fiscale = %s;"
            result = db.write_in_db(cur, sQuery, (sCodiceFiscale,))

            if result == 0:
                return "Cittadino eliminato con successo", 200
            elif result == -1:
                return "Cittadino non trovato", 404
            else:
                return "Errore durante l'eliminazione", 500

        except Exception as e:
            print("Errore: ", e)
            return "Errore interno", 500
    else:
        return "Content-Type non supportato", 400

if __name__ == "__main__":
    api.run(host='0.0.0.0', port=8080, debug=True)
