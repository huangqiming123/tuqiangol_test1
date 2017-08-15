import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.dev_manage.dev_manage_page_read_csv import DevManagePageReadCsv
from pages.dev_manage.dev_manage_pages import DevManagePages


class TestCase100DevManageSearchDevAfterIssuedWorkType(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.dev_manage_page_read_csv = DevManagePageReadCsv()
        self.assert_text = AssertText()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_search_dev_after_issued_work_type(self):

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in_jimitest()
        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()
        # 搜索 包含下级 加 平台即将到期
        self.dev_manage_page.search_platform_expire_and_contain_next_in_dev_page()

        # 获取查询的页数
        page_number = self.dev_manage_page.get_total_page_number_in_dev_manager()
        if page_number == 0:
            # 断言暂无数据
            text = self.dev_manage_page.get_no_data_text_after_search_in_dev_page()
            self.assertIn(self.assert_text.account_center_page_no_data_text(), text)
            # 点击本次查询全部发送指令
            self.dev_manage_page.click_batch_issued_work_type_button()
            # 断言数据为零
            self.assertEqual('0', self.dev_manage_page.get_total_number_in_issued_work_type_page())
            self.assertEqual(0, self.dev_manage_page.get_total_number_list_in_issued_work_type_page())

        elif page_number == 1:
            # 查询本页的条数
            number = self.dev_manage_page.get_total_number_per_page_in_dev_manager()
            # 获取到查询到的所有imei
            search_imei = []
            for n in range(number):
                imei = self.dev_manage_page.get_per_imei_in_dev_page(n)
                search_imei.append(imei)

            # 点击本次查询全部发送指令
            self.dev_manage_page.click_batch_issued_work_type_button()
            # 获取全部下发指令页面 统计的总数和列表中设备的总数
            check_number = self.dev_manage_page.get_total_number_in_issued_work_type_page()
            check_list_number = self.dev_manage_page.get_total_number_list_in_issued_work_type_page()
            a = (number - int(check_number)) >= 0
            self.assertEqual(True, a)
            b = (number - check_list_number) >= 0
            self.assertEqual(True, b)

            # 获取下发指令页面的所有imei
            issued_imei = []
            for m in range(check_list_number):
                imei = self.dev_manage_page.get_per_imei_in_issued_work_type_page(m)
                issued_imei.append(imei)
            # 断言下发指令页面的设备都在查询的里面
            for dev in issued_imei:
                self.assertIn(dev, search_imei)

        else:
            search_imei = []
            for x in range(page_number):
                self.dev_manage_page.click_per_page(x + 1)
                # 查询本页的条数
                number = self.dev_manage_page.get_total_number_per_page_in_dev_manager()
                # 获取到查询到的所有imei
                for y in range(number):
                    imei = self.dev_manage_page.get_per_imei_in_dev_page(y)
                    search_imei.append(imei)

            # 点击本次查询全部发送指令
            self.dev_manage_page.click_batch_issued_work_type_button()
            sleep(5)
            # 获取全部下发指令页面 统计的总数和列表中设备的总数
            check_number = self.dev_manage_page.get_total_number_in_issued_work_type_page()
            check_list_number = self.dev_manage_page.get_total_number_list_in_issued_work_type_page()
            a = (len(search_imei) - int(check_number)) >= 0
            self.assertEqual(True, a)
            b = (len(search_imei) - check_list_number) >= 0
            self.assertEqual(True, b)

            # 获取下发指令页面的所有imei
            issued_imei = []
            for m in range(check_list_number):
                imei = self.dev_manage_page.get_per_imei_in_issued_work_type_page(m)
                issued_imei.append(imei)
            # 断言下发指令页面的设备都在查询的里面
            for dev in issued_imei:
                self.assertIn(dev, search_imei)
