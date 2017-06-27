import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase2111GuideManchineReportSearchUser(unittest.TestCase):
    '''
    导游播报统计搜索用户
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

    def test_case_2111_guide_manchine_report_search_user(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击停留报表
        self.statistical_form_page.click_guide_manchine_report_button()
        # 断言
        self.assertEqual('导游播报统计', self.statistical_form_page.actual_text_after_click_guide_manchine_report_button())

        # 循环点击用户
        self.statistical_form_page.switch_to_guide_manchine_report_frame()
        for n in range(5):
            self.statistical_form_page.click_search_user_button_in_guide_manchine_report()
            get_user_name = self.statistical_form_page.get_user_name_in_guide_manchine_report(n + 1)
            self.statistical_form_page.click_per_user_in_guide_manchine_report(n + 1)
            user_name = self.statistical_form_page.user_name_in_guide_manchine_report()
            self.assertEqual(get_user_name, user_name)
        self.driver.default_frame()
