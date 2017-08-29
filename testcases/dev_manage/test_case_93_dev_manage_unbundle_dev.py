import unittest
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase93DevManageUnbundleDev(unittest.TestCase):
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

    def test_case_dev_manage_unbundle_dev(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in_jimitest()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 搜索绑定的设备
        self.dev_manage_page.search_bundle_dev()
        #  获取第一个设备的imei
        imei_in_list = self.dev_manage_page.get_imei_in_list()

        # 点击解绑
        self.dev_manage_page.click_unbundle_dev()

        imei_in_list_again = self.dev_manage_page.get_imei_in_list()

        self.assertNotEqual(imei_in_list, imei_in_list_again, '解绑失败')
