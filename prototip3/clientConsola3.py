# Aquest client de consola fa el següent:
# Recull el username de l'usuari.
# Obté la informació de l'usuari pel seu username.

import requests

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"[User] ID: {self.id}, Username: {self.username}, Email: {self.email}"

class Child:
    def __init__(self, id, name, sleep_average, treatment, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment = treatment
        self.time = time

    def __str__(self):
        return f"[Child] ID: {self.id}, Name: {self.name}, Sleep Avg: {self.sleep_average}, Treatment: {self.treatment}, Time: {self.time}h"

class APIClient:
    BASE_URL = "http://localhost:5000/prototip3"  # puerto por defecto def en server2.py y para no copiar la url cada vez
    token = None  # Per guardar el token
   
    @staticmethod
    def login(username, password):
        try:
            response = requests.post(f"{APIClient.BASE_URL}/login", json={"username": username, "password": password})
            if response.status_code == 200:
                data = response.json()
                APIClient.token = data["token"]  # Guardem el token per a futures peticions
                print("Login correcte!")
                return User(data['id'], data['username'], data['email']) 
            else:
                print(f"Error: {response.json().get('error', 'Usuari o contrasenya incorrectes')}")
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None
        
    @staticmethod
    def get_user(username):
        if not APIClient.token: #si no hi ha token
            print("Error: No estàs autenticat. Fes login primer.")
            return None
        try:
            headers = {"Authorization": APIClient.token}
            response = requests.get(f"{APIClient.BASE_URL}/getuser", headers=headers)
            #response = requests.get(f"{APIClient.BASE_URL}/getuser", params={"username": username})
            if response.status_code == 200:
                data = response.json()
                return User(data['id'], data['username'], data['email'])
            else:
                #print(f"Error: {response.json().get('error', 'Usuari no trobat')}")
                print(f"Error: {response.json().get('error', 'No es pot obtenir l’usuari')}")
                return None
        except Exception as e:
            print(f"Connection Error: {e}")
            return None

    @staticmethod
    def get_children(username):
        try:
            response = requests.get(f"{APIClient.BASE_URL}/getchildren/{username}")
            # if response.status_code == 200:
            #     children = response.json()
            #     return [Child(c["id"], c["name"], c["sleep_average"], c["treatment_id"], c["time"]) for c in children]
            if response.status_code == 200:
                children_data = response.json()
                return [Child(c["id"], c["name"], c["sleep_average"], c["treatment"], c["time"]) for c in children_data]
            else:
                print(f"Error: {response.json().get('error', 'No children found')}")
                return []
        except Exception as e:
            print(f"Connection Error: {e}")
            return []
     
class ConsoleView:
    logged_user = None

    @staticmethod
    def login():
        username = input("Introdueix el nom d'usuari: ")
        password = input("Introdueix la contrasenya: ")
        ConsoleView.logged_user = APIClient.login(username, password)

    @staticmethod
    def menu():
        print("\n--- MENÚ ---")
        print("1. Consultar informació de l'usuari")
        print("2. Consultar nens de l'usuari")
        print("3. Sortir")

    @staticmethod
    def run():
        print("=== Benvingut a TapadApp! ===")
        # while True:
        #     ConsoleView.menu()
        #     option = input("Selecciona una opció: ")

        #     if option == "1":
        #         username = input("Introdueix el nom d'usuari: ")
        #         password = input("Introdueix la contrasenya: ")
        #         APIClient.login(username, password)

        #     elif option == "2":
        #         user = APIClient.get_user()
        #         if user:
        #             print(user)

        #     elif option == "3":
        #         print("Adeu!")
        #         break

        #     else:
        #         print("Opció incorrecta. Torna a intentar-ho.")
        ConsoleView.login()

        if ConsoleView.logged_user:
            while True:
                ConsoleView.menu()
                option = input("Selecciona una opció: ")

                if option == "1":
                    print(ConsoleView.logged_user)

                elif option == "2":
                    children = APIClient.get_user() #APIClient.get_children(ConsoleView.logged_user.username)
                    if children:
                        for child in children:
                            print(child)
                    else:
                        print("Aquest usuari no té nens associats")

                elif option == "3":
                    print("Adeu!")
                    break

                else:
                    print("Opció incorrecta. Torna a intentar-ho.")
        else:
            print("No s'ha pogut iniciar sessió.")

if __name__ == "__main__":
    ConsoleView.run()
