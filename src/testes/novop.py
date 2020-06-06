# Configurações e Importações
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TesteGoogle(unittest.TestCase):
    # Antes do teste acontecer
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')

    def test_title(self):
        title = self.driver.title
        assert title == "Google"

    # depois do teste acontecer
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
