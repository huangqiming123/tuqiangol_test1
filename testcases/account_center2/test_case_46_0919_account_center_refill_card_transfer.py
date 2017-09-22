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


# 账户详情-充值卡--充值卡转移
# author:戴招利
class TestCase460918AccountCenterRefillCardTransfer(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
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

    def test_transfer_refill_card_succeed(self):
        '''充值卡--充值卡转移成功'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        # self.log_in_base.log_in_with_csv("kankan111", "jimi123")
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()

        csv_file = self.account_center_page_read_csv.read_csv('transfer_refill_card.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "account": row[0],
                "year_number": row[1],
                "lifetime_number": row[2],
                "username": row[3]

            }
            # 进入充值卡页面
            self.account_center_page_refill_card.click_refill_card()
            sleep(2)
            # 获取头部数量
            top_quantity = self.account_center_page_refill_card.get_refill_card_page_top_quantity()

            # 点转移
            self.account_center_page_refill_card.click_refill_card_transfer_button()
            # 获取数量
            transfer_quantity = self.account_center_page_refill_card.get_refill_card_transfer_quantity()
            self.assertEqual(top_quantity["year_number"], transfer_quantity["year_quantity"] + "张", "页面顶部与转移中显示的年卡不一致")
            self.assertEqual(top_quantity["lifetime_number"], transfer_quantity["lifetime_quantity"] + "张",
                             "页面顶部与转移中显示的终身卡不一致")

            # 充值卡转移-取消
            self.account_center_page_refill_card.refill_card_transfer_cancel()
            self.account_center_page_refill_card.click_refill_card_transfer_button()
            # 充值卡转移
            self.account_center_page_refill_card.refill_card_transfer(data["account"], data["year_number"],
                                                                      data["lifetime_number"])
            # 获取转移提示
            information = self.account_center_page_refill_card.get_refill_card_transfer_data_information()

            statu = self.account_center_page_refill_card.get_operate_status()
            self.assertEqual(self.assert_text2.account_center_refill_card_transfer_succeed(), statu, "充值卡转移失败")

            # 验证转移数据与转移提示中的信息
            self.assertEqual(data["username"], information["target_user"], "转移提示中，目标账号显示不一致")
            self.assertEqual(data["year_number"] + " 张", information["year_number"], "转移提示中，一年充值卡显示不一致")
            self.assertEqual(data["lifetime_number"] + " 张", information["lifetime_number"], "转移提示中，终身充值卡显示不一致")

        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
