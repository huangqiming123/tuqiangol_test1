import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_complex_search_page import GlobalComplexSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv

# 全局搜索-高级搜索- 欠费设备的操作(下发指令)

# author:zhangao

class TestCase171GlobalComplexSearchDevArrearageOpeartion(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_complex_search_page = GlobalComplexSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_complex_search_dev_arrearage_operation(self):
        '''测试全局搜索-高级搜索-通过设备状态单一查找功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击全局搜索栏-高级搜素按钮
        self.global_complex_search_page.click_complex_search()
        # 勾选设备状态-欠费
        self.global_complex_search_page.complex_search_select_dev_status("欠费")
        # 点击搜索按钮
        self.global_complex_search_page.complex_search_click()
        sleep(2)

        self.global_complex_search_page.search_dev_arrearage_opeartion()
        sleep(2)
        actual_text = self.base_page.reset_passwd_stat_cont()
        self.assertEqual('设备已过期，暂不能发送指令', actual_text)

        # 关闭高级搜索对话框
        self.global_complex_search_page.close_dev_search()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
