import unittest
import functions 
import datetime

class TestStringMethods(unittest.TestCase):
     
    def test_welcome(self):  # Accept an optional argument for name_ohce
       
        self.assertEqual(functions.greet(time=21, name="Anibal"), "¡Buenas noches Anibal!")
        self.assertEqual(functions.greet(time= 7, name = "Anibal"), "¡Buenos dias Anibal!")
        self.assertEqual(functions.greet(time =13, name = "Anibal" ), "¡Buenas tardes Anibal!")

if __name__ == '__main__':
    unittest.main()