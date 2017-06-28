import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.base.base_page_server import BasePageServer
from pages.login.login_page import LoginPage


# 登录页点击忘记密码
# author:孙燕妮

class TestCase005LoginForgetPasswd(unittest.TestCase):
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

    def test_login_forget_passwd(self):
        '''测试忘记密码功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 点击忘记密码
        self.login_page.forget_password()
        self.driver.wait()

        # 断言找回密码的文本框
        self.assertEqual(self.assert_text.log_in_page_find_password_text(),
                         self.login_page.get_text_after_forget_password())
        # 输入账号
        self.login_page.forget_passwd_account("test_007")
        # 输入电话
        self.login_page.forget_passwd_phone("13530050000")
        # 取消修改密码
        self.login_page.dis_forget_passwd()
        self.driver.wait()
        # 通过能否获取到登录按钮的文本内容来判断是否成功取消弹框
        login_button_text = self.login_page.login_button_text()
        self.assertEqual(self.assert_text.log_in_page_log_in_text(), login_button_text)
