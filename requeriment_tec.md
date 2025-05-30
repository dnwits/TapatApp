# Requeriments tècnics
## 1. Backend (Servidor i Gestió de Dades)
El backend serà el cor del sistema, encarregat de gestionar dades, usuaris, i la lògica del sistema.

### a. Requisits del servidor
- Allotjament: hosting compartit
- Base de dades: MySQL
- Sistema operatiu del servidor: Linux
- APIs i serveis web: RESTFul i Flask
### b. Llenguatges de programació
- Llenguatge de programació: Python(?)
### c. Seguretat
- Autenticació i autorització: login (usuari i password) 
- Xifratge de dades: token SHA512
- Còpies de seguretat automàtiques: si, cada dia pero deixant a l'usuari decidir si es canvia els intervals de temps.

## 2. Frontend
### a. Tipus de Clients
- Web i Mòbil
- Llenguatge de programació: Java, Python(?)
- Compatibilitat dispositius: Android, iOS, Windows.

## 3. Requisits Generals
### a. Gestió d'usuari i autenticació
- Rols d’usuari: administradors, cuidadors, pacients.
- Base de dades: MariaDB
- Seguretat: Password en Md5 en BBDD
- Autenticació: login usuari o mail i contrasenya, per Token

### b. Emmagatzematge local i sincronització
- Dades que es guarden en local, són sensibles? si, noms, historia medica dels pacients
- Seguretat: HTTPS, validació per token

### c. Gestió d’accessibilitat
- Nivells A, AA y AAA d’accessibilitat: AA (si es pot AAA)

## 4. Requisits d'Infraestructura
- Xarxa i comunicació HTTPS (xarxa)
- Espai d’emmagatzematge al núvol: Depen del hosting compartit (1Tb)
- APIs de tercers: no

## 5. Requisits del Procés de Desenvolupament
- IDE’s: VScode , Miniconda3 (python)
- Extensions VSCode: python, python snippets
- Control de Versions: Git, GitHub
- Mètode de desenvolupament: Seguir una metodologia àgil com Scrum per iterar i validar funcionalitats amb usuaris reals.
- Proves de qualitat (QA): Tests de proves Unitàries