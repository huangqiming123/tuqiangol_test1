import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase137SearchUserByTypeCreatNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_137_search_user_by_type_creat_new_user(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 点击账号中心
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)
        self.global_dev_search_page.click_easy_search()
        # 选择用户搜索
        self.global_dev_search_page.click_dev_search()
        self.global_dev_search_page.click_search_buttons()
        self.global_dev_search_page.swith_to_search_frame()

        # 获取用户列表有多少页
        user_account = ''
        total_page = self.global_dev_search_page.get_total_page_after_search_user()
        for n in range(total_page):
            self.global_dev_search_page.click_per_page(n)
            # 获取每页有多少条
            number = self.global_dev_search_page.get_per_page_total_number_in_search_user()
            for i in range(number):
                # 获取各个用户的用户类型
                user_type = self.global_dev_search_page.get_user_type_in_search_user(i)
                user_account = self.global_dev_search_page.get_user_account_in_search_user(i)
                if user_type == '销售':
                    break
        # 搜索获取到的销售类型的用户，搜索
        self.global_dev_search_page.search_user(user_account)
        # 点击新增下级用户
        self.global_dev_search_page.click_add_next_user_in_search_user()
        # 获取新增下级用户时，下级的客户类型有几种
        user_type_number = self.global_dev_search_page.get_user_type_number_in_search_user()
        self.assertEqual(3, user_type_number)

        self.global_dev_search_page.search_user('')
        user_account = ''
        total_page = self.global_dev_search_page.get_total_page_after_search_user()
        for n in range(total_page):
            self.global_dev_search_page.click_per_page(n)
            # 获取每页有多少条
            number = self.global_dev_search_page.get_per_page_total_number_in_search_user()
            for i in range(number):
                # 获取各个用户的用户类型
                user_type = self.global_dev_search_page.get_user_type_in_search_user(i)
                user_account = self.global_dev_search_page.get_user_account_in_search_user(i)
                if user_type == '代理商':
                    break
        # 搜索获取到的销售类型的用户，搜索
        self.global_dev_search_page.search_user(user_account)
        # 点击新增下级用户
        self.global_dev_search_page.click_add_next_user_in_search_user()
        # 获取新增下级用户时，下级的客户类型有几种
        user_type_number = self.global_dev_search_page.get_user_type_number_in_search_user()
        self.assertEqual(2, user_type_number)

        self.global_dev_search_page.search_user('')
        user_account = ''
        total_page = self.global_dev_search_page.get_total_page_after_search_user()
        for n in range(total_page):
            self.global_dev_search_page.click_per_page(n)
            # 获取每页有多少条
            number = self.global_dev_search_page.get_per_page_total_number_in_search_user()
            for i in range(number):
                # 获取各个用户的用户类型
                user_type = self.global_dev_search_page.get_user_type_in_search_user(i)
                user_account = self.global_dev_search_page.get_user_account_in_search_user(i)
                if user_type == '用户':
                    break
        # 搜索获取到的销售类型的用户，搜索
        self.global_dev_search_page.search_user(user_account)
        # 获取新增下级用户的display值
        get_new_next_display = self.global_dev_search_page.get_new_next_display_in_search_user()
        self.assertEqual('display: none;', get_new_next_display)

        self.driver.default_frame()
