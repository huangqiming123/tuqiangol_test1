import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage


class TestCase102LoginSuccessWithOrdinaryUser(unittest.TestCase):
    # 测试用户类型的客户
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.driver.set_window_max()
        self.assert_text = AssertText()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_ordinary_user_login_by_csv(self):
        '''通过csv测试普通用户账户成功登录和成功退出功能'''
        data = [" 首页", " 设备管理", " 控制台", " 统计报表", " 安全区域", " 设备分布"]

        csv_file = self.log_in_page_read_csv.read_csv('login_with_ordinary_user.csv')
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
            self.driver.wait(1)
            # 点首页
            self.login_page.click_home_page()
            current_handle = self.driver.get_current_window_handle()
            self.base_page.change_windows_handle(current_handle)
            # 判断登录成功后跳转页面是否正确
            actual_url = self.driver.get_current_url()
            expect_url = self.base_url + "/nomalUserCenter"
            self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

            # 验证模块
            module = self.account_center_page_navi_bar.get_page_module()
            self.assertEqual(data, module, "用户账号登录，模块显示错误")

            # 判断登录成功后招呼栏的用户名是否正确
            usr_info_account = self.account_center_page_navi_bar.usr_info_account()
            company_name = self.login_page.get_company_name()
            user_account = self.login_page.get_user_account()
            user_type = self.login_page.get_user_type()
            user_phone = self.login_page.get_user_phone()
            expect_usr = user_to_login["account"]
            self.assertEqual(expect_usr, usr_info_account)
            self.assertEqual(expect_usr, user_account)
            # 数据库获取登录账号信息
            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()

            sql = "SELECT o.account,o.type,o.phone,o.companyName FROM user_info o WHERE o.account = '" + user_to_login[
                "account"] + "';"
            cursor.execute(sql)
            user_info = cursor.fetchall()
            current_user_info = []
            for range1 in user_info:
                for range2 in range1:
                    current_user_info.append(range2)
            print(current_user_info)
            # 当前客户类型
            type = self.assert_text.log_in_page_account_type(current_user_info[1])
            self.assertEqual(type, user_type)
            # 当前客户公司名
            if current_user_info[3] == '':
                self.assertEqual('', company_name)
            else:
                self.assertEqual(current_user_info[3], company_name)
            # 当前客户电话
            if current_user_info[2] == '':
                self.assertEqual('', user_phone)
            else:
                self.assertEqual(current_user_info[2], user_phone)

            get_account_user_info_sql = "SELECT o.parentId from user_info o WHERE o.account = '" + user_to_login[
                "account"] + "';"
            cursor.execute(get_account_user_info_sql)
            get_account_user_info = cursor.fetchall()
            current_user_info = []
            for range1 in get_account_user_info:
                for range2 in range1:
                    current_user_info.append(range2)

            get_up_account_info_sql = "SELECT o.account,o.contact,o.phone FROM user_info o WHERE o.userId = '" + \
                                      current_user_info[0] + "';"
            cursor.execute(get_up_account_info_sql)
            get_up_user_info = cursor.fetchall()
            up_user_info = []
            for range1 in get_up_user_info:
                for range2 in range1:
                    up_user_info.append(range2)
            print(up_user_info)

            # 获取上级客户的信息
            up_user_account = self.login_page.get_up_user_account()
            up_user_contact = self.login_page.get_up_user_contact()
            up_user_phone = self.login_page.get_up_user_phone()
            self.assertEqual(up_user_info[0], up_user_account)
            self.assertEqual(up_user_info[1], up_user_contact)
            self.assertEqual(up_user_info[2], up_user_phone)

            # 成功退出系统
            sleep(2)
            self.account_center_page_navi_bar.usr_log_out()

            # 判断是否成功退出到登录页
            self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")
            cursor.close()
            connect.close()
        csv_file.close()
