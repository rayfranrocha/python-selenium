# Configurações e Importações
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Instanciação do Webdriver
class Exemplo(unittest.TestCase):
    # Antes do teste acontecer
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.cea.com.br/')

    def test_produto_existente(self):
        search_field = self.driver.find_element_by_id('q')
        search_button = self.driver.find_element_by_class_name('busca__button')
        search_field.send_keys('Paco Rabanne')
        search_button.click()
        self.assertTrue(
            '101' in self.driver.page_source)

    def test_produto_nao_existente(self):
        search_field = self.driver.find_element_by_id('q')
        search_button = self.driver.find_element_by_class_name('busca__button')
        search_field.send_keys('Quasar')
        search_button.click()
        self.assertTrue(
            'Não encontramos nenhum resultado para sua busca' in self.driver.page_source)

    # depois do teste acontecer
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
