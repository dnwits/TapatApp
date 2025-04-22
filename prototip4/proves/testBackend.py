import unittest
import prototip4.proves.test_server2 as test_server2

class TestFuncions(unittest.TestCase):
    def test_login(self):
        self.assertEqual(test_server2.login("mare", "12345"), "Token")
        self.assertEqual(test_server2.login("admin", "1234"), "Error")
        

if __name__ == '__main__':
    unittest.main()