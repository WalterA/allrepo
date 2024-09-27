from flask import Flask, json, request

api = Flask(__name__)

#mettere una lista di liste dove ogni lista è un cittadino

#la chiave è il codice fiscale
#add cittadino
#read cittadino
#update cittadino
#delete cittadino


@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        jsonReq = request.json
        print(jsonReq)
        #cittadini.append(jsonReq)
        jsonResp = {"Esito":"200", "Msg":"ok"}
        return json.dumps(jsonResp)
    else:
        return 'Content-Type not supported!'


api.run(host="127.0.0.1", port=8080)