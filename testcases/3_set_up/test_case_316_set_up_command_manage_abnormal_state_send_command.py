import unittest
from time import sleep
import csv
from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv


class TestCase56CommandManagerAbnormalStateSendCommand(unittest.TestCase):
    # 测试 设置 - 指令管理 - 模板管理 - 异常状态imei下发指令
    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver(choose='firefox')
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
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_command_manage_abnormal_state_send_command(self):
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
        expect_title_text_after_click_work_type_template_management = \
            self.assert_text.command_manager_page_work_type_template_management()
        self.assertEqual(expect_title_text_after_click_work_type_template_management,
                         self.command_management_page.actual_title_text_after_click_work_type_template_management())

        # 点击下发指令
        self.command_management_page.click_send_command()

        # 读取数据
        csv_file = self.command_management_page_read_csv.read_csv("send_command_with_abnormal_dev.csv")
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            abnormal_state_data = {
                "state": row[0]
            }

            # 下发指令并获取文本
            send_command_text = self.command_management_page. \
                get_text_after_send_command_with_abnormal_dev(abnormal_state_data["state"])

            # 断言
            self.assertEqual(send_command_text, self.assert_text.
                             text_with_abnormal_dev_send_command(abnormal_state_data["state"]))

            # 关闭提示框
            self.command_management_page.close_send_command_fail_frame()
        csv_file.close()
