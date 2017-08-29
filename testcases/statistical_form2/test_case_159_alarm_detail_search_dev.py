import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.search_sql import SearchSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page2 import StatisticalFormPage2
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


class TestCase159AlarmDetailSearchDev(unittest.TestCase):
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
        self.search_sql = SearchSql(self.driver, self.base_url)
        self.statistical_form_page2 = StatisticalFormPage2(self.driver, self.base_url)

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.assert_text = AssertText()
        self.log_in_base.log_in_jimitest()
        # 登录之后点击控制台，然后点击指令管理
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_alarm_detail_search_dev(self):
        # 断言url
        expect_url = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 点击告警详情
        self.alarm_info_page.click_alarm_detail_list()
        # 断言
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.assertEqual(self.assert_text.account_center_page_alarm_details_text(),
                         self.alarm_info_page.actual_text_after_click_alarm_detail())

        # 验证搜索下级的imei可以搜索到
        # 填写下级的imei搜索
        sleep(2)
        self.statistical_form_page2.input_imei_to_search_in_alarm_detail_form(self.statistical_form_page2.get_imei())
        # 断言
        # 获取查询设备的imei
        search_imei = self.statistical_form_page2.get_search_imei_in_alarm_detail_forms()
        self.assertEqual(search_imei, self.statistical_form_page2.get_imei())

        # 验证停机的设备无法搜索到
        self.statistical_form_page2.input_imei_to_search_in_alarm_detail_form(
            self.statistical_form_page2.get_no_active_imei())
        # 获取搜索的数量
        get_number_after_search = self.statistical_form_page.get_number_after_search_in_alarm_detail_form()
        self.assertEqual(0, get_number_after_search)

        get_text_after_search = self.statistical_form_page.get_text_after_search_in_alarm_detail_form()
        self.assertIn(self.assert_text.account_center_page_no_data_text(), get_text_after_search)

        self.driver.default_frame()
