import unittest
from juego_ppt import determinar_ganador


class TestJuego(unittest.TestCase):

    def test_empates(self):
        self.assertEqual(determinar_ganador("piedra", "piedra"), "empate")
        self.assertEqual(determinar_ganador("papel", "papel"), "empate")
        self.assertEqual(determinar_ganador("tijera", "tijera"), "empate")

    def test_gana_usuario(self):
        self.assertEqual(determinar_ganador("piedra", "tijera"), "usuario")
        self.assertEqual(determinar_ganador("papel", "piedra"), "usuario")
        self.assertEqual(determinar_ganador("tijera", "papel"), "usuario")

    def test_gana_sistema(self):
        self.assertEqual(determinar_ganador("piedra", "papel"), "sistema")
        self.assertEqual(determinar_ganador("papel", "tijera"), "sistema")
        self.assertEqual(determinar_ganador("tijera", "piedra"), "sistema")


if __name__ == "__main__":
    unittest.main()