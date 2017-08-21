import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
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


# 全部选择

class TestCase69CustManageAllSelect(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
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
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_all_select(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        sleep(2)

        # 点击全选
        self.cust_manage_basic_info_and_add_cust_page.click_all_select_button()
        input_all_select = self.cust_manage_basic_info_and_add_cust_page.get_all_select_value()
        self.assertEqual(True, input_all_select)

        # 验证下面的是否被全选
        # 获取本页列表的数量
        list_number = self.cust_manage_basic_info_and_add_cust_page.get_per_account_number()
        for n in range(list_number):
            list_input_value = self.driver.get_element(
                'x,//*[@id="customerlist"]/tr[%s]/td[1]/span/div/input' % str(n + 1)).is_selected()
            self.assertEqual(True, list_input_value)

        # 取消全选
        self.cust_manage_basic_info_and_add_cust_page.click_all_select_button()
        input_all_select = self.cust_manage_basic_info_and_add_cust_page.get_all_select_value()
        self.assertEqual(False, input_all_select)

        for n in range(list_number):
            list_input_value = self.driver.get_element(
                'x,//*[@id="customerlist"]/tr[%s]/td[1]/span/div/input' % str(n + 1)).is_selected()
            self.assertEqual(False, list_input_value)

        # 全选后取消选择其中一个
        self.cust_manage_basic_info_and_add_cust_page.click_all_select_button()
        self.cust_manage_basic_info_and_add_cust_page.click_cancel_select_list()
        # 判断全选是否为真
        self.assertEqual(False, self.cust_manage_basic_info_and_add_cust_page.get_all_select_value())

        # 在一次选择上列表中的那个
        self.cust_manage_basic_info_and_add_cust_page.click_cancel_select_list()
        # 判断全选是否为真
        self.assertEqual(True, self.cust_manage_basic_info_and_add_cust_page.get_all_select_value())

        # 在选择每页显示30条
        self.cust_manage_basic_info_and_add_cust_page.select_per_page_numbers()
        self.assertEqual(False, self.cust_manage_basic_info_and_add_cust_page.get_all_select_value())
