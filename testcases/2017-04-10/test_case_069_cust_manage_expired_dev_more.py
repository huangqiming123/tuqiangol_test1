import csv
import unittest


from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-过期设备列表-更多

# author:孙燕妮

class TestCase069CustManageExpiredDevMore(unittest.TestCase):
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
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_expired_dev_more(self):
        '''客户管理-过期设备列表-更多'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 点击进入到期客户
        self.cust_manage_cust_list_page.click_expired_cust()

        # 选择用户到期
        #self.cust_manage_cust_list_page.select_expired_type("用户到期")

        # 选择已过期
        self.cust_manage_cust_list_page.select_expired_status("已过期")

        # 选择过期时间段
        self.cust_manage_cust_list_page.select_expired_time("30天内")

        self.driver.wait()

        # 点击已过期用户
        self.cust_manage_cust_list_page.click_const_acc()

        self.driver.wait()

        # 右侧过期设备列表中的设备-更多-二维码
        self.cust_manage_cust_list_page.expired_dev_more("二维码")

        # 右侧过期设备列表中的设备-更多-查看围栏
        self.cust_manage_cust_list_page.expired_dev_more("查看围栏")

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 右侧过期设备列表中的设备-更多-查看告警
        self.cust_manage_cust_list_page.expired_dev_more("查看告警")


        expect_url = self.base_url + '/alarmInfo/toAlarmInfo'

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


