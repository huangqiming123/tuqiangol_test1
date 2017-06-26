import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase1106SafeAreaMarkPointOperation(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.driver.set_window_max()
        self.log_in_base.log_in_jimitest()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1106_safe_area_mark_point_operation(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())
        # 点击标注点
        self.safe_area_page.click_mark_button()

        # 获取列表中第一个标注点名称
        mark_point_name = self.safe_area_page.get_first_name_in_mark_point_list()

        # 点击编辑
        self.safe_area_page.click_edit_button_in_mark_point()
        get_name = self.safe_area_page.get_name_after_click_edit()
        self.assertIn(get_name, mark_point_name)
        self.safe_area_page.click_cancel_edit()

        # 点击编辑
        self.safe_area_page.click_edit_button_in_mark_point()
        get_name = self.safe_area_page.get_name_after_click_edit()
        self.assertIn(get_name, mark_point_name)
        self.safe_area_page.click_ensure()
        text = self.safe_area_page.get_text_after_ensure()
        self.assertEqual('操作成功.', text)

        # 点击新建按钮
        self.safe_area_page.click_create_mark_point()
        text = self.safe_area_page.get_text_after_create_map()
        self.assertEqual('请在地图上单击左键开始绘制，双击完成', text)

        # 点击删除
        self.safe_area_page.click_delete_in_mark_point()
        text = self.safe_area_page.get_text_after_click_delete()
        self.assertEqual('请选择要删除的记录!', text)
        self.safe_area_page.click_ensure()

        self.safe_area_page.click_delete_in_mark_point()
        text = self.safe_area_page.get_text_after_click_delete()
        self.assertEqual('请选择要删除的记录!', text)
        self.safe_area_page.click_close()
