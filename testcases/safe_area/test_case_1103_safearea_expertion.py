import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase1103SafeAreaExpertion(unittest.TestCase):
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

    def test_case_1103_safe_area_expertion(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 点击删除按钮
        self.safe_area_page.click_delete_button()
        text = self.safe_area_page.get_text_after_click_delete()
        self.assertEqual('请选择要删除的记录!', text)
        self.safe_area_page.click_ensure()

        self.safe_area_page.click_delete_button()
        text = self.safe_area_page.get_text_after_click_delete()
        self.assertEqual('请选择要删除的记录!', text)
        self.safe_area_page.click_close()

        # 点击新建
        self.safe_area_page.click_creat_map()
        # 获取文本
        text = self.safe_area_page.get_text_after_create_map()
        self.assertEqual('请在地图上单击左键开始绘制，双击完成', text)

        # 选择黑车库操作
        self.safe_area_page.click_select_black_address_button()
        # 获取列表第一个的名称
        black_address_name = self.safe_area_page.get_first_list_black_address_name()
        # 点击编辑
        self.safe_area_page.click_edit_black_address()
        # 获取打开编辑之后的黑车地址库名字
        name = self.safe_area_page.get_black_address_after_click_edit()
        self.assertEqual(black_address_name, name)
        # 验证黑车库的按钮是否被选中
        black_address_value = self.safe_area_page.get_black_address_input_value()
        self.assertEqual(True, black_address_value)
        # 点击关闭
        self.safe_area_page.click_cancel_edit()

        # 点击编辑
        self.safe_area_page.click_edit_black_address()
        # 获取打开编辑之后的黑车地址库名字
        name = self.safe_area_page.get_black_address_after_click_edit()
        self.assertEqual(black_address_name, name)
        # 验证黑车库的按钮是否被选中
        black_address_value = self.safe_area_page.get_black_address_input_value()
        self.assertEqual(True, black_address_value)
        # 点击关闭
        self.safe_area_page.click_ensure()
        # 获取保存后的文本
        text = self.safe_area_page.get_text_after_ensure()
        self.assertEqual('操作成功.', text)

        # 选择围栏编辑
        self.safe_area_page.click_select_fence_button()
        # 获取第一个围栏的名称
        fence_name = self.safe_area_page.get_first_list_fence_name()

        # 点击编辑
        self.safe_area_page.click_edit_fence()
        # 获取打开编辑之后的围栏名称
        names = self.safe_area_page.get_fence_name_after_edit()
        self.assertEqual(fence_name, names)
        # 点击取消
        self.safe_area_page.click_cancel_edit()

        # 点击编辑
        self.safe_area_page.click_edit_fence()
        # 获取打开编辑之后的围栏名称
        names = self.safe_area_page.get_fence_name_after_edit()
        self.assertEqual(fence_name, names)
        # 点击取消
        self.safe_area_page.click_ensure()
        # 获取保存后的文本
        text = self.safe_area_page.get_text_after_ensure()
        self.assertEqual('操作成功.', text)
