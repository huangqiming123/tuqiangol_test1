import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.user_center import UserCenterPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer

__author__ = ''

class TestCase202UserCenterModifyInfo2(unittest.TestCase):
    # 测试个人中心修改资料，包括特殊符号、异常
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.user_center_page = UserCenterPage(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.clear_cookies()
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.log_in_base.log_in()

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_info2(self):
        # 通过csv测试修改资料功能
        current_handle = self.driver.get_current_window_handle()
        self.account_center_page_navi_bar.click_account_center_button()
        self.base_page.change_windows_handle(current_handle)
        # 点击个人中心 - 修改资料
        self.user_center_page.click_user_center_button()
        self.user_center_page.click_modify_user_info()

        # 1.特殊字符
        special_char = "/\^<>!~%*"
        # 在客户名称、电话中输入特殊字符
        self.user_center_page.input_user_name_in_modify_info(special_char)
        self.user_center_page.input_user_phone_in_modify_info(special_char)
        # 点击保存
        self.user_center_page.click_ensure_button()

        # 验证
        # 获取主页上的用户名称和电话
        user_name = self.user_center_page.get_user_name_in_main_page()
        user_phone = self.user_center_page.get_user_phone_in_main_page()
        self.assertNotEqual(special_char, user_name)
        self.assertNotEqual(special_char, user_phone)

        # 2.验证客户名称必填
        self.user_center_page.input_user_name_in_modify_info('')
        self.user_center_page.input_user_phone_in_modify_info('')
        # 点击保存
        self.user_center_page.click_ensure_button()
        # 获取到客户名称的异常提醒
        user_name_exception = self.user_center_page.get_user_name_exception_in_modify_info_page()
        self.assertEqual(self.assert_text.user_name_not_null(), user_name_exception)

        # 3.长度限制
        long_char = 'fsaffsdafsadfvczxfsdsafdfasdfasdfsdfsdfasdfasdffffffffffffffffffffffarfwqefsadfasdfasdcfsaasdcascsdc'
        self.user_center_page.input_user_name_in_modify_info(long_char)
        # 点击保存
        self.user_center_page.click_ensure_button()
        # 获取到客户名称的异常提醒
        user_name_exception = self.user_center_page.get_user_name_exception_in_modify_info_page()
        self.assertEqual(self.assert_text.user_name_not_to_long(), user_name_exception)

        shot_char = '12'
        self.user_center_page.input_user_name_in_modify_info(shot_char)
        # 点击保存
        self.user_center_page.click_ensure_button()
        # 获取到客户名称的异常提醒
        user_name_exception = self.user_center_page.get_user_name_exception_in_modify_info_page()
        self.assertEqual(self.assert_text.user_name_not_to_shot(), user_name_exception)

        # 4.邮箱格式限制
        email_format = "fdsaffadsfasdf"
        self.user_center_page.input_user_email_in_modify_info(email_format)
        # 点击保存
        self.user_center_page.click_ensure_button()
        # 获取到客户邮箱的异常提示
        user_email_exception = self.user_center_page.get_user_email_exception_in_modify_info_page()
        self.assertEqual(self.assert_text.user_email_format_error(), user_email_exception)
