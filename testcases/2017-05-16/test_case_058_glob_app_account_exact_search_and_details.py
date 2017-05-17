import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_app_account_search_page import GlobalAppAccountSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv

# 全局搜索-App用户搜索-精确查找

# author:孙燕妮

class TestCase058GlobAppAccountExactSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_app_account_search_page = GlobalAppAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()

        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_app_account_exact_search(self):
        '''测试全局搜索-App用户搜索-精确查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in_jimitest()

        # 全局搜索栏-APP用户搜索
        self.global_app_account_search_page.click_app_account_search()

        # 在APP用户搜索对话框输入搜索关键词进行搜索
        self.global_app_account_search_page.account_dial_search("13880322437")

        # 获取搜索结果
        name_text = self.global_app_account_search_page.get_exact_search_name()

        # 验证搜素结果账户与搜索输入的关键词账户是否一致
        self.assertIn("13880322437", name_text, "搜索结果与输入的搜索词不一致")

        csv_file_01 = self.global_search_page_read_csv.read_csv('app_account_link.csv')
        csv_data_01 = csv.reader(csv_file_01)

        for row in csv_data_01:
            link_info = {
                "link_name": row[0],
                "link_url": row[1]
            }

            # 获取当前窗口句柄
            account_center_handle = self.driver.get_current_window_handle()

            # 点击app用户及其设备各个操作链接
            self.global_app_account_search_page.click_app_acc_and_dev_link(link_info["link_name"])

            expect_url = self.base_url + link_info["link_url"]

            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()
                    # 验证控制台页面是否跳转正确
                    self.assertEqual(expect_url, current_url, link_info["link_name"] + "页面跳转错误!")
                    # 关闭当前窗口
                    self.driver.close_current_page()
                    # 回到账户中心窗口
                    self.driver.switch_to_window(account_center_handle)
                    self.driver.wait()

        csv_file_01.close()

        # 点击当前用户“重置密码”
        self.global_app_account_search_page.curr_acc_reset_passwd()

        # 获取“重置密码”弹框文本内容
        text = self.global_app_account_search_page.reset_passwd_content()

        # 验证弹框内容是否正确
        self.assertIn("重置后密码为:888888", text, "弹框内容正确")

        # 确定重置密码
        self.global_app_account_search_page.reset_passwd_ensure()

        # 获取“重置密码”-确定-操作状态
        status = self.global_app_account_search_page.get_reset_status()

        # 验证是否重置成功
        self.assertIn("操作成功", status, "操作成功")

        # 点击当前用户绑定设备的详情并返回
        self.global_app_account_search_page.app_dev_details()
        # 关闭当前搜索对话框
        self.global_app_account_search_page.close_dev_search()
        self.driver.wait()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
