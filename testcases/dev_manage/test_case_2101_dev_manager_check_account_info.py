import unittest
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase2101DevManageCheckAccountInfo(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_2101_dev_manage_check_account_info(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 循环点击
        for n in range(5):
            self.dev_manage_page.click_per_account_in_dev_manage_page(n)
            # 获取点击后的用户账号
            user_account = self.dev_manage_page.get_per_user_account_in_dev_manage_page()
            # 连接数据库，获取该账号的信息
            get_account_info = self.dev_manage_page.get_account_info(user_account)
            # 断言用户信息
            get_user_nickname_in_page = self.dev_manage_page.get_user_nickname_in_page()
            get_user_type_in_page = self.dev_manage_page.get_user_type_in_page()
            get_user_phone_in_page = self.dev_manage_page.get_user_phone_in_page()

            self.assertEqual(get_account_info['nickname'], get_user_nickname_in_page)
            self.assertEqual(get_account_info['phone'], get_user_phone_in_page)

            type = self.assert_text.log_in_page_account_type(get_account_info['type'])
            self.assertEqual(get_user_type_in_page, type)

            get_account_nickname_in_cust_tree = self.dev_manage_page.get_account_nickname_in_cust_tree(n)
            self.assertEqual(get_user_nickname_in_page, get_account_nickname_in_cust_tree)

            # 点击监控用户
            current_handle = self.driver.get_current_window_handle()
            self.dev_manage_page.click_control_account_button()
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != current_handle:
                    self.driver.switch_to_window(handle)
                    expect_url = self.driver.base_url + '/index'
                    self.assertEqual(self.driver.get_current_url(), expect_url)

                    self.driver.close_current_page()
                    self.driver.switch_to_window(current_handle)

            # 点击编辑用户
            edit_style = self.dev_manage_page.get_edit_style_in_dev_page()
            if edit_style == 'display: inline;':
                self.dev_manage_page.click_edit_account_button()
                self.dev_manage_page.click_close_edit_button()

                self.dev_manage_page.click_edit_account_button()

                self.dev_manage_page.switch_to_dev_edit_frame()

                # 验证打开的信息是否正确
                # 分别获取上级客户、客户类型、客户名称、登录账号、电话
                up_user = self.dev_manage_page.get_up_user_edit_user_in_dev_page()
                user_type = self.dev_manage_page.get_user_type_edit_user_in_dev_page()
                user_name = self.dev_manage_page.get_user_name_edit_user_in_dev_page()
                account = self.dev_manage_page.get_user_account_edit_in_dev_page()
                user_phone = self.dev_manage_page.get_user_phone_edit_in_dev_page()

                # 断言
                self.assertEqual(type, user_type)
                self.assertEqual(user_name, get_user_nickname_in_page)
                self.assertEqual(account, user_account)
                self.assertEqual(user_phone, get_account_info['phone'])
                self.driver.default_frame()
                self.dev_manage_page.click_close_edit_button()
