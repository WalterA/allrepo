from flask import Flask, render_template, request

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/visualizza', methods=['GET'])
def visualizza():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    return render_template('visualizza.html', nome=nome, cognome=cognome)

if __name__ == '__main__':
    api.run(host="0.0.0.0", port=8085)

