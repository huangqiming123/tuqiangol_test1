import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
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
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.login.login_page import LoginPage


class TestCase04AccountCenterFastSaleAddCust(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.assert_text = AssertText()
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

    def test_account_center_fast_sale_add_cust(self):
        '''通过csv测试账户详情-快捷销售-新增客户并成功销售设备给新客户'''

        csv_file = self.account_center_page_read_csv.read_csv('fast_sale_add_cust_and_sale.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            add_info = {
                "acc_type": row[0],
                "acc_name": row[1],
                "account": row[2],
                "pwd": row[3],
                "phone": row[4],
                "email": row[5],
                "conn": row[6],
                "com": row[7]
            }

            search_info = {
                "device_imei": row[8],
                "imei_count": row[9],
                "selected_dev": row[10]
            }
            # 打开途强在线首页-登录页
            self.base_page.open_page()
            # 登录账号
            self.log_in_base.log_in()
            self.account_center_page_navi_bar.click_account_center_button()

            # 进入快捷销售页面
            self.account_center_page_details.account_center_iframe()
            self.account_center_page_details.fast_sales()
            self.driver.default_frame()

            self.account_center_page_details.add_cust_cancel()
            # 新增客户
            self.account_center_page_details.add_cust(add_info["acc_type"],
                                                      add_info["acc_name"],
                                                      add_info["account"],
                                                      add_info["pwd"],
                                                      add_info["phone"],
                                                      add_info["email"],
                                                      add_info["conn"],
                                                      add_info["com"])

            # 获取新增客户保存状态
            status = self.account_center_page_details.get_add_save_status()
            succeed_prompt = self.assert_text.account_center_page_operation_done()
            # 验证是否操作成功
            self.assertIn(succeed_prompt, status, "操作失败")
            sleep(2)
            self.account_center_page_details.account_center_iframe()
            self.driver.click_element("showTree-btn")
            sleep(2)
            # 查找新增成功的客户
            self.account_center_page_details.search_cust(add_info["account"])

            # 输入设备imei精确查找设备并添加
            imei_count = self.account_center_page_details.fast_sales_find_and_add_device(search_info["device_imei"])
            expect_imei_count = search_info["imei_count"]
            self.assertEqual(expect_imei_count, imei_count, "imei计数错误")

            # 验证已选设备计数是否准确
            dev_num = self.account_center_page_details.get_selected_device_num()
            expect_dev_num = search_info["selected_dev"]
            self.assertEqual(int(expect_dev_num), dev_num, "已选设备个数错误")
            # 销售
            self.account_center_page_details.sale_button()
            # 通过弹出框状态验证是否销售成功
            sale_status_text = self.account_center_page_details.get_sale_status()
            self.assertIn(succeed_prompt, sale_status_text, "销售失败")
            self.driver.default_frame()

            # 转移设备
            self.account_center_page_details.shift_facility(add_info, search_info)
            self.assertEqual(succeed_prompt, sale_status_text, "设备管理页面，销售失败！")
            sleep(2)
            # 点击进入客户管理页面,选择当前账号
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
            self.driver.click_element("treeDemo_1_span")
            # 搜索新增客户
            self.cust_manage_lower_account_page.input_search_info(add_info["account"])

            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()

            # 删除该新增客户
            self.cust_manage_lower_account_page.delete_acc()

            # 确定删除
            self.cust_manage_lower_account_page.delete_acc_ensure()

            # 获取删除操作状态
            del_status = self.cust_manage_lower_account_page.get_del_status()

            # 验证是否操作成功
            self.assertIn(succeed_prompt, del_status, "操作失败")

        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()