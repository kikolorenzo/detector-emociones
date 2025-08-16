import unittest
from traductor import traducir_a_ingles
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

class TestTraductor(unittest.TestCase):

    def setUp(self):
        """Configura el modelo de traductor y el tokenizador para las pruebas."""
        self.modelo = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
        self.tokenizador = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

    def test_traducir_chino_a_ingles(self):
        """Prueba la traducción del chino al inglés."""
        texto_chino = "你好，你好吗？"
        texto_traducido = traducir_a_ingles(texto_chino, self.modelo, self.tokenizador)
        # La traducción puede no ser exacta, así que verificamos las palabras clave
        self.assertIn("Hello", texto_traducido)
        self.assertIn("how", texto_traducido)

    def test_traducir_aleman_a_ingles(self):
        """Prueba la traducción del alemán al inglés."""
        texto_aleman = "Hallo, wie geht es Ihnen?"
        texto_traducido = traducir_a_ingles(texto_aleman, self.modelo, self.tokenizador)
        self.assertIn("Hello", texto_traducido)
        self.assertIn("how", texto_traducido)

if __name__ == '__main__':
    unittest.main()