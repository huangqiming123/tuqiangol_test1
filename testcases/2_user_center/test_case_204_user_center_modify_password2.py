import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
import csv


class TestCase204UserCenterModifyPassword2(unittest.TestCase):
    # 测试个人中心 - 修改密码异常
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.clear_cookies()

    def test_modify_password_exception(self):

        self.log_in_base.log_in()
        current_handle = self.driver.get_current_window_handle()
        self.account_center_page_navi_bar.click_account_center_button()
        self.base_page.change_windows_handle(current_handle)
        self.driver.wait(1)
        # 点击招呼栏的修改密码
        self.account_center_page_navi_bar.click_modify_usr_password()

        csv_find = self.account_center_page_read_csv.read_csv("modify_password_exception.csv")
        csv_data = csv.reader(csv_find)
        for row in csv_data:
            data = {
                "old_password": row[0],
                "new_password": row[1],
                "new_password2": row[2],
                "old_pwd_prompt": row[3],
                "new_pwd_prompt": row[4],
                "new_pwd2_prompt": row[5]
            }

            all_prompt = self.account_center_page_navi_bar.get_modify_pwd_exception_prompt(data)

            self.assertEqual(data["old_pwd_prompt"], all_prompt["old_Pwd"], "修改密码，旧密码错误提示语显示不一致")

            self.assertEqual(data["new_pwd_prompt"], all_prompt["new_Pwd"], "修改密码，新密码提示语显示不一致")

            self.assertEqual(data["new_pwd2_prompt"], all_prompt["new_Pwd2"], "修改密码，确认新密码提示语显示不一致")

            try:
                self.assertEqual("原密码不正确", all_prompt["text"], "修改密码，提示语显示不一致")
            except:
                print("没有原密码不正确的提示")

        csv_find.close()
        # 关闭修改资料框
        self.account_center_page_navi_bar.click_password_cancel()
        self.driver.wait(1)
        # 退出
        self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
