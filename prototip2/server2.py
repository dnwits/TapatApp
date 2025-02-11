from flask import Flask, request, jsonify
import dadesServer as dades
from dadesServer import User

# Exemple d'ús de la llista d'usuaris
for x in dades.users:
    print(x)

# Exemple d'ús de la classe User
a= User(id=1, username="Kurl", password="12345", email="prova2@gmail.com")
print(a)

    
class DAOUsers:
    def __init__(self):
        self.users=dades.users
    # Crear metodo que hace la busqueda
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u #.__dict__
        return None
    
class DAOChild(id_user):
    def __init__(self):
        self.id=dades.users
    def getChildByUserId(self,id):
        
# declara que utilizaremos flask
# variable que llama al metodo DAOUsers de antes
app = Flask(__name__)       
daoUser= DAOUsers()

@app.route('/prototip1/getuser/', defaults={'username': None}, methods=['GET'])
@app.route('/prototip1/getuser/<username>', methods=['GET'])
def get_user(username):
    if username is None or username.strip() == "":
        return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"}), 400  # Código 400: Bad Request

    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            # "relation": dades.relation_user_child,
            # "rol": dades.Role
        }), 200  # Código 200: OK
    else:
        return jsonify({"error": "Usuari no trobat..."}), 404  # Código 404: No encontrado
    
if __name__ == '__main__':
     app.run(debug=True,host="192.168.144.157",port="10050") #,host="0.0.0.0",port="10050"
