import csv
import unittest
from time import sleep

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


# 账户中心-账户详情-快捷销售-新增客户并成功销售设备给新客户
# author:孙燕妮

class TestCase018AccountCenterFastSaleAddCust(unittest.TestCase):
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
            self.driver.wait()
            # 进入快捷销售页面
            self.account_center_page_details.fast_sales()
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

            # 验证是否操作成功
            self.assertIn("操作成功", status, "操作失败")

            self.driver.click_element('x,//*[@id="addRole"]/div/div/div[3]/button[2]')
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
            self.assertEqual(expect_dev_num, dev_num, "已选设备个数错误")
            # 销售
            self.account_center_page_details.sale_button()
            # 通过弹出框状态验证是否销售成功
            sale_status_text = self.account_center_page_details.get_sale_status()
            self.assertIn("操作成功", sale_status_text, "销售失败")

            # 转移设备
            self.driver.click_element('x,//*[@id="device"]/a')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="treeDemo_cusTreeKey"]', add_info['account'])
            # 搜索
            self.driver.click_element('x,//*[@id="treeDemo_cusTreeSearchBtn"]')
            self.driver.wait()
            # 选中查询结果
            self.driver.click_element("c,autocompleter-item")
            self.driver.wait(1)

            self.driver.operate_input_element('x,//*[@id="searchIMEI"]', search_info['device_imei'])
            self.driver.click_element('x,//*[@id="allDev"]/div[2]/div[1]/div/div[4]/div[6]/div[7]/button[1]')
            sleep(3)

            self.driver.click_element('x,//*[@id="markDevTable"]/tr[1]/td[11]/a[2]')
            sleep(2)

        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
