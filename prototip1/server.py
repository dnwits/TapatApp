class User:
    def __init__(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__(self):
        return "ID: "+ str(self.id)+"\n"+"Usuari:" + self.username+"\n" +"Email: " + self.email

listUsers=[
    User(1, "usuari1", "12345", "user1@gmail.com"),
    User(2, "usuari2", "12345", "user2@gmail.com"),
    User(3, "usuari3", "meow1", "user3@xtec.cat"),
    User(4, "usuari4", "meow4", "user4@xtec.cat")
]

for u in listUsers:
    print(u)

class DAOUsers:
    def __init__(self):
        self.users=listUsers

    def getUserByUsername(self,username):
        for u in self.users:
            if u.username == username:
                print("\n"+str(u)+ " existeix :3")
                return u
        return None
        
daoUser= DAOUsers()

u=daoUser.getUserByUsername("usuari1")

# if (u):
#     print(str(u)+ "existeix :3")
# else:
#     print("no trobat")
app = Flask(__name__)
@app.route('hello', methods=['GET'])
def hello():
    return "Hello World :3"
if __name__== '__main__':
    app.run(debug=True) #,host="0.0.0.0",port="10100"