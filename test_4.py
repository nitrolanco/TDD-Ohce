import unittest
import functions


class TestStringMethods(unittest.TestCase):
    def test_main_loop(self):
        expected_output = f"""{functions.greet(name= "Anibal", time = 12)}
{functions.handle_word("hola")}
{functions.handle_word("vaca")}
{functions.handle_word("oso")}
{functions.handle_stop(name = "Anibal")}"""
        self.assertEqual(
            functions.main_loop(12, "Anibal", "hola", "vaca", "oso", "stop!"), expected_output
        )
        expected_output = f"""{functions.greet(name = "Pedro",time= 24)}
{functions.handle_word("chap")}
{functions.handle_word("chancho")}
{functions.handle_word("sitis")}
{functions.handle_stop(name= "Pedro")}"""
        self.assertEqual(
            functions.main_loop(24, "Pedro", "chap", "chancho", "sitis", "stop!"), expected_output
        )


if __name__ == "__main__":
    unittest.main()
