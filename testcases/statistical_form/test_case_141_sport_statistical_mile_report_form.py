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


class TestCase141SportStatisticalMileReportForm(unittest.TestCase):
    '''
    用例第141条，运动统计 里程报表
    author:zhangAo
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
        self.seasrch_sql = SearchSql(self.driver, self.base_url)
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

    def test_case_141_sport_statistical_mile_report_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_mileage_form_buttons()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_mile_form(),
                         self.statistical_form_page.actual_text_after_click_mileage_form_buttons())

        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('milage_report_search_data.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'search_user': row[0],
                'type': row[1],
                'choose_date': row[2],
                'begin_time': row[3],
                'end_time': row[4]
            }
            self.statistical_form_page.add_datas_to_search_mileage_form(search_data)
            self.statistical_form_page.switch_to_mile_report_form_frame()

            # 连接数据库
            # 连接数据库
            all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()
            # 判断查询的条件

            # 判断查询条件
            get_total_sql_01 = self.seasrch_sql.search_sport_mile_report_sql_01(all_dev, search_data)
            get_total_sql_02 = self.seasrch_sql.search_sport_mile_report_sql_02(all_dev, search_data)
            get_total_sql_03 = self.seasrch_sql.search_sport_mile_report_sql_03(all_dev, search_data)
            get_total_sql_04 = self.seasrch_sql.search_sport_mile_report_sql_04(all_dev, search_data)
            get_total_sql_05 = self.seasrch_sql.search_sport_mile_report_sql_05(all_dev, search_data)
            get_total_sql_06 = self.seasrch_sql.search_sport_mile_report_sql_06(all_dev, search_data)
            get_total_sql_07 = self.seasrch_sql.search_sport_mile_report_sql_07(all_dev, search_data)
            get_total_sql_08 = self.seasrch_sql.search_sport_mile_report_sql_08(all_dev, search_data)
            get_total_sql_09 = self.seasrch_sql.search_sport_mile_report_sql_09(all_dev, search_data)
            get_total_sql_10 = self.seasrch_sql.search_sport_mile_report_sql_10(all_dev, search_data)
            get_total_sql_11 = self.seasrch_sql.search_sport_mile_report_sql_11(all_dev, search_data)
            get_total_sql_12 = self.seasrch_sql.search_sport_mile_report_sql_12(all_dev, search_data)
            get_total_01 = self.seasrch_sql.search_sport_mile_report_sql_get_total_01(all_dev, search_data)
            get_total_02 = self.seasrch_sql.search_sport_mile_report_sql_get_total_02(all_dev, search_data)
            get_total_03 = self.seasrch_sql.search_sport_mile_report_sql_get_total_03(all_dev, search_data)
            get_total_04 = self.seasrch_sql.search_sport_mile_report_sql_get_total_04(all_dev, search_data)
            get_total_05 = self.seasrch_sql.search_sport_mile_report_sql_get_total_05(all_dev, search_data)
            get_total_06 = self.seasrch_sql.search_sport_mile_report_sql_get_total_06(all_dev, search_data)
            get_total_07 = self.seasrch_sql.search_sport_mile_report_sql_get_total_07(all_dev, search_data)
            get_total_08 = self.seasrch_sql.search_sport_mile_report_sql_get_total_08(all_dev, search_data)
            get_total_09 = self.seasrch_sql.search_sport_mile_report_sql_get_total_09(all_dev, search_data)
            get_total_10 = self.seasrch_sql.search_sport_mile_report_sql_get_total_10(all_dev, search_data)
            get_total_11 = self.seasrch_sql.search_sport_mile_report_sql_get_total_11(all_dev, search_data)
            get_total_12 = self.seasrch_sql.search_sport_mile_report_sql_get_total_12(all_dev, search_data)
            print(get_total_sql_01)
            print(get_total_01)

            # 判断查询的条件
            if search_data['type'] == 'mile':
                # 查询的选择里程
                cursor_02.execute(get_total_sql_01)
                get_all_mlie_and_time_01 = cursor_02.fetchall()
                get_all_mlie_and_time_list_01 = []
                for range1 in get_all_mlie_and_time_01:
                    for range2 in range1:
                        get_all_mlie_and_time_list_01.append(range2)

                cursor_02.execute(get_total_sql_02)
                get_all_mlie_and_time_02 = cursor_02.fetchall()
                get_all_mlie_and_time_list_02 = []
                for range1 in get_all_mlie_and_time_02:
                    for range2 in range1:
                        get_all_mlie_and_time_list_02.append(range2)

                cursor_02.execute(get_total_sql_03)
                get_all_mlie_and_time_03 = cursor_02.fetchall()
                get_all_mlie_and_time_list_03 = []
                for range1 in get_all_mlie_and_time_03:
                    for range2 in range1:
                        get_all_mlie_and_time_list_03.append(range2)

                cursor_02.execute(get_total_sql_04)
                get_all_mlie_and_time_04 = cursor_02.fetchall()
                get_all_mlie_and_time_list_04 = []
                for range1 in get_all_mlie_and_time_04:
                    for range2 in range1:
                        get_all_mlie_and_time_list_04.append(range2)

                cursor_02.execute(get_total_sql_05)
                get_all_mlie_and_time_05 = cursor_02.fetchall()
                get_all_mlie_and_time_list_05 = []
                for range1 in get_all_mlie_and_time_05:
                    for range2 in range1:
                        get_all_mlie_and_time_list_05.append(range2)

                cursor_02.execute(get_total_sql_06)
                get_all_mlie_and_time_06 = cursor_02.fetchall()
                get_all_mlie_and_time_list_06 = []
                for range1 in get_all_mlie_and_time_06:
                    for range2 in range1:
                        get_all_mlie_and_time_list_06.append(range2)

                cursor_02.execute(get_total_sql_07)
                get_all_mlie_and_time_07 = cursor_02.fetchall()
                get_all_mlie_and_time_list_07 = []
                for range1 in get_all_mlie_and_time_07:
                    for range2 in range1:
                        get_all_mlie_and_time_list_07.append(range2)

                cursor_02.execute(get_total_sql_08)
                get_all_mlie_and_time_08 = cursor_02.fetchall()
                get_all_mlie_and_time_list_08 = []
                for range1 in get_all_mlie_and_time_08:
                    for range2 in range1:
                        get_all_mlie_and_time_list_08.append(range2)

                cursor_02.execute(get_total_sql_09)
                get_all_mlie_and_time_09 = cursor_02.fetchall()
                get_all_mlie_and_time_list_09 = []
                for range1 in get_all_mlie_and_time_09:
                    for range2 in range1:
                        get_all_mlie_and_time_list_09.append(range2)

                cursor_02.execute(get_total_sql_10)
                get_all_mlie_and_time_10 = cursor_02.fetchall()
                get_all_mlie_and_time_list_10 = []
                for range1 in get_all_mlie_and_time_10:
                    for range2 in range1:
                        get_all_mlie_and_time_list_10.append(range2)

                cursor_02.execute(get_total_sql_11)
                get_all_mlie_and_time_11 = cursor_02.fetchall()
                get_all_mlie_and_time_list_11 = []
                for range1 in get_all_mlie_and_time_11:
                    for range2 in range1:
                        get_all_mlie_and_time_list_11.append(range2)

                cursor_02.execute(get_total_sql_12)
                get_all_mlie_and_time_12 = cursor_02.fetchall()
                get_all_mlie_and_time_list_12 = []
                for range1 in get_all_mlie_and_time_12:
                    for range2 in range1:
                        get_all_mlie_and_time_list_12.append(range2)

                cursor_02.execute(get_total_01)
                total_number_01 = cursor_02.fetchall()
                total_number_list_01 = []
                for range1 in total_number_01:
                    for range2 in range1:
                        total_number_list_01.append(range2)

                cursor_02.execute(get_total_02)
                total_number_02 = cursor_02.fetchall()
                total_number_list_02 = []
                for range1 in total_number_02:
                    for range2 in range1:
                        total_number_list_02.append(range2)

                cursor_02.execute(get_total_03)
                total_number_03 = cursor_02.fetchall()
                total_number_list_03 = []
                for range1 in total_number_03:
                    for range2 in range1:
                        total_number_list_03.append(range2)

                cursor_02.execute(get_total_04)
                total_number_04 = cursor_02.fetchall()
                total_number_list_04 = []
                for range1 in total_number_04:
                    for range2 in range1:
                        total_number_list_04.append(range2)

                cursor_02.execute(get_total_05)
                total_number_05 = cursor_02.fetchall()
                total_number_list_05 = []
                for range1 in total_number_05:
                    for range2 in range1:
                        total_number_list_05.append(range2)

                cursor_02.execute(get_total_06)
                total_number_06 = cursor_02.fetchall()
                total_number_list_06 = []
                for range1 in total_number_06:
                    for range2 in range1:
                        total_number_list_06.append(range2)

                cursor_02.execute(get_total_07)
                total_number_07 = cursor_02.fetchall()
                total_number_list_07 = []
                for range1 in total_number_07:
                    for range2 in range1:
                        total_number_list_07.append(range2)

                cursor_02.execute(get_total_08)
                total_number_08 = cursor_02.fetchall()
                total_number_list_08 = []
                for range1 in total_number_08:
                    for range2 in range1:
                        total_number_list_08.append(range2)

                cursor_02.execute(get_total_09)
                total_number_09 = cursor_02.fetchall()
                total_number_list_09 = []
                for range1 in total_number_09:
                    for range2 in range1:
                        total_number_list_09.append(range2)

                cursor_02.execute(get_total_10)
                total_number_10 = cursor_02.fetchall()
                total_number_list_10 = []
                for range1 in total_number_10:
                    for range2 in range1:
                        total_number_list_10.append(range2)

                cursor_02.execute(get_total_11)
                total_number_11 = cursor_02.fetchall()
                total_number_list_11 = []
                for range1 in total_number_11:
                    for range2 in range1:
                        total_number_list_11.append(range2)

                cursor_02.execute(get_total_12)
                total_number_12 = cursor_02.fetchall()
                total_number_list_12 = []
                for range1 in total_number_12:
                    for range2 in range1:
                        total_number_list_12.append(range2)

                total = len(total_number_list_01) + len(total_number_list_02) + len(
                    total_number_list_03) + len(total_number_list_04) + len(total_number_list_05) + len(
                    total_number_list_06) + len(total_number_list_07) + len(total_number_list_08) + len(
                    total_number_list_09) + len(total_number_list_10) + len(total_number_list_11) + len(
                    total_number_list_12)
                web_total = self.statistical_form_page.get_total_search_mileage_form()
                self.assertEqual(total, web_total)
                # 计算总里程 和 总时间
                total_mile = sum(get_all_mlie_and_time_list_01) + sum(get_all_mlie_and_time_list_02) + sum(
                    get_all_mlie_and_time_list_03) + sum(get_all_mlie_and_time_list_04) + sum(
                    get_all_mlie_and_time_list_05) + sum(get_all_mlie_and_time_list_06) + sum(
                    get_all_mlie_and_time_list_07) + sum(get_all_mlie_and_time_list_08) + sum(
                    get_all_mlie_and_time_list_09) + sum(get_all_mlie_and_time_list_10) + sum(
                    get_all_mlie_and_time_list_11) + sum(get_all_mlie_and_time_list_12)
                # 断言总时间和总里程，总油耗
                # 计算总油耗
                if total_mile == 0:
                    self.assertEqual('0', self.statistical_form_page.get_mileage_total_oil())
                else:
                    if self.statistical_form_page.get_mileage_total_oil() == '0':
                        pass
                    else:
                        get_total_oil = total_mile / 1000 / 100 * 8
                        total_oil = '%.2f' % get_total_oil
                        self.assertEqual(str(total_oil), self.statistical_form_page.get_mileage_total_oil())

            elif search_data['type'] == 'day':
                # 如果选择天
                cursor_02.execute(get_total_sql_01)
                get_all_mile_data = cursor_02.fetchall()
                get_all_mile_list = []
                for range1 in get_all_mile_data:
                    for range2 in range1:
                        get_all_mile_list.append(range2)
                total = len(get_all_mile_list)
                web_total = self.statistical_form_page.get_total_search_mileage_form_with_day()
                self.assertEqual(total, web_total)

                total_mile_with_day = sum(get_all_mile_list)
                # 断言
                self.assertAlmostEqual(total_mile_with_day / 1000,
                                       float(self.statistical_form_page.get_mileage_with_day_total_mile()))

            # 点击导出
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
