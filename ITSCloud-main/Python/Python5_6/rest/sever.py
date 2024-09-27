from flask import Flask , json, request

api = Flask (__name__)

@api.route ('/add_cottadono', methods=['POST'])
def GestisciAddCittadino():
    
    return




api.run(host="127.0.0.1", port=8080)
