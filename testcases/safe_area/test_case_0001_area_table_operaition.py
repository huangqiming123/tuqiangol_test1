import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase0001AreaTableOperaition(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_0001_area_table_operaition(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 点击删除按钮
        self.safe_area_page.click_all_select_button()
        # 点击删除
        self.safe_area_page.click_delete_button()
        sleep(1)
        # 点击取消删除
        self.safe_area_page.click_cancel_detele_button()

        # 点击列表中的编辑
        self.safe_area_page.click_list_edit_button()
        # 断言
        self.assertEqual('编辑', self.safe_area_page.get_text_after_click_edit())
        # 输入内容保存
        self.safe_area_page.ensure_edit_list('名称', '描述')

        # 点击列表中的编辑
        self.safe_area_page.click_list_edit_button()
        # 断言
        self.assertEqual('编辑', self.safe_area_page.get_text_after_click_edit())
        # 输入内容保存
        self.safe_area_page.click_cancel_edit()


        # 点击列表中的删除
        self.safe_area_page.click_list_delete_button()
        # 取消
        self.safe_area_page.click_cancel_detele_button()

        # 点击列表中的删除
        self.safe_area_page.click_list_delete_button()
        # 关闭
        self.safe_area_page.click_close_detele_button()

