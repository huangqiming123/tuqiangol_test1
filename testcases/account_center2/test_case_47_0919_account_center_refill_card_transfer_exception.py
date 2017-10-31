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


# 账户详情-充值卡--充值卡转移--异常验证
# author:戴招利
class TestCase470919AccountCenterRefillCardTransferException(unittest.TestCase):
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

    def test_transfer_refill_card_exception_verify(self):
        '''充值卡转移--异常验证和循环点击下级账号'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        # self.log_in_base.log_in()
        self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入充值卡页面
        self.account_center_page_refill_card.click_refill_card()
        #获取顶部张数
        top_quantity = self.account_center_page_refill_card.get_refill_card_page_top_quantity()

        #点转移
        self.account_center_page_refill_card.click_refill_card_transfer_button()

        csv_file = self.account_center_page_read_csv.read_csv('transfer_refill_card_exception.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "user": row[0],
                "year_number": row[1],
                "lifetime_number": row[2],
                "user_hint": row[3],
                "year_hint": row[4],
                "lifetime_hint": row[5]

            }

            self.account_center_page_refill_card.refill_card_transfer(data["user"], data["year_number"],
                                                                      data["lifetime_number"])
            #提示
            prompt = self.account_center_page_refill_card.get_transfer_refill_card_exception_hint()

            self.assertEqual(data["user_hint"], prompt["user_prompt2"], "目标用户提示不一致")
            #一年卡
            try:
                self.assertIn(data["year_hint"], prompt["year_prompt2"], "一年充值卡提示不一致")
            except:
                year_number = top_quantity["year_number"].split("张")[0]
                self.assertEqual("请输入0~" + year_number + "的整数", prompt["year_prompt2"], "一年卡张数不一致")

            #终身卡
            try:
                self.assertIn(data["lifetime_hint"], prompt["lifetimet_prompt2"], "终身充值卡提示不一致")
            except:
                lifetime_number = top_quantity["lifetime_number"].split("张")[0]
                self.assertEqual("请输入0~" + lifetime_number + "的整数", prompt["lifetimet_prompt2"], "终身卡张数不一致")

        # 验证输入用户提示
        # self.account_center_page_refill_card.transfer_refill_card_search_user("用户111")
        #status = self.account_center_page_refill_card.get_operate_status()
        #self.assertEqual("普通用户不能作为转移目标用户",status,"提示不一致")


        #取消
        #self.account_center_page_refill_card.click_refill_card_transfer_cancel()
        #循环点击下级用户
        for i in range(5):
            self.account_center_page_refill_card.click_transfer_target_user(i)

        csv_file.close()
