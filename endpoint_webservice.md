## Definició dels EndPoints del WebService

Què necessitem per cada End-point

- Descripció: saber si un usuari existeix al sistema
- HOST: http://192.168.144.157:10050/
- End-point (URL): /prototip1/getuser/<username>
- Method: GET
- Tipus de petició (headers):

        Content-Type: application/json
        Content-Length: 123
        Date: Mon, 22 Jan 2025 14:00:00 GMT
        Server: Apache/2.4.41 (Ubuntu)

- Parametres que necessita la petició: (identifica els paràmetres i posa exemples en el cas de peticions GET) --> Username
- Resposta: Si l'usuari existeix mostrarà la informació bàsica (username i email) en format json. Si l'username introduït no existeix mostrarà una resposta que indiqui això.
   - Codi 200:

                {
                "email": "user1@gmail.com",
                "id": 1,
                "password": "12345",
                "username": "usuari1"
                }

   - Codi 404 (si l'username introduït no existeix):

                return jsonify({"error": "Usuario no trobat..."})

   - Codi 400 (si no s'introdueix cap username):

                 return jsonify({"error": "No s'ha proporcionat cap nom d'usuari"})