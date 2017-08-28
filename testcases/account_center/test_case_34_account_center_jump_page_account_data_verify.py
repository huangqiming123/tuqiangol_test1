import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.login.login_page import LoginPage


# 账户中心-账户详情--跳转页面后验证登录账户的数据
# author:戴招利
class TestCase34AccountCenterJumpPageAccountDataVerify(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_jump_page_account_data_verify(self):
        """ 跳转页面后验证登录账户的数据是否正确"""
        # data = ["库存", "总进货数", "即将到期", "已过期", "设备管理", "已激活", "未激活"]
        data = ["即将到期", "已过期", "已激活", "未激活"]

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        sleep(2)

        # 获取当前登录账号
        # self.account_center_page_details.account_center_iframe()
        current_account = self.log_in_base.get_log_in_account()
        #self.driver.default_frame()
        account_center_handle = self.driver.get_current_window_handle()

        # 点击页面跳转到设备管理页面
        for page in data:
            self.account_center_page_details.account_center_iframe()
            self.account_center_page_details.account_overview(page)
            self.driver.default_frame()

            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    sleep(2)
                    actual_url = self.driver.get_current_url()
                    expect_url = self.base_url + self.assert_text2.get_page_expect_url(page)
                    self.assertEqual(expect_url, actual_url, '实际的url和期望的地址不一样！')

                    # 获取数据库登录账号数据
                    connect = self.connect_sql.connect_tuqiang_sql()
                    cursor = connect.cursor()
                    get_account_user_info_sql = "SELECT o.type,o.phone,o.parentId,o.nickName from user_info o " \
                                                "WHERE o.account = '" + current_account + "'"
                    cursor.execute(get_account_user_info_sql)
                    get_account_user_info = cursor.fetchall()
                    current_user_info = []
                    for range1 in get_account_user_info:
                        for range2 in range1:
                            current_user_info.append(range2)
                    print(current_user_info)

                    # 断言客户类型
                    type = self.assert_text.log_in_page_account_type(current_user_info[0])
                    account_type = self.cust_manage_basic_info_and_add_cust_page.get_account_type()
                    self.assertEqual(type, account_type, "客户类型不一致")

                    # 断言账号
                    account = self.cust_manage_basic_info_and_add_cust_page.get_account()
                    self.assertEqual(current_account, account, "账号不一致")
                    # 断言电话
                    account_phone = self.cust_manage_basic_info_and_add_cust_page.get_account_phone()
                    self.assertEqual(current_user_info[1], account_phone, "电话号码不一致")
                    # 断言昵称
                    account_name = self.cust_manage_basic_info_and_add_cust_page.get_account_name()
                    self.assertEqual(current_user_info[3], account_name, "客户昵称不一致")

                    # 点击设备管理页---监控用户
                    self.cust_manage_basic_info_and_add_cust_page.click_dev_page_monitoring_account_button()
                    self.driver.close_current_page()
                    sleep(2)
                    all_handles2 = self.driver.get_all_window_handles()

                    for handle in all_handles2:

                        if handle != account_center_handle:
                            self.driver.switch_to_window(handle)
                            actual_url = self.driver.get_current_url()
                            self.assertEqual(self.base_url + "/index", actual_url, "控制台地址与期望不一致")
                            username = self.cust_manage_basic_info_and_add_cust_page.get_console_page_username()
                            self.assertEqual(current_user_info[3], username, "客户昵称不一致")
                            sleep(3)
                            self.driver.close_current_page()
                            self.driver.switch_to_window(account_center_handle)
                            sleep(2)
