import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage


class TestCase48IssuedWorkTypeManagementOperation(unittest.TestCase):
    """ 下发工作模式管理的操作 """
    # author:邓肖斌

    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    command_management_page = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver(choose='firefox')
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.assert_text = AssertText()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_issued_work_type_management_operation(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = self.assert_text.command_manager_page_command_type()
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())
        # 点击下发工作模式管理
        self.command_management_page.click_lift_list('issued_work_type_management')
        # 断言
        expect_title_text_click_issued_work_type = self.assert_text.command_manager_page_issued_work_type()
        self.assertEqual(expect_title_text_click_issued_work_type,
                         self.command_management_page.actual_text_click_look_equipment())
        # 点击查看
        self.command_management_page.click_look_issued_work_type()
        # 断言
        expect_title_text_after_click_look_issued = self.assert_text.command_manager_page_issued_work_look_type()
        self.assertEqual(expect_title_text_after_click_look_issued,
                         self.command_management_page.actual_text_after_click_look_issued())
        # 点击关闭查看
        self.command_management_page.click_close_look_issued_work_type()
        # 断言
        self.assertEqual(expect_title_text_click_issued_work_type,
                         self.command_management_page.actual_text_click_look_equipment())
