import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase111GlobSearchDevSearchHigher(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_global_search_dev_search_higher(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()

        # 点击高级
        # self.global_dev_search_page.click_dev_searchs()
        self.global_dev_search_page.click_higher_search()

        # 验证选择用户
        # 点下拉客户树
        # 循环点击
        for n in range(5):
            self.global_dev_search_page.click_pull_down_customer()
            get_customer_name = self.global_dev_search_page.get_customer_name(n)
            self.global_dev_search_page.click_customer_in_higher_search(n)
            # 获取点击之后抬头显示的客户名字
            get_customer_text = self.global_dev_search_page.get_customer_text()
            self.assertEqual(get_customer_name, get_customer_text)

        # 验证结束日期的格式
        # 点击时间段
        self.global_dev_search_page.click_time_quantum_button()
        get_time_quantum_input_value = self.global_dev_search_page.get_time_quantum_input_value()
        self.assertEqual(True, get_time_quantum_input_value)
        # 输入结束日期
        self.global_dev_search_page.check_end_date_type('2022021551')
        # 获取日期错误的提示
        get_text = self.global_dev_search_page.get_text_after_input_date()
        self.assertEqual(self.assert_text.glob_search_page_date_formate_error(), get_text)

        # 验证欠费、激活的按钮
        self.global_dev_search_page.click_arrearage_button()
        get_arrearage_input_value = self.global_dev_search_page.get_arrearage_input_value()
        self.assertEqual(True, get_arrearage_input_value)

        self.global_dev_search_page.click_not_active_button()
        get_not_active_input_value = self.global_dev_search_page.get_not_active_input_value()
        self.assertEqual(True, get_not_active_input_value)

        # 验证基本信息的提示语是否正确
        # imei
        get_text = self.global_dev_search_page.get_text_dev_info()
        self.assertEqual(self.assert_text.glob_search_page_text('imei'), get_text)

        # 车牌号
        self.global_dev_search_page.click_car_plate_number_dev_info()
        get_text = self.global_dev_search_page.get_text_dev_info()
        self.assertEqual(self.assert_text.glob_search_page_text('车牌号'), get_text)

        # sn
        self.global_dev_search_page.click_sn_dev_info()
        get_text = self.global_dev_search_page.get_text_dev_info()
        self.assertEqual(self.assert_text.glob_search_page_text('sn'), get_text)

        # 车架号
        self.global_dev_search_page.click_vin_dev_info()
        get_text = self.global_dev_search_page.get_text_dev_info()
        self.assertEqual(self.assert_text.glob_search_page_text('车架号'), get_text)

        # sim卡号
        self.global_dev_search_page.click_sim_dev_info()
        get_text = self.global_dev_search_page.get_text_dev_info()
        self.assertEqual(self.assert_text.glob_search_page_text('sim'), get_text)

        # 设备名称
        self.global_dev_search_page.click_dev_name_dev_info()
        get_text = self.global_dev_search_page.get_text_dev_info()
        self.assertEqual(self.assert_text.glob_search_page_text('name'), get_text)
