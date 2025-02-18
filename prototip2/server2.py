from flask import Flask, request, jsonify
import dadesServer as dades
from dadesServer import User, Child, users, children, relation_user_child

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
    
# class DAOChild(id_user):
#     def __init__(self):
#         self.id=dades.users
#     def getChildByUserId(self,id):
class DAOChild:
    def __init__(self):
        self.children = children
        self.relations = relation_user_child

    def getChildrenByUserId(self, user_id):
        result = []
        for relation in self.relations:
            if relation["user_id"] == user_id:
                for child in self.children:
                    if child.id == relation["child_id"]:
                        result.append(child)
        return result
# declara que utilizaremos flask
# variable que llama al metodo DAOUsers de antes
app = Flask(__name__)
daoUser = DAOUsers()
daoChild = DAOChild()

# Endpoints
@app.route('/prototip2/getuser/', defaults={'username': None}, methods=['GET'])
@app.route('/prototip2/getuser/<username>', methods=['GET'])
def get_user(username):
    if not username:
        return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"}), 400

    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email
        }), 200
    else:
        return jsonify({"error": "Usuari no trobat..."}), 404

@app.route('/prototip2/getchildren/<username>', methods=['GET'])
def get_children(username):
    user = daoUser.getUserByUsername(username)
    if not user:
        return jsonify({"error": "Usuari no trobat..."}), 404

    children = daoChild.getChildrenByUserId(user.id)
    if children:
        return jsonify([
            {
                "id": child.id,
                "name": child.child_name,
                "sleep_average": child.sleep_average,
                "treatment_id": child.treatment_id,
                "time": child.time
            } for child in children
        ]), 200
    else:
        return jsonify({"error": "Aquest usuari no té nens associats"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="192.168.144.157", port=10050)