import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.base.base_page_server import BasePageServer
from pages.login.login_page import LoginPage

__author__ = ''

class TestCase106LoginChangeLanguage(unittest.TestCase):
    # 切换语言
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_change_language(self):
        '''测试登录切换语言'''
        language = ["English", "España", "Portugal", "Polska", "Deutschland"]

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 通过登录按钮的文本内容判断默认是否为中文
        login_button_text = self.login_page.login_button_text()
        self.assertEqual(self.assert_text.log_in_page_log_in_text(), login_button_text)

        # 切换语言
        login_button_text = self.login_page.change_language(language[0])
        # 通过登录按钮的文本内容判断默认是否与所切换的语言一致
        self.assertEqual("Log in", login_button_text[0])
        self.assertEqual("Input Account", login_button_text[1])
        self.assertEqual("Input password", login_button_text[2])

        login_button_text = self.login_page.change_language(language[1])
        # 通过登录按钮的文本内容判断默认是否与所切换的语言一致
        self.assertEqual("Ingresar", login_button_text[0])
        self.assertEqual("Ingrese cuenta", login_button_text[1])
        self.assertEqual("Ingrese contraseña", login_button_text[2])

        login_button_text = self.login_page.change_language(language[2])
        # 通过登录按钮的文本内容判断默认是否与所切换的语言一致
        self.assertEqual("Iniciar", login_button_text[0])
        self.assertEqual("Digitar conta", login_button_text[1])
        self.assertEqual("Digitar password", login_button_text[2])

        login_button_text = self.login_page.change_language(language[3])
        # 通过登录按钮的文本内容判断默认是否与所切换的语言一致
        self.assertEqual("Zaloguj", login_button_text[0])
        self.assertEqual("Wprowadz konto", login_button_text[1])
        self.assertEqual("Wprowadz haslo", login_button_text[2])

        login_button_text = self.login_page.change_language(language[4])
        # 通过登录按钮的文本内容判断默认是否与所切换的语言一致
        self.assertEqual("Einloggen", login_button_text[0])
        self.assertEqual("Konto eingeben", login_button_text[1])
        self.assertEqual("Passwort eintragen", login_button_text[2])
