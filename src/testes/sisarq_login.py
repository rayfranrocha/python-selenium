# Configurações e Importações
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TesteSisarq(unittest.TestCase):
    # Antes do teste acontecer
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://iconsti.com/sisarq/')

    def test_1(self):
        title = self.driver.title
        assert "SISARQ" in title, "Teste falhou"

    def test_2(self):
        login = self.driver.find_element_by_id("j_username")
        login.send_keys("teste.sisarq")

        senha = self.driver.find_element_by_id("j_password")
        senha.send_keys("123")

        btnEntrar = self.driver.find_element_by_xpath("//input[@type='submit' and @value='Entrar']")
        btnEntrar.click()

        assert "Suporte 3212-9021" in self.driver.page_source, "Teste falhou"

    def test_3(self):
        login = self.driver.find_element_by_id("j_username")
        login.send_keys("icon")

        senha = self.driver.find_element_by_id("j_password")
        senha.send_keys("senhaincorreta")

        btnEntrar = self.driver.find_element_by_xpath("//input[@type='submit' and @value='Entrar']")
        btnEntrar.click()

        assert "O usuário e senha informados não são válidos!" in self.driver.page_source, "Teste falhou"

    # depois do teste acontecer
    def tearDown(self):
        self.driver.close()
        # self.driver.quit()


if __name__ == "__main__":
    unittest.main()
