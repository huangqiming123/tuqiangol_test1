import csv
import unittest
from time import sleep

import pymysql

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


# 客户管理-下级客户-单个客户编辑

# author:孙燕妮

class TestCase082CustManageLowerAccountEdit(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page  = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page  = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_lower_account_edit(self):
        '''客户管理-下级客户-单个客户编辑'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()


        # 点击进入下级客户
        self.cust_manage_lower_account_page.enter_lower_acc()


        csv_file = self.cust_manage_page_read_csv.read_csv('lower_acc_edit.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            edit_info = {
                "acc_type": row[0],
                "acc_name": row[1],
                "phone": row[2],
                "email": row[3],
                "conn": row[4],
                "com": row[5]
            }


            # 点击单个用户的编辑
            self.cust_manage_lower_account_page.click_acc_edit()

            # 选择客户类型
            sleep(3)
            self.cust_manage_lower_account_page.acc_type_choose(edit_info["acc_type"])
            # 编辑信息
            self.cust_manage_lower_account_page.edit_acc_input_info_edit(edit_info["acc_name"],
                                                                         edit_info["phone"],
                                                                         edit_info["email"],
                                                                         edit_info["conn"],
                                                                         edit_info["com"])

            # 保存
            self.cust_manage_lower_account_page.edit_info_save()

            # 获取操作状态
            status = self.cust_manage_lower_account_page.edit_info_save_status()

            # 验证是否操作成功
            self.assertIn("操作成功", status, "操作失败")




        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

