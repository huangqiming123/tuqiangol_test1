import unittest

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1104DevManageSelectIssuedCommand(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1104_dev_manage_select_issued_command(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        imei_in_list = self.dev_manage_page.get_imei_in_list()
        dev_type_in_list = self.dev_manage_page.get_dev_type_in_list()

        # 选中一个列表中的设备
        self.dev_manage_page.click_dev_in_list()
        # 判断是否选中
        input_value = self.dev_manage_page.check_input_value()
        self.assertEqual(True, input_value)

        # 点击选中发送指令
        self.dev_manage_page.click_select_send_command()
        # 点击关闭
        self.dev_manage_page.click_close_select_send_command()

        # 点击选中发送指令
        self.dev_manage_page.click_select_send_command()
        # 点击取消
        self.dev_manage_page.click_cancel_select_send_command()

        # 点击选中发送指令
        self.dev_manage_page.click_select_send_command()

        # 判断数量
        get_dev_number = self.dev_manage_page.get_dev_number_in_send_command()
        self.assertEqual(1, get_dev_number)

        get_dev_count = self.dev_manage_page.get_dev_count_number_in_send_command()
        self.assertEqual(str(get_dev_number), get_dev_count)

        # 验证设备信息
        get_imei = self.dev_manage_page.get_imei_in_send_command()
        self.assertEqual(imei_in_list, get_imei)

        get_dev_type = self.dev_manage_page.get_dev_type_in_send_command()
        self.assertEqual(dev_type_in_list, get_dev_type)

        get_dev_user = self.dev_manage_page.get_dev_user_in_send_command()

        connect = self.connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_account_sql = "select o.account from equipment_mostly e inner join user_info o on e.userId = o.userId where e.imei = '%s';" % imei_in_list
        cursor.execute(get_account_sql)
        account_data = cursor.fetchall()
        account = account_data[0][0]
        cursor.close()
        connect.close()

        self.assertEqual(get_dev_user, account)

        # 点击删除设备
        self.dev_manage_page.click_detele_dev_in_send_command()

        self.dev_manage_page.click_send_command_in_send_command()
        get_text = self.dev_manage_page.get_fail_text()
        self.assertEqual('没有可发送指令的设备', get_text)
