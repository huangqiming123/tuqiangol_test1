import csv
import unittest

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-用户搜索-不输入搜索信息查找

# author:孙燕妮

class TestCase042GlobAccountSearchList(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_acc_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_account_search_list(self):
        '''测试全局搜索-用户搜索-不输入搜索信息查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 不输入搜索关键词点击“用户”搜索按钮
        self.driver.wait(1)

        self.global_acc_search_page.click_account_search()

        # 点击用户搜索对话框的搜索按钮
        self.global_acc_search_page.click_account_dial_search()
        first_account = self.global_acc_search_page.get_first_account()

        csv_file = self.global_search_page_read_csv.read_csv('acc_list_link.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            link_info = {
                "link_name": row[0],
                "link_url": row[1]
            }

            # 验证设备列表中各个页面的链接跳转是否正确

            self.global_acc_search_page.click_acc_list_link(link_info["link_name"])

            expect_url = self.base_url + link_info["link_url"]

            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()

                    self.assertEqual(expect_url, current_url, link_info["link_name"] + "页面跳转错误!")
                    # 关闭当前窗口
                    self.driver.close_current_page()
                    # 回到账户中心窗口
                    self.driver.switch_to_window(account_center_handle)
                    self.driver.wait()

        csv_file.close()

        # 列表点击详情进入子模块验证“返回列表”功能
        # 点击详情
        self.global_acc_search_page.click_acc_details()

        # 点击返回列表
        self.global_acc_search_page.return_list()

        # 点击重置密码
        self.global_acc_search_page.click_acc_reset_pwd()

        # 验证弹框文本内容
        content = self.global_acc_search_page.reset_passwd_content()
        self.assertIn("重置后密码为:888888", content, "弹窗文本内容不全")

        # 取消重置
        self.global_acc_search_page.reset_passwd_dismiss()

        # 点击当前设备用户的重置密码按钮
        self.global_acc_search_page.click_acc_reset_pwd()

        # 验证弹框文本内容
        content = self.global_acc_search_page.reset_passwd_content()
        self.assertIn("重置后密码为:888888", content, "弹窗文本内容不全")

        # 确定重置
        self.global_acc_search_page.reset_passwd_ensure()

        # 验证操作状态是否成功
        status = self.global_acc_search_page.get_reset_status()

        self.assertIn("操作成功", status, "操作失败")

        self.driver.wait()

        # 导出
        self.global_acc_search_page.acc_list_export()

        # 关闭当前设备搜索对话框
        self.global_acc_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

        # 用已重置的账号登录系统-account_01
        self.log_in_base.log_in_with_csv(first_account, "888888")
        self.driver.wait()

        # 验证是否成功登录跳转至首页
        expect_url = self.base_url + "/customer/toAccountCenter"

        self.assertEqual(expect_url, self.driver.get_current_url(), "页面跳转错误")

        # 重置密码后首次登录强制修改密码
        self.base_page.force_reset_passwd("jimi123")

        # 验证重置状态
        reset_stat = self.base_page.reset_passwd_stat_cont()
        self.assertIn("密码修改成功", reset_stat, "密码强制修改成功")

        # 点击弹框确定
        self.base_page.reset_passwd_succ_ensure()
