import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.command_management.command_management_page import CommandManagementPage
from pages.command_management.command_management_page_read_csv import CommandManagementPageReadCsv


class TestCase1105CommandManageIssuedCommand(unittest.TestCase):
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
        self.log_in_base.log_in_jimitest()

        # 登录之后点击控制台，然后点击指令管理
        self.command_management_page.click_control_after_click_command_management()
        sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1105_command_manage_issued_command(self):
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

        # 点击下发指令
        self.command_management_page.click_issued_commands()
        # 点击关闭
        self.command_management_page.click_close_issued_command()
        # 点击下发指令
        self.command_management_page.click_issued_commands()

        csv_file = self.command_management_page_read_csv.read_csv('issued_command_datas.csv')
        csv_data = csv.reader(csv_file)
        is_header = True
        data = []
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data.append(row[0])
        csv_file.close()
        # 添加不存在的设备
        no_data = data[0]
        self.command_management_page.add_dev_to_issued_command(no_data)
        get_command_name = self.command_management_page.get_command_name_fail()
        self.assertEqual(no_data, get_command_name)
        get_command_status = self.command_management_page.get_command_status_fail()
        self.assertEqual('失败', get_command_status)
        get_command_reason = self.command_management_page.get_command_reason_fail()
        self.assertEqual('不存在', get_command_reason)
        # 关闭提示
        self.command_management_page.close_issued_command_fail()

        # 不支持的设备
        no_data = data[1]
        self.command_management_page.add_dev_to_issued_command(no_data)
        get_command_name = self.command_management_page.get_command_name_fail()
        self.assertEqual(no_data, get_command_name)
        get_command_status = self.command_management_page.get_command_status_fail()
        self.assertEqual('失败', get_command_status)
        get_command_reason = self.command_management_page.get_command_reason_fail()
        self.assertEqual('不支持', get_command_reason)
        # 关闭提示
        self.command_management_page.close_issued_command_fail()

        # 重复
        no_data = data[2]
        self.command_management_page.add_dev_to_issued_command(no_data)
        self.command_management_page.add_dev_to_issued_command(no_data)
        get_command_name = self.command_management_page.get_command_name_fail()
        self.assertEqual(no_data, get_command_name)
        get_command_status = self.command_management_page.get_command_status_fail()
        self.assertEqual('失败', get_command_status)
        get_command_reason = self.command_management_page.get_command_reason_fail()
        self.assertEqual('重复', get_command_reason)
        # 关闭提示
        self.command_management_page.close_issued_command_fail()

        # 点击发送指令
        self.command_management_page.click_send_issued_command()
        text = self.command_management_page.get_text_after_ensure()
        self.assertEqual('操作成功', text)
