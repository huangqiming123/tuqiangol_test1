import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 账户中心招呼栏修改密码
# author:孙燕妮

class TestCase010AccountCenterModifyPasswd(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_modify_info(self):
        '''通过csv测试修改密码功能'''
        csv_file = self.account_center_page_read_csv.read_csv('user_to_modify_passwd.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            user_to_modify_passwd = {
                "account": row[0],
                "old_passwd": row[1],
                "new_passwd": row[2],
            }

            # 打开途强在线首页-登录页
            self.base_page.open_page()
            # 登录账号
            self.login_page.user_login(user_to_modify_passwd["account"],
                                       user_to_modify_passwd["old_passwd"])
            self.driver.wait()
            # 招呼栏修改资料
            modify_status = self.account_center_page_navi_bar.modify_user_passwd(user_to_modify_passwd["old_passwd"],
                                                                                 user_to_modify_passwd["new_passwd"])
            # 判断是否修改成功
            self.assertEqual("密码修改成功", modify_status, "密码修改失败")
            # 点击确定
            self.account_center_page_navi_bar.modify_passwd_success_comfrim()
            # 判断点击确定后是否关闭弹框并回到登录页
            self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "修改成功后页面跳转错误")


            # 登录账号
            self.login_page.user_login(user_to_modify_passwd["account"],
                                       user_to_modify_passwd["new_passwd"])

            self.driver.wait()
            # 招呼栏修改资料
            modify_status = self.account_center_page_navi_bar.modify_user_passwd(user_to_modify_passwd["new_passwd"],
                                                                                 user_to_modify_passwd["old_passwd"])
            # 判断是否修改成功
            self.assertEqual("密码修改成功", modify_status, "密码修改失败")
            # 点击确定
            self.account_center_page_navi_bar.modify_passwd_success_comfrim()
            # 判断点击确定后是否关闭弹框并回到登录页
            self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "修改成功后页面跳转错误")
        csv_file.close()
