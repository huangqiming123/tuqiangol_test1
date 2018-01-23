import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage

__author__ = ''

class TestCase101LoginSuccessWithSalesAndAgent(unittest.TestCase):
    # 测试登录代理商和销售类型的客户
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.log_in_read_csv = LogInPageReadCsv()
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_sales_and_agent_login_by_csv(self):
        # 通过csv测试销售和代理商账户成功登录和成功退出功能

        csv_file = self.log_in_read_csv.read_csv('login_with_sales_and_agent_user.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            user_to_login = {
                "account": row[0],
                "passwd": row[1]
            }
            # 打开途强在线首页-登录页
            self.base_page.open_page()
            # 输入用户信息进行登录
            self.login_page.user_login(user_to_login["account"], user_to_login["passwd"])
            # 点账户中心
            current_handle = self.driver.get_current_window_handle()
            print('handle', current_handle)
            self.account_center_page_navi_bar.click_account_center_button()
            self.base_page.change_windows_handle(current_handle)

            # 判断登录成功后跳转页面是否正确
            actual_url = self.driver.get_current_url()
            expect_url = self.base_url + "/customer/toAccountCenter"
            self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")
            sleep(1)
            # 断言当前登录账号的用户名
            usr_info_account = self.account_center_page_navi_bar.usr_info_account()
            expect_usr_info_account = user_to_login["account"]
            self.assertIn(expect_usr_info_account, usr_info_account, "账户总览左下方显示的账户错误")

            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_account_user_info_sql = "SELECT o.type,o.phone,o.parentId,o.nickName,o.companyName from user_info o WHERE o.account = '" + \
                                        user_to_login['account'] + "';"
            cursor.execute(get_account_user_info_sql)
            get_account_user_info = cursor.fetchall()
            current_user_info = []
            for range1 in get_account_user_info:
                for range2 in range1:
                    current_user_info.append(range2)
            cursor.close()
            connect.close()
            print("当前号", current_user_info)

            # 客户名称
            user_name = self.login_page.get_user_name()
            self.assertEqual(user_name, current_user_info[3])

            # 获取登录之后用户的公司名称
            company_name = self.login_page.get_company_name()
            if current_user_info[4] == '':
                self.assertEqual('', company_name)
            else:
                self.assertEqual(current_user_info[4], company_name)

            # 客户类型
            type = self.assert_text.log_in_page_account_type(current_user_info[0])
            usr_info_type = self.login_page.get_account_user_type()
            self.assertEqual(type, usr_info_type, "账户总览左下方显示的客户类型错误")

            # 电话
            usr_info_phone = self.login_page.get_account_user_telephone()
            expect_usr_info_phone = current_user_info[1]
            if expect_usr_info_phone == None:
                self.assertEqual("", usr_info_phone, "账户总览左下方显示的客户电话错误")
            else:
                self.assertEqual(expect_usr_info_phone, usr_info_phone, "账户总览左下方显示的客户电话错误")
            # 成功退出系统
            sleep(2)

            self.account_center_page_navi_bar.usr_logout()
            # 判断是否成功退出到登录页
            self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
        csv_file.close()
