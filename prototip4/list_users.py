import mysql.connector

def list_users():
    try:
        connection = mysql.connector.connect( 
            host="localhost",
            user="root",
            password="root",
            database="tapatapp")
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM User")
        users = cursor.fetchall()
        for user in users:
            print(user)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
if __name__ == '__main__':
    list_users()
    
    # def __init__(self):
    #     self.db_config = mysql.connector.connect (
    #         host="localhost",
    #         user="root",
    #         password="root",
    #         database="tapatapp")  # Configuració de la base de dades
    #     self.cursor = self.db_config.cursor(dictionary=True)
    # def connect(self):
    #     try:
    #         connection = mysql.connector.connect(**self.db_config)
    #         return connection
    #     except mysql.connector.Error as err:
    #         print(f"Error: {err}")
    #         return None
    # def close_connection(self, connection):
    #     if connection:
    #         connection.close()
    # def get_user_by_id(self, user_id):
    #     connection = self.connect()
    #     if not connection:
    #         return None
    #     cursor = connection.cursor(dictionary=True)
    #     query = "SELECT * FROM users WHERE id = %s"
    #     cursor.execute(query, (user_id,))
    #     user = cursor.fetchone()
    #     self.close_connection(connection)
    #     return user  
    # def validate_user(self, username, password):
    #     connection = self.connect()
    #     if not connection:
    #         return None
    #     cursor = connection.cursor(dictionary=True)
    #     query = "SELECT * FROM users WHERE username = %s AND password = %s"
    #     cursor.execute(query, (username, password))
    #     user = cursor.fetchone()
    #     self.close_connection(connection)
    #     return user