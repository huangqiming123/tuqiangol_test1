import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage


class TestCase135SafeAreaExpertion(unittest.TestCase):
    """ web_autotest账号，选择单个区域右侧编辑操作 """

    # author：邓肖斌

    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.safe_area_page.click_control_after_click_safe_area()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_safe_area_expertion(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 点击删除按钮
        self.safe_area_page.click_delete_button()
        text = self.safe_area_page.get_text_after_click_delete()
        self.assertEqual(self.assert_text.safe_area_page_choose_delete_content(), text)
        self.safe_area_page.click_ensure()

        self.safe_area_page.click_delete_button()
        text = self.safe_area_page.get_text_after_click_delete()
        self.assertEqual(self.assert_text.safe_area_page_choose_delete_content(), text)
        self.safe_area_page.click_close()

        # 点击新建
        self.safe_area_page.click_creat_map()
        # 获取文本
        text = self.safe_area_page.get_text_after_create_map()
        self.assertEqual(self.assert_text.safe_area_page_map_text(), text)

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
        # 点击取消
        self.safe_area_page.click_cancel_edit()

        # 点击编辑
        self.safe_area_page.click_edit_black_address()
        # 获取打开编辑之后的黑车地址库名字
        name = self.safe_area_page.get_black_address_after_click_edit()
        self.assertEqual(black_address_name, name)
        # 验证黑车库的按钮是否被选中
        black_address_value = self.safe_area_page.get_black_address_input_value()
        self.assertEqual(True, black_address_value)
        # 点击保存
        self.safe_area_page.click_ensure()
        # 获取保存后的文本
        text = self.safe_area_page.get_text_after_ensure()
        print(self.assert_text.account_center_page_operation_done())
        print(text)
        self.assertIn(self.assert_text.account_center_page_operation_done(), text)

        # 选择围栏编辑
        self.safe_area_page.click_select_fence_button()
        # 获取第一个围栏的名称
        fence_name = self.safe_area_page.get_first_list_fence_name()
        print('1 = %s' % fence_name)

        # 点击编辑
        self.safe_area_page.click_edit_fence()
        # 获取打开编辑之后的围栏名称
        names = self.safe_area_page.get_fence_name_after_edit()
        print('2 = %s' % names)
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
        self.assertIn(self.assert_text.account_center_page_operation_done(), text)
