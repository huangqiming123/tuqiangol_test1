import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_refill_card_page import AccountCenterRefillCardPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户详情-充值卡--申请充值卡
# author:戴招利
class TestCase410918AccountCenterRefillCardAddApply(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_refill_card = AccountCenterRefillCardPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.assert_text2 = AssertText2()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_apply_refill_card(self):
        '''充值卡-申请记录--申请充值卡'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        # self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.log_in_base.log_in()
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()

        # 进入充值卡页面
        # self.account_center_page_navi_bar.switch_to_chongzhi_card()
        self.account_center_page_refill_card.click_refill_card()

        csv_file = self.account_center_page_read_csv.read_csv('apply_refill_card.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "year": row[0],
                "lifetime": row[1],
                "name": row[2],
                "phone": row[3],
                "payment_account": row[4]

            }
            # 验证页面顶部我的账号
            my_account = self.account_center_page_refill_card.get_title_display_account()
            # 取消
            self.account_center_page_refill_card.apply_refill_card_cancel()

            # 验证账号
            self.account_center_page_refill_card.click_apply_refill_card_button()
            apply_page_account = self.account_center_page_refill_card.get_refill_account()
            self.assertEqual(my_account, apply_page_account, "充值账号显示不一致")

            # 添加充值卡
            self.account_center_page_refill_card.apply_refill_card_add(data["year"], data["lifetime"],
                                                                       data["name"], data["phone"],
                                                                       data["payment_account"])

            information = self.account_center_page_refill_card.get_applicant_information()

            statu = self.account_center_page_refill_card.get_operate_status()
            self.assertEqual(self.assert_text2.account_center_refill_card_apply_succeed(), statu, "申请充值卡失败")

            # 验证添加数据与申请人信息
            self.assertEqual(apply_page_account, information["applicant_account"], "申请人信息中，充值账号显示不一致")
            self.assertEqual(data["year"] + "张", information["year"], "申请人信息中，一年充值卡张数显示不一致")
            self.assertEqual(data["lifetime"] + "张", information["lifetime"], "申请人信息中，终身充值卡张数显示不一致")
            self.assertEqual(data["name"], information["name"], "申请人信息中，付款人姓名显示不一致")
            self.assertEqual(data["phone"], information["phone"], "申请人信息中，充值联系方式显示不一致")
            self.assertEqual(data["payment_account"], information["payment_account"], "申请人信息中，付款账号显示不一致")

        csv_file.close()
        # 退出登录
        # self.account_center_page_navi_bar.usr_logout()
