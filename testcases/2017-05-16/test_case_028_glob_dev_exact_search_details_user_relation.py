import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv


# 全局搜索-精确查找设备结果唯一设备详情页面-用户关系模块的操作
# author:孙燕妮


class TestCase028GlobDevExactSearchDetailsUserRelation(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_dev_exact_search_details_user_relation(self):
        '''通过csv测试全局搜索-精确查找设备结果唯一设备详情页面-用户关系模块的操作功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()
        self.global_dev_search_page.click_equipment_button()
        sleep(2)

        csv_file = self.global_search_page_read_csv.read_csv('exact_dev_search_keyword.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            exact_search_keyword = {
                'search_imei': row[0],
                "link_name": row[1],
                "link_url": row[2]
            }
            # 全局搜索栏输入搜索关键词进行设备搜索
            self.global_dev_search_page.device_easy_search(exact_search_keyword['search_imei'])
            # 点击搜索结果-用户关系下的各个操作，并验证所跳转的页面正确
            self.global_dev_search_page.click_user_relation_link(exact_search_keyword["link_name"])
            expect_url = self.base_url + exact_search_keyword["link_url"]
            # 获取当前所有窗口句柄
            all_handles = self.driver.get_all_window_handles()
            for handle in all_handles:
                if handle != account_center_handle:
                    self.driver.switch_to_window(handle)
                    self.driver.wait(1)
                    current_url = self.driver.get_current_url()
                    self.assertEqual(expect_url, current_url, exact_search_keyword["link_name"] + "页面跳转错误!")
                    # 关闭当前窗口
                    self.driver.close_current_page()
                    # 回到账户中心窗口
                    self.driver.switch_to_window(account_center_handle)
                    self.driver.wait()
        csv_file.close()
        # 点击当前设备用户的重置密码按钮
        # 在重置密码前 获取用户名
        account = self.global_dev_search_page.get_account_before_reset_password()
        self.global_dev_search_page.curr_dev_reset_passwd()
        # 验证弹框文本内容
        content = self.global_dev_search_page.reset_passwd_content()
        self.assertIn("重置后密码为:888888", content, "弹窗文本内容不全")
        # 取消重置
        self.global_dev_search_page.reset_passwd_dismiss()
        # 点击当前设备用户的重置密码按钮
        self.global_dev_search_page.curr_dev_reset_passwd()
        # 验证弹框文本内容
        content = self.global_dev_search_page.reset_passwd_content()
        self.assertIn("重置后密码为:888888", content, "弹窗文本内容不全")
        # 确定重置
        self.global_dev_search_page.reset_passwd_ensure()
        # 验证操作状态是否成功
        status = self.global_dev_search_page.get_reset_status()
        self.assertIn("操作成功", status, "操作失败")
        self.driver.wait()
        # 关闭当前设备搜索对话框
        self.global_dev_search_page.close_dev_search()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
        # 用已重置的账号登录系统-account_01
        self.log_in_base.log_in_with_csv(account, "888888")
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
