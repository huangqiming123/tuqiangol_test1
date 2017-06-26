import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-搜索栏用户精确查找
# author:孙燕妮

class TestCase034GlobAccountExactSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_global_account_exact_search(self):
        '''通过csv测试全局搜索-搜索栏用户精确查找功能'''

        csv_file = open(r"E:\git\tuqiangol_test\data\global_search\account_search_keyword.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            account_search = {
                "user_name": row[0],
                "account": row[1]
            }

            # 打开途强在线首页-登录页
            self.base_page.open_page()

            # 登录
            self.login_page.user_login("test_007", "jimi123")

            # 在全局搜索栏输入搜索关键词-账户
            self.global_account_search_page.acc_easy_search(account_search["account"])

            # 获取搜索结果
            acc_text = self.global_account_search_page.get_exact_search_acc()

            # 验证搜素结果账户与搜索输入的关键词账户是否一致
            self.assertIn(account_search["account"], acc_text, "搜索结果与输入的搜索词不一致")

            # 关闭当前搜索对话框
            self.global_account_search_page.close_dev_search()

            # 点击全局搜索栏-设备搜索按钮
            self.global_account_search_page.click_easy_search()

            # 设备搜索对话框中选择搜索类型为“用户”
            self.global_account_search_page.change_dev_dial_to_account()

            # 关闭当前搜索对话框
            self.global_account_search_page.close_dev_search()

            # 点击全局搜索栏-用户搜索按钮
            self.global_account_search_page.click_account_search()

            # 用户搜索对话框搜索用户账户名称
            self.global_account_search_page.account_dial_search(account_search["user_name"])

            # 获取搜索结果
            name_text = self.global_account_search_page.get_exact_search_name()

            # 验证搜素结果账户名称与搜索输入的关键词账户名称是否一致
            self.assertIn(account_search['user_name'], name_text, "搜索结果与输入的搜索词不一致")

            # 关闭当前搜索对话框
            self.global_account_search_page.close_dev_search()

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()

        csv_file.close()
