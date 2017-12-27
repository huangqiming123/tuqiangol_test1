import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv
from pages.login.login_page import LoginPage


class TestCase401CustomerManagementCheckAccount(unittest.TestCase):
    # 测试 客户管理 检查客户管理抬头用户信息
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_customer_management_check_account(self):

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        csv_file = self.cust_manage_page_read_csv.read_csv('check_account_data.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            data = {
                'account': row[0]
            }
            self.cust_manage_basic_info_and_add_cust_page.add_data_to_search_account(data)

            connect = self.connect_sql.connect_tuqiang_sql()
            cursor = connect.cursor()

            get_account_sql = "SELECT o.type,o.phone,o.nickName from user_info o WHERE o.account = '" + data[
                'account'] + "';"

            cursor.execute(get_account_sql)
            get_account_user_info = cursor.fetchall()
            current_user_info = []
            for range1 in get_account_user_info:
                for range2 in range1:
                    current_user_info.append(range2)
            print(current_user_info)
            type = self.assert_text.log_in_page_account_type(current_user_info[0])
            # 断言客户类型
            account_type = self.cust_manage_basic_info_and_add_cust_page.get_account_type()
            self.assertEqual(type, account_type)

            # 断言账号
            account = self.cust_manage_basic_info_and_add_cust_page.get_account()
            self.assertEqual(data['account'], account)

            # 断言电话
            account_phone = self.cust_manage_basic_info_and_add_cust_page.get_account_phone()
            if current_user_info[1] == None:
                self.assertEqual("", account_phone, "手机号不一致")
            else:
                self.assertEqual(current_user_info[1], account_phone)

            # 断言昵称
            account_name = self.cust_manage_basic_info_and_add_cust_page.get_account_name()
            if current_user_info[2] == None:
                self.assertEqual("", account_name, "昵称不一致")
            else:
                self.assertEqual(current_user_info[2], account_name)

            # 点击监控用户
            current_window = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.click_monitoring_account_button()
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != current_window:
                    self.driver.switch_to_window(handle)

                    expect_url = self.base_url + '/index'
                    self.assertEqual(expect_url, self.driver.get_current_url())

                    self.driver.close_current_page()
                    sleep(2)
                    self.driver.switch_to_window(current_window)

            # 点击编辑用户
            style_value = self.cust_manage_basic_info_and_add_cust_page.edit_button_style_value()
            if style_value == 'display: inline;':
                self.cust_manage_basic_info_and_add_cust_page.click_edit_account_button()
                # 点击关闭
                self.cust_manage_basic_info_and_add_cust_page.click_close_edit_accunt_button()

                # 点击编辑
                self.cust_manage_basic_info_and_add_cust_page.click_edit_account_button()

                # 查询用户上一级信息
                connect_02 = self.connect_sql.connect_tuqiang_sql()
                cursor_02 = connect_02.cursor()
                get_id_sql = "SELECT o.parentId from user_info o WHERE o.account = '" + account + "';"
                cursor_02.execute(get_id_sql)
                get_id_info = cursor_02.fetchall()
                current_user = []
                for range1 in get_id_info:
                    for range2 in range1:
                        current_user.append(range2)
                print(current_user)

                get_up_account_info_sql = "SELECT o.nickName FROM user_info o WHERE o.userId = '" + current_user[
                    0] + "';"
                cursor_02.execute(get_up_account_info_sql)
                get_up_user_info = cursor_02.fetchall()
                up_user_info = []
                for range1 in get_up_user_info:
                    for range2 in range1:
                        up_user_info.append(range2)
                account_name = up_user_info[0]
                get_web_account_name = self.cust_manage_basic_info_and_add_cust_page.get_account_name_after_click_edit()
                self.assertEqual(account_name, get_web_account_name, '用户上级显示错误！')
                self.cust_manage_basic_info_and_add_cust_page.click_close_edit_accunt_button()

                # 断言账号类型
                cursor_02.close()
                connect_02.close()
            cursor.close()
            connect.close()
        csv_file.close()
