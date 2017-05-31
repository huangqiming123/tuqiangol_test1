import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户详情(快速销售)--添加客户异常操作
# author:戴招利
class TestCase1105AccountCenterOverviewException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_detail = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def test_account_detail_add_user_exception(self):
        '''快速销售---添加用户错误提示'''

        # 登录
        self.log_in_base.log_in()
        # 点击快速销售
        self.account_center_page_detail.fast_sales()
        # 点击添加按钮
        self.account_center_page_detail.click_add_button()

        csv_file = self.account_center_page_read_csv.read_csv('overview_add_user_exception.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "name": row[0],
                "account": row[1],
                "password": row[2],
                "confirm_pwd": row[3],
                "email": row[4],
                "name_prompt": row[5],
                "account_prompt": row[6],
                "pwd_prompt": row[7],
                "pwd2_prompt": row[8],
                "email_prompt": row[9],
                "text": row[10],
            }
            # 取错误提示
            prompt = self.account_center_page_detail.get_add_user_exception_prompt(data)
            self.assertEqual(data["name_prompt"], prompt["name_prompt2"], "客户名称错误提示语显示不一致")

            self.assertEqual(data["account_prompt"], prompt["account_prompt2"], "登录账号错误提示语显示不一致")

            self.assertEqual(data["pwd_prompt"], prompt["pwd_prompt2"], "密码错误提示语显示不一致")

            self.assertEqual(data["pwd2_prompt"], prompt["pwd2_prompt2"], "确认密码错误提示语显示不一致")

            self.assertEqual(data["email_prompt"], prompt["email_prompt2"], "邮箱错误提示语显示不一致")

            self.assertEqual(data["text"], prompt["text2"], "弹框中提示语显示不一致")

        # 取长度
        len = self.account_center_page_detail.get_add_user_element_len()
        self.assertEqual(50, len["name_len"], "客户名称长度显示不一致")
        self.assertEqual(30, len["account_len"], "登录账号长度显示不一致")
        self.assertEqual(20, len["phone_len"], "电话号码长度显示不一致")
        self.assertEqual(50, len["email_len"], "邮箱长度显示不一致")
        self.assertEqual(50, len["contact_len"], "联系人长度显示不一致")
        self.assertEqual(50, len["companyName_len"], "公司名称长度显示不一致")
        # 取消
        self.account_center_page_detail.click_add_cancel_button()
        csv_file.close()
        self.driver.wait()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
