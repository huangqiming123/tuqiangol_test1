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


# 新增客户--添加虚拟账号
# author:戴招利
class TestCase70CustManageCustSearch(unittest.TestCase):
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

    def test_cust_manage_add_cust_search(self):
        # 打开途强在线首页-登录页

        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        self.cust_manage_basic_info_and_add_cust_page.add_acc()
        self.cust_manage_basic_info_and_add_cust_page.cancel_add_account()
        self.cust_manage_basic_info_and_add_cust_page.add_acc()

        # 添加客户名称、账号,点击保存
        self.cust_manage_basic_info_and_add_cust_page.add_account_name("虚拟账号")
        self.cust_manage_basic_info_and_add_cust_page.add_account("xnzh_dzl022")
        self.cust_manage_basic_info_and_add_cust_page.acc_add_save()

        connect = self.connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_account_sql = "select account from user_info where account = 'xnzh_dzl022';"
        cursor.execute(get_account_sql)
        user = cursor.fetchall()
        print(user)
        print(len(user))
        self.assertEqual(0, len(user), "添加普通账号时，可成功添加虚拟账户")

    def tearDown(self):
        self.driver.quit_browser()
