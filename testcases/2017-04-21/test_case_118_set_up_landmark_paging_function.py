import unittest
from time import sleep

from selenium.webdriver.support.select import Select

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.login.login_page import LoginPage
from pages.set_up.set_up_page import SetUpPage


class TestCase118SetUpLandmarkPagingFunction(unittest.TestCase):
    """
    用例第118条，地标设置页面分页功能
    author：zhangAo
    """
    driver = None
    base_url = None
    base_page = None
    log_in_page = None
    base_paging_function = None

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.set_up_page = SetUpPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)

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

    def test_case_118_set_up_landmark_paging_function(self):
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

        # 点击下一页
        self.base_paging_function.click_paging_next_page('set_up_landmark')
        # 点击上一页
        self.base_paging_function.click_paging_previous_page('set_up_landmark')
        # 点击跳转
        self.base_paging_function.click_skip_paging('set_up_landmark','set_up_landmark', 'set_up_landmark',2)
        # 断言当前的页面页数
        self.assertEqual('2', self.base_paging_function.check_current_page_text_after_click_skip())
        # 循环页面跳转
        self.base_paging_function.click_number_ship('set_up_landmark')

        # 分别点击每页显示多少行
        self.base_paging_function.select_per_page_numbers('set_up_landmark', 'set_up_landmark', '10')

        self.base_paging_function.select_per_page_numbers('set_up_landmark', 'set_up_landmark', '30')

        self.base_paging_function.select_per_page_numbers('set_up_landmark', 'set_up_landmark', '50')

        self.base_paging_function.select_per_page_numbers('set_up_landmark', 'set_up_landmark', '100')
