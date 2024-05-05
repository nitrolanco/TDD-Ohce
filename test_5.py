import unittest
import functions 
import datetime

class TestStringMethods(unittest.TestCase):
     
    def test_start(self):  # Accept an optional argument for name_ohce
       
        self.assertEqual(functions.start_game("ohce Anibal"), "Anibal")
        self.assertEqual(functions.start_game("ohce"), None)
        self.assertEqual(functions.start_game("Anibal" ), None)

if __name__ == '__main__':
    unittest.main()