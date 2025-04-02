from flask import Flask, request, jsonify, g
import dadesServer as dades
import jwt
import datetime
from functools import wraps
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

class DAORoles:
    def __init__(self):
        self.roles = dades.roles

    def getRolById(self, rol_id):
        for rol in self.roles:
            if rol.id == rol_id:
                return rol.type_rol
        return None
   
class DAOChild:
    def __init__(self):
        self.children = dades.children
        self.relations = dades.relation_user_child
        self.treatments = dades.treatments

    def getChildrenByUserId(self, user_id):
        result = []
        allowed_roles = [1, 2, 3]  # comprovació de rols
        #seen_children = set()  # Para evitar duplicados

        for relation in self.relations:
            if relation.user_id == user_id and relation.rol_id in allowed_roles:
                for child in self.children:
                    if child.id == relation.child_id:
                        treatment = self.getTreatmentById(child.treatment_id)
                        result.append({
                            "id": child.id,
                            "name": child.child_name,
                            "sleep_average": child.sleep_average,
                            "treatment": treatment.name if treatment else "Cap tractament",
                            "time": child.time
                        })
        return result

    def getTreatmentById(self, treatment_id):
        for treatment in self.treatments:
            if treatment.id == treatment_id:
                return treatment
        return None


app = Flask(__name__)
daoChild = DAOChild()
daoUser = DAOUsers()
app.config["SECRET_KEY"] = "1234qwer"  # Canvia això per una clau més segura!
#print(daoChild.getChildrenByUserId(1))  # Debug
# Endpoints
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token d'autenticació requerit"}), 403
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            g.user_id = data["user_id"]  # Guardamos el user_id en g (global de Flask)
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token caducat"}), 403
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token invàlid"}), 403
        return f(*args, **kwargs)  # Continúa con la función decorada
    return decorated

@app.route('/prototip3/login', methods=['POST'])
#@token_required
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    user = daoUser.getUserByUsername(username)
    # if user and user["password"] == password:
    #     return jsonify(user), 200
    # else:
    #     return jsonify({"error": "Usuari o contrasenya incorrectes"}), 401
    if user and user["password"] == password:
        token = jwt.encode(
            {"user_id": user["id"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1000)},
            app.config["SECRET_KEY"],
            algorithm="HS256"
        )
        #return jsonify({"token": token, "username": user["username"], "email": user["email"]}), 200
        return jsonify({
                "token": token,
                "id": user["id"],  # Afegim l'ID de l'usuari
                "username": user["username"],
                "email": user["email"]
            }), 200

    else:
        return jsonify({"error": "Usuari o contrasenya incorrectes"}), 401

from functools import wraps

@app.route('/prototip3/getuser/', methods=['GET'])
@token_required
def get_user(): #user_id se pasa desde token_required
    try:
        user_id = g.user_id  # Obtenemos el user_id del decorador
        user = daoUser.getUserByUsername(user_id)  # Cambia a getUserByUsername si es necesario
        if user:
            return jsonify(user), 200
        else:
            return jsonify({"error": "Usuari no trobat"}), 404
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug
        return jsonify({"error": f"Error inesperat: {str(e)}"}), 500


@app.route('/prototip3/getchildren/', methods=['GET'])
@token_required
def get_children():
    try:
        user_id = g.user_id  # Obtenemos el user_id del decorador
        #print(f"User ID: {user_id}")  # Debug
        children = daoChild.getChildrenByUserId(user_id)
        #print(f"Children: {children}")  # Debug
        return jsonify(children), 200
    except Exception as e:
        #print(f"Error: {str(e)}")  # Debug
        # Capturamos cualquier error inesperado y devolvemos un mensaje de error
        return jsonify({"error": f"Error inesperat: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True) #192.168.144.157 , host="0.0.0.0", port=10050