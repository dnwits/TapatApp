from flask import Flask, request, jsonify
# Definir la clase User con sus atributos (en python solo se puede 1 constructor)
class User:
    def __init__(self, id, username, password, email=""): #email amb valor per defecte (vacio)
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    # def __str__(self):
    #     return "ID: "+ str(self.id)+"\n"+"Usuari:" + self.username+"\n" +"Email: " + self.email

# Crear lista de usuarios (id, username, pass y email)
listUsers=[
    User(1, "usuari1", "12345", "user1@gmail.com"),
    User(2, "usuari2", "12345", "user2@gmail.com"),
    User(3, "usuari3", "meow1", "user3@xtec.cat"),
    User(4, "usuari4", "meow4", "user4@xtec.cat")
]

# Crear objeto para verificar si el usuario existe (buscando en la lista de users)
class DAOUsers:
    def __init__(self):
        self.users=listUsers
    # Crear metodo que hace la busqueda
    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                return u #.__dict__
        return None
    
# declara que utilizaremos flask
# variable que llama al metodo DAOUsers de antes
app = Flask(__name__)       
daoUser= DAOUsers()

@app.route('/hello', methods=['GET'])
def hello():
    user = str(request.args.get('username'))
    return jsonify(daoUser.getUserByUsername("usuari1"))


# Nuevo endpoint para buscar usuarios por username
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
            "email": user.email
        }), 200  # Código 200: OK
    else:
        return jsonify({"error": "Usuari no trobat..."}), 404  # Código 404: No encontrado
    
# CLASE 21/01/25 BIEN!!!!!!!!!!!!!!
@app.route('/tapatapp/getuser', methods=['GET'])
def getUser():
    n = str(request.args.get('name'))
    email = str(request.args.get('email'))
    return "Hello :3            "+"Nom: "+n+", email: "+email

if __name__ == '__main__':
     app.run(debug=True,host="192.168.144.157",port="10050") #,host="0.0.0.0",port="10050"
