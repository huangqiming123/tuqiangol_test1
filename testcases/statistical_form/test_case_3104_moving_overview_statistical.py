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


class TestCase3104MovingOverviewStatistical(unittest.TestCase):
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

    def test_case_3104_moving_overview_statistical(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())
        # 读数据
        csv_file = self.statistical_form_page_read_csv.read_csv('sport_statistical_sport_overview_search_data.csv')
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
            self.statistical_form_page.add_data_to_search_sport_overview(search_data)
            self.statistical_form_page.switch_to_sport_overview_form_frame()
            # 获取总的里程数
            total_mile = self.statistical_form_page.get_total_mile_in_moving_overview()
            total_over_speed_times = self.statistical_form_page.get_total_over_speed_times_in_moving_overview()
            total_stop_over_times = self.statistical_form_page.get_total_stop_over_times_in_moving_overview()

            get_total_number = self.statistical_form_page.get_total_number_in_moving_overview()
            if get_total_number != 0:
                # 获取列表中里程的列表
                mile_list = []
                for n in range(get_total_number):
                    a = self.statistical_form_page.get_per_mile_in_list_in_moving_overview(n)
                    mile_list.append(float(a))
                total_mile_list = sum(mile_list)
                total_mile_lists = '%.3f' % total_mile_list
                self.assertEqual(total_mile, str(total_mile_lists))

                # 获取列表中超速报表的总数
                over_speed_list = []
                for n in range(get_total_number):
                    b = self.statistical_form_page.get_per_over_speed_in_list_in_moving_overview(n)
                    over_speed_list.append(int(b))
                total_over_speed_list = sum(over_speed_list)
                self.assertEqual(total_over_speed_times, str(total_over_speed_list))

                # 获取列表中停留的总数
                stop_over_list = []
                for n in range(get_total_number):
                    c = self.statistical_form_page.get_per_stop_over_in_list_in_moving_overview(n)
                    stop_over_list.append(int(c))
                total_stop_over_list = sum(stop_over_list)
                self.assertEqual(total_stop_over_times, str(total_stop_over_list))

            self.driver.default_frame()
        csv_file.close()
