import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage


# 登录页点击忘记密码---异常操作
# author:戴招利
class TestCase1102LoginForgetPasswordException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def test_login_forget_passwd(self):
        '''测试忘记密码---异常操作提示'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 点击忘记密码
        self.login_page.forget_password()
        self.driver.wait()
        csv_file = self.log_in_page_read_csv.read_csv('login_forget_pwd_exception.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "account": row[0],
                "phone": row[1],
                "verify_code": row[2],
                "account_prompt": row[3],
                "phone_prompt": row[4],
                "code_prompt": row[5],
                "type": row[6],
                "text": row[7]
            }

            # 找回密码--异常验证
            all_prompt = self.login_page.get_forget_pwd_error_prompt(data)

            self.assertEqual(data["account_prompt"], all_prompt["account_prompt2"], "账号错误提示语显示不一致")
            self.assertEqual(data["phone_prompt"], all_prompt["phone_prompt2"], "手机号错误提示语显示不一致")
            self.assertEqual(data["code_prompt"], all_prompt["code_prompt2"], "验证码错误提示语显示不一致")
            self.assertEqual(data["text"], all_prompt["text_prompt"], "弹框中提示语显示不一致")

        # 点取消
        self.login_page.dis_forget_passwd()
        csv_file.close()

    def tearDown(self):
        self.driver.quit_browser()
