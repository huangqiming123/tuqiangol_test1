import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from model.write_excel import write_excel
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.form_export_page import FormExportPage
from pages.statistical_form.form_page import FormPage
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv
from testcases.total.page import Page

__author__ = ''


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
        self.driver.close_window()
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

        l_data = [['序号', '所属账号', '客户名称', '设备名称', 'imei', '型号', '设备分组', '总里程(KM)', '超速(次)', '停留(次)', '司机名称', '电话', '车牌号',
                   '身份证号', '车架号', '电动机/发动机号']]
        for m in web_data:
            l_data.append(
                [m['序号'], m['所属账号'], m['客户名称'], m['设备名称'], m['IMEI'], m['型号'], m['设备分组'], m['总里程(KM)'], m['超速(次)'],
                 m['停留(次)'], m['司机名称'], m['电话'], m['车牌号'], m['身份证号'], m['车架号'], m['电动机／发动机号']])
        print(l_data)
        write_excel('add', l_data)

        self.driver.default_frame()
