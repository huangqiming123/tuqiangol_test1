import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.user_center import UserCenterPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


class TestCase201UserCenterModifyInfo(unittest.TestCase):
    # 测试个人中心修改资料
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.user_center_page = UserCenterPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.clear_cookies()
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.log_in_base.log_in()

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_info(self):
        # 通过csv测试修改资料功能
        self.account_center_page_navi_bar.click_account_center_button()

        csv_file = self.account_center_page_read_csv.read_csv('user_to_modify_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            user_to_modify_info = {
                "username": row[0],
                "phone": row[1],
                "email": row[2]
            }
            # 获取当前登录账号
            log_in_account = self.log_in_base.get_log_in_account()

            # 从数据库获取登录账号的客户名称、电话、邮箱
            account_info = self.user_center_page.get_account_info(log_in_account)
            print(account_info)
            # 点击个人中心 - 修改资料
            self.user_center_page.click_user_center_button()
            self.user_center_page.click_modify_user_info()
            # 获取修改资料里面的信息
            user_account = self.user_center_page.get_user_account_in_modify_page()
            user_name = self.user_center_page.get_user_name_in_modify_page()
            user_phone = self.user_center_page.get_user_phone_in_modify_page()
            user_email = self.user_center_page.get_user_email_in_modify_page()
            # 断言
            self.assertEqual(log_in_account, user_account)
            self.assertEqual(account_info[0], user_name)
            self.assertEqual(account_info[1], user_phone)
            self.assertEqual(account_info[2], user_email)

            # 填写客户名称、电话、邮箱
            self.user_center_page.add_data_to_modify_info(user_to_modify_info)
            # 点击取消的按钮
            self.user_center_page.click_cancel_button()
            # 从数据库获取登录账号的客户名称、电话、邮箱
            account_info1 = self.user_center_page.get_account_info(log_in_account)
            print(account_info1)
            self.assertEqual(account_info, account_info1)

            # 点击个人中心 - 修改资料
            self.user_center_page.click_user_center_button()
            self.user_center_page.click_modify_user_info()
            # 获取修改资料里面的信息
            user_account = self.user_center_page.get_user_account_in_modify_page()
            user_name = self.user_center_page.get_user_name_in_modify_page()
            user_phone = self.user_center_page.get_user_phone_in_modify_page()
            user_email = self.user_center_page.get_user_email_in_modify_page()
            # 断言
            self.assertEqual(log_in_account, user_account)
            self.assertEqual(account_info1[0], user_name)
            self.assertEqual(account_info1[1], user_phone)
            self.assertEqual(account_info1[2], user_email)
            # 点击关闭 # 填写客户名称、电话、邮箱
            self.user_center_page.add_data_to_modify_info(user_to_modify_info)
            self.user_center_page.click_close_button()
            # 从数据库获取登录账号的客户名称、电话、邮箱
            account_info2 = self.user_center_page.get_account_info(log_in_account)
            print(account_info2)
            self.assertEqual(account_info, account_info2)

            # 点击个人中心 - 修改资料
            self.user_center_page.click_user_center_button()
            self.user_center_page.click_modify_user_info()
            # 获取修改资料里面的信息
            user_account = self.user_center_page.get_user_account_in_modify_page()
            user_name = self.user_center_page.get_user_name_in_modify_page()
            user_phone = self.user_center_page.get_user_phone_in_modify_page()
            user_email = self.user_center_page.get_user_email_in_modify_page()
            # 断言
            self.assertEqual(log_in_account, user_account)
            self.assertEqual(account_info2[0], user_name)
            self.assertEqual(account_info2[1], user_phone)
            self.assertEqual(account_info2[2], user_email)
            # 填写客户名称、电话、邮箱
            self.user_center_page.add_data_to_modify_info(user_to_modify_info)
            # 点击确认
            self.user_center_page.click_ensure_button()
            # 从数据库获取登录账号的客户名称、电话、邮箱
            account_info3 = self.user_center_page.get_account_info(log_in_account)
            print(account_info3)
            web_data = [user_to_modify_info['username'], user_to_modify_info['phone'], user_to_modify_info['email']]
            self.assertEqual(account_info3, web_data)
            # 点击个人中心 - 修改资料
            self.user_center_page.click_user_center_button()
            self.user_center_page.click_modify_user_info()
            # 获取修改资料里面的信息
            user_account = self.user_center_page.get_user_account_in_modify_page()
            user_name = self.user_center_page.get_user_name_in_modify_page()
            user_phone = self.user_center_page.get_user_phone_in_modify_page()
            user_email = self.user_center_page.get_user_email_in_modify_page()
            # 断言
            self.assertEqual(log_in_account, user_account)
            self.assertEqual(account_info3[0], user_name)
            self.assertEqual(account_info3[1], user_phone)
            self.assertEqual(account_info3[2], user_email)
            self.user_center_page.click_close_button()
        csv_file.close()
