import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1110DevManageShutDown(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1110_dev_manage_shut_down(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 测试选中停机
        self.dev_manage_page.click_dev_in_list()

        # 点击选中停机
        self.dev_manage_page.click_select_shut_down()
        # 点击确定
        self.dev_manage_page.click_ensure()
        get_dev_status = self.dev_manage_page.get_dev_status_in_list()
        self.assertEqual('停机', get_dev_status)

        # 点击选中停机
        self.dev_manage_page.click_dev_in_list()
        self.dev_manage_page.click_select_shut_down()
        # 点击取消
        self.dev_manage_page.click_cancel()
        get_dev_status = self.dev_manage_page.get_dev_status_in_list()
        self.assertEqual('停机', get_dev_status)

        # 点击选中停机
        self.dev_manage_page.click_select_shut_down()
        # 点击关闭
        self.dev_manage_page.click_close()
        get_dev_status = self.dev_manage_page.get_dev_status_in_list()
        self.assertEqual('停机', get_dev_status)

        # 点击本次查询全部停机
        self.dev_manage_page.click_all_shut_down()
        self.dev_manage_page.click_ensure()

        # 断言
        get_all_page = self.dev_manage_page.get_all_pages()

        if get_all_page == 0:
            pass
        elif get_all_page == 1:
            per_number = self.dev_manage_page.get_per_number()
            for m in range(per_number):
                text = self.dev_manage_page.get_text_dev_status(m + 1)
                self.assertEqual('停机', text)
        else:
            for n in range(get_all_page):
                self.dev_manage_page.click_per_page(n + 1)
                sleep(2)
                # 获取当前页面有多少条
                per_number = self.dev_manage_page.get_per_number()

                for m in range(per_number):
                    text = self.dev_manage_page.get_text_dev_status(m + 1)
                    self.assertEqual('停机', text)
