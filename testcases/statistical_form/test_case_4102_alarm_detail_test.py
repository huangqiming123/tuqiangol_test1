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


class TestCase4102MovingDetailTest(unittest.TestCase):
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
        self.base_page.click_chinese_button()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击设置
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_4102_moving_detail_test(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())

        self.statistical_form_page.click_alarm_detail_list()
        self.statistical_form_page.switch_to_alarm_detail_frame()
        # 查询当前用户全部设备的告警信息
        self.statistical_form_page.search_current_account_alarms_in_alarm_detail()

        # 获取查询结果的所有imei
        # 获取查询总共有多少页
        page_number = self.statistical_form_page.get_total_page_after_search()
        dev_list = []
        if page_number == 0:
            pass
        elif page_number == 1:
            # 获取本页总共有多少条记录
            number = self.statistical_form_page.get_page_number_data_in_alarm_detail()
            for n in range(number):
                dev_imei = self.statistical_form_page.get_per_dev_imei_in_dev_alarm_detail(n)
                dev_list.append(dev_imei)
        else:
            for m in range(page_number):
                self.statistical_form_page.cilck_per_page_in_alarm_detail(m)
                number = self.statistical_form_page.get_page_number_data_in_alarm_detail()
                for n in range(number):
                    dev_imei = self.statistical_form_page.get_per_dev_imei_in_dev_alarm_detail(n)
                    dev_list.append(dev_imei)
        print(dev_list)
        dev_lists = list(set(dev_list))
        dev_lists.sort(key=dev_list.index)
        print(dev_lists)
        # 搜索当前用户的下级，并搜索
        self.statistical_form_page.search_next_account_in_alarm_detail()
        self.statistical_form_page.search_current_account_alarms_in_alarm_detail()

        page_numbers = self.statistical_form_page.get_total_page_after_search()
        dev_list_again = []
        if page_numbers == 0:
            pass
        elif page_numbers == 1:
            # 获取本页总共有多少条记录
            number = self.statistical_form_page.get_page_number_data_in_alarm_detail()
            for n in range(number):
                dev_imei = self.statistical_form_page.get_per_dev_imei_in_dev_alarm_detail(n)
                dev_list_again.append(dev_imei)
        else:
            for m in range(page_numbers):
                self.statistical_form_page.cilck_per_page_in_alarm_detail(m)
                number = self.statistical_form_page.get_page_number_data_in_alarm_detail()
                for n in range(number):
                    dev_imei = self.statistical_form_page.get_per_dev_imei_in_dev_alarm_detail(n)
                    dev_list_again.append(dev_imei)
        print(dev_list_again)
        dev_lists_again = list(set(dev_list_again))
        dev_lists_again.sort(key=dev_list_again.index)
        print(dev_lists_again)
        # for i in range(len(dev_lists)):
        #     self.assertIn(dev_lists[i], dev_lists_again)
        for dev in dev_list:
            self.assertEqual(dev, dev_lists_again)
        self.driver.default_frame()
