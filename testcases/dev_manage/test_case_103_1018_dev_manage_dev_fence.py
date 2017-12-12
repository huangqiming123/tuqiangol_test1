import unittest

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase103DevManageDevFence(unittest.TestCase):
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

    def test_case_103_dev_manage_dev_fence(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 搜索设备564123456789567
        self.dev_manage_page.search_dev_in_dev_manage_page('121201234567889')
        self.dev_manage_page.click_look_dev_fence_in_dev_page()

        # 判断进出围栏是否勾选
        in_fence = self.dev_manage_page.get_in_fence_select_in_look_fence_page()
        out_fence = self.dev_manage_page.get_out_fence_select_in_look_fence_page()
        if in_fence == True:
            self.dev_manage_page.click_in_fence_input_checkbox()
            in_fence = self.dev_manage_page.get_in_fence_select_in_look_fence_page()
            self.assertEqual(False, in_fence)
        else:
            self.dev_manage_page.click_in_fence_input_checkbox()
            in_fence = self.dev_manage_page.get_in_fence_select_in_look_fence_page()
            self.assertEqual(True, in_fence)

        if out_fence == True:
            self.dev_manage_page.click_out_fence_input_checkbox()
            out_fence = self.dev_manage_page.get_out_fence_select_in_look_fence_page()
            self.assertEqual(False, out_fence)
        else:
            self.dev_manage_page.click_out_fence_input_checkbox()
            out_fence = self.dev_manage_page.get_out_fence_select_in_look_fence_page()
            self.assertEqual(True, out_fence)

        # 点击保存
        # self.dev_manage_page.click_ensure()
        # 点击取消
        self.dev_manage_page.click_cancels()
