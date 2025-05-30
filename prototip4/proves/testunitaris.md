# Activitats
1- (testunitaris.md) Què són els tests unitaris?
Són proves que verifiquen que un fragment de codi funciona correctament. Es fan per garantir la qualitat del programari i la satisfacció de l'usuari.
- S'executen de forma aïllada i ràpida.
- Es realitzen immediatament després d'escriure el codi.
- Són fàcils d'automatitzar, Són econòmiques.
- Es poden provar diferents unitats de manera simultània.

2- (testunitaris.md) Fes una recerca de llibreries de test amb Python.  Com funciona específicament la llibreria ***unittest*** de Python?
Llibreries de test amb Python:
- [Pytest](https://docs.pytest.org/en/7.1.x/)
- [Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html)
- [Schemathesis](https://schemathesis.readthedocs.io/en/stable/)
- [Playwright](https://playwright.dev/python/)
- [Unittest](https://docs.python.org/3/library/unittest.html) : El mòdul unittest és un marc de proves integrat a Python, disponible com a part de la biblioteca estàndard. L'objectiu principal del mòdul unittest és facilitar la creació de casos de prova i conjunts de proves per verificar el comportament i la correcció d'unitats de codi individuals.

    - Avantatges de Unittest

        - Ve inclòs amb el llenguatge i és un dels més usats en els projectes Python.
        - Sol tenir compatibilitat amb la resta de llibreries com Pytest, per la qual cosa es recomana començar-hi.
        - Té inclòs un servei de discovery que permet trobar i executar els tests automàticament.
        - Molt senzill dutilitzar, té alguns mètodes que controlen el cicle de vida dels teus tests.

    - Desavantatges

        - Funcionalitats limitades per complementar el testing com saber el coverage de la teva aplicació
        - Sense extensions o sistema de plugins per completar la seva funcionalitat com té pytest.

3-  ([prototip4/testsuma.py](testsuma.py)) Exercici exemple test.
Creació i execució d’un **test senzill amb Python** per exemple testejar una funció de suma. Genera un fitxer python que testeji aquesta funció.
```
def suma(a, b):
    """Retorna la suma de dos nombres."""
    return a + b
```

4- ([prototip4/testfuncions.py](testfuncions.py)) Exercici exemple varies  funcions.
**Testeja més funcions**, afegeix una resta i una divisió (que retorni un error quan la divisió és per 0)  

```
def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b
```

5-  (testunitaris.md) Fes una Llista de les assertions més importants en unittest i explica per a que  serveixen.
**Assertions bàsics de comparació:**
- assertEqual(a, b) :
    - Verifica que a == b
    - Exemple: self.assertEqual(resultat_esperat, resultat_real)
- assertNotEqual(a, b):
    - Verifica que a != b
    - Útil per assegurar que dos valors no són iguals

**Assertions de veritat/falsedat:**
- assertTrue(x):
    - Verifica que x és True
    - Equivalent a self.assertTrue(bool(x))
- assertFalse(x):
    - Verifica que x és False
    - Equivalent a self.assertFalse(bool(x))

**Assertions d'identitat (no igualtat):**
- assertIs(a, b):
    - Verifica que a is b (mateix objecte en memòria)
    - Exemple: self.assertIs(instancia, Singleton.instancia)
- assertIsNot(a, b):
    - Verifica que a is not b
    - Comprova que no són el mateix objecte

**Assertions de valors None:**
- assertIsNone(x):
    - Verifica que x is None
    - Millor que assertEqual(x, None)
- assertIsNotNone(x):
    - Verifica que x is not None
    - Millor que assertNotEqual(x, None)

**Assertions de pertinença:**
- assertIn(a, b):
    - Verifica que a in b
    - Exemple: self.assertIn(element, llista)
- assertNotIn(a, b):
    - Verifica que a not in b
    - Exemple: self.assertNotIn(element_prohibit, llista)

**Assertions de tipus:**
- assertIsInstance(a, b):
    - Verifica que isinstance(a, b)
    - Exemple: self.assertIsInstance(resultat, int)
- assertNotIsInstance(a, b):
    - Verifica que not isinstance(a, b)
    - Exemple: self.assertNotIsInstance(resultat, str)


6-  ([prototip4/testBackend.py](testBackend.py))  Fes els tests Unitaris dels teus DAO i webservice del prototip 2 que tens a la carpeta prototip 3
