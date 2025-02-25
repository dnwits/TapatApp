''' Aquest client de consola fa el següent:
Recull el username de l'usuari.
Obté la informació de l'usuari pel seu username.
'''

import requests

# Clase User
class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
    
    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"

# Clase Child
class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Sleep Average: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}h"

# Clase UserDAO
class UserDAO:
    def get_user_by_username(username):
        response = requests.get(f'http://localhost:10050/prototip2/getuser?username={username}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None

# Clase ViewConsole
class ViewConsole:
    def getInputUsername():
        return input("Enter username: ")

    def showUserInfo(username):
        user = UserDAO.get_user_by_username(username)
        if user:
            print(f"\nUser Info: {user}")
            ViewConsole.show_children_info(username)
        else:
            print("User not found.")

    # def showChildrenInfo(username):
    #     children = ChildDAO.get_children_by_username(username)
    #     if children:
    #         print("\nChildren Information:")
    #         for child in children:
    #             print(child)
    #     else:
    #         print("\nThis user has no associated children.")

if __name__ == "__main__":
    username = ViewConsole.getInputUsername()
    ViewConsole.showUserInfo(username)
