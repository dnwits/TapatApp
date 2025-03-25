from flask import Flask, request, jsonify

app = Flask(__name__)

# Token d'autenticació esperat
TOKEN_VALID = "secret123"

@app.route('/sumar', methods=['POST'])
def sumar():
    # Obtenir el token del header
    auth_header = request.headers.get('Authorization')

    # Verificar si el token és correcte
    if not auth_header or auth_header.split(" ")[1] != TOKEN_VALID:
        return jsonify({'error': 'Accés no autoritzat'}), 401

    # Obtenir dades JSON
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Falten paràmetres'}), 400

    return jsonify({'resultat': num1 + num2})

if __name__ == '__main__':
    app.run(debug=True)