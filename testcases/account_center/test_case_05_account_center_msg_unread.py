import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_change_page import AccountCenterChangePage
from pages.account_center.account_center_msg_center_page import AccountCenterMsgCenterPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-消息中心-未读消息验证
# author:孙燕妮

class TestCase020AccountCenterMsgUnread(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_msg_center = AccountCenterMsgCenterPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.account_center_change_page = AccountCenterChangePage(self.driver, self.base_page)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_msg_unread(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入消息中心
        self.account_center_page_msg_center.enter_msg_center()
        self.driver.wait(7)
        # 进入iframe
        # self.account_center_page_msg_center.message_center_iframe()

        # 获取消息中心title
        msg_center_title = self.account_center_page_msg_center.get_msg_center_title()
        # 验证消息中心title是否正确显示
        self.assertIn(self.assert_text.account_center_page_message_center_text(), msg_center_title, "消息中心title有误!")
        #退出iframe
        # self.driver.default_frame()

        # 获取左侧栏目-消息中心-x条未读
        unread_msg_num = int(self.account_center_page_msg_center.get_unread_msg_num())
        print(unread_msg_num)
        if unread_msg_num > 0:
            # 设置搜索条件-消息状态为“未读”，搜索出结果，统计结果列表中的未读消息共几条
            self.account_center_page_msg_center.set_search_status_unread()
            self.driver.wait(4)
            count_unread_msg_num = self.account_center_page_msg_center.get_total_unread_logs_num()
            # 判断消息中心左侧栏目的未读消息与搜索结果的未读消息数量是否一致
            self.assertEqual(unread_msg_num, count_unread_msg_num, "消息中心左侧栏目的未读消息与搜索结果的未读消息数量不一致")
            # self.driver.default_frame()
            # 退出登录
            # self.account_center_page_navi_bar.usr_logout()
        else:
            print("当前未读消息共：" + str(unread_msg_num) + "条!")
            # 退出登录
            # self.account_center_page_navi_bar.usr_logout()
