import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text2 import AssertText2
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

__author__ = ''

class TestCase415CustomerManagementEditUserResetPassword(unittest.TestCase):
    # 测试编辑客户 -- 重置密码
    def setUp(self):
        self.driver = AutomateDriverServer()
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
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.assert_text2 = AssertText2()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.close_window()
        self.driver.quit_browser()

    def test_customer_management_edit_user_reset_password(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        sleep(2)
        current_handle = self.driver.get_current_window_handle()
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.base_page.change_windows_handle(current_handle)
        account = "bbb123"
        # 搜索一个客户
        self.cust_manage_lower_account_page.input_search_info(account)
        # 搜索
        self.cust_manage_lower_account_page.click_search_btn()

        # 点击重置密码
        self.cust_manage_basic_info_and_add_cust_page.click_reset_password_button()
        # 点击取消
        self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        self.log_in_base.log_in_with_csv(account, 'jimi123')
        hello_usr = self.account_center_page_navi_bar.usr_info_account()
        self.assertIn(account, hello_usr)
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        # 登录
        self.log_in_base.log_in()
        # 进入客户管理页面
        current_handle_01 = self.driver.get_current_window_handle()
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.base_page.change_windows_handle(current_handle_01)
        # 搜索一个客户
        self.cust_manage_lower_account_page.input_search_info(account)
        # 搜索
        self.cust_manage_lower_account_page.click_search_btn()

        # 点击重置密码
        self.cust_manage_basic_info_and_add_cust_page.click_reset_password_button()
        # 点击取消
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        self.log_in_base.log_in_with_csv(account, '888888')

        # 输入新的密码 ，
        self.cust_manage_basic_info_and_add_cust_page.click_new_password('jimi123')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()
        self.cust_manage_basic_info_and_add_cust_page.click_ensuress()
        sleep(4)
        self.log_in_base.log_in_with_csv(account, 'jimi123')
        sleep(2)
        hello_usr = self.account_center_page_navi_bar.usr_info_account()

        self.assertIn(account, hello_usr)
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
