''' Aquest client de consola fa el següent:
Recull el username de l'usuari.
Obté la informació de l'usuari pel seu username.
'''

import requests

# Classe User
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
    
    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"

# Classe Child
class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Sleep Average: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}h"

# Classe UserDAO
class UserDAO:
    def get_user_by_username(username):
        response = requests.get(f'http://localhost:10050/prototip2/getuser?username={username}')
        #response = requests.get(f'http://localhost:10050/prototip2/getuser/{username}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None
        
# Classe ChildDAO
class ChildDAO:
    BASE_URL = "http://localhost:10050/prototip2"

    @staticmethod
    def get_children_by_username(username):
        response = requests.get(f'{ChildDAO.BASE_URL}/getchildren/{username}')
        if response.status_code == 200:
            children_data = response.json()
            children = [Child(c["id"], c["name"], c["sleep_average"], c["treatment"], c["time"]) for c in children_data]
            return children
        else:
            print(f"Error: {response.json().get('error', 'No se pudo obtener la información de los niños')}")
            return None
# Classe ViewConsole
class ViewConsole:
    def getInputUsername():
        return input("Enter username: ")

    def showUserInfo(username):
        user = UserDAO.get_user_by_username(username)
        if user:
            print(f"User Info: {user}")
        else:
            print(f"User with username {username} not found")

    def showChildrenInfo(username):
        children = ChildDAO.get_children_by_username(username)
        if children:
            print("\nChildren Information:")
            for child in children:
                print(child)
        else:
            print("\nThis user has no associated children.")

if __name__ == "__main__":
    username = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(username)