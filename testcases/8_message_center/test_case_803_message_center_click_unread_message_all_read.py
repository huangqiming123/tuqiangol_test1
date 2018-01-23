import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.help.help_page import HelpPage
from pages.message_center.message_center_page import MessageCenterPage

__author__ = ''

class TestCase803MessageCenterClickUnreadMessageAllRead(unittest.TestCase):
    ###############################################################
    # # 测试 消息中心 全部标记为已读
    ###############################################################
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.message_center_page = MessageCenterPage(self.driver, self.base_url)
        self.help_page = HelpPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.clear_cookies()
        self.base_page.open_page()
        self.log_in_base.log_in()

    def tearDown(self):
        self.driver.close_window()
        self.driver.quit_browser()

    def test_case_803_message_center_click_unread_message_all_read(self):
        # 获取未读消息的总数
        unread_message_total_number = self.message_center_page.get_unread_message_total_number()
        print(unread_message_total_number)
        # 点击消息中心
        self.message_center_page.click_message_center_button()
        sleep(10)

        # 点击全部标记为已读
        self.message_center_page.click_set_unread_message_all_read()
        sleep(10)
        unread_message_total_number_01 = self.message_center_page.get_unread_message_total_number()
        print(unread_message_total_number_01)
        self.assertEqual('0', unread_message_total_number_01)

        # 搜索未读消息数量
        data = {
            'imei': '',
            'massage_type': '',
            'is_read': '未读'
        }
        self.message_center_page.add_data_search_message_data(data)
        # 获取搜索出来的未读消息的总数
        search_unread_message_total_number = self.message_center_page.get_web_total_search_center_massage()
        self.assertEqual(0, search_unread_message_total_number)
