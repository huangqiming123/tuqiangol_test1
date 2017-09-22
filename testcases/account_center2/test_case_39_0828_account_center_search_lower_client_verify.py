import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-下级客户--搜索验证
# author:戴招利

class TestCase37AccountCenterSearchLowerClientVerify(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_search_lower_client(self):
        '''通过csv测试账户详情--下级客户--查找不同账号功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()
        self.account_center_page_details.account_center_iframe()

        csv_file = self.account_center_page_read_csv.read_csv('search_different_account.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            search_account = {
                "account": row[0]

            }
            # 进入快捷销售页面
            self.account_center_page_details.fast_sales()

            # 查找账户
            search_result = self.account_center_page_details.subordinate_account_search(search_account["account"])
            if type(search_result) is str:
                self.assertIn(self.assert_text.account_center_page_no_data_text(), search_result, "搜索结果为暂无数据时，提示不一致")

            else:
                for subscript in range(len(search_result)):
                    text = search_result[subscript].split("(")[0]
                    self.assertIn(search_account["account"], text, "搜索结果不一致")

            self.driver.wait()

        # 直接选择用户
        for user in range(8):
            self.account_center_page_details.fast_sales()
            self.account_center_page_details.click_list_subordinate_client(user + 1)

        # 验证enter键输入
        self.account_center_page_details.fast_sales()
        self.account_center_page_details.search_subordinate_client_click_enter("1234")

        self.driver.wait()
        self.driver.default_frame()
        csv_file.close()
