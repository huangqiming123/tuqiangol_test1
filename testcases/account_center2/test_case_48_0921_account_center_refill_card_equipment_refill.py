import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_refill_card_page import AccountCenterRefillCardPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.account_center.search_sql import SearchSql
from pages.login.login_page import LoginPage


# 账户详情-充值卡--设备充值
# author:戴招利
class TestCase480921AccountCenterRefillCardEquipmentRefill(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_refill_card = AccountCenterRefillCardPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.connect_sql = ConnectSql()
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

    def test_equipment_refill_succeed(self):
        '''充值卡-设备充值成功'''

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

            }
            # 进入充值卡页面
            self.account_center_page_refill_card.click_refill_card()

            # 验证页面顶部我的账号
            my_account = self.account_center_page_refill_card.get_title_display_account()
            self.assertIn(self.account_center_page_refill_card.get_current_login_account(), my_account, "登录账号显示一致")


            # 验证顶部充值卡数量
            top_quantity = self.account_center_page_refill_card.get_refill_card_page_top_quantity()
            # 点击设备充值
            self.account_center_page_refill_card.click_equipment_refill()
            sleep(1)
            # 获取设备充值-数量
            equipment_number = self.account_center_page_refill_card.get_equipment_refill_number()
            self.assertEqual(top_quantity["year_number"], equipment_number["year_quantity"], "页面顶部与设备充值中显示的年卡不一致")
            self.assertEqual(top_quantity["lifetime_number"], equipment_number["lifetime_quantity"],
                             "页面顶部与设备充值中显示的终身卡不一致")

            # 输入设备个数验证
            information = self.account_center_page_refill_card.equipment_refill(data["type"], data["imei"])
            import_imei = information["import_imei_number"]
            self.assertEqual(import_imei["import_count"], int(import_imei["add_count"]), '输入的imei计数不一致')

            # 验证充值提示信息
            list_data = self.account_center_page_refill_card.get_list_imei_number()
            # 取消提示
            self.account_center_page_refill_card.equipment_refill_hint()
            # 获取充值提示数据
            prompt_data = self.account_center_page_refill_card.equipment_refill_hint_data()
            self.assertEqual(list_data["number"], int(prompt_data["prompt_refill_count"]), '充值提示中的台数跟列表添加数不一致')


            self.assertEqual(data["type"], prompt_data["time_limit"], '充值提示中，充值年限与设置的不一致')
            # 确定充值按钮
            self.account_center_page_refill_card.click_confirm_refill()
            sleep(3)
            # 验证操作提示
            # statu = self.account_center_page_refill_card.get_equipment_status()
            # self.assertEqual(self.assert_text2.account_center_refill_card_refill_succeed(),statu,"续费失败")

            # 获取当前账号id
            sql_data = self.search_sql.search_current_account_data(my_account)
            connect1 = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect1.cursor()
            reill_time_sql = self.search_sql.search_refill_record_reill_time_sql(sql_data[0], list_data["imei"])
            cur.execute(reill_time_sql)
            # 读取数据
            reill_time = cur.fetchall()
            print("读取", reill_time)
            sleep(2)
            print(reill_time[0][0])

            get_sql = self.search_sql.search_refill_record_expire_time_sql(str(reill_time[0][0]))
            cur.execute(get_sql)
            # 读取数据
            date = cur.fetchall()
            print("读取", date)
            sleep(3)
            # 设备充值后，最后时间
            update_time = self.account_center_page_refill_card.get_article_one_time()
            self.assertEqual(str(date[0][0]), update_time, "充值后设备到期时间显示不一致")

        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
