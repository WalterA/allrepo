from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize

sAnagrafe = "./anagrafe.json"
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
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale not in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok", "Cittadino": dNuovoCittadino}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401

@api.route('/cerca_cittadino', methods=['GET'])
def CercaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            anagrafe = JsonDeserialize(sAnagrafe)
            if sCodiceFiscale in anagrafe:
                dCittadino = anagrafe[sCodiceFiscale]
                jsonResp = {"Esito": "000", "Msg": "ok", "Cittadino": dCittadino}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Content-Type not supported!', 401

@api.route('/modifica', methods=['PUT'])
def ModificaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        jsonReq = request.json
        sCodiceFiscale = jsonReq["codice fiscale"]
        anagrafe = JsonDeserialize(sAnagrafe)
        if sCodiceFiscale in anagrafe:
            dNuovoCittadino = jsonReq
            anagrafe[sCodiceFiscale] = dNuovoCittadino
            JsonSerialize(anagrafe,sAnagrafe)
            jsonResp = {"Esito":"000", "Msg":"ok", "Cittadino": dNuovoCittadino}
            return json.dumps(jsonResp),200
        else:
            jsonResp = {"Esito":"001", "Msg":"Cittadino gia presente"}
            return json.dumps(jsonResp),200
    else:
        return 'Content-Type not supported!',401
    
@api.route('/elimina', methods=['DELETE'])
def eliminaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        try:
            jsonReq = request.json
            sCodiceFiscale = jsonReq["codice fiscale"]
            anagrafe = JsonDeserialize(sAnagrafe)
            if sCodiceFiscale in anagrafe:
                del  anagrafe[sCodiceFiscale]
                JsonSerialize(anagrafe,sAnagrafe)
                jsonResp = {"Esito": "000", "Msg": "ok", "Cittadino": "eliminato"}
                return json.dumps(jsonResp), 200
            else:
                jsonResp = {"Esito": "001", "Msg": "Cittadino non trovato"}
                return json.dumps(jsonResp), 200
        except Exception as e:
            return str(e), 500
    else:
        return 'Content-Type not supported!', 401
api.run(host="127.0.0.1", port=8080)
