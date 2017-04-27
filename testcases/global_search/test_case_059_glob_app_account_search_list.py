import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_app_account_search_page import GlobalAppAccountSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-App用户搜索-不输入搜索信息查找，列表操作

# author:孙燕妮

class TestCase058GlobAppAccountSearchList(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_app_account_search_page = GlobalAppAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_app_account_search_list(self):
        '''测试全局搜索-App用户搜索-不输入搜索信息查找，列表操作'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("jimitest", "jimi123")



        # 全局搜索栏-APP用户搜索
        self.global_app_account_search_page.click_app_account_search()

        # APP用户搜索对话框-搜索
        self.global_app_account_search_page.click_app_acc_dial_search()


        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 点击列表的控制台链接
        self.global_app_account_search_page.click_acc_list_console_link()


        expect_url = self.base_url + "/index"

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                self.driver.wait(1)
                current_url = self.driver.get_current_url()
                # 验证控制台页面是否跳转正确
                self.assertEqual(expect_url, current_url,  "列表控制台页面跳转错误!")
                # 关闭当前窗口
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()


        # 点击列表导出
        self.global_app_account_search_page.acc_list_export()

        # 点击列表的详情
        self.global_app_account_search_page.click_acc_details()


        # 关闭当前搜索对话框
        self.global_app_account_search_page.close_dev_search()
        self.driver.wait()


        # 退出登录
        self.account_center_page_navi_bar.usr_logout()


