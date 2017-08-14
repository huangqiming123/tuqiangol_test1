import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase145SportStatisticalStayForm(unittest.TestCase):
    '''
    用例第150条，运动统计，停留报表
    author ： zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.assert_text = AssertText()
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_sport_statistical_stay_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击停留报表
        self.statistical_form_page.click_stay_form_button()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_stay_form(),
                         self.statistical_form_page.actual_text_after_click_stay_form_button())
        # 读数据
        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_stay_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'choose_date': row[1],
                'begin_time': row[2],
                'end_time': row[3]
            }
            self.statistical_form_page.add_data_to_search_stay_form(search_data)

            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()

            # 判断查询条件
            get_total_sql = self.search_sql.search_sport_stay_sql(all_dev, search_data)
            get_total_sql_01 = self.search_sql.search_sport_stay_sql_01(all_dev, search_data)
            get_total_sql_02 = self.search_sql.search_sport_stay_sql_02(all_dev, search_data)
            get_total_sql_03 = self.search_sql.search_sport_stay_sql_03(all_dev, search_data)
            get_total_sql_04 = self.search_sql.search_sport_stay_sql_04(all_dev, search_data)
            get_total_sql_05 = self.search_sql.search_sport_stay_sql_05(all_dev, search_data)
            get_total_sql_06 = self.search_sql.search_sport_stay_sql_06(all_dev, search_data)
            get_total_sql_07 = self.search_sql.search_sport_stay_sql_07(all_dev, search_data)
            get_total_sql_08 = self.search_sql.search_sport_stay_sql_08(all_dev, search_data)
            get_total_sql_09 = self.search_sql.search_sport_stay_sql_09(all_dev, search_data)
            get_total_sql_10 = self.search_sql.search_sport_stay_sql_10(all_dev, search_data)
            get_total_sql_11 = self.search_sql.search_sport_stay_sql_11(all_dev, search_data)
            get_total_sql_12 = self.search_sql.search_sport_stay_sql_12(all_dev, search_data)

            print(get_total_sql_01)

            cursor_02.execute(get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            # 拆分列表
            total_number_list = []
            total_time_list = []
            for n in range(len(total_list)):
                if n % 2 == 0:
                    total_number_list.append(total_list[n])
                elif n % 2 == 1:
                    total_time_list.append(total_list[n])

            cursor_02.execute(get_total_sql_01)
            get_total_01 = cursor_02.fetchall()
            total_list_01 = []
            for range1 in get_total_01:
                for range2 in range1:
                    total_list_01.append(range2)
            # 拆分列表
            total_number_list_01 = []
            total_time_list_01 = []
            for n in range(len(total_list_01)):
                if n % 2 == 0:
                    total_number_list_01.append(total_list_01[n])
                elif n % 2 == 1:
                    total_time_list_01.append(total_list_01[n])

            cursor_02.execute(get_total_sql_02)
            get_total_02 = cursor_02.fetchall()
            total_list_02 = []
            for range1 in get_total_02:
                for range2 in range1:
                    total_list_02.append(range2)
            # 拆分列表
            total_number_list_02 = []
            total_time_list_02 = []
            for n in range(len(total_list_02)):
                if n % 2 == 0:
                    total_number_list_02.append(total_list_02[n])
                elif n % 2 == 1:
                    total_time_list_02.append(total_list_02[n])

            cursor_02.execute(get_total_sql_03)
            get_total_03 = cursor_02.fetchall()
            total_list_03 = []
            for range1 in get_total_03:
                for range2 in range1:
                    total_list_03.append(range2)
            # 拆分列表
            total_number_list_03 = []
            total_time_list_03 = []
            for n in range(len(total_list_03)):
                if n % 2 == 0:
                    total_number_list_03.append(total_list_03[n])
                elif n % 2 == 1:
                    total_time_list_03.append(total_list_03[n])

            cursor_02.execute(get_total_sql_04)
            get_total_04 = cursor_02.fetchall()
            total_list_04 = []
            for range1 in get_total_04:
                for range2 in range1:
                    total_list_04.append(range2)
            # 拆分列表
            total_number_list_04 = []
            total_time_list_04 = []
            for n in range(len(total_list_04)):
                if n % 2 == 0:
                    total_number_list_04.append(total_list_04[n])
                elif n % 2 == 1:
                    total_time_list_04.append(total_list_04[n])

            cursor_02.execute(get_total_sql_05)
            get_total_05 = cursor_02.fetchall()
            total_list_05 = []
            for range1 in get_total_05:
                for range2 in range1:
                    total_list_05.append(range2)
            # 拆分列表
            total_number_list_05 = []
            total_time_list_05 = []
            for n in range(len(total_list_05)):
                if n % 2 == 0:
                    total_number_list_05.append(total_list_05[n])
                elif n % 2 == 1:
                    total_time_list_05.append(total_list_05[n])

            cursor_02.execute(get_total_sql_06)
            get_total_06 = cursor_02.fetchall()
            total_list_06 = []
            for range1 in get_total_06:
                for range2 in range1:
                    total_list_06.append(range2)
            # 拆分列表
            total_number_list_06 = []
            total_time_list_06 = []
            for n in range(len(total_list_06)):
                if n % 2 == 0:
                    total_number_list_06.append(total_list_06[n])
                elif n % 2 == 1:
                    total_time_list_06.append(total_list_06[n])

            cursor_02.execute(get_total_sql_07)
            get_total_07 = cursor_02.fetchall()
            total_list_07 = []
            for range1 in get_total_07:
                for range2 in range1:
                    total_list_07.append(range2)
            # 拆分列表
            total_number_list_07 = []
            total_time_list_07 = []
            for n in range(len(total_list_07)):
                if n % 2 == 0:
                    total_number_list_07.append(total_list_07[n])
                elif n % 2 == 1:
                    total_time_list_07.append(total_list_07[n])

            cursor_02.execute(get_total_sql_08)
            get_total_08 = cursor_02.fetchall()
            total_list_08 = []
            for range1 in get_total_08:
                for range2 in range1:
                    total_list_08.append(range2)
            # 拆分列表
            total_number_list_08 = []
            total_time_list_08 = []
            for n in range(len(total_list_08)):
                if n % 2 == 0:
                    total_number_list_08.append(total_list_08[n])
                elif n % 2 == 1:
                    total_time_list_08.append(total_list_08[n])

            cursor_02.execute(get_total_sql_09)
            get_total_09 = cursor_02.fetchall()
            total_list_09 = []
            for range1 in get_total_09:
                for range2 in range1:
                    total_list_09.append(range2)
            # 拆分列表
            total_number_list_09 = []
            total_time_list_09 = []
            for n in range(len(total_list_09)):
                if n % 2 == 0:
                    total_number_list_09.append(total_list_09[n])
                elif n % 2 == 1:
                    total_time_list_09.append(total_list_09[n])

            cursor_02.execute(get_total_sql_10)
            get_total_10 = cursor_02.fetchall()
            total_list_10 = []
            for range1 in get_total_10:
                for range2 in range1:
                    total_list_10.append(range2)
            # 拆分列表
            total_number_list_10 = []
            total_time_list_10 = []
            for n in range(len(total_list_10)):
                if n % 2 == 0:
                    total_number_list_10.append(total_list_10[n])
                elif n % 2 == 1:
                    total_time_list_10.append(total_list_10[n])

            cursor_02.execute(get_total_sql_11)
            get_total_11 = cursor_02.fetchall()
            total_list_11 = []
            for range1 in get_total_11:
                for range2 in range1:
                    total_list_11.append(range2)
            # 拆分列表
            total_number_list_11 = []
            total_time_list_11 = []
            for n in range(len(total_list_02)):
                if n % 2 == 0:
                    total_number_list_11.append(total_list_11[n])
                elif n % 2 == 1:
                    total_time_list_11.append(total_list_11[n])

            cursor_02.execute(get_total_sql_12)
            get_total_12 = cursor_02.fetchall()
            total_list_12 = []
            for range1 in get_total_12:
                for range2 in range1:
                    total_list_12.append(range2)
            # 拆分列表
            total_number_list_12 = []
            total_time_list_12 = []
            for n in range(len(total_list_12)):
                if n % 2 == 0:
                    total_number_list_12.append(total_list_12[n])
                elif n % 2 == 1:
                    total_time_list_12.append(total_list_12[n])

            # 断言查询的条
            total = len(total_number_list_01) + len(total_number_list_02) + len(total_number_list_03) + len(
                total_number_list_04) + len(total_number_list_05) + len(total_number_list_06) + len(
                total_number_list_07) + len(total_number_list_08) + len(total_number_list_09) + len(
                total_number_list_10) + len(total_number_list_11) + len(total_number_list_12) + len(total_number_list)
            sleep(3)
            self.statistical_form_page.switch_to_stay_report_form_frame()
            web_total = self.statistical_form_page.get_total_search_stay_form_number()
            self.assertEqual(total, web_total)

            # 断言查询的总的停留时间
            total_time = sum(total_time_list_01) + sum(total_time_list_02) + sum(total_time_list_03) + sum(
                total_time_list_04) + sum(total_time_list_05) + sum(total_time_list_06) + sum(total_time_list_07) + sum(
                total_time_list_08) + sum(total_time_list_09) + sum(total_time_list_10) + sum(total_time_list_11) + sum(
                total_time_list_12) + sum(total_time_list)
            chang_total_time_type = self.statistical_form_page.change_sec_time(total_time)
            web_total_time = self.statistical_form_page.get_total_stay_form_time()
            self.assertEqual(chang_total_time_type, web_total_time)

            # 点击导出停留报表
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
