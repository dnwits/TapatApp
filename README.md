# Descripció del projecte TapatApp
Una cataracta congènita és l'opacitat del cristal·lí de l'ull present des del naixement. La incidència de cataracta congènita és d'aproximadament 3 de cada 10.000 nens al cap d'un any de vida. A l'Hospital de Sant Joan de Déu s'han operat al voltant de 100 cataractes infantils durant l'últim any. Les cataractes són la causa més freqüent de ceguesa tractable en la infància, i es calcula que hi ha al voltant de 200.000 nens cecs per cataractes arreu del món.

L'ull amb cataracta congènita, un cop operat, ha de seguir un règim exhaustiu de rehabilitació per evitar l'ambliopia, coneguda comunament com a "ull gandul". Aquí és on TapatApp! vol ajudar.

A més del tractament amb lents de contacte d'alta graduació i, posteriorment, lents intraoculars, el tractament més eficaç en aquesta patologia consisteix en l'aplicació d'un pegat (parxe) a l'ull dominant. Això força l'ull operat a desenvolupar-se al màxim. El repte consisteix a aplicar aquest tractament de manera equilibrada per aconseguir el màxim desenvolupament de l'ull operat sense penalitzar l'ull dominant, que també ha d'"aprendre a veure" durant l'anomenada etapa plàstica del cervell, que finalitza entre els 6 i 8 anys.

Durant aquesta etapa, el tractament amb pegat varia en funció de l'edat del nen. S'inicia aplicant-lo durant la meitat del temps que el nen estigui despert durant els primers mesos de vida i es continua amb un temps fix diari que estableix l'oftalmòleg. La dificultat real d'aquest procés rau en controlar el nombre de minuts que el nen porta o li queda per portar el pegat, ja que el seu patró de son és variable i freqüent durant el dia. Moltes famílies manifesten la dificultat de gestionar aquest temps a causa de les freqüents migdiades dels petits i la incertesa de quan es tornaran a adormir al llarg del dia.

L'objectiu de TapatApp és proporcionar a totes les famílies afectades per cataracta congènita, o per qualsevol patologia que requereixi pegat ocular, una eina senzilla i gratuïta que els ajudi a seguir aquest tractament de manera equilibrada. Això permet obtenir el màxim desenvolupament de l'agudesa visual.

## Objectius del Projecte
- Controlar el temps que el nen porta el pegat ocular.
- Desenvolupar una aplicació mòbil per a Android.
- Diferenciar entre el temps relatiu del pegat per a infants menors de 6 mesos i el temps absolut per a nens més grans de 6 mesos.
- Crear una aplicació multiusuari que permeti a diversos cuidadors gestionar el control del tractament.
- Restar el temps que el nen passa adormit.
- Implementar un sistema intel·ligent (intel·ligència artificial) amb notificacions per preveure quan el pegat està a punt de completar el seu temps.

## Requeriments Funcionals del Projecte
- Servidor per allotjar la part de backend.
- Desenvolupar el backend de l'aplicació amb serveis web.
- Desenvolupar el frontend de l'aplicació mòbil.
- Possibilitat de crear una web quan l'aplicació estigui en producció.

## Requeriments tècnics
[Requeriments tècnics](requeriment_tec.md)

## HTTP Request / Response
[HTTP request i response](req_resp.md)

## Definició dels EndPoints del WebService
Definició dels EndPoints del Servei Web:

Què necessitem per cada End-point

- Descripció: saber si un usuari existeix al sistema
- HOST: http://192.168.144.157:10050/
- End-point (URL): /prototip/getuser/<username>
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