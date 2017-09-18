import unittest

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase101DevManageBatchSetOverdueTime(unittest.TestCase):
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

    def test_dev_manage_search_dev_after_issued_work_type(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in_jimitest()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        imei_in_list = self.dev_manage_page.get_imei_in_list()

        # 点击批量设置用户到期时间
        self.dev_manage_page.click_batch_set_user_overdue_time_button()
        # 点击关闭
        self.dev_manage_page.click_close_set_user_overdue_time_button()

        # 点击批量设置用户到期时间
        self.dev_manage_page.click_batch_set_user_overdue_time_button()
        # 点击关闭
        self.dev_manage_page.click_clance_set_user_overdue_time_button()

        # 点击批量设置用户到期时间
        self.dev_manage_page.click_batch_set_user_overdue_time_button()
        # 验证界面
        text = self.dev_manage_page.get_text_after_click_set_user_overdue_time_button()
        self.assertEqual(self.assert_text.batch_set_user_overdue_time_text(), text)

        # 点击添加imei
        self.dev_manage_page.click_add_imei_to_set_user_overdue_time('不存在')
        # 获取失败的状态和原因
        fail_status = self.dev_manage_page.get_fail_status_after_clcik_ensure()
        self.assertEqual(self.assert_text.dev_page_fail_text(), fail_status)
        fail_reason = self.dev_manage_page.get_fail_reason_after_click_ensure()
        self.assertEqual(self.assert_text.dev_page_inexistence_text(), fail_reason)

        # 点击关闭
        self.dev_manage_page.click_close_fail_text()

        # 点击添加imei
        self.dev_manage_page.click_add_imei_to_set_user_overdue_time(imei_in_list)
        self.dev_manage_page.click_add_imei_to_set_user_overdue_time(imei_in_list)
        # 获取失败的状态和原因
        fail_status = self.dev_manage_page.get_fail_status_after_clcik_ensure()
        self.assertEqual(self.assert_text.dev_page_fail_text(), fail_status)
        fail_reason = self.dev_manage_page.get_fail_reason_after_click_ensure()
        self.assertEqual(self.assert_text.dev_page_repetition_text(), fail_reason)

        # 点击关闭
        self.dev_manage_page.click_close_fail_text()
