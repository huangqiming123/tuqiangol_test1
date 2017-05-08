import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base import LogInBase
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage
from pages.set_up.set_up_page import SetUpPage
from pages.set_up.set_up_page_read_csv import SetUpPageReadCsv


class TeseCase119SetUpEquipmentTypeListOperation(unittest.TestCase):
    '''
    用例第119条，设备型号设置页面操作
    author:zhangAo
    '''
    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    set_up_page = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.set_up_page = SetUpPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.set_up_page_read_csv = SetUpPageReadCsv()

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_base.log_in()

        # 登录之后点击控制台，然后点击设置
        self.set_up_page.click_control_after_click_set_up()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_119_set_up_equipment_type_list_operation(self):
        # 断言url
        expect_url_after_click_set_up = self.base_url + '/setup/toSetUp'
        self.assertEqual(expect_url_after_click_set_up, self.set_up_page.check_url_after_click_set_up(), 'url地址和实际不一致')

        # 断言左侧导航标题文本
        expect_title_text_after_click_set_up = '我的设置'
        self.assertEqual(expect_title_text_after_click_set_up, self.set_up_page.check_title_text_after_click_set_up(),
                         '左侧导航标题和实际不一致')

        # 点击设备型号设置
        self.set_up_page.click_set_up_page_lift_list('set_up_equipment_type')
        sleep(2)

        # 断言
        expect_text_after_click_set_up_equipment_type = '设备型号设置'
        self.assertEqual(expect_text_after_click_set_up_equipment_type,
                         self.set_up_page.check_text_after_click_set_up_equipment())

        csv_file = self.set_up_page_read_csv.read_csv('set_up_equipment_type_data.csv')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            equipment_type_data = {
                'new_type': row[0]
            }
            # 点击设置型号
            self.set_up_page.set_up_equipment_type_click_set_type()
            sleep(2)
            # 断言
            expect_text_after_click_set_type = '设置型号'
            self.assertEqual(expect_text_after_click_set_type, self.set_up_page.check_text_after_click_set_type())
            # 设置型号
            self.set_up_page.set_up_equipment_type(equipment_type_data)
            sleep(2)
        csv_file.close()

        # 点击设置型号
        self.set_up_page.set_up_equipment_type_click_set_type()
        sleep(2)
        # 断言
        expect_text_after_click_set_type = '设置型号'
        self.assertEqual(expect_text_after_click_set_type, self.set_up_page.check_text_after_click_set_type())
        # 点击×
        self.set_up_page.set_up_equipment_type_close_set_new_type()
        # 断言关闭成功
        expect_text_after_click_set_up_equipment_type = '设备型号设置'
        self.assertEqual(expect_text_after_click_set_up_equipment_type,
                         self.set_up_page.check_text_after_click_set_up_equipment())

        # 点击设置型号
        self.set_up_page.set_up_equipment_type_click_set_type()
        sleep(2)
        # 断言
        expect_text_after_click_set_type = '设置型号'
        self.assertEqual(expect_text_after_click_set_type, self.set_up_page.check_text_after_click_set_type())
        # 点击取消设置新型号
        self.set_up_page.set_up_equipment_type_cancel_set_new_type()
        # 断言取消成功
        expect_text_after_click_set_up_equipment_type = '设备型号设置'
        self.assertEqual(expect_text_after_click_set_up_equipment_type,
                         self.set_up_page.check_text_after_click_set_up_equipment())
