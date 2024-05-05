import unittest
import functions 
import datetime

class TestStringMethods(unittest.TestCase):
     
    def test_handle_stop(self):  # Accept an optional argument for name_ohce
       
        self.assertEqual(functions.handle_stop("asd"), "Adios asd")
        self.assertEqual(functions.handle_stop("Anibal"), "Adios Anibal")
        self.assertEqual(functions.handle_stop("name"), "Adios name")

if __name__ == '__main__':
    unittest.main()