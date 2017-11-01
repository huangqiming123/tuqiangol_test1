import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
import csv


# 账户中心招呼栏修改资料---异常操作
# author:戴招利
class TestCase271AccountCenterModifyInfoException(unittest.TestCase):
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

    def test_modify_info_exception(self):
        "修改资料错误提示"

        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        self.driver.wait(1)
        # 点击招呼栏的修改资料
        self.account_center_page_navi_bar.click_modify_usr_info()

        csv_find = self.account_center_page_read_csv.read_csv("modify_info_exception.csv")
        csv_data = csv.reader(csv_find)
        for row in csv_data:
            data = {
                "name": row[0],
                "phone": row[1],
                "email": row[2],
                "name_prompt": row[3],
                "phone_prompt": row[4],
                "email_prompt": row[5]
            }

            all_prompt = self.account_center_page_navi_bar.get_modify_info_exception_prompt(data)

            self.assertEqual(data["name_prompt"], all_prompt["name"], "个人资料，客户名称错误提示语显示不一致")

            self.assertEqual(data["phone_prompt"], all_prompt["phone"], "个人资料，电话错误提示语显示不一致")

            self.assertEqual(data["email_prompt"], all_prompt["email"], "个人资料，邮箱错误提示语显示不一致")

        # 验证长度
        len = self.account_center_page_navi_bar.get_modifgy_info_element_len()
        self.assertEqual(20, len["phone_len"], "电话号码长度显示不一致")
        self.assertEqual(50, len["email_len"], "邮箱长度显示不一致")

        csv_find.close()
        # 关闭修改资料框
        self.account_center_page_navi_bar.cancel_modify_user_info()
        # 退出
        # self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
