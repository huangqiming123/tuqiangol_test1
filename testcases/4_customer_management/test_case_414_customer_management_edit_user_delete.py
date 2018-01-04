import unittest
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


class TestCase414CustomerManagementEditDelete(unittest.TestCase):
    # 测试编辑客户 -- 删除
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
        self.driver.quit_browser()

    def test_customer_management_edit_user_delete(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        current_handle = self.driver.get_current_window_handle()
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.base_page.change_windows_handle(current_handle)

        # 搜索一个客户
        self.cust_manage_lower_account_page.input_search_info('abc12344')
        # 搜索
        self.cust_manage_lower_account_page.click_search_btn()
        user_account = self.cust_manage_basic_info_and_add_cust_page.get_user_account_in_customer_page()
        user_type = self.cust_manage_basic_info_and_add_cust_page.get_user_type_in_customer_page()
        user_name = self.cust_manage_basic_info_and_add_cust_page.get_user_name_in_customer_page()
        user_phone = self.cust_manage_basic_info_and_add_cust_page.get_user_phone_in_customer_page()
        user_contact = self.cust_manage_basic_info_and_add_cust_page.get_user_contact_in_customer_page()

        # 点击删除
        self.cust_manage_basic_info_and_add_cust_page.click_delete_user_button()
        # 点击取消
        self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()
        user_account_01 = self.cust_manage_basic_info_and_add_cust_page.get_user_account_in_customer_page()
        user_type_01 = self.cust_manage_basic_info_and_add_cust_page.get_user_type_in_customer_page()
        user_name_01 = self.cust_manage_basic_info_and_add_cust_page.get_user_name_in_customer_page()
        user_phone_01 = self.cust_manage_basic_info_and_add_cust_page.get_user_phone_in_customer_page()
        user_contact_01 = self.cust_manage_basic_info_and_add_cust_page.get_user_contact_in_customer_page()

        self.assertEqual(user_account, user_account_01)
        self.assertEqual(user_type, user_type_01)
        self.assertEqual(user_name, user_name_01)
        self.assertEqual(user_phone, user_phone_01)
        self.assertEqual(user_contact, user_contact_01)

        # 点击删除
        self.cust_manage_basic_info_and_add_cust_page.click_delete_user_button()
        # 点击取消
        self.cust_manage_basic_info_and_add_cust_page.click_close_edit_accunt_button()
        user_account_02 = self.cust_manage_basic_info_and_add_cust_page.get_user_account_in_customer_page()
        user_type_02 = self.cust_manage_basic_info_and_add_cust_page.get_user_type_in_customer_page()
        user_name_02 = self.cust_manage_basic_info_and_add_cust_page.get_user_name_in_customer_page()
        user_phone_02 = self.cust_manage_basic_info_and_add_cust_page.get_user_phone_in_customer_page()
        user_contact_02 = self.cust_manage_basic_info_and_add_cust_page.get_user_contact_in_customer_page()

        self.assertEqual(user_account, user_account_02)
        self.assertEqual(user_type, user_type_02)
        self.assertEqual(user_name, user_name_02)
        self.assertEqual(user_phone, user_phone_02)
        self.assertEqual(user_contact, user_contact_02)
