import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.login.login_page import LoginPage


# 账户中心-账户详情-快捷销售-精确查找账户及imei成功销售
# author:孙燕妮

class TestCase017AccountCenterFastSaleReset(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_fast_sale(self):
        '''通过csv测试账户详情-快捷销售-精确查找账户及imei成功销售功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        current_account = self.log_in_base.get_log_in_account()
        self.driver.wait()
        csv_file = self.account_center_page_read_csv.read_csv('fast_sale_exact_find_and_sale.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            search_account = {
                "account": row[0],
                "device_imei": row[1],
                "imei_count": row[2],
                "selected_dev": row[2]
            }
            # 进入快捷销售页面
            self.account_center_page_details.fast_sales()
            # 查找账户
            self.account_center_page_details.fast_sales_find_account(search_account["account"])
            # 输入设备imei精确查找设备并添加
            imei_count = self.account_center_page_details.fast_sales_find_and_add_device(search_account["device_imei"])
            expect_imei_count = search_account["imei_count"]
            self.assertEqual(expect_imei_count, imei_count, "imei计数不准确")

            # 验证已选设备计数是否准确
            dev_num = self.account_center_page_details.get_selected_device_num()
            expect_dev_num = search_account["selected_dev"]
            self.assertEqual(expect_dev_num, dev_num, "已选设备个数不准确")
            # 销售
            self.account_center_page_details.sale_button()

            # 通过弹出框状态验证是否销售成功
            sale_status_text = self.account_center_page_details.get_sale_status()
            self.assertIn("操作成功", sale_status_text, "销售失败")

            self.driver.wait()

            # 进入客户管理
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

            # 选中销售客户
            self.cust_manage_cust_list_page.acc_exact_search(search_account["account"])
            self.driver.wait()

            # 搜索已销售的imei
            self.cust_manage_my_dev_page.search_dev_by_imei(search_account["device_imei"])
            self.cust_manage_my_dev_page.click_search_btn()
            self.driver.wait()
            # 点击销售
            self.cust_manage_my_dev_page.one_dev_sale()
            # 选中当前登录账户
            self.cust_manage_my_dev_page.select_sale_acc(current_account)
            # 销售
            self.cust_manage_my_dev_page.sale_button()
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
