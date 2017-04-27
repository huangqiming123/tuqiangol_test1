import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage
from pages.set_up.set_up_page import SetUpPage


class TestCase121BlackCarAddressLibraryAddBlackCarAddress(unittest.TestCase):
    """
    用例第121条，黑车地址库-创建黑车地址
    author：zhangAo
    """

    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    set_up_page = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.set_up_page = SetUpPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver,self.base_url)

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

    def test_case_121_black_car_address_library_add_black_car_address(self):
        # 断言url
        expect_url_after_click_set_up = self.base_url + '/setup/toSetUp'
        self.assertEqual(expect_url_after_click_set_up, self.set_up_page.check_url_after_click_set_up(), 'url地址和实际不一致')

        # 点击黑车地址库
        self.set_up_page.click_set_up_page_lift_list('black_car_adress_library')
        sleep(2)

        # 断言右侧页面左上角的文本
        expect_text_after_click_black_car_address='黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,self.set_up_page.check_text_after_click_black_car_address())

        # 点击创建黑车地址库
        self.set_up_page.click_add_black_car_address()

        # 断言打开的地图title的文本
        expect_title_text_after_click_add_black_car_address='创建黑车地址'
        self.assertEqual(expect_title_text_after_click_add_black_car_address,self.set_up_page.check_title_text_after_click_add_black_address())

        # 点击关闭创建黑车地址库
        self.set_up_page.click_close_add_black_car_address()

        # 断言是否关闭成功
        expect_text_after_click_black_car_address='黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,self.set_up_page.check_text_after_click_black_car_address())