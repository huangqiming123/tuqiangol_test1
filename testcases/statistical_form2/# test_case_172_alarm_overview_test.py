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


class TestCase172MovingOverviewTest(unittest.TestCase):
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
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_moving_overview_statistical(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())

        # 查询当前登录用户下设备当月的告警
        self.statistical_form_page.click_alarm_overview_list()
        self.statistical_form_page.switch_to_alarm_overview_form_frame()
        self.statistical_form_page.get_this_month_and_current_account_alarms()

        # 获取查询出来存在告警的设备imei
        current_dev = []
        get_number_in_search = self.statistical_form_page.get_total_number_in_search()
        for n in range(get_number_in_search):
            dev_imei = self.statistical_form_page.get_per_dev_imei_in_list(n)
            current_dev.append(dev_imei)
        print(current_dev)

        # 搜索下级用户
        self.statistical_form_page.search_next_account_in_alarm_overview()
        # 添加下级的设备
        self.statistical_form_page.add_next_dev_imei_in_alarm_overview()

        # 获取查询出来存在告警的设备imei
        current_dev_again = []
        get_number_in_search = self.statistical_form_page.get_total_number_in_search()
        for n in range(get_number_in_search):
            dev_imei = self.statistical_form_page.get_per_dev_imei_in_list(n)
            current_dev_again.append(dev_imei)
        print(current_dev_again)
        for i in range(len(current_dev)):
            self.assertIn(current_dev[i], current_dev_again)
        self.driver.default_frame()
