import unittest
import time

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase73DevManageDevSearchByTime(unittest.TestCase):
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

    def test_dev_manage_dev_search_by_time(self):
        '''测试设备管理-设备搜索-by imei'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        self.dev_manage_page.click_more_button()

        # 选择激活时间输入开始时间为XXX,点击搜索，点击搜索，点击导出
        begin_time = '2016-08-30'
        end_time = '2017-04-05'
        begin_time_strptime = time.strptime(begin_time, '%Y-%m-%d')
        end_time_strptime = time.strptime(end_time, '%Y-%m-%d')
        self.dev_manage_page.input_begin_time_to_serach(begin_time)
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                active_time = self.dev_manage_page.get_active_time_after_search(n)
                active_time_strptime = time.strptime(active_time, '%Y-%m-%d')
                a = active_time_strptime > begin_time_strptime
                self.assertEqual(True, a)

        # 选择激活时间输入结束时间为XXX,点击搜索，点击搜索，点击导出
        self.dev_manage_page.input_begin_time_to_serach('')
        self.dev_manage_page.input_end_time_to_search(end_time)
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                active_time = self.dev_manage_page.get_active_time_after_search(n)
                active_time_strptime = time.strptime(active_time, '%Y-%m-%d')
                a = active_time_strptime > end_time_strptime
                self.assertEqual(False, a)

        # 选择激活时间输入开始时间为XXX,结束时间为XXX点击搜索
        self.dev_manage_page.input_begin_time_to_serach(begin_time)
        self.dev_manage_page.input_end_time_to_search(end_time)
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                active_time = self.dev_manage_page.get_active_time_after_search(n)
                active_time_strptime = time.strptime(active_time, '%Y-%m-%d')
                a = active_time_strptime > end_time_strptime
                self.assertEqual(False, a)
                b = active_time_strptime > begin_time_strptime
                self.assertEqual(True, b)

        # 选择平台到期时间输入开始时间为XXX,点击搜索，点击搜索，点击导出
        # 选择平台到期时间
        self.dev_manage_page.choose_platform_time_to_serach()
        self.dev_manage_page.input_begin_time_to_serach(begin_time)
        self.dev_manage_page.click_search_btn()
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                platform_time = self.dev_manage_page.get_platform_time_after_search(n)
                platform_time_strptime = time.strptime(platform_time, '%Y-%m-%d')
                a = platform_time_strptime > begin_time_strptime
                self.assertEqual(True, a)

        # 选择平台到期时间输入结束时间为XXX,点击搜索，点击搜索，点击导出
        self.dev_manage_page.choose_platform_time_to_serach()
        self.dev_manage_page.input_begin_time_to_serach('')
        self.dev_manage_page.input_end_time_to_search(end_time)
        self.dev_manage_page.click_search_btn()
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                platform_time = self.dev_manage_page.get_platform_time_after_search(n)
                platform_time_strptime = time.strptime(platform_time, '%Y-%m-%d')
                a = platform_time_strptime > end_time_strptime
                self.assertEqual(False, a)

        # 选择平台到期时间输入开始时间为XXX,结束时间为XXX点击搜索
        self.dev_manage_page.choose_platform_time_to_serach()
        self.dev_manage_page.input_begin_time_to_serach(begin_time)
        self.dev_manage_page.input_end_time_to_search(end_time)
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                platform_time = self.dev_manage_page.get_platform_time_after_search(n)
                platform_time_strptime = time.strptime(platform_time, '%Y-%m-%d')
                a = platform_time_strptime > end_time_strptime
                self.assertEqual(False, a)
                b = platform_time_strptime > begin_time_strptime
                self.assertEqual(True, b)

        # 选择用户到期时间输入开始时间为XXX,点击搜索，点击搜索，点击导出
        self.dev_manage_page.choose_user_time_to_serach()
        self.dev_manage_page.input_begin_time_to_serach(begin_time)
        self.dev_manage_page.click_search_btn()
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                user_time = self.dev_manage_page.get_user_time_after_search(n)
                user_time_strptime = time.strptime(user_time, '%Y-%m-%d')
                a = user_time_strptime > begin_time_strptime
                self.assertEqual(True, a)

        # 选择用户到期时间输入结束时间为XXX,点击搜索，点击搜索，点击导出
        self.dev_manage_page.choose_user_time_to_serach()
        self.dev_manage_page.input_begin_time_to_serach('')
        self.dev_manage_page.input_end_time_to_search(end_time)
        self.dev_manage_page.click_search_btn()
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                user_time = self.dev_manage_page.get_user_time_after_search(n)
                user_time_strptime = time.strptime(user_time, '%Y-%m-%d')
                a = user_time_strptime > end_time_strptime
                self.assertEqual(False, a)

        # 选择用户到期时间输入开始时间为XXX,结束时间为XXX点击搜索
        self.dev_manage_page.choose_user_time_to_serach()
        self.dev_manage_page.input_begin_time_to_serach(begin_time)
        self.dev_manage_page.input_end_time_to_search(end_time)
        self.dev_manage_page.click_search_btn()
        # 获取查询出来的条数
        number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if number == 0:
            text = self.dev_manage_page.get_search_no_dev_name_text()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
        else:
            for n in range(number):
                user_time = self.dev_manage_page.get_user_time_after_search(n)
                user_time_strptime = time.strptime(user_time, '%Y-%m-%d')
                a = user_time_strptime > end_time_strptime
                self.assertEqual(False, a)
                b = user_time_strptime > begin_time_strptime
                self.assertEqual(True, b)
