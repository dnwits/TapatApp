# Prototip 2

##  Implementació Prototip 2
[Wireframe prototip 2](wireframe_prototip2.mermaid)

### Backend:

***Base de dades***:
- Importar les dades del usuaris per fer funcionar el servei (DAOUsers).
- Importar les dades del nens per fer funcionar el servei (DAOChild).
- Relacionar obj user & child (relation & treatement).


### Frontend:

[Frontend prototip 2](dgrm_class_frontend_p2.mermaid)

### Backend:

[Backend prototip 2](dgrm_class_backend_p2.mermaid)

***Vista de Login***:
- Descripció: pantalla de Login on l'usuari es validarà
- Inputs: Usuari (email o username) i Contrasenya
- Botó: "Iniciar sessió", "Registrar-se", "He oblidat la contrasenya"

***Vista per Restablir contrasenya***:
- Descripció: formulari per restablir contrasenya 
- Inputs: Email, nova contrasenya
- Botó: "Enviar enllaç de restabliment"

***Vista de Registre***:
- Descripció: formulari de Registre d'Usuari 
- Inputs: Usuari (email o username) i Contrasenya
- Botó: "Crear compte"

***Vista de Llistat nens***:
- Descripció: mostra els nens assignats al cuidador
- Opcions: Seleccionar nen
- Botó: "Afegir un nen nou", seleccionar nen (click a sobre)

***Vista per Afegir un nen***:
- Descripció: formulari per afegir nen
- Input: Nom del nen, Edat, tractament (hores o percentatge)
- Botó: "Afegir", "Cancelar"

***Vista d'Informació del nen***:
- Descripció: pantalla per mostrar informació del nen i estat tap
- Input: estat del tap
- Botó: "Desar canvis", "Cancelar"

##  Diagrama final arquitectura Prototip 2
[Arquitectura prototip 2](dgrm_arch_p2.mermaid)
