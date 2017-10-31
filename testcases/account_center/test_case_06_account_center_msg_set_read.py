import unittest

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_msg_center_page import AccountCenterMsgCenterPage

from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage

# 账户中心-消息中心-设置消息为已读
# author:孙燕妮

class TestCase06AccountCenterMsgSetRead(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_msg_center = AccountCenterMsgCenterPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_msg_set_read(self):
        '''通过csv测试消息中心-设置消息为已读功能'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入消息中心
        self.account_center_page_msg_center.enter_msg_center()
        self.driver.wait(8)
        # 进入iframe
        self.account_center_page_msg_center.message_center_iframe()
        # 获取消息中心title
        msg_center_title = self.account_center_page_msg_center.get_msg_center_title()

        # 验证消息中心title是否正确显示
        self.assertIn(self.assert_text.account_center_page_message_center_text(), msg_center_title, "消息中心title有误!")
        # 退出iframe
        self.driver.default_frame()

        # 获取左侧栏目-消息中心-x条未读
        unread_msg_num = int(self.account_center_page_msg_center.get_unread_msg_num())

        if unread_msg_num > 0:
            self.account_center_page_msg_center.message_center_iframe()
            # 设置搜索条件-消息状态为“未读”，搜索出结果，统计当前未读消息总数
            self.account_center_page_msg_center.set_search_status_unread()
            self.driver.wait(4)

            # 判断消息中心左侧栏目的未读消息与搜索结果的未读消息数量是否一致
            count_unread_msg_num = self.account_center_page_msg_center.get_total_unread_logs_num()
            self.assertEqual(unread_msg_num, count_unread_msg_num, "消息中心左侧栏目的未读消息与搜索结果的未读消息数量不一致")

            # 根据未读消息总数，将所有未读消息设为已读
            if 0 < count_unread_msg_num <= 10:
                # 当前页全选
                self.account_center_page_msg_center.select_current_page_all_msg()

                # 获取当前页所有消息的复选框
                select_msg_list = self.account_center_page_msg_center.get_current_page_all_msg_checkbox()
                print(select_msg_list)
                msg_list_len = len(select_msg_list)
                print(msg_list_len)
                # 将选中的标为已读
                self.account_center_page_msg_center.set_current_page_status_read()

                # 验证操作状态是否成功
                self.driver.wait()
                status_text = self.account_center_page_msg_center.get_status_text()

                self.assertIn(self.assert_text.account_center_page_operation_done(), status_text, "操作失败")
                self.driver.wait()

                # 设置搜索条件-消息状态为“未读”，判断未读消息列表是否为空
                self.account_center_page_msg_center.set_search_status_unread()
                no_msg_text = self.account_center_page_msg_center.get_no_msg_text()
                self.driver.wait()
                self.assertIn(self.assert_text.account_center_page_no_data_text(), no_msg_text, "未读消息列表未清空")



            else:

                # 将所有消息全部标为已读
                self.account_center_page_msg_center.set_all_msg_status_read()

                # 验证操作状态是否成功
                self.driver.wait(1)

                status_text = self.account_center_page_msg_center.get_status_text()

                self.assertIn(self.assert_text.account_center_page_operation_done(), status_text, "操作失败")

                # 设置搜索条件-消息状态为“未读”，判断未读消息列表是否为空
                self.account_center_page_msg_center.set_search_status_unread()
                no_msg_text = self.account_center_page_msg_center.get_no_msg_text()
                self.assertIn(self.assert_text.account_center_page_no_data_text(), no_msg_text, "未读消息列表未清空")
                # 退出登录
                self.account_center_page_navi_bar.usr_logout()
        else:
            print("当前未读消息共：" + str(unread_msg_num) + "条!")

        self.driver.default_frame()
        # 退出登录
        # self.account_center_page_navi_bar.usr_logout()
