import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.set_up.set_up_page import SetUpPage


class TestCase116SetUpLandmarkAddLandmark(unittest.TestCase):
    """
    用例第116条，地标设置—创建地标
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

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_page.account_input('test_007')
        self.log_in_page.password_input('jimi123')
        self.log_in_page.remember_me()
        self.log_in_page.login_button_click()
        self.driver.implicitly_wait(5)

        # 登录之后点击控制台，然后点击设置
        self.set_up_page.click_control_after_click_set_up()
        sleep(3)

    def tearDown(self):
        # 退出浏览器
        self.driver.quit_browser()

    def test_case_116_set_up_landmark_add_landmark(self):
        # 断言url
        expect_url_after_click_set_up = self.base_url + '/setup/toSetUp'
        self.assertEqual(expect_url_after_click_set_up, self.set_up_page.check_url_after_click_set_up(), 'url地址和实际不一致')

        # 断言左侧导航标题文本
        expect_title_text_after_click_set_up = '我的设置'
        self.assertEqual(expect_title_text_after_click_set_up, self.set_up_page.check_title_text_after_click_set_up(),
                         '左侧导航标题和实际不一致')

        # 点击地标设置
        self.set_up_page.click_set_up_page_lift_list('set_up_landmark')
        self.driver.implicitly_wait(2)

        # 断言右侧页面标题文本
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '右侧页面标题文本和实际不一致')

        # 点击创建地标
        self.set_up_page.click_set_up_landmark_page_add_landmark()
        sleep(2)

        # 断言，创建地标页面的标题文本
        expect_title_text_after_click_add_landmark = '创建地标'
        self.assertEqual(expect_title_text_after_click_add_landmark,
                         self.set_up_page.check_title_text_after_click_add_landmark(), '创建页面右上角文本与实际不一致')

        # 关闭创建地标

        self.set_up_page.close_add_landmark()

        # 断言是否关闭成功
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '右侧页面标题文本和实际不一致')