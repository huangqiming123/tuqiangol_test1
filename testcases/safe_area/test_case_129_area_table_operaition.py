import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage
from pages.safe_area.safe_area_search_sql import SafeAreaSearchSql


class TestCase129AreaTableOperaition(unittest.TestCase):
    """ 围栏页面操作 """

    # author：邓肖斌
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.assert_text = AssertText()
        self.log_in_base.log_in()
        self.safe_area_page.click_control_after_click_safe_area()
        self.connect_sql = ConnectSql()
        self.search_sql = SafeAreaSearchSql()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_area_table_operaition(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        # 点击全选按钮
        self.safe_area_page.click_all_select_button()

        # 点击删除
        self.safe_area_page.click_delete_button()
        sleep(1)
        # 点击取消删除
        self.safe_area_page.click_cancel_detele_button()

        # 点击选择围栏
        self.safe_area_page.click_select_fence_button()

        # 点击列表中的编辑
        self.safe_area_page.click_list_edit_button()
        # 获取名称
        name_text = self.safe_area_page.get_first_fence_name_text()
        # 断言
        self.assertEqual(self.assert_text.safe_area_page_edit_text(), self.safe_area_page.get_text_after_click_edit())
        # 输入内容保存
        self.safe_area_page.ensure_edit_list('名称b', '描述b')
        # 获取保存之后的名称
        name_after_save = self.safe_area_page.get_first_fence_name_text()

        # 断言1：网页上围栏名称的变化
        self.assertNotEqual(name_text, name_after_save)
        # 创建数据库连接
        connect = self.connect_sql.connect_tuqiang_sql()
        # 创建游标
        cursor = connect.cursor()
        # 断言2：用修改之前的名称在数据库搜索
        get_total_count_sql = self.search_sql.search_sql_in_test_case_129(name_text)
        print(get_total_count_sql)
        cursor.execute(get_total_count_sql)
        current_total = cursor.fetchall()
        total_list1 = []
        for range1 in current_total:
            for range2 in range1:
                total_list1.append(range2)
        total = len(total_list1)
        self.assertEqual(0, total)
        # 断言3：用修改之后的名称在数据库搜索
        get_total_count_sql = self.search_sql.search_sql_in_test_case_129(name_after_save)
        print(get_total_count_sql)
        cursor.execute(get_total_count_sql)
        current_total = cursor.fetchall()
        total_list2 = []
        for range1 in current_total:
            for range2 in range1:
                total_list2.append(range2)
        total = len(total_list2)
        self.assertEqual(1, total)
        self.assertEqual('描述b', total_list2[0])

        # 点击列表中的编辑
        self.safe_area_page.click_list_edit_button()
        # 输入内容保存
        self.safe_area_page.ensure_edit_list('名称a', '描述a')

        # 点击列表中的编辑
        self.safe_area_page.click_list_edit_button()
        # 断言
        self.assertEqual(self.assert_text.safe_area_page_edit_text(), self.safe_area_page.get_text_after_click_edit())
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

        # 点击列表中的编辑
        self.safe_area_page.click_list_edit_button()
        # 点击关联列表中的删除
        self.safe_area_page.click_del_in_fences_edit_page()
        # 获取文本
        text = self.safe_area_page.get_text_in_fence_edit_page_after_click_del()
        # 断言
        self.assertEqual(text, "请选择要删除的记录")
        # 关闭
        self.safe_area_page.click_close_detele_buttons()

        cursor.close()
        connect.close()
