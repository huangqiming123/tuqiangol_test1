import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_refill_card_page import AccountCenterRefillCardPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.account_center.search_sql import SearchSql
from pages.login.login_page import LoginPage


# 账户详情-充值卡--申请充值卡--异常验证
# author:戴招利
class TestCase430918AccountCenterRefillCardApplyException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_refill_card = AccountCenterRefillCardPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
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

    def test_apply_refill_card_exception_verify(self):
        '''充值卡-申请记录--申请充值卡-异常验证'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入充值卡页面
        self.account_center_page_refill_card.click_refill_card()
        # 点申请充值卡
        self.account_center_page_refill_card.click_apply_refill_card_button()

        csv_file = self.account_center_page_read_csv.read_csv('apply_refill_card_exception.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "year": row[0],
                "lifetime": row[1],
                "name": row[2],
                "phone": row[3],
                "payment_account": row[4],
                "year_prompt1": row[5],
                "lifetime_prompt1": row[6],
                "name_prompt1": row[7],
                "phone_prompt1": row[8],
                "account_prompt1": row[9]

            }

            # 获取提示
            prompt = self.account_center_page_refill_card.get_apply_refill_card_exception_hint(data["year"],
                                                                                               data["lifetime"],
                                                                                               data["name"],
                                                                                               data["phone"],
                                                                                               data["payment_account"])

            self.assertIn(data["year_prompt1"], prompt["year_prompt2"], "一年充值卡提示不一致")
            self.assertIn(data["lifetime_prompt1"], prompt["lifetimet_prompt2"], "终身充值卡提示不一致")
            self.assertEqual(data["name_prompt1"], prompt["name_prompt2"], "付款姓名提示不一致")
            self.assertEqual(data["phone_prompt1"], prompt["phone_prompt2"], "付款手机号卡提示不一致")
            self.assertEqual(data["account_prompt1"], prompt["account_prompt2"], "付款账号提示不一致")

        #长度
        length = self.account_center_page_refill_card.get_apply_refill_card_len()
        self.assertEqual(5, length["year_len"], "一年充值卡长度不一致")
        self.assertEqual(5, length["lifetime_len"], "终身充值卡长度不一致")
        self.assertEqual(20, length["name_len"], "姓名长度不一致")
        self.assertEqual(20, length["phone_len"], "手机号长度不一致")
        self.assertEqual(200, length["account_len"], "付款账号长度不一致")
