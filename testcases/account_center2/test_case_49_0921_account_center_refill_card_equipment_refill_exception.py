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


# 充值卡--设备充值-验证统计、删除、重置数据
# author:戴招利
class TestCase490921AccountCenterRefillCardEquipmentRefillException(unittest.TestCase):
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

    def test_equipment_refill_exception(self):
        '''充值卡-设备充值验证统计、数据'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        # self.log_in_base.log_in_with_csv("dzltest", "jimi123")
        self.log_in_base.log_in()
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()

        csv_file = self.account_center_page_read_csv.read_csv('equipment_refill.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "type": row[0],
                "imei": row[1],
                "more_imei": row[2]

            }
            # 进入充值卡页面
            self.account_center_page_refill_card.click_refill_card()

            #点击设备充值
            self.account_center_page_refill_card.click_equipment_refill()
            sleep(1)
            #取消
            self.account_center_page_refill_card.equipment_refill_cancel()
            self.account_center_page_refill_card.click_equipment_refill()

            # 输入设备个数验证
            information = self.account_center_page_refill_card.inport_equipment(data["more_imei"])
            self.assertEqual(information["import_count"], int(information["add_count"]), '输入的imei计数不一致')
            sleep(1)

            #获取添加结果中的信息
            list_failure_count = self.account_center_page_refill_card.list_failure_count()
            add_results = self.account_center_page_refill_card.equipment_refill_add_results_data()

            # 验证失败个数
            self.assertEqual(list_failure_count, add_results["fail_unmber"], "添加结果中的失败个数与行数不一致")

            #断言失败提示中的信息
            for s in range(list_failure_count):
                self.assertIsNotNone(add_results["imei"], "sim卡号为空")
                self.assertIsNotNone(add_results["cause"], "失败原因中存在空数据")

            #点击关闭
            self.account_center_page_refill_card.add_results_x()

            #验证成功个数
            list_count = self.account_center_page_refill_card.get_list_imei_number()
            self.assertEqual(list_count["number"], add_results["succeed_unmber"], "添加结果中的成功个数与列表中的不一致")

            #删除
            self.account_center_page_refill_card.delete_list_device()
            list_data = self.account_center_page_refill_card.get_list_imei_number()
            self.assertEqual(0, list_data["number"], "删除设备后，列表中imei不是0")

            # 重置
            information = self.account_center_page_refill_card.inport_equipment(data["more_imei"])
            self.account_center_page_refill_card.add_results_x()
            sleep(2)
            self.account_center_page_refill_card.click_reset_button()
            count = self.account_center_page_refill_card.get_list_imei_number()
            self.assertEqual(0, list_data["number"], "重置后，列表中imei不是0")




        csv_file.close()
        # 退出登录
        #self.account_center_page_navi_bar.usr_logout()
