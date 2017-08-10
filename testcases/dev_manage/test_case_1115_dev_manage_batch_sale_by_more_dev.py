import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1115DevManageBatchSaleByMoreDev(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.assert_text = AssertText()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1115_dev_manage_batch_sale_by_more_dev(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        # 选择多个设备点击批量销售
        self.dev_manage_page.choose_one_dev_to_search()
        self.dev_manage_page.choose_more_dev_to_search()
        # 点击批量
        self.dev_manage_page.click_batch_sale_button()
        self.dev_manage_page.click_close_batch_sale_button()
        self.dev_manage_page.click_batch_sale_button()
        # 验证界面
        get_sale_title = self.dev_manage_page.get_sale_title_text_in_sale_dev()
        self.assertEqual(self.assert_text.batch_sale_text(), get_sale_title)

        # 获取统计的数量和列表中的总数
        get_dev_number = self.dev_manage_page.get_dev_number_in_sale_dev()
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(get_dev_number, str(get_dev_in_list_number))

        # 删除一个设备列表已添加的设备
        self.dev_manage_page.delete_one_dev_in_dev_list()
        get_dev_number = self.dev_manage_page.get_dev_number_in_sale_dev()
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(get_dev_number, str(get_dev_in_list_number))

        # 输入所选账号下存在的未添加到已选设备列表的设备和已添加到已选设备列表的设备以及不存在的设备，121201234567889
        self.dev_manage_page.add_imei_in_sale_dev_page('121201234567889')
        sleep(2)
        get_dev_number = self.dev_manage_page.get_dev_number_in_sale_dev()
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(get_dev_number, str(get_dev_in_list_number))

        # 删除一个设备列表已添加的设备后再添加该设备
        self.dev_manage_page.delete_one_devs_in_dev_list()
        get_dev_number = self.dev_manage_page.get_dev_number_in_sale_dev()
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(get_dev_number, str(get_dev_in_list_number))

        self.dev_manage_page.add_imei_in_sale_dev_page('121201234567889')
        sleep(2)
        get_dev_number = self.dev_manage_page.get_dev_number_in_sale_dev()
        get_dev_in_list_number = self.dev_manage_page.get_dev_in_list_number()
        self.assertEqual(get_dev_number, str(get_dev_in_list_number))
