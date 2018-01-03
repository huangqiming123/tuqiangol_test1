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
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv
from testcases.total.page import Page


class TestCase701FormExportSportOverviewExport(unittest.TestCase):
    # 测试 报表导出 运动总览导出
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
        self.form_page = FormPage(self.driver, self.base_url)
        self.page = Page(self.driver, self.base_url)
        self.form_export_page = FormExportPage(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        current_handle = self.driver.get_current_window_handle()
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)
        self.base_page.change_windows_handle(current_handle)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_sport_overview_export(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())

        # 切换到运动总览的frame
        self.statistical_form_page.switch_to_sport_overview_form_frame()
        # 点击搜索按钮
        self.form_export_page.click_search_button_in_sport_overview()

        # 让其展示所有列
        # 点击展示列
        self.form_page.click_display_line_button_sport_overview()
        # 获取有多少个展示列
        display_line_number = self.form_page.get_display_line_number_sport_overview()
        for n in range(display_line_number):
            # 获取每一个展示列是否被勾选
            display_style = self.form_page.get_per_display_style_sport_overview(n)
            if display_style == False:
                self.form_page.click_per_display_input_button(n)
        self.form_page.click_display_line_button_sport_overview()

        # 获取页面中的数据
        data_total_number = self.form_export_page.get_data_total_number_in_sport_overview()
        web_data = []
        for i in range(data_total_number):
            web_data.append(self.form_export_page.get_per_line_data(i))

        print('web', web_data)

        # 点击导出所有列
        self.form_export_page.click_export_button_in_sport_overview()
        # 判断有多少个div的标签
        export_div_number = self.form_export_page.get_sport_overview_export_div_number()
        for m in range(export_div_number - 2):
            # 获取基本信息和客户信息是否被勾选
            input_style = self.form_export_page.get_input_style_select_in_sport_overview_export(m)
            if input_style == False:
                self.form_export_page.click_per_in_sport_overview_export(m)
        # 点击生成任务按钮
        self.form_export_page.click_create_task_button_in_sport_overview_export()
        # 查找刚刚导出的文件
        file = self.form_export_page.find_expect_file()
        print(file)
        # 读excel文件
        excel_data = self.form_export_page.read_excel_file_by_index(file, col_name_index=1)
        del excel_data[0]
        print('excel', excel_data)

        self.assertEqual(web_data, excel_data)

        self.driver.default_frame()
