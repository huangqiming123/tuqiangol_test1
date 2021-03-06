import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page import AccountCenterPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_refill_card_page import AccountCenterRefillCardPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.account_center.search_sql import SearchSql
from pages.login.login_page import LoginPage


class TestCase50AccountCenterOrderManage(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_refill_card = AccountCenterRefillCardPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.account_center_page = AccountCenterPage(self.driver, self.base_url)
        self.search_sql = SearchSql()
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_account_center_order_manage(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in_jimitest()
        self.account_center_page_navi_bar.click_account_center_button()
        account = self.log_in_base.get_log_in_account()
        # 点击订单管理
        self.account_center_page_navi_bar.switch_to_chongzhi_card()
        self.account_center_page.clcik_order_manage_button_in_account_info_page()

        csv_file = self.account_center_page_read_csv.read_csv('order_manage.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'order_id': row[0],
                'date_type': row[1],
                'begin_time': row[2],
                'end_time': row[3],
                'goods_name': row[4],
                'order_type': row[5],
                'is_order': row[6],
                'is_pay': row[7]
            }
            self.account_center_page.add_data_to_search_order_manage_in_bill_list_page(search_data)

            ## 获取数据库查询的条数
            sql_number = self.account_center_page.get_sql_number_after_click_order_manage_search_button(account,
                                                                                                        search_data)
            # 获取页面上的条数
            web_number = self.account_center_page.get_web_number_after_click_order_manage_search_button()
            self.assertEqual(sql_number, web_number)
        csv_file.close()
