import csv
import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.safe_area.safe_area_search_sql import SafeAreaSearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.safe_area.safe_area_page import SafeAreaPage
from pages.safe_area.safe_area_page_read_csv import SafeAreaPageReadCsv


class TestCase138SafeAreaMarkPointOperation(unittest.TestCase):
    """ 围栏编辑页面搜索关联设备 """

    # author：邓肖斌
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.safe_area_page = SafeAreaPage(self.driver, self.base_url)
        self.safe_area_page_read_csv = SafeAreaPageReadCsv()
        self.assert_text = AssertText()
        self.connect_sql = ConnectSql()
        self.safe_area_search_sql = SafeAreaSearchSql()

        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.log_in_base.log_in_jimitest()

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_safe_area_mark_point_operation(self):
        self.log_in_base.click_account_center_button()
        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()

        # 跳转到安全区域
        self.safe_area_page.click_control_after_click_safe_area()
        # 断言url
        expect_url = self.base_url + "/safearea/geozonemap?flag=0"
        self.assertEqual(expect_url, self.driver.get_current_url())
        # 点击围栏
        self.safe_area_page.click_select_fence_button()
        # 点击编辑
        self.safe_area_page.click_edit_fence()
        # 获取围栏名称
        fence_name = self.safe_area_page.get_fence_name_of_cur_edit()
        print("当前围栏名称为：%s" % fence_name)

        i = 0

        # 读csv
        csv_file = self.safe_area_page_read_csv.read_csv('safe_area_fences_relation_dev_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                "account": row[0],
                "search_type": row[1],
                "search_content": row[2]
            }

            self.safe_area_page.fences_edit_page_search_dev(data)

            # 断言
            # 连接数据库
            connect = self.connect_sql.connect_tuqiang_sql()
            # 建立游标
            cursor = connect.cursor()
            geo_id_sql = self.safe_area_search_sql.search_sql_in_test_case_138_01(fence_name)
            # 执行
            cursor.execute(geo_id_sql)
            geo = cursor.fetchall()
            print(geo)
            for row1 in geo:
                geo_id = {
                    "geo_id": row1[0]
                }

                # 判断搜索条件
                get_sql = self.safe_area_search_sql. \
                    search_sql_in_test_case_138_02(geo_id["geo_id"], current_account, data)
                # 执行sql
                print(get_sql)
                cursor.execute(get_sql)

                current_total = cursor.fetchall()
                total_list = []
                for range1 in current_total:
                    for range2 in range1:
                        total_list.append(range2)
                total_num = len(total_list)
                web_total = self.safe_area_page.get_fence_relation_dev_num()
                i += 1
                print('第%s次查询页面的条数是：%s' % (i, web_total))
                print('第%s次查询数据库的条数为：%s' % (i, total_num))
                self.assertEqual(total_num, web_total)

            cursor.close()
            connect.close()
