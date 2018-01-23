import csv
import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.help.help_page import HelpPage
from pages.message_center.message_center_page import MessageCenterPage

__author__ = ''

class TestCase801MessageCenterSearchMassage(unittest.TestCase):
    ###############################################################
    # # 测试 消息中心 消息搜索
    ###############################################################
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.message_center_page = MessageCenterPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.help_page = HelpPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.clear_cookies()
        self.base_page.open_page()
        self.log_in_base.log_in()

    def tearDown(self):
        self.driver.close_window()
        self.driver.quit_browser()

    def test_case_801_message_center_search_massage(self):
        user_account = self.log_in_base.get_log_in_account()
        # 点击消息中心
        self.message_center_page.click_message_center_button()

        csv_file = self.account_center_page_read_csv.read_csv('message_center_search.csv')
        csv_data = csv.reader(csv_file)
        i = 1
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            search_data = {
                'imei': row[0],
                'massage_type': row[1],
                'is_read': row[2]
            }
            print(search_data)
            self.message_center_page.add_data_search_message_data(search_data)
            # 获取当前用户和下级用户的所有用户id
            all_user_id = self.help_page.get_all_user_id(user_account)
            # 获取数据库查询的条数
            sql_total = self.message_center_page.get_sql_total_search_center_massage(search_data, all_user_id)
            # 获取页面上的数据条数
            web_total = self.message_center_page.get_web_total_search_center_massage()
            print('第%s次查询的数据库总数：%s' % (i, sql_total))
            print('第%s次查询的页面总数：%s' % (i, web_total))
            i += 1
            self.assertEqual(sql_total, web_total)

        csv_file.close()
