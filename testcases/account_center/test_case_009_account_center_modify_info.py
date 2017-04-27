import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage


# 账户中心招呼栏修改资料
# author:孙燕妮

class TestCase009AccountCenterModifyInfo(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_modify_info(self):
        '''通过csv测试修改资料功能'''
        csv_file = self.account_center_page_read_csv.read_csv('user_to_modify_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            user_to_modify_info = {
                "username": row[0],
                "phone": row[1],
                "email": row[2]
            }
            # 打开途强在线首页-登录页
            self.base_page.open_page()
            # 登录账号
            self.log_in_base.log_in()
            # 招呼栏修改资料
            save_status = self.account_center_page_navi_bar.modify_usr_info(user_to_modify_info["username"],
                                                                            user_to_modify_info["phone"],
                                                                            user_to_modify_info["email"])
            # 判断是否修改成功
            self.assertEqual("操作成功", save_status, "修改失败")
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
