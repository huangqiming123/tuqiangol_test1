import csv
import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv
from pages.login.login_page import LoginPage

__author__ = ''

class TestCase404CustomerManagementAddAUserWebLimit(unittest.TestCase):
    # 测试客户管理-新增用户-验证web登陆权限
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.close_window()
        self.driver.quit_browser()

    def test_add_user_web_limit_verify(self):
        '''测试客户管理-web权限验证'''

        self.base_page.open_page()

        csv_file = self.cust_manage_page_read_csv.read_csv('add_user_web_limit_data.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            info = {
                "keyword": row[0],
                "type": row[1],
                "name": row[2],
                "account": row[3],
                "passwd": row[4],
                "phone": row[5],
                "email": row[6],
                "conn": row[7],
                "com": row[8],
                "web_setting": row[9],
                "app_setting": row[10]
            }

            # 登录
            self.log_in_base.log_in()

            # 进入客户管理页面
            current_handle = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
            self.base_page.change_windows_handle(current_handle)

            self.cust_manage_basic_info_and_add_cust_page.add_acc()
            self.cust_manage_basic_info_and_add_cust_page.close_add_account()

            self.cust_manage_basic_info_and_add_cust_page.add_acc()
            self.cust_manage_basic_info_and_add_cust_page.locate_to_iframe()
            self.cust_manage_basic_info_and_add_cust_page.add_acc_input_info_edit(info["name"], info["account"],
                                                                                  info["passwd"],
                                                                                  info["phone"], info["email"],
                                                                                  info["conn"], info["com"])
            # 是或否勾选web和app登录权限
            web_status = self.cust_manage_basic_info_and_add_cust_page.setting_web_login_permissions(
                info["web_setting"])
            app_status = self.cust_manage_basic_info_and_add_cust_page.setting_app_login_permissions(
                info["app_setting"])
            self.assertEqual(info["web_setting"], str(web_status), "勾选状态与期望不一致")
            self.assertEqual(info["app_setting"], str(app_status), "勾选状态与期望不一致")
            self.driver.default_frame()
            sleep(2)
            self.cust_manage_basic_info_and_add_cust_page.acc_add_save()
            sleep(1)

            self.account_center_page_navi_bar.usr_logout()

            # 没有web登录权限验证
            if web_status == False:
                self.log_in_base.log_in_with_csv(info["account"], info["passwd"])
                self.assertEqual(self.assert_text2.login_no_permissions(), self.login_page.get_exception_text(),
                                 "没有获取到没有权限登录的提示")
            # 有web登录权限验证
            elif web_status == True:
                self.log_in_base.log_in_with_csv(info["account"], info["passwd"])
                sleep(2)
                hello_usr = self.account_center_page_navi_bar.usr_info_account()
                self.assertIn(info["account"], hello_usr, "登录成功后招呼栏账户名显示错误")
                sleep(1)
                self.log_in_base.click_account_center_button()
                self.account_center_page_navi_bar.usr_logout()

            self.log_in_base.log_in()

            current_handle_01 = self.driver.get_current_window_handle()
            self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
            self.base_page.change_windows_handle(current_handle_01)

            # 搜索新增客户
            self.cust_manage_lower_account_page.input_search_info(info["account"])
            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()
            # 删除该新增客户
            self.cust_manage_lower_account_page.delete_acc()
            self.cust_manage_lower_account_page.delete_acc_ensure()
            # 获取删除操作状态
            del_status = self.cust_manage_lower_account_page.get_del_status()
            self.assertIn(self.assert_text.account_center_page_operation_done(), del_status, "操作失败")

            # 退出登录
            sleep(1)
            self.account_center_page_navi_bar.usr_logout()
        csv_file.close()
