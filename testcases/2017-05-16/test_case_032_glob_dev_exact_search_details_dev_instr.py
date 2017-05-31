import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一设备详情页面-设备指令模块的操作
# author:孙燕妮

class TestCase031GlobDevExactSearchDetailsDevInstr(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_dev_exact_search_details_dev_instr(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一设备详情页面-设备指令模块的操作功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 点击全局搜索栏的搜索框
        self.global_dev_search_page.click_easy_search()

        csv_file = self.global_search_page_read_csv.read_csv('dev_instr_type.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            dev_instr_info = {
                "keyword": row[0],
                "instr_type": row[1]
            }
            # 输入关键词搜索
            self.global_dev_search_page.dev_dial_search(dev_instr_info["keyword"])

            # 点击搜索结果-设备指令
            self.global_dev_search_page.click_dev_instr()
            sleep(2)
            self.global_dev_search_page.dev_instr_type_edit(dev_instr_info["instr_type"])

            self.global_dev_search_page.dev_instr_send()
        # 关闭当前设备搜索对话框
        self.global_dev_search_page.close_dev_search()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
        csv_file.close()
