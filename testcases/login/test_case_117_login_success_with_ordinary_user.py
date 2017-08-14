import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage


# 普通用户账户成功登录功能的测试
# author:孙燕妮

class TestCase117LoginSuccessWithOrdinaryUser(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_ordinary_user_login_by_csv(self):
        '''通过csv测试普通用户账户成功登录和成功退出功能'''
        data = ["首页", "设备管理", "控制台", "统计报表", "安全区域", "设备分布"]

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
            # 判断登录成功后跳转页面是否正确
            actual_url = self.driver.get_current_url()
            expect_url = self.base_url + "/nomalUserCenter"
            self.assertEqual(expect_url, actual_url, "登录成功后页面跳转错误")

            # 判断登录成功后招呼栏的用户名是否正确
            hello_usr = self.account_center_page_navi_bar.hello_user_account()
            expect_usr = user_to_login["account"]
            self.assertIn(expect_usr, hello_usr, "登录成功后招呼栏账户名显示错误")

            # 验证模块
            module = self.account_center_page_navi_bar.get_page_module()
            for m in range(len(module)):
                self.assertIn(data[m], module[m], "用户账号登录，模块显示错误")

            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()
            get_account_user_info_sql = "SELECT o.parentId from user_info o WHERE o.account = '" + \
                                        user_to_login['account'] + "'"
            cursor.execute(get_account_user_info_sql)
            get_account_user_info = cursor.fetchall()
            current_user_info = []
            for range1 in get_account_user_info:
                for range2 in range1:
                    current_user_info.append(range2)
            print(current_user_info)
            get_up_account_info_sql = "SELECT o.account,o.nickName,o.phone FROM user_info o WHERE o.userId = '" + \
                                      current_user_info[0] + "';"
            cursor.execute(get_up_account_info_sql)
            get_up_user_info = cursor.fetchall()
            up_user_info = []
            for range1 in get_up_user_info:
                for range2 in range1:
                    up_user_info.append(range2)
            print(up_user_info)
            usr_service_provider = self.account_center_page_navi_bar.ordinary_usr_service_provider()
            expect_usr_service_provider = up_user_info[0]
            self.assertIn(expect_usr_service_provider, usr_service_provider, "服务商显示错误")
            if up_user_info[1] != '':
                service_provider_connect = self.account_center_page_navi_bar.ordinary_usr_service_provider_connect()
                expect_service_provider_connect = up_user_info[1]
                self.assertIn(expect_service_provider_connect, service_provider_connect, "联系人显示错误")

            service_provider_phone = self.account_center_page_navi_bar.ordinary_usr_service_provider_phone()
            expect_service_provider_phone = up_user_info[2]
            self.assertIn(expect_service_provider_phone, service_provider_phone, "电话显示错误")

            # 成功退出系统
            self.account_center_page_navi_bar.usr_log_out()

            # 判断是否成功退出到登录页
            self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "退出系统失败")

            # 验证退出系统后“记住我”是否是未勾选状态
            box_status = self.login_page.check_remember_me()
            self.assertEqual(False, box_status, '记住密码为勾选状态！')

        csv_file.close()
