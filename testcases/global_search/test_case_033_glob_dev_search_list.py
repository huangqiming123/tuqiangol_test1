import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.login.login_page import LoginPage


# 全局搜索-搜索栏设备不输入搜索信息查找功能
# author:孙燕妮

class TestCase027GlobDevNoKeywordSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_global_dev_no_keyword_search(self):
        '''测试全局搜索-搜索栏设备不输入搜索信息查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 不输入搜索关键词点击“设备”搜索按钮
        self.global_dev_search_page.click_easy_search()
        # 点击设备搜索对话框的搜索按钮
        self.global_dev_search_page.click_dev_dial_search()

        csv_file = self.global_search_page_read_csv.read_csv('dev_list_link.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            link_info = {
                "link_name": row[0],
                "link_url": row[1]
            }

            # 验证设备列表中各个页面的链接跳转是否正确

            self.global_dev_search_page.click_dev_list_link(link_info["link_name"])

            expect_url = self.base_url + link_info["link_url"]

            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()
                    self.assertEqual(expect_url, current_url, link_info["link_name"] + "页面跳转错误!")
                    # 关闭当前窗口
                    self.driver.close_current_page()
                    # 回到账户中心窗口
                    self.driver.switch_to_window(account_center_handle)
                    self.driver.wait()
        csv_file.close()
        # 列表点击详情进入子模块验证“返回列表”功能
        # 点击详情
        self.global_dev_search_page.click_dev_details()
        # 点击返回列表
        sleep(3)
        # 关闭当前设备搜索对话框
        self.global_dev_search_page.close_dev_search()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
