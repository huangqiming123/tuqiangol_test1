import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.statistical_form.form_page import FormPage
from pages.statistical_form.statistic_form_page3 import StatisticFormPage3
from pages.statistical_form.statistical_form_page import StatisticalFormPage


class TestCase195StatusVerifyTheDisplayLine(unittest.TestCase):
    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page3 = StatisticFormPage3(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.form_page = FormPage(self.driver, self.base_url)
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

    def test_case_195_status_verify_the_display_line(self):
        # 断言url
        expect_url_after_click_statistical_form = self.base_url + '/deviceReport/statisticalReport'
        self.assertEqual(expect_url_after_click_statistical_form,
                         self.statistical_form_page.actual_url_after_statistical_form())
        # 断言
        self.assertEqual(self.assert_text.statistical_form_sport_overview_form(),
                         self.statistical_form_page.actual_text_after_click_sport_overview())
        self.statistical_form_page.click_status_form_button()
        self.statistical_form_page.switch_to_status_report_form_frame()
        # 点击展示列
        self.form_page.click_display_line_button_status()
        # 获取有多少个展示列
        display_line_number = self.form_page.get_display_line_number_status()
        self.form_page.click_display_line_button_status()
        for n in range(display_line_number):
            # 获取每一个展示列是否被勾选
            self.form_page.click_display_line_button_status()
            display_style = self.form_page.get_per_display_style_status(n)
            display_style_list = []
            for n1 in range(display_line_number):
                display_styles = self.form_page.get_per_display_style_status(n1)
                if display_styles == True:
                    display_style_list.append(display_styles)
            display_line_name = self.form_page.get_per_display_name_status(n)
            # 点击
            self.form_page.click_per_display_input_button_status(n)
            # 点击展示列
            self.form_page.click_display_line_button_status()
            # 获取展示列数量
            display_line_name_list = []
            display_line_name_number = self.form_page.get_display_line_name_number_status()
            for m in range(display_line_name_number):
                display_name = self.form_page.get_per_display_name_on_line_status(m)
                display_line_name_list.append(display_name)
            if len(display_style_list) == 1:
                self.assertIn(display_line_name, display_line_name_list)
            else:
                if display_style == True:
                    self.assertNotIn(display_line_name, display_line_name_list)
                elif display_style == False:
                    self.assertIn(display_line_name, display_line_name_list)

        self.driver.default_frame()
