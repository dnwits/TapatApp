import unittest
def resta(a, b):
    """Retorna la resta de dos nombres."""
    return a - b

def divideix(a, b):
    """Retorna la divisió de dos nombres. Retorna 'Error' si b és 0."""
    if b == 0:
        return "Error: divisió per zero"
    return a / b

class TestFuncions(unittest.TestCase):
    def test_resta(self):
        self.assertEqual(resta(1, 2), -1)
        self.assertEqual(resta(0, 0), 0)
        self.assertEqual(resta(2, 3), -1)
        self.assertEqual(divideix(1, 2), 0.5)
        self.assertEqual(divideix(0, 0), "Error: divisió per zero")
        self.assertEqual(divideix(2, 3), 2/3)

if __name__ == '__main__':
    unittest.main()