import unittest
from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase1102DevManageBatchUploadPictures(unittest.TestCase):
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
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_1102_dev_manage_batch_upload_pictures(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.base_page.click_chinese_button()
        # 登录
        self.log_in_base.log_in()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 点击批量
        self.dev_manage_page.click_batch_upload_pictures_button()
        self.dev_manage_page.click_close_batch_upload_pictures_button()

        self.dev_manage_page.click_batch_upload_pictures_button()
        self.dev_manage_page.click_cancel_batch_upload_pictures_button()

        self.dev_manage_page.click_batch_upload_pictures_button()
        self.dev_manage_page.click_ensure_upload()
