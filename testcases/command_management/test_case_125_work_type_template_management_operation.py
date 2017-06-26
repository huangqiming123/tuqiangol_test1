import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv


class TestCase125WorkTypeTemplateManagementOperation(unittest.TestCase):
    '''
    用例第124条，工作模板的操作：修改、删除、下发指令
    author：zhangAo
    '''
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

    def test_case_125_work_type_template_management_operation(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = '指令类型'
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击工作模式模板管理
        self.command_management_page.click_lift_list('work_type_template_management')
        # 断言右侧页面的title文本
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击修改
        self.command_management_page.work_template_operation_revise()
        # 断言
        expect_title_text_after_click_create_template = '新建自定义指令'
        self.assertEqual(expect_title_text_after_click_create_template,
                         self.command_management_page.actual_title_text_after_click_create_template())
        # 取消修改模板
        self.command_management_page.click_cancel_create_template()
        # 断言是否关闭成功
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击修改
        self.command_management_page.work_template_operation_revise()
        # 断言
        expect_title_text_after_click_create_template = '新建自定义指令'
        self.assertEqual(expect_title_text_after_click_create_template,
                         self.command_management_page.actual_title_text_after_click_create_template())
        # 关闭修改模板
        self.command_management_page.click_close_create_template()
        # 断言是否关闭成功
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击修改
        self.command_management_page.work_template_operation_revise()
        # 断言
        expect_title_text_after_click_create_template = '新建自定义指令'
        self.assertEqual(expect_title_text_after_click_create_template,
                         self.command_management_page.actual_title_text_after_click_create_template())
        # 点击保存
        self.command_management_page.create_template_click_ensure()
        # 断言
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击删除
        self.command_management_page.work_template_operation_delete()
        # 断言
        expect_text_after_click_delete = '确定'
        self.assertEqual(expect_text_after_click_delete, self.command_management_page.actual_text_after_click_delete())
        # 点击取消
        self.command_management_page.cancel_work_template_operation_delete()
        # 断言
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击删除
        self.command_management_page.work_template_operation_delete()
        # 断言
        expect_text_after_click_delete = '确定'
        self.assertEqual(expect_text_after_click_delete, self.command_management_page.actual_text_after_click_delete())
        # 点击关闭
        self.command_management_page.close_work_template_operation_delete()
        # 断言
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())
