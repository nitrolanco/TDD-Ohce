import unittest
import functions 
import datetime

class TestStringMethods(unittest.TestCase):
     
    def test_handle_word(self):  # Accept an optional argument for name_ohce
       
        self.assertEqual(functions.handle_word("hola"), "aloh")
        self.assertEqual(functions.handle_word("chao"), "oahc")
        self.assertEqual(functions.handle_word("oso" ), "oso\n¡Bonita palabra!")

if __name__ == '__main__':
    unittest.main()