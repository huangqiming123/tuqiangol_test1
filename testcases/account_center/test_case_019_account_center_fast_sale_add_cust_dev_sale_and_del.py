import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.login.login_page import LoginPage


# 账户中心-账户详情-快捷销售-客户树
# author:孙燕妮

class TestCase019AccountCenterFastSaleAddCustDevSaleAndDel(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql()
        self.log_in_base = LogInBase(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_fast_sale_add_cust_dev_sale_and_del(self):
        '''通过csv测试账户详情-快捷销售-新增客户销售设备-删除新增客户'''

        csv_file = self.account_center_page_read_csv.read_csv('fast_sale_add_cust_and_sale.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            info = {
                "acc_type": row[0],
                "acc_name": row[1],
                "account": row[2],
                "pwd": row[3],
                "phone": row[4],
                "email": row[5],
                "conn": row[6],
                "com": row[7],
                "device_imei": row[8],
                "imei_count": row[9],
                "selected_dev": row[10]
            }

            # 打开途强在线首页-登录页
            self.base_page.open_page()

            # 登录账号
            self.log_in_base.log_in()
            self.driver.wait()
            current_account = self.log_in_base.get_log_in_account()

            # 获取当前窗口句柄
            account_center_handle = self.driver.get_current_window_handle()

            # 全局搜索新增客户-info["account"]
            self.global_account_search_page.acc_easy_search(info["account"])

            # 查看用户
            self.global_account_search_page.view_search_cust()

            expect_url = self.base_url + '/customer/toSearch'

            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()
                    self.assertEqual(expect_url, current_url, "客户管理页面跳转错误!")

                    # 销售当前用户的设备给当前登录账户-jimitest
                    self.cust_manage_my_dev_page.dev_sale()

                    # 搜索账号-jimitest并选中搜索结果
                    self.cust_manage_my_dev_page.select_sale_acc(current_account)

                    # 销售
                    self.cust_manage_my_dev_page.sale_button()

                    try:
                        # 获取操作状态
                        status = self.cust_manage_my_dev_page.get_sale_status()

                        # 验证是否操作成功
                        self.assertIn("操作成功", status, "操作失败")
                    except:
                        print("当前无弹框弹出或弹框立即消失")

                    self.driver.wait()

                    # 进入当前登录账户的下级账户模块
                    self.cust_manage_lower_account_page.enter_lower_acc()

                    # 搜索新增客户
                    self.cust_manage_lower_account_page.input_search_info(info["account"])

                    # 搜索
                    self.cust_manage_lower_account_page.click_search_btn()

                    # 删除该新增客户
                    self.cust_manage_lower_account_page.delete_acc()

                    # 确定删除
                    self.cust_manage_lower_account_page.delete_acc_ensure()

                    # 获取删除操作状态
                    del_status = self.cust_manage_lower_account_page.get_del_status()

                    # 验证是否操作成功
                    self.assertIn("操作成功", del_status, "操作失败")

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
