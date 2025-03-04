from flask import Flask, request, jsonify
import dadesServer as dades
#from dadesServer import User, Child, users, children, relation_user_child, treatments

#DAOS DE LES CLASSES QUE UTILITZAREM
class DAOUsers:
    def __init__(self):
        self.users=dades.users
    # Crear metodo que hace la busqueda
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u.__dict__
        return None
    
class DAOChild:
    def __init__(self):
        self.children = dades.children
        self.relations = dades.relation_user_child
        self.treatments = dades.treatments

    def getChildrenByUserId(self, user_id):
        result = []
        for relation in self.relations:
            if relation["user_id"] == user_id:
                for child in self.children:
                    if child.id == relation["child_id"]:
                        # result.append(child)
                        # Buscar el tratamiento asociado
                        treatment = self.getTreatmentById(child.treatment_id)
                        result.append({
                            "id": child.id,
                            "name": child.child_name,
                            "sleep_average": child.sleep_average,
                            "treatment": treatment.name if treatment else "No treatment",
                            "time": child.time
                        })
        return result
    
    def getTreatmentById(self, treatment_id):
        for treatment in self.treatments:
            if treatment.id == treatment_id:
                return treatment
        return None
# declara que utilizaremos flask
# variable que llama al metodo DAOUsers de antes
app = Flask(__name__)
daoChild = DAOChild()
daoUser = DAOUsers()
# Endpoints
# @app.route('/prototip2/getuser/', defaults={'username': None}, methods=['GET'])
# @app.route('/prototip2/getuser/<username>', methods=['GET'])
# def get_user(username):
#     if not username:
#         return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"}), 400

#     user = daoUser.getUserByUsername(username)
#     if user:
#         return jsonify({
#             "id": user.id,
#             "username": user.username,
#             "email": user.email
#         }), 200
#     else:
#         return jsonify({"error": "Usuari no trobat..."}), 404
@app.route('/prototip2/getuser/', methods=['GET'])
def get_user():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"}), 400

    user = daoUser.getUserByUsername(username)
    if user:
        return jsonify({
            "id": user["id"],
            "username": user["username"],
            "email": user["email"]
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
    app.run(debug=True, port=10050) #192.168.144.157 , host="0.0.0.0"