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


class TestCase48AccountCenterVerifyInfo(unittest.TestCase):
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

    def test_account_center_verify_info(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in_jimitest()
        self.account_center_page_navi_bar.click_account_center_button()

        ## 进入账号详情的frame
        self.account_center_page.switch_to_account_info_frame()
        ## 获取到登录账号的信息
        account = self.account_center_page.get_account_in_account_info_page()
        account_type = self.account_center_page.get_account_type_in_account_info_page()
        account_telephone = self.account_center_page.get_account_telephone_in_account_info_page()
        ## 获取最下方客户信息
        account_01 = self.account_center_page.get_account_01_in_account_info_page()
        account_type_01 = self.account_center_page.get_account_type_01_in_account_info_page()
        account_telephone_01 = self.account_center_page.get_account_telephone_01_in_account_info_page()
        ## 断言
        self.assertEqual(account, account_01)
        self.assertEqual(account_type, account_type_01)
        self.assertEqual(account_telephone, account_telephone_01)

        ## 获取电话、短信告警总数信息
        telephone_alarm_number = self.account_center_page.get_telephone_alarm_number_in_account_info_page()
        massage_alarm_number = self.account_center_page.get_massage_alarm_number_in_account_info_page()

        ## 获取数据库剩余电话短信的条数
        telephone_and_massage_alarm_number_in_mysql = self.account_center_page.get_telephone_and_massage_alarm_number_in_mysql(
            account)
        telephone_alarm_number_01 = str(telephone_and_massage_alarm_number_in_mysql[0][0]) + '分钟'
        massage_alarm_number_01 = str(telephone_and_massage_alarm_number_in_mysql[0][1]) + '条'
        self.assertEqual(telephone_alarm_number, telephone_alarm_number_01)
        self.assertEqual(massage_alarm_number, massage_alarm_number_01)

        ## 获取充值卡剩余数量
        year_card_number = self.account_center_page.get_year_card_number_in_account_info_page()
        life_card_number = self.account_center_page.get_life_card_number_in_account_info_page()

        ## 获取数据库剩余充值卡数量
        year_and_life_card_number_in_mysql = self.account_center_page.get_year_and_life_card_number_in_mysql(account)
        year_card_number_01 = str(year_and_life_card_number_in_mysql[0][0]) + '张'
        life_card_number_01 = str(year_and_life_card_number_in_mysql[0][1]) + '张'

        self.assertEqual(year_card_number, year_card_number_01)
        self.assertEqual(life_card_number, life_card_number_01)

        ## 获取昨天消费统计数
        consume_massage_alarm_number = self.account_center_page.get_consume_massage_alarm_number_in_account_info_page()
        consume_telephone_alarm_number = self.account_center_page.get_consume_telephone_alarm_number_in_account_info_page()
        consume_year_card_number = self.account_center_page.get_consume_year_card_number_in_account_info_page()
        consume_life_card_number = self.account_center_page.get_consume_life_card_number_in_account_info_page()

        # 分别获取昨天的短信、电话、年卡、终生卡消费情况
        begin_time = self.account_center_page.get_bengin_time('昨天')
        end_time = self.account_center_page.get_end_time('昨天')
        consume_number = self.account_center_page.get_consume_number_in_mysql(begin_time, end_time, account)
        self.assertEqual(consume_massage_alarm_number, consume_number[0])
        self.assertEqual(consume_telephone_alarm_number, consume_number[1])
        self.assertEqual(consume_year_card_number, consume_number[2])
        self.assertEqual(consume_life_card_number, consume_number[3])

        # 点击当月
        self.account_center_page.click_this_month_in_account_page()

        ## 获取昨天消费统计数
        consume_massage_alarm_number = self.account_center_page.get_consume_massage_alarm_number_in_account_info_page()
        consume_telephone_alarm_number = self.account_center_page.get_consume_telephone_alarm_number_in_account_info_page()
        consume_year_card_number = self.account_center_page.get_consume_year_card_number_in_account_info_page()
        consume_life_card_number = self.account_center_page.get_consume_life_card_number_in_account_info_page()

        # 分别获取昨天的短信、电话、年卡、终生卡消费情况
        begin_time = self.account_center_page.get_bengin_time('本月')
        end_time = self.account_center_page.get_end_time('本月')
        consume_number = self.account_center_page.get_consume_number_in_mysql(begin_time, end_time, account)
        self.assertEqual(consume_massage_alarm_number, consume_number[0])
        self.assertEqual(consume_telephone_alarm_number, consume_number[1])
        self.assertEqual(consume_year_card_number, consume_number[2])
        self.assertEqual(consume_life_card_number, consume_number[3])

        # 点击上月
        self.account_center_page.click_last_month_in_account_page()

        ## 获取昨天消费统计数
        consume_massage_alarm_number = self.account_center_page.get_consume_massage_alarm_number_in_account_info_page()
        consume_telephone_alarm_number = self.account_center_page.get_consume_telephone_alarm_number_in_account_info_page()
        consume_year_card_number = self.account_center_page.get_consume_year_card_number_in_account_info_page()
        consume_life_card_number = self.account_center_page.get_consume_life_card_number_in_account_info_page()

        # 分别获取昨天的短信、电话、年卡、终生卡消费情况
        begin_time = self.account_center_page.get_bengin_time('上月')
        end_time = self.account_center_page.get_end_time('上月')
        consume_number = self.account_center_page.get_consume_number_in_mysql(begin_time, end_time, account)
        self.assertEqual(consume_massage_alarm_number, consume_number[0])
        self.assertEqual(consume_telephone_alarm_number, consume_number[1])
        self.assertEqual(consume_year_card_number, consume_number[2])
        self.assertEqual(consume_life_card_number, consume_number[3])

        self.driver.default_frame()
