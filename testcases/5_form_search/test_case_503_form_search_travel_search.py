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


class TestCase503FormSearchTravelSearch(unittest.TestCase):
    # 测试 报表 行程报表 搜索功能
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
        self.assert_text = AssertText()
        self.search_sql = SearchSql(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.log_in_base.log_in_jimitest()

        current_handle = self.driver.get_current_window_handle()
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)
        self.base_page.change_windows_handle(current_handle)

    def tearDown(self):
        self.driver.close_window()
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_travel_search(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_mileage_form_button()
        # 断言
        self.assertEqual(self.assert_text.statistical_form_tracl_form(),
                         self.statistical_form_page.actual_text_after_click_mileage_form_button())
        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_milage_form_search_data.csv')
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
            self.statistical_form_page.add_data_to_search_mileage_form(search_data)
            self.statistical_form_page.switch_to_tracel_report_form_frame()

            # 连接数据库
            # 连接数据库
            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()
            # 判断查询的条件

            # 判断查询条件
            # get_total_sql = self.search_sql.search_sport_mile_sql(all_dev, search_data)
            get_total_sql_01 = self.search_sql.search_sport_mile_sql_01(all_dev, search_data)
            get_total_sql_02 = self.search_sql.search_sport_mile_sql_02(all_dev, search_data)
            get_total_sql_03 = self.search_sql.search_sport_mile_sql_03(all_dev, search_data)
            get_total_sql_04 = self.search_sql.search_sport_mile_sql_04(all_dev, search_data)
            get_total_sql_05 = self.search_sql.search_sport_mile_sql_05(all_dev, search_data)
            get_total_sql_06 = self.search_sql.search_sport_mile_sql_06(all_dev, search_data)
            get_total_sql_07 = self.search_sql.search_sport_mile_sql_07(all_dev, search_data)
            get_total_sql_08 = self.search_sql.search_sport_mile_sql_08(all_dev, search_data)
            get_total_sql_09 = self.search_sql.search_sport_mile_sql_09(all_dev, search_data)
            get_total_sql_10 = self.search_sql.search_sport_mile_sql_10(all_dev, search_data)
            get_total_sql_11 = self.search_sql.search_sport_mile_sql_11(all_dev, search_data)
            get_total_sql_12 = self.search_sql.search_sport_mile_sql_12(all_dev, search_data)
            print(get_total_sql_01)

            # 判断查询的条件
            if search_data['type'] == 'mile':
                # 查询的选择里程
                '''cursor_02.execute(get_total_sql_01)
                get_all_mlie_and_time = cursor_02.fetchall()
                get_all_mlie_and_time_list = []
                for range1 in get_all_mlie_and_time:
                    for range2 in range1:
                        get_all_mlie_and_time_list.append(range2)'''

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

                total = len(get_all_mlie_and_time_list_01) / 2 + len(
                    get_all_mlie_and_time_list_02) / 2 + len(get_all_mlie_and_time_list_03) / 2 + len(
                    get_all_mlie_and_time_list_04) / 2 + len(get_all_mlie_and_time_list_05) / 2 + len(
                    get_all_mlie_and_time_list_06) / 2 + len(get_all_mlie_and_time_list_07) / 2 + len(
                    get_all_mlie_and_time_list_08) / 2 + len(get_all_mlie_and_time_list_09) / 2 + len(
                    get_all_mlie_and_time_list_10) / 2 + len(get_all_mlie_and_time_list_11) / 2 + len(
                    get_all_mlie_and_time_list_12) / 2
                web_total = self.statistical_form_page.get_total_search_mileage_form()
                self.assertEqual(total, web_total)

                # 拆分列表
                all_mile_list = []
                all_time_list = []
                '''for n in range(len(get_all_mlie_and_time_list)):
                    if n % 2 == 0:
                        all_mile_list.append(get_all_mlie_and_time_list[n])
                    elif n % 2 == 1:
                        all_time_list.append(get_all_mlie_and_time_list[n])'''

                # 拆分列表
                all_mile_list_01 = []
                all_time_list_01 = []
                for n in range(len(get_all_mlie_and_time_list_01)):
                    if n % 2 == 0:
                        all_mile_list_01.append(get_all_mlie_and_time_list_01[n])
                    elif n % 2 == 1:
                        all_time_list_01.append(get_all_mlie_and_time_list_01[n])

                # 拆分列表
                all_mile_list_02 = []
                all_time_list_02 = []
                for n in range(len(get_all_mlie_and_time_list_02)):
                    if n % 2 == 0:
                        all_mile_list_02.append(get_all_mlie_and_time_list_02[n])
                    elif n % 2 == 1:
                        all_time_list_02.append(get_all_mlie_and_time_list_02[n])

                # 拆分列表
                all_mile_list_03 = []
                all_time_list_03 = []
                for n in range(len(get_all_mlie_and_time_list_03)):
                    if n % 2 == 0:
                        all_mile_list_03.append(get_all_mlie_and_time_list_03[n])
                    elif n % 2 == 1:
                        all_time_list_03.append(get_all_mlie_and_time_list_03[n])

                # 拆分列表
                all_mile_list_04 = []
                all_time_list_04 = []
                for n in range(len(get_all_mlie_and_time_list_04)):
                    if n % 2 == 0:
                        all_mile_list_04.append(get_all_mlie_and_time_list_04[n])
                    elif n % 2 == 1:
                        all_time_list_04.append(get_all_mlie_and_time_list_04[n])

                # 拆分列表
                all_mile_list_05 = []
                all_time_list_05 = []
                for n in range(len(get_all_mlie_and_time_list_05)):
                    if n % 2 == 0:
                        all_mile_list_05.append(get_all_mlie_and_time_list_05[n])
                    elif n % 2 == 1:
                        all_time_list_05.append(get_all_mlie_and_time_list_05[n])

                # 拆分列表
                all_mile_list_06 = []
                all_time_list_06 = []
                for n in range(len(get_all_mlie_and_time_list_06)):
                    if n % 2 == 0:
                        all_mile_list_06.append(get_all_mlie_and_time_list_06[n])
                    elif n % 2 == 1:
                        all_time_list_06.append(get_all_mlie_and_time_list_06[n])

                # 拆分列表
                all_mile_list_07 = []
                all_time_list_07 = []
                for n in range(len(get_all_mlie_and_time_list_07)):
                    if n % 2 == 0:
                        all_mile_list_07.append(get_all_mlie_and_time_list_07[n])
                    elif n % 2 == 1:
                        all_time_list_07.append(get_all_mlie_and_time_list_07[n])

                # 拆分列表
                all_mile_list_08 = []
                all_time_list_08 = []
                for n in range(len(get_all_mlie_and_time_list_08)):
                    if n % 2 == 0:
                        all_mile_list_08.append(get_all_mlie_and_time_list_08[n])
                    elif n % 2 == 1:
                        all_time_list_08.append(get_all_mlie_and_time_list_08[n])

                # 拆分列表
                all_mile_list_09 = []
                all_time_list_09 = []
                for n in range(len(get_all_mlie_and_time_list_09)):
                    if n % 2 == 0:
                        all_mile_list_09.append(get_all_mlie_and_time_list_09[n])
                    elif n % 2 == 1:
                        all_time_list_09.append(get_all_mlie_and_time_list_09[n])

                # 拆分列表
                all_mile_list_10 = []
                all_time_list_10 = []
                for n in range(len(get_all_mlie_and_time_list_10)):
                    if n % 2 == 0:
                        all_mile_list_10.append(get_all_mlie_and_time_list_10[n])
                    elif n % 2 == 1:
                        all_time_list_10.append(get_all_mlie_and_time_list_10[n])

                # 拆分列表
                all_mile_list_11 = []
                all_time_list_11 = []
                for n in range(len(get_all_mlie_and_time_list_11)):
                    if n % 2 == 0:
                        all_mile_list_11.append(get_all_mlie_and_time_list_11[n])
                    elif n % 2 == 1:
                        all_time_list_11.append(get_all_mlie_and_time_list_11[n])

                # 拆分列表
                all_mile_list_12 = []
                all_time_list_12 = []
                for n in range(len(get_all_mlie_and_time_list_12)):
                    if n % 2 == 0:
                        all_mile_list_12.append(get_all_mlie_and_time_list_12[n])
                    elif n % 2 == 1:
                        all_time_list_12.append(get_all_mlie_and_time_list_12[n])

                # 计算总里程 和 总时间
                total_mile = sum(all_mile_list) + sum(all_mile_list_01) + sum(all_mile_list_02) + sum(
                    all_mile_list_03) + sum(all_mile_list_04) + sum(all_mile_list_05) + sum(all_mile_list_06) + sum(
                    all_mile_list_07) + sum(all_mile_list_08) + sum(all_mile_list_09) + sum(all_mile_list_10) + sum(
                    all_mile_list_11) + sum(all_mile_list_12)
                total_time = sum(all_time_list) + sum(all_time_list_01) + sum(all_time_list_02) + sum(
                    all_time_list_03) + sum(all_time_list_04) + sum(all_time_list_05) + sum(all_time_list_06) + sum(
                    all_time_list_07) + sum(all_time_list_08) + sum(all_time_list_09) + sum(all_time_list_10) + sum(
                    all_time_list_11) + sum(all_time_list_12)
                # 断言总时间和总里程，总油耗
                web_total_mile = self.statistical_form_page.get_mileage_all_mile()
                self.assertAlmostEqual(total_mile / 1000, float(web_total_mile))

                web_total_time = self.statistical_form_page.get_mileage_all_time()
                chang_total_time_type = self.statistical_form_page.change_sec_time(total_time)
                self.assertEqual(chang_total_time_type, web_total_time)

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

            # 点击导出
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
