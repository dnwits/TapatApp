import unittest
def suma(a, b):
    #Retorna la suma de dos nombres.
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma(self): 
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(2, 3), 5)
        # self.assertEqual(suma(-1, 1), 0)
        # self.assertEqual(suma(-1, -1), -2)
        # self.assertEqual(suma(1, -1), 0)
        # self.assertEqual(suma(1, 0), 1)
        # self.assertEqual(suma(0, 1), 1)
        # self.assertEqual(suma(0, -1), -1)
    

if __name__ == '__main__':
    unittest.main()