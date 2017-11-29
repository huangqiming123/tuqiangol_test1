import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-下级客户-单个客户操作（控制台、重置密码、删除）

# author:孙燕妮

class TestCase61CustManageLowerAccountOperate(unittest.TestCase):
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
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_lower_account_operate(self):
        '''客户管理-下级客户-单个客户操作'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        self.driver.wait(1)
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.driver.wait()
        # account = self.cust_manage_basic_info_and_add_cust_page.get_account_text()

        # 点击单个用户的重置密码
        self.cust_manage_lower_account_page.acc_reset_passwd()

        # 获取重置密码弹框文本内容
        text = self.cust_manage_lower_account_page.reset_passwd_content()

        # 验证重置密码弹框文本内容是否正确显示
        self.assertIn(self.assert_text.cust_page_are_you_reset_this_password(), text, "重置密码弹框文本内容显示错误")

        # 确定重置密码
        self.cust_manage_lower_account_page.reset_passwd_ensure()

        # 获取重置状态
        reset_status = self.cust_manage_lower_account_page.reset_passwd_content()

        # 验证操作状态是否成功
        self.assertIn(self.assert_text.account_center_page_operation_done(), reset_status, "操作失败")


        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()
        # 点击单个用户的控制台
        self.cust_manage_lower_account_page.enter_console()
        self.driver.wait()

        expect_url = self.base_url + "/index"

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                current_url = self.driver.get_current_url()

                self.assertEqual(expect_url, current_url, "控制台页面跳转错误!")

                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 点击单个用户的删除
        self.cust_manage_lower_account_page.delete_acc()
        self.driver.click_element('c,layui-layer-btn1')
