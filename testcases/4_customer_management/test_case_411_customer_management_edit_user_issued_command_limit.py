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


class TestCase411CustomerManagementEditUserIssuedCommandLimit(unittest.TestCase):
    # 测试编辑客户 -- 修改用户 批量下发指令
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

    def test_customer_management_edit_user_issued_command_limit(self):
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

        # 点击编辑 - 取消
        self.cust_manage_basic_info_and_add_cust_page.click_edit_account_buttons()
        # 点击取消
        self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()
        # 点击编辑
        self.cust_manage_basic_info_and_add_cust_page.click_edit_account_buttons()

        # 获取批量下发指令的状态
        self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
        web_login_status = self.cust_manage_basic_info_and_add_cust_page.get_issued_command_status()
        self.driver.default_frame()

        if web_login_status == True:
            # 点击
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.cust_manage_basic_info_and_add_cust_page.click_issued_command_status_ins()
            self.driver.default_frame()

            # 确定
            self.cust_manage_basic_info_and_add_cust_page.click_ensure()

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()

            # 登录刚刚的账号
            self.log_in_base.log_in_with_csv(user_account, 'jimi123')
            # 进入设备管理 获取设备管理页面操的文本

            current_handle_05 = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.click_dev_management_button()
            self.base_page.change_windows_handle(current_handle_05)

            dev_operation_text = self.cust_manage_basic_info_and_add_cust_page.get_facility_manage_page_function_button()

            send_command = self.assert_text2.dev_manage_select_send_command()
            all_send_command = self.assert_text2.dev_manage_select_all_send_command()
            self.assertNotIn(send_command, dev_operation_text)
            self.assertNotIn(all_send_command, dev_operation_text)
            # 退出登录
            self.account_center_page_navi_bar.usr_logout()

            # 登录
            self.log_in_base.log_in()

            current_handle_01 = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
            self.base_page.change_windows_handle(current_handle_01)

            # 搜索一个客户
            self.cust_manage_lower_account_page.input_search_info('abc12344')
            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()
            # 点击编辑 - 取消
            self.cust_manage_basic_info_and_add_cust_page.click_edit_account_buttons()
            # 点击取消
            self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()
            # 点击编辑
            self.cust_manage_basic_info_and_add_cust_page.click_edit_account_buttons()

            # 点击
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.cust_manage_basic_info_and_add_cust_page.click_issued_command_status_ins()
            self.driver.default_frame()

            self.cust_manage_basic_info_and_add_cust_page.click_ensure()

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()

            # 登录刚刚的账号
            self.log_in_base.log_in_with_csv(user_account, 'jimi123')

            hello_usr = self.account_center_page_navi_bar.usr_info_account()
            self.assertIn(user_account, hello_usr)

            # 进入设备管理 获取设备管理页面操的文本
            current_handle_02 = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.click_dev_management_button()
            self.base_page.change_windows_handle(current_handle_02)

            dev_operation_text = self.cust_manage_basic_info_and_add_cust_page.get_facility_manage_page_function_button()

            send_command = self.assert_text2.dev_manage_select_send_command()
            all_send_command = self.assert_text2.dev_manage_select_all_send_command()
            self.assertIn(send_command, dev_operation_text)
            self.assertIn(all_send_command, dev_operation_text)

        elif web_login_status == False:
            # 点击
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.cust_manage_basic_info_and_add_cust_page.click_issued_command_status_ins()
            self.driver.default_frame()
            self.cust_manage_basic_info_and_add_cust_page.click_ensure()
            # 退出登录
            self.account_center_page_navi_bar.usr_logout()
            # 登录刚刚的账号
            self.log_in_base.log_in_with_csv(user_account, 'jimi123')
            hello_usr = self.account_center_page_navi_bar.usr_info_account()
            self.assertIn(user_account, hello_usr)
            # 进入设备管理 获取设备管理页面操的文本
            dev_operation_text = self.cust_manage_basic_info_and_add_cust_page.get_facility_manage_page_function_button()

            send_command = self.assert_text2.dev_manage_select_send_command()
            all_send_command = self.assert_text2.dev_manage_select_all_send_command()
            self.assertIn(send_command, dev_operation_text)
            self.assertIn(all_send_command, dev_operation_text)

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()
            self.log_in_base.log_in()

            current_handle_03 = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
            self.base_page.change_windows_handle(current_handle_03)

            # 搜索一个客户
            self.cust_manage_lower_account_page.input_search_info('abc12344')
            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()
            # 点击编辑 - 取消
            self.cust_manage_basic_info_and_add_cust_page.click_edit_account_buttons()
            # 点击取消
            self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()
            # 点击编辑
            self.cust_manage_basic_info_and_add_cust_page.click_edit_account_buttons()

            # 点击
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.cust_manage_basic_info_and_add_cust_page.click_issued_command_status_ins()
            self.driver.default_frame()

            # 确定
            self.cust_manage_basic_info_and_add_cust_page.click_ensure()
            # 退出登录
            self.account_center_page_navi_bar.usr_logout()
            # 登录刚刚的账号
            self.log_in_base.log_in_with_csv(user_account, 'jimi123')

            # 进入设备管理 获取设备管理页面操的文本
            current_handle_04 = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.click_dev_management_button()
            self.base_page.change_windows_handle(current_handle_04)

            dev_operation_text = self.cust_manage_basic_info_and_add_cust_page.get_facility_manage_page_function_button()

            send_command = self.assert_text2.dev_manage_select_send_command()
            all_send_command = self.assert_text2.dev_manage_select_all_send_command()
            self.assertNotIn(send_command, dev_operation_text)
            self.assertNotIn(all_send_command, dev_operation_text)
