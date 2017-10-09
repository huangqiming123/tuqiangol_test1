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
from testcases.total.page import Page


class TestCase148SportStatisticalOverview(unittest.TestCase):
    '''
    运动统计，运动总览
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
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.page = Page(self.driver, self.base_url)
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

    def test_case_sport_statistical_sport_overview(self):
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
            # 点击导出
            self.page.click_expect_button()
            # 查找刚刚导出的文件
            file = self.page.find_expect_file_after_click_expect_button()
            print(file)
            # 读excel文件
            excel_data = self.page.read_excel_file_by_index(file, col_name_index=1)
            del excel_data[0]
            print(len(excel_data))
            number = self.page.get_number_in_sport_overview_form()
            web_data = []
            for n in range(number):
                web_data.append({
                    '序号': self.page.get_xuhao(n),
                    '型号': self.page.get_dev_type(n),
                    '停留(次)': self.page.get_stay_times(n),
                    '总里程(KM)': self.page.get_total_mile(n),
                    '超速(次)': self.page.get_over_speed_times(n),
                    '设备IMEI': self.page.get_imei(n),
                    '设备名称': self.page.get_dev_name(n)
                })
            self.assertEqual(web_data, excel_data)
            self.driver.default_frame()
            break
        csv_file.close()
