import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage
from pages.safe_area.safe_area_page_read_csv import SafeAreaPageReadCsv
from pages.safe_area.safe_area_search_sql import SafeAreaSearchSql


class TestCase131MarkOperation(unittest.TestCase):
    """
    web_autotest账号，标注点页面操作
    author：邓肖斌
    """
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.log_in_base.log_in()
        self.safe_area_page.click_control_after_click_safe_area()
        self.safe_area_page_read_csv = SafeAreaPageReadCsv()
        self.assert_text = AssertText()
        self.connect_sql = ConnectSql()
        self.search_sql = SafeAreaSearchSql()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_mark_operation(self):
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())

        self.safe_area_page.click_mark_button()
        sleep(2)

        # 全选
        self.safe_area_page.click_all_select_button_with_mark()
        # 点击删除
        self.safe_area_page.click_detele_button_with_mark()
        # 点击取消
        self.safe_area_page.click_cancel_detele_button()
        # 点击删除
        self.safe_area_page.click_detele_button_with_mark()
        # 点击关闭
        self.safe_area_page.click_close_detele_button()

        # 点击新建按钮
        self.safe_area_page.click_create_mark_point()
        text = self.safe_area_page.get_text_after_create_map()
        self.assertEqual(self.assert_text.safe_area_page_map_text(), text)

        # 获取第一个地标的名称
        mark_name = self.safe_area_page.get_first_mark_name_text()
        # 点击列表的编辑
        self.safe_area_page.click_edit_button_in_list()
        # 点击保存
        self.safe_area_page.click_ensure_edit_in_list('名称1', '描述1')
        # 获取保存之后的地标名称
        mark_name_after_save = self.safe_area_page.get_first_mark_name_text()

        # 断言1：网页上名称的变化
        self.assertNotEqual(mark_name, mark_name_after_save)
        # 断言2：用修改之前的名称在数据库搜索
        # 创建数据库连接
        connect = self.connect_sql.connect_tuqiang_sql()
        # 创建游标
        cursor = connect.cursor()
        get_total_count_sql = self.search_sql.search_sql_in_test_case_131('%s') % mark_name
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
        get_total_count_sql = self.search_sql.search_sql_in_test_case_131('%s') % mark_name_after_save
        print(get_total_count_sql)
        cursor.execute(get_total_count_sql)
        current_total = cursor.fetchall()
        total_list2 = []
        for range1 in current_total:
            for range2 in range1:
                total_list2.append(range2)
        total = len(total_list2)
        self.assertEqual(1, total)
        self.assertEqual('描述1', total_list2[0])

        # 点击列表的编辑
        self.safe_area_page.click_edit_button_in_list()
        # 点击保存
        self.safe_area_page.click_ensure_edit_in_list('名称', '描述')

        # 点击列表的编辑
        self.safe_area_page.click_edit_button_in_list()
        # 点击取消
        self.safe_area_page.click_cancel_edit_in_list()

        # 点击列表中的删除
        self.safe_area_page.click_delete_button_in_list()
        self.safe_area_page.click_cancel_detele_button()

        # 点击关闭
        self.safe_area_page.click_delete_button_in_list()
        self.safe_area_page.click_close_detele_button()
