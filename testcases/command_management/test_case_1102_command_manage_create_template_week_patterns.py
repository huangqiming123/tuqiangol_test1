import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv


class TestCase1102CommandManageCreateTemplateWeekPatterns(unittest.TestCase):
    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    command_management_page = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.command_management_page_read_csv = CommandManagementPageReadCsv()
        self.assert_text = AssertText()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1102_command_manage_create_template_week_patterns(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = self.assert_text.command_manager_page_command_type()
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击工作模式模板管理
        self.command_management_page.click_lift_list('work_type_template_management')
        # 断言右侧页面的title文本
        expect_title_text_after_click_work_type_template_management = self.assert_text.command_manager_page_work_type_template_management()
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击创建模板
        self.command_management_page.click_create_template()
        # 断言打开的创建模板的title文本
        expect_title_text_after_click_create_template = self.assert_text.command_manager_page_new_command_text()
        self.assertEqual(expect_title_text_after_click_create_template,
                         self.command_management_page.actual_title_text_after_click_create_template())

        # 点击星期模式
        self.command_management_page.click_week_patterns()

        # 验证创建模板的提示语
        template_name = self.command_management_page.get_create_template_name_text()
        self.assertEqual(self.assert_text.command_manager_page_template_name(), template_name)

        # 验证定时模式下输入框的规则
        # 模板名称 1 为空
        self.command_management_page.add_template_name_in_create_template('')
        self.command_management_page.click_ensure()
        get_name_text_fail = self.command_management_page.get_text_after_click_ensure()
        self.assertEqual(self.assert_text.command_manager_page_not_null(), get_name_text_fail)

        # 验证上报时间 星期
        self.command_management_page.click_ensure()
        get_text_fail_report_time_week = self.command_management_page.get_text_fail_report_time_week()
        self.assertEqual(self.assert_text.command_manager_page_not_null(), get_text_fail_report_time_week)
        # 上报时间
        self.command_management_page.click_ensure()
        get_text_fail_report_time = self.command_management_page.get_text_fail_report_time()
        self.assertEqual(self.assert_text.command_manager_page_not_null(), get_text_fail_report_time)

        # 限时周期
        # 为空
        self.command_management_page.click_ensure()
        get_text_fail_limit_cycle = self.command_management_page.get_text_fail_limit_cycle()
        self.assertEqual(self.assert_text.command_manager_page_not_null(), get_text_fail_limit_cycle)

        # 大于15
        self.command_management_page.add_limit_cycle_in_create_template('16')
        self.command_management_page.click_ensure()
        get_text_fail_limit_cycle = self.command_management_page.get_text_fail_limit_cycle()
        self.assertEqual(self.assert_text.command_manager_page_must_than_15(), get_text_fail_limit_cycle)

        # 非正整数
        self.command_management_page.add_limit_cycle_in_create_template('刷刷刷')
        self.command_management_page.click_ensure()
        get_text_fail_limit_cycle = self.command_management_page.get_text_fail_limit_cycle()
        self.assertEqual(self.assert_text.command_manager_page_must_be_integer(), get_text_fail_limit_cycle)

        # 非正整数 大于15
        self.command_management_page.add_limit_cycle_in_create_template('2323刷刷刷')
        self.command_management_page.click_ensure()
        get_text_fail_limit_cycle = self.command_management_page.get_text_fail_limit_cycle()
        get_texts_fail_limit_cycle = self.command_management_page.get_texts_fail_limit_cycle()
        self.assertEqual(
            self.assert_text.command_manager_page_must_than_15() + self.assert_text.command_manager_page_must_be_integer(),
            get_text_fail_limit_cycle + get_texts_fail_limit_cycle)

        # 点击添加
        self.command_management_page.click_add_user_defined_template()
        # 验证是否添加成功
        number = self.command_management_page.get_total_number_template()
        self.assertEqual(2, number)

        # 点击删除
        self.command_management_page.click_delete_user_defined_template()
        number = self.command_management_page.get_total_number_template()
        self.assertEqual(1, number)
