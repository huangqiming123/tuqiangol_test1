import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase148SportStatisticalMileageForm(unittest.TestCase):
    '''
    用例第148条，运动统计 里程报表
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
        self.seasrch_sql = SearchSql()
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_148_sport_statistical_mileage_form(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 点击里程报表
        self.statistical_form_page.click_mileage_form_button()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')
        self.assertEqual('里程报表', self.statistical_form_page.actual_text_after_click_mileage_form_button())
        self.driver.default_frame()

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
            self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')

            # 连接数据库
            # 连接数据库
            all_dev = self.seasrch_sql.search_current_account_equipment(search_data['search_user'])

            # 连接另一个数据库
            connect_02 = self.connect_sql.connect_tuqiang_form()
            # 创建游标
            cursor_02 = connect_02.cursor()
            # 判断查询的条件

            # 判断查询条件
            get_total_sql = self.seasrch_sql.search_sport_mile_sql(all_dev, search_data)
            print(get_total_sql)

            # 判断查询的条件
            if search_data['type'] == 'mile':
                # 查询的选择里程
                cursor_02.execute(get_total_sql)
                get_all_mlie_and_time = cursor_02.fetchall()
                get_all_mlie_and_time_list = []
                for range1 in get_all_mlie_and_time:
                    for range2 in range1:
                        get_all_mlie_and_time_list.append(range2)

                total = len(get_all_mlie_and_time_list) / 2
                web_total = self.statistical_form_page.get_total_search_mileage_form()
                self.assertEqual(total, web_total)

                # 拆分列表
                all_mile_list = []
                all_time_list = []
                for n in range(len(get_all_mlie_and_time_list)):
                    if n % 2 == 0:
                        all_mile_list.append(get_all_mlie_and_time_list[n])

                    elif n % 2 == 1:
                        all_time_list.append(get_all_mlie_and_time_list[n])

                # 计算总里程 和 总时间
                total_mile = sum(all_mile_list)
                total_time = sum(all_time_list)
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
                    get_total_oil = total_mile / 1000 / 100 * 8
                    total_oil = '%.2f' % get_total_oil
                    self.assertEqual(str(total_oil), self.statistical_form_page.get_mileage_total_oil())

            elif search_data['type'] == 'day':
                # 如果选择天
                cursor_02.execute(get_total_sql)
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
            self.statistical_form_page.click_export_mileage_form()
            self.driver.default_frame()
            cursor_02.close()
            connect_02.close()
        csv_file.close()
