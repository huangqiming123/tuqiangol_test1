import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv
from pages.login.login_page import LoginPage


class TestCase124WorkTypeTemplateManagementCreatTemplate(unittest.TestCase):
    '''
    用例第123条，创建模板
    author:zhangAo
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
        self.log_in_page = LoginPage(self.driver, self.base_url)
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

    def test_case_124_work_type_template_management_creat_template(self):
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

        # 点击创建模板
        self.command_management_page.click_create_template()
        # 断言打开的创建模板的title文本
        expect_title_text_after_click_create_template = '新建自定义指令'
        self.assertEqual(expect_title_text_after_click_create_template,
                         self.command_management_page.actual_title_text_after_click_create_template())
        # 关闭创建模板
        self.command_management_page.click_close_create_template()
        # 断言是否关闭成功
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击创建模板
        self.command_management_page.click_create_template()
        # 断言打开的创建模板的title文本
        expect_title_text_after_click_create_template = '新建自定义指令'
        self.assertEqual(expect_title_text_after_click_create_template,
                         self.command_management_page.actual_title_text_after_click_create_template())
        # 取消创建模板
        self.command_management_page.click_cancel_create_template()
        # 断言是否关闭成功
        expect_title_text_after_click_work_type_template_management = '工作模式模板管理'
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 输入参数
        csv_file = self.command_management_page_read_csv.read_csv('work_template_time_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            work_template_time_data = {
                'name': row[0],
                'type': row[1],
                'day': row[2],
                'circulation': row[3],
                'circulation_day': row[4],
                'week': row[5],
                'circulation1': row[6],
                'circulation_day1': row[7],
                'jiange': row[8],
                'circulation2': row[9],
                'circulation_day2': row[10],
            }
            # 点击创建模板
            self.command_management_page.click_create_template()
            # 断言打开的创建模板的title文本
            expect_title_text_after_click_create_template = '新建自定义指令'
            self.assertEqual(expect_title_text_after_click_create_template,
                             self.command_management_page.actual_title_text_after_click_create_template())
            sleep(3)
            self.command_management_page.add_create_template_data(work_template_time_data)
            # 点击保存
            self.command_management_page.create_template_click_ensure()
            sleep(2)
            # 点击删除
            self.command_management_page.delete_add_new_template()
        csv_file.close()
