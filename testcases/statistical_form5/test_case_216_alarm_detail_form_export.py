import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.form_export_page import FormExportPage
from pages.statistical_form.form_page import FormPage
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistic_form_page3 import StatisticFormPage3
from pages.statistical_form.statistic_form_page4 import StatisticFormPage4
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv
from testcases.total.page import Page


class TestCase216AlarmDetailFormExport(unittest.TestCase):
    # 告警详情 - 导出
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
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.form_page = FormPage(self.driver, self.base_url)
        self.page = Page(self.driver, self.base_url)
        self.form_export_page = FormExportPage(self.driver, self.base_url)
        self.statistical_form_page4 = StatisticFormPage4(self.driver, self.base_url)
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

    def test_case_216_alarm_detail_form_export(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())

        # 切换到里程报表的frame
        self.statistical_form_page.click_alarm_detail_reoport()
        self.statistical_form_page.switch_to_alarm_detail_frame()
        # 搜索数据
        self.form_export_page.search_alarm_detail_data()

        # 让其展示所有列
        # 点击展示列
        self.form_page.click_display_line_button_alarm_detail()
        # 获取有多少个展示列
        display_line_number = self.form_page.get_display_line_number_alarm_detail()
        for n in range(display_line_number):
            # 获取每一个展示列是否被勾选
            display_style = self.form_page.get_per_display_style_alarm_detail(n)
            if display_style == False:
                self.form_page.click_per_display_input_button_alarm_detail(n)
        self.form_page.click_display_line_button_alarm_detail()
        # 获取页面中的数据
        web_data = []
        total_page = self.statistical_form_page4.get_total_page_in_alarm_detail()
        if total_page == 0:
            pass
        else:
            if total_page == 1:
                total_number_per_page = self.statistical_form_page4.get_total_number_per_page_in_alarm_detail()
                for a in range(total_number_per_page):
                    web_data.append(self.form_export_page.get_per_line_data_alarm_detail(a))

            else:
                for x in range(total_page):
                    self.statistical_form_page3.click_per_page_in_mile_report_form(x)
                    total_number_per_page = self.statistical_form_page4.get_total_number_per_page_in_alarm_detail()
                    for a in range(total_number_per_page):
                        web_data.append(self.form_export_page.get_per_line_data_alarm_detail(a))

            # 点击导出所有列
            self.form_export_page.click_export_button_in_mileage()
            # 点击关闭按钮
            # self.form_export_page.click_close_button()
            # 点击导出所有列
            # self.form_export_page.click_export_button_in_mileage()
            # 切换到导出的frame中
            self.driver.default_frame()
            self.form_export_page.switch_export_framea()
            self.form_export_page.click_export_button_in_alarm_detail_page()
            # 查找刚刚导出的文件
            file = self.form_export_page.find_expect_file()
            print(file)
            # 读excel文件
            excel_data = self.form_export_page.read_excel_file_by_index(file, n=0)
            del excel_data[0]
            for per_data in excel_data:
                del per_data['告警天数']
            print('excel', excel_data)
            print('web', web_data)

            self.assertEqual(web_data, excel_data)

        self.driver.default_frame()
