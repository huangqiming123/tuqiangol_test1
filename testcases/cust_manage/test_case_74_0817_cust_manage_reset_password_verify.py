import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-单个客户操作 --取消和确定重置密码验证
# author:戴招利
class TestCase7408171CustManagelResetPasswordVerify(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.assert_text2 = AssertText2()
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cancel_and_ascertain_reset_password(self):
        '''客户管理-取消和确定重置密码操作'''
        account = ["jianyigezh1"]

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        self.driver.wait(1)
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        # 搜索账号
        self.cust_manage_lower_account_page.input_search_info(account[0])
        self.cust_manage_lower_account_page.click_search_btn()
        self.assertEqual(account[0], self.cust_manage_lower_account_page.get_search_result_account(), "搜索结果账号不一致")
        # 取消重置密码
        self.cust_manage_lower_account_page.click_reset_passwd_dismiss()

        # 取消重置密码后的验证
        self.account_center_page_navi_bar.usr_logout()
        self.log_in_base.log_in_with_csv(account[0], "jimi123")
        hello_usr = self.account_center_page_navi_bar.hello_user_account()
        self.assertIn(account[0], hello_usr, "登录成功后招呼栏账户名显示错误")
        sleep(1)
        self.account_center_page_navi_bar.usr_logout()

        #再次登录，重置密码
        self.log_in_base.log_in()
        self.driver.wait(1)
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.cust_manage_lower_account_page.input_search_info(account[0])
        self.cust_manage_lower_account_page.click_search_btn()
        # 点击单个用户的重置密码
        self.cust_manage_lower_account_page.acc_reset_passwd()

        # 获取重置密码弹框文本内容
        text = self.cust_manage_lower_account_page.reset_passwd_content()
        hint_password = text.split(":")[2]
        # 验证重密码是否正确显示
        self.assertEqual("888888", hint_password, "弹框中的重置密码显示的不是888888")

        # 确定重置密码
        self.cust_manage_lower_account_page.reset_passwd_ensure()
        # 获取重置状态
        reset_status = self.cust_manage_lower_account_page.reset_passwd_content()
        # 验证操作状态是否成功
        self.assertIn(self.assert_text.account_center_page_operation_done(), reset_status, "操作失败")
        # 退出登录
        sleep(1)
        self.account_center_page_navi_bar.usr_logout()

        # 修改用户的默认密码
        self.log_in_base.log_in_with_csv(account[0], hint_password)
        sleep(2)
        # 修改用户默认密码(jimi123)
        self.cust_manage_basic_info_and_add_cust_page.user_default_password_edit("jimi123")
        sleep(2)
        # 获取密码修改成功
        status = self.cust_manage_basic_info_and_add_cust_page.user_default_password_edit_prompt()
        self.assertIn(self.assert_text2.home_page_edit_password_success(), status, "修改密码失败！")
        sleep(2)
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "修改默认密码后，没有返回到登录页")
