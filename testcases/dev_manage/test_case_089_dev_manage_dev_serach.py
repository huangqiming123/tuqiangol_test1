import unittest
import time

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase089DevManageDevSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_search(self):
        '''测试设备管理-设备搜索-by imei'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        self.dev_manage_page.click_more_button()

        # 过期状态选择平台即将过期，点击搜索，点击导出
        self.dev_manage_page.choose_platform_soon_expire_time()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                platform_time = self.dev_manage_page.get_platform_time_after_search(n)
                platform_time_strptime = time.strptime(platform_time.split('(')[0], '%Y-%m-%d')
                new_times = time.strftime('%Y-%m-%d')
                new_time = time.strptime(new_times, '%Y-%m-%d')
                a = new_time < platform_time_strptime
                self.assertEqual(True, a)

                expire_time_platform = int(platform_time.split('(')[1].split('天')[0])
                b = expire_time_platform > 0
                c = expire_time_platform < 30
                self.assertEqual(True, b)
                self.assertEqual(True, c)

        # 过期状态选择平台已过期，点击搜索，点击导出出
        self.dev_manage_page.choose_platform_expire_time()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                platform_time = self.dev_manage_page.get_platform_time_after_search(n)
                self.assertEqual(self.assert_text.account_center_page_expired_text(), platform_time)

        # 过期状态选择用户即将过期，点击搜索
        self.dev_manage_page.choose_user_soon_expire_time()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                user_time = self.dev_manage_page.get_user_time_after_search(n)
                user_time_strptime = time.strptime(user_time.split('(')[0], '%Y-%m-%d')
                new_times = time.strftime('%Y-%m-%d')
                new_time = time.strptime(new_times, '%Y-%m-%d')
                a = new_time < user_time_strptime
                self.assertEqual(True, a)

                expire_time_user = int(user_time.split('(')[1].split('天')[0])
                b = expire_time_user > 0
                c = expire_time_user < 30
                self.assertEqual(True, b)
                self.assertEqual(True, c)

        # 过期状态选择用户已过期，点击搜索，点击导出
        self.dev_manage_page.choose_user_expire_time()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                user_time = self.dev_manage_page.get_user_time_after_search(n)
                self.assertEqual(self.assert_text.account_center_page_expired_text(), user_time)

        # 激活状态选择已激活，点击搜索，点击导出
        self.dev_manage_page.no_choose_expire_time()
        self.dev_manage_page.choose_active_dev()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                active_state = self.dev_manage_page.get_active_state_after_search(n)
                self.assertNotEqual(self.assert_text.account_center_page_activing_text(), active_state)

        # 激活状态选择未激活，点击搜索，点击导出
        self.dev_manage_page.choose_noactive_dev()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                active_state = self.dev_manage_page.get_active_state_after_search(n)
                self.assertEqual(self.assert_text.account_center_page_activing_text(), active_state)

        # 绑定状态选择已绑定，点击搜索，点击导出
        self.dev_manage_page.no_choose_active_state_dev()
        self.dev_manage_page.choose_band_dev()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                band_state = self.dev_manage_page.get_band_state_after_search(n)
                self.assertNotEqual('', band_state)

        # 绑定状态选择未绑定，点击搜索，点击导出
        self.dev_manage_page.choose_no_band_dev()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                band_state = self.dev_manage_page.get_band_state_after_search(n)
                self.assertEqual('', band_state)

        # 所有分组选择选中用户的一个分组，点击搜索，点击导出
        self.dev_manage_page.no_choose_band_state_dev()
        self.dev_manage_page.choose_user_group_to_search()
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_numbers_after_click_search()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                get_choose_group_name = self.dev_manage_page.get_choose_group_name()
                get_group_name_in_list = self.dev_manage_page.get_group_name_in_list(n)
                self.assertEqual(get_choose_group_name, get_group_name_in_list)
