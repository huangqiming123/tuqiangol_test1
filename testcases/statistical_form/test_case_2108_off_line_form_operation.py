import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase2108OffLineFormOperation(unittest.TestCase):
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
        self.search_sql = SearchSql()
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

    def test_case_2108_off_line_form_operation(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())

        # 点击离线统计
        self.statistical_form_page.click_off_line_form_button()

        # 断言文本
        text = self.statistical_form_page.get_text_after_click_off_line_form_button()
        self.assertEqual('离线统计', text)

        # 检查里面时间格式
        self.statistical_form_page.add_off_time_in_off_line_form('sss')
        # 点击搜索
        self.statistical_form_page.click_search_button_in_off_line_form()
        get_text = self.statistical_form_page.get_text_after_click_search()
        self.assertEqual('必须是正整数！', get_text)

        # 循环客户树
        for n in range(5):
            self.statistical_form_page.click_customer_in_off_line(n)

        # 搜索客户树无数据
        self.statistical_form_page.add_data_to_search_customer_in_off_line('无数据')
        text = self.statistical_form_page.get_text_after_click_search_in_off_line()
        self.assertEqual('  暂无数据 ', text)
