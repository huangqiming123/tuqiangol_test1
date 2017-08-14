import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.search_sql import SearchSql
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 菜单栏 帮助 意见反馈

class TestCase37FeedbackTest(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.search_sql = SearchSql()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_feedback_test(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()

        # 点击招呼栏-业务日志
        self.account_center_page_operation_log.click_help_button()
        # 判断当前页面是否正确跳转至业务日志页面
        expect_url = self.base_url + "/userFeedback/toHelp"
        self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")

        # 选择追踪问题/轨迹问题/指令问题/功能建议/围栏问题/告警问题/我有疑问/其他
        self.account_center_page_navi_bar.switch_to_feedback_frame()
        get_total_numbers = self.account_center_page_navi_bar.get_total_numbers_feedback()

        for n in range(get_total_numbers):
            a = self.account_center_page_navi_bar.click_per_feedback_in_feedback_page(n)
            self.assertEqual('active', a)

        # 输入参数为空，点击保存
        self.account_center_page_navi_bar.click_ensuer_button_in_feedback_page()

        error_content = self.account_center_page_navi_bar.get_error_content_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_content(), error_content)
        error_contact = self.account_center_page_navi_bar.get_error_contact_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_contact(), error_contact)
        error_phone = self.account_center_page_navi_bar.get_error_phone_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_phone(), error_phone)

        # 输入描述内容，点击保存
        self.account_center_page_navi_bar.input_content_after_ensuer_in_feedback_page(
            'fasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdcfasfasfdasdfasdfasdfcasdfffcasdfcasdc')

        error_content = self.account_center_page_navi_bar.get_error_content_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_contents(), error_content)

        # 输入联系人，点击保存
        self.account_center_page_navi_bar.input_contact_after_ensuer_in_feedback_page(
            'fdfasfasdfasdfaswe fbfbvdfvasdcvxzcqwefdqwerfdsac asfewqrfqwedfqwed qwefdqwef qwefcasdfc wqerrcvsa v qerfv')
        error_contact = self.account_center_page_navi_bar.get_error_contact_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_contacts(), error_contact)

        # 输入联系电话，点击保存
        self.account_center_page_navi_bar.input_phone_after_ensuer_in_feedback_page('dfadsf')
        error_phone = self.account_center_page_navi_bar.get_error_phone_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_phones(), error_phone)

        self.account_center_page_navi_bar.input_phone_after_ensuer_in_feedback_page('123')
        error_phone = self.account_center_page_navi_bar.get_error_phone_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_phoness(), error_phone)

        self.account_center_page_navi_bar.input_phone_after_ensuer_in_feedback_page(
            '123123123123123123123123122312312123412412')
        error_phone = self.account_center_page_navi_bar.get_error_phone_in_feedback()
        self.assertEqual(self.assert_text.feedback_page_error_phoness(), error_phone)

        # 正确选择并输入各项参数，点击保存
        self.account_center_page_navi_bar.input_content_after_ensuer_in_feedback_page('这是反馈内容')
        self.account_center_page_navi_bar.input_contact_after_ensuer_in_feedback_page('这是联系人')
        self.account_center_page_navi_bar.input_phone_after_ensuer_in_feedback_page('110110110')
        self.account_center_page_navi_bar.click_ensuer_button_in_feedback_page()
        text = self.account_center_page_navi_bar.get_feedback_text_after_click_ensuer()
        self.assertEqual(self.assert_text.feedback_page_ensuer_succeed_text(), text)
