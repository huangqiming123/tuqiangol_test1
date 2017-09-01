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


# 客户管理-单个客户操作 --取消和确定删除账号验证
# author:戴招利
class TestCase7508171CustManagelDeleteAccountVerify(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
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

    def test_cancel_and_ascertain_delete_account(self):
        '''客户管理-取消和确定删除账号操作'''


        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.driver.wait(1)
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 删除有绑定或分配有设备的账号
        search_data = {'account': "csscgndh", "account_type": "", "info": "scybdsbhfpysbdh"}
        self.cust_manage_lower_account_page.add_data_to_search_account(search_data)
        self.assertEqual(search_data["info"], self.cust_manage_lower_account_page.get_search_result_account(),
                         "搜索结果账号不一致")
        #确定删除
        self.cust_manage_lower_account_page.delete_acc()
        self.cust_manage_lower_account_page.delete_acc_ensure()
        self.assertEqual(self.assert_text2.cust_manage_exist_facility_cannot_del(),
                         self.cust_manage_lower_account_page.get_del_status(), "删除提示不一致")
        sleep(3)

        # 删除有下级客户的账号
        account = ["csscgndh"]
        self.cust_manage_basic_info_and_add_cust_page.click_left_tree_current_user()
        # 搜索账号
        self.cust_manage_lower_account_page.input_search_info(account[0])
        self.cust_manage_lower_account_page.click_search_btn()
        self.assertEqual(account[0], self.cust_manage_lower_account_page.get_search_result_account(), "搜索结果账号不一致")
        #确定删除
        self.cust_manage_lower_account_page.delete_acc()
        self.cust_manage_lower_account_page.delete_acc_ensure()
        #验证有下级客户的账号
        self.assertEqual(self.assert_text2.cust_manage_exist_user_cannot_del(),
                         self.cust_manage_lower_account_page.get_del_status(), "删除提示不一致")
        sleep(2)

        #取消删除后的验证
        self.cust_manage_lower_account_page.delete_acc_x()
        #退出
        self.account_center_page_navi_bar.usr_logout()
        self.log_in_base.log_in_with_csv(account[0], "jimi123")
        self.driver.wait(1)
        hello_usr = self.account_center_page_navi_bar.hello_user_account()
        self.assertIn(account[0], hello_usr, "登录成功后招呼栏账户名显示错误")
        sleep(1)
        self.account_center_page_navi_bar.usr_logout()
