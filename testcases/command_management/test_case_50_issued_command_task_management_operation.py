import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage


class TestCase50IssuedCommandTaskManagementOperation(unittest.TestCase):
    """ 发工作指令任务的操作 """
    # author:邓肖斌

    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    command_management_page = None
    base_paging_function = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
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

    def test_case_issued_command_task_management_operation(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = self.assert_text.command_manager_page_command_type()
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击下发任务指令管理
        self.command_management_page.click_lift_list('issued_command_task_management')
        # 断言
        expect_title_text_after_click_issued_command_task_management = \
            self.assert_text.command_manager_page_issued_command_task()
        self.assertEqual(expect_title_text_after_click_issued_command_task_management,
                         self.command_management_page.actual_text_after_click_issued_command_task())

        # 点击查看设备
        self.command_management_page.click_look_equipment_in_issued_command_task()

        # 断言
        expect_text_after_click_look_equipment = self.assert_text.command_manager_page_issued_command_manager()
        self.assertEqual(expect_text_after_click_look_equipment,
                         self.command_management_page.actual_text_after_click_look_equipment())
