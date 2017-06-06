import unittest

from automate_driver.automate_driver import AutomateDriver

from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase

from pages.statistical_form.statistical_form_page import StatisticalFormPage
from pages.statistical_form.statistical_form_page2 import StatisticalFormPage2
from pages.statistical_form.statistical_form_page_read_csv import StatisticalFormPageReadCsv


# 统计报表--停留报表--异常搜索验证
# author:戴招利
class TestCase1104SportStatisticalStayFormExceptionSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.statistical_form_page = StatisticalFormPage(self.driver, self.base_url)
        self.statistical_form_page2 = StatisticalFormPage2(self.driver, self.base_url)
        self.statistical_form_page_read_csv = StatisticalFormPageReadCsv()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()

    def test_stay_form_exception_search(self):
        """
         停留报表页面，异常搜索数据验证
        """
        # 登录
        self.log_in_base.log_in_jimitest()
        # 点击进入统计报表、停留报表
        self.statistical_form_page.click_control_after_click_statistical_form_page()
        self.statistical_form_page.click_stay_form_button()

        # 取开始、结束时间
        type = ["今天", "本周", "昨天", "上周", "本月", "上月", "自定义"]
        data = ["暂无数据"]

        for time in type:
            time = self.statistical_form_page2.stay_form_validation_time(time)
            self.assertEqual(time["page_time"]["page_start_time"], time["sql_time"]["sql_start_time"], "实际与显示的开始时间不相符")
            self.assertEqual(time["page_time"]["page_end_time"], time["sql_time"]["sql_end_time"], "实际与显示的结束时间不相符")

        # 验证提示
        for user in data:
            text = self.statistical_form_page2.search_inexistence_user(user)
            print(text)
            self.assertIn(user, text, "搜索后的数据不存在实际搜索出的数据中")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()
