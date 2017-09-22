import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_refill_card_page import AccountCenterRefillCardPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.account_center.search_sql import SearchSql
from pages.login.login_page import LoginPage


# 账户详情-充值卡--充值记录数据搜索
# author:戴招利
class TestCase450919AccountCenterRefillCardRefillRecordSearch(unittest.TestCase):
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
        self.driver.set_window_max()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_refill_record_search(self):
        '''充值卡-充值记录--搜索'''
        csv_file = self.account_center_page_read_csv.read_csv('search_apply_record_data.csv')
        csv_data = csv.reader(csv_file)

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.driver.wait(1)
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入充值卡页面
        self.account_center_page_refill_card.click_refill_card()

        # 验证页面顶部我的账号
        my_account = self.account_center_page_refill_card.get_title_display_account()
        self.assertIn(self.account_center_page_refill_card.get_current_login_account(), my_account, "登录账号显示一致")

        for row in csv_data:
            data = {
                "refill_type": row[2],

            }

            self.account_center_page_refill_card.refill_card_page_iframe()
            # 点击充值记录
            self.account_center_page_refill_card.click_refill_record()
            # 搜索
            self.account_center_page_refill_card.refill_record_search_data(data["refill_type"])

            # 获取页面列表条数
            page_number = self.account_center_page_refill_card.get_refill_record_number()

            # 获取当前账号id
            sql_data = self.search_sql.search_current_account_data(my_account)

            connect1 = self.connect_sql.connect_tuqiang_sql()
            # 创建数据库游标
            cur = connect1.cursor()
            # 获取数据库条数
            get_sql = self.search_sql.search_refill_record_sql(sql_data[0], data["refill_type"])
            print(get_sql)
            cur.execute(get_sql)
            # 读取数据
            total_data = cur.fetchall()
            # 从数据tuple中获取最终查询记录统计条数
            total_list = []
            for range1 in total_data:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)
            print('本次查询数据库的条数为：%s' % total)

            # 获取数据库条数

            self.assertEqual(total, page_number, "转移记录中，平台与sql搜索出来的数据条数不一致")
            self.driver.default_frame()
        csv_file.close()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
