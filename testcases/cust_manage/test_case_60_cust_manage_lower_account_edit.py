import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv

from pages.login.login_page import LoginPage


class TestCase60CustManageLowerAccountEdit(unittest.TestCase):
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
        self.assert_text = AssertText()
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
        self.driver.wait(1)
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

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
            sleep(2)
            # 取消
            self.cust_manage_lower_account_page.edit_info_cancel()
            # 点击单个用户的编辑
            self.cust_manage_lower_account_page.click_acc_edit()

            # 选择客户类型
            sleep(3)
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.cust_manage_lower_account_page.acc_type_choose(edit_info["acc_type"])
            # 编辑信息
            self.cust_manage_lower_account_page.edit_acc_input_info_edit(edit_info["acc_name"],
                                                                         edit_info["phone"],
                                                                         edit_info["email"],
                                                                         edit_info["conn"],
                                                                         edit_info["com"])

            # 保存
            self.driver.default_frame()
            self.cust_manage_lower_account_page.edit_info_save()

            # 获取操作状态
            status = self.cust_manage_lower_account_page.edit_info_save_status()

            # 验证是否操作成功
            self.assertIn(self.assert_text.account_center_page_operation_done(), status, "操作失败")
