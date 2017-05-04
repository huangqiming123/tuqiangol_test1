import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv

from pages.login.login_page import LoginPage


# 客户管理-我的设备-单个设备操作-销售、查看位置

# author:孙燕妮

class TestCase076CustManageMyDevSaleAndLocate(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.driver.set_window_max()
        self.driver.clear_cookies()

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_my_dev_sale_and_locate(self):
        '''客户管理-我的设备-单个设备操作-销售、查看位置'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        csv_file = self.cust_manage_page_read_csv.read_csv('dev_sale.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            sale_info = {
                "user_name": row[0],
                "imei": row[1]
            }

            # 点击单个设备-销售
            self.cust_manage_my_dev_page.dev_sale()

            # 获取当前已选中的设备数
            selected_dev = self.cust_manage_my_dev_page.get_curr_selected_dev_num().text
            if int(selected_dev) > 0:
                # 右侧搜索框搜索销售客户
                self.cust_manage_my_dev_page.select_sale_acc(sale_info["user_name"])
            else:
                # 输入imei号
                self.cust_manage_my_dev_page.input_dev_imei(sale_info["imei"])
                # 右侧搜索框搜索销售客户
                self.cust_manage_my_dev_page.select_sale_acc(sale_info["user_name"])
            # 销售
            self.cust_manage_my_dev_page.sale_button()
            sleep(2)
            '''sale_status = self.cust_manage_my_dev_page.get_sale_status()
            # 验证是否操作成功
            self.assertIn("操作成功", sale_status, "操作失败")'''
        csv_file.close()
        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()
        # 单个设备 - 查看位置
        self.cust_manage_my_dev_page.dev_site()
        expect_url = self.base_url + '/index'

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                current_url = self.driver.get_current_url()

                self.assertEqual(expect_url, current_url, "查看位置页面跳转错误!")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
