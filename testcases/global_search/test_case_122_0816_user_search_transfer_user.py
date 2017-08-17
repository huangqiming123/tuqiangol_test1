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


class TestCase122UserSearchTransferUser(unittest.TestCase):
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

    def test_case_user_search_transfer_user(self):
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

        # 获取列表中第二个用户的账号
        self.global_dev_search_page.swith_to_search_frame()
        get_second_user_account = self.global_account_search_page.get_second_user_account_after_search_user()
        # 点击详情
        self.global_account_search_page.click_user_detail_button()
        # 点击销售设备
        self.global_account_search_page.click_transfer_user_button_in_user_detail_button()
        # 选择的用户是该用户（用户详情所属的用户）或其下级用户，提示“选择的用户不能作为上级用户”
        self.global_account_search_page.search_user_to_transfer_user_in_user_detail(get_second_user_account)
        get_text = self.global_account_search_page.get_text_after_click_transfer_user()
        self.assertEqual(self.assert_text.the_selected_user_cannot_be_the_superior(), get_text)
