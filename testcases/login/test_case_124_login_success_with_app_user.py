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


# app账号成功登录功能的测试
# author:戴招利

class TestCase124LoginSuccessWithphAppUser(unittest.TestCase):
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

    def test_app_user_login_by_csv(self):
        '''通过csv测试app账户成功登录和成功退出功能'''
        data = ["首页", "设备管理", "操控台", "统计报表", "安全区域", "设备分布"]

        csv_file = self.log_in_read_csv.read_csv('login_with_app_user.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            user_to_login = {
                "account": row[0],
                "passwd": row[1]
            }
            # 打开途强在线首页-登录页
            self.base_page.open_page()
            # 输入用户信息进行登录
            self.login_page.user_login(user_to_login["account"], user_to_login["passwd"])
            # 点首页
            # self.login_page.click_home_page()
            # 判断登录成功后跳转页面是否正确
            actual_url = self.driver.get_current_url()
            expect_url = self.base_url + "/nomalUserCenter"
            self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

            # 判断登录成功后招呼栏的用户名是否正确
            hello_usr = self.account_center_page_navi_bar.hello_user_account()
            expect_usr = user_to_login["account"]
            self.assertEqual(expect_usr, hello_usr, "登录成功后招呼栏账户名显示错误")

            # 验证模块
            module = self.account_center_page_navi_bar.get_page_module()
            for m in range(len(module)):
                self.assertIn(data[m], module[m], "用户账号登录，模块显示错误")

            # 获取当前app账号有几个服务商
            service_number = self.account_center_page_details.get_current_account_service_number()

            # 获取数据库服务商的个数
            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_up_account_info_sql = "select userId from user_info where account = '%s';" % user_to_login['account']

            cursor.execute(get_up_account_info_sql)
            get_up_user_info = cursor.fetchall()
            get_current_id = []
            for range1 in get_up_user_info:
                for range2 in range1:
                    get_current_id.append(range2)
            print(get_current_id)

            get_service_sql = "select userId from equipment_mostly where bindUserId = '" + get_current_id[
                0] + "' group by userId ;"
            cursor.execute(get_service_sql)
            get_service = cursor.fetchall()
            service_number_list = []
            for range1 in get_service:
                for range2 in range1:
                    service_number_list.append(range2)
            service_total = len(service_number_list)
            cursor.close()
            connect.close()
            # 断言
            # self.assertEqual(service_number - 1, service_total)
            self.assertEqual(service_number, service_total)

            # 成功退出系统
            sleep(2)
            self.account_center_page_navi_bar.app_usr_logout()
            # 判断是否成功退出到登录页
            self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
        csv_file.close()
