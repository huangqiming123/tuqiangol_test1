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


class TestCase153GuideManchineReport(unittest.TestCase):
    '''
    用例第153条，导游播报统计 仅仅hemi的账号有
    author ：zhangAo
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

    def test_case_153_guide_manchine_report(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击停留报表
        self.statistical_form_page.click_guide_manchine_report_button()
        # 断言
        self.assertEqual('导游播报统计', self.statistical_form_page.actual_text_after_click_guide_manchine_report_button())

        # 读取查询数据
        csv_file = self.statistical_form_page_read_csv.read_csv('guide_manchine_report_search_data.csv')
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
                'end_time': row[3],
                'status': row[4],
            }
            self.statistical_form_page.switch_to_guide_manchine_report_frame()
            self.statistical_form_page.add_data_to_search_guide_manchine_report(search_data)

            # 获取当前用户所有的设备
            all_dev = self.search_sql.search_current_account_equipment(search_data['search_user'])
            all_user_dev = self.search_sql.search_current_account_equipment_and_next(search_data['search_user'])
            connect = self.connect_sql.connect_tuqiang_form()
            cursor = connect.cursor()
            get_total_and_times_sql = self.search_sql.get_total_and_times_sql(all_dev, all_user_dev, search_data)
            print(get_total_and_times_sql)
            cursor.execute(get_total_and_times_sql)
            data = cursor.fetchall()
            list_times = []
            for range1 in data:
                for range2 in range1:
                    list_times.append(range2)
            # 可用次数
            usable_numbers_list = []
            # 已用次数
            used_numbers_list = []
            for n in range(len(list_times)):
                if n % 3 == 1:
                    usable_numbers_list.append(list_times[n])
                elif n % 3 == 2:
                    used_numbers_list.append(list_times[n])
            total = len(list_times)
            web_total = self.statistical_form_page.get_total_number_in_guide_machine_report()
            self.assertEqual(total, web_total)

            total_usable_numbers = sum(usable_numbers_list)
            web_total_usable_numbers = self.statistical_form_page.get_web_total_usable_numbers_in_guide_machine_report()
            self.assertEqual(str(total_usable_numbers), web_total_usable_numbers)

            total_used_numbers = sum(used_numbers_list)
            web_total_used_numbers = self.statistical_form_page.get_web_total_used_numbers_in_guide_machine_report()
            self.assertEqual(str(total_used_numbers), web_total_used_numbers)
            cursor.close()
            connect.close()
            self.driver.default_frame()
        csv_file.close()
