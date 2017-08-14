import unittest
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase2102DevManageEditAccount(unittest.TestCase):
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

    def test_case_2102_dev_manage_edit_account(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 点击下级用户
        self.dev_manage_page.click_next_user_in_dev_page()

        # 点击编辑用户
        self.dev_manage_page.click_edit_account_button()
        self.dev_manage_page.click_close_edit_button()
        self.dev_manage_page.click_edit_account_button()

        self.dev_manage_page.switch_to_dev_edit_frame()
        # 搜索用户
        self.dev_manage_page.search_account_in_edit_user()
        get_user_name_after_search = self.dev_manage_page.get_user_name_after_search_in_edit_user()
        up_user = self.dev_manage_page.get_up_user_edit_user_in_dev_page()
        self.assertIn(up_user, get_user_name_after_search)

        # 循环点击
        for n in range(5):
            self.dev_manage_page.click_user_to_search_up_user_in_edit_user(n)
            up_user = self.dev_manage_page.get_up_user_edit_user_in_dev_page()
            get_user_name_after_search = self.dev_manage_page.get_user_name_after_search_in_edit_user()
            self.assertIn(up_user, get_user_name_after_search)

        self.driver.default_frame()
