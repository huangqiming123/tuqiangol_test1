import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
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


# 列表转移---客户树操作

class TestCase67CustManageCustTransferCustSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
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
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_transfer_cust_search(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        sleep(2)

        # 点击编辑用户
        self.cust_manage_basic_info_and_add_cust_page.click_transfer_customer()

        self.cust_manage_basic_info_and_add_cust_page.click_cancel_edit()

        self.cust_manage_basic_info_and_add_cust_page.click_transfer_customer()

        # 循环点击五次
        for n in range(5):
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.driver.click_element('x,//*[@id="treeDemo2_%s_span"]' % str(n + 3))
            sleep(2)
            self.driver.default_frame()

        # 搜索
        # 1 搜索无数据的内容
        """
        self.cust_manage_basic_info_and_add_cust_page.search_cust('无数据')
        get_text = self.cust_manage_basic_info_and_add_cust_page.get_search_no_data_text()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text)
        """

        # 2搜索
        seatch_data = ["无", "test", "yonghu222啦啦啦", "休息休息12", "#@@@ %"]
        for user in range(len(seatch_data)):
            search_result = self.cust_manage_basic_info_and_add_cust_page.transfer_import_account_search(
                seatch_data[user])
            if type(search_result) is str:
                self.assertIn(self.assert_text.account_center_page_no_data_text(), search_result, "搜索结果为暂无数据时，提示不一致")

            else:
                for subscript in range(len(search_result)):
                    text = search_result[subscript].split("(")[0]
                    self.assertIn(seatch_data[user], text, "搜索结果不一致")
