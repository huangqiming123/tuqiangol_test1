'''import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv


class TestCase317SetUpCommandManageExportCommandLog(unittest.TestCase):
    # 测试 设置 - 指令管理 - 下发指令管理导出功能
    def setUp(self):
        self.driver = AutomateDriver(choose='firefox')
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
        self.command_management_page_read_csv = CommandManagementPageReadCsv()
        self.connect_sql = ConnectSql()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.assert_text = AssertText()
        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.current_account = self.log_in_base.get_log_in_account()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_317_set_up_command_manage_export_command_log(self):
        # 断言url
        expect_url_after_click_command_management = self.base_url + '/custom/toTemplate'
        self.assertEqual(expect_url_after_click_command_management,
                         self.command_management_page.actual_url_click_command_management())
        # 断言左侧列表的title文本
        expect_title_text_after_click_command_management = self.assert_text.command_manager_page_command_type()
        self.assertEqual(expect_title_text_after_click_command_management,
                         self.command_management_page.actual_title_text_after_click_command_management())

        # 点击下发指令管理
        self.command_management_page.click_lift_list('issued_command_management')
        # 断言
        expect_title_text = self.assert_text.command_manager_page_issued_command_manager()
        self.assertEqual(expect_title_text, self.command_management_page.actual_text_after_click_look_equipment())

        # 点击搜索
        self.command_management_page.click_search_button_in_command_log_page()

        # 获取查询结果总共有多少页
        total_page = self.command_management_page.search_total_page_issued_command_management()
        print(total_page)

        web_data = []
        if total_page == 0:
            pass
        elif total_page == 1:
            # 获取每页有多少条
            page_number = self.command_management_page.get_per_page_number_in_command_log_page()
            for n in range(page_number):
                web_data.append(self.command_management_page.get_per_line_data_in_command_log_page(n))

        else:
            for m in range(total_page - 1):
                self.command_management_page.click_per_page_number(m)
                page_number = self.command_management_page.get_per_page_number_in_command_log_page()
                for n in range(page_number):
                    web_data.append(self.command_management_page.get_per_line_data_in_command_log_page(n))
        print(web_data)
'''
