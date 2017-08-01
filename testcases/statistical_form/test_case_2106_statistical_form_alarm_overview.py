import unittest
import time
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase2106StatisticalFormAlarmOverview(unittest.TestCase):
    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_2106_statistical_form_alarm_overview(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())

        # 点击告警总览
        self.alarm_info_page.click_alarm_overview_list()

        for n in range(5):
            self.statistical_form_page.click_customer_in_alarm_overview(n)
            # 点击搜索设备按钮
            self.statistical_form_page.click_search_dev_button_alarm_form()
            # 获取有多少组
            number = self.statistical_form_page.get_group_number_in_alarm_overview_form()
            if number == 0:
                pass
            else:
                for m in range(number):
                    # 收起默认组
                    self.statistical_form_page.click_defalut_group_in_alarm_overview_form()
                    # 获取每个组设备的数量
                    dev_number = self.statistical_form_page.get_dev_number_in_alarm_overview_form(m)
                    # 点开每一个分组
                    self.statistical_form_page.click_per_group_in_alarm_overview_form(m)
                    dev_number_list = self.statistical_form_page.get_dev_number_list_in_alarm_overview_form(m)
                    self.assertEqual(str(dev_number_list), dev_number)
