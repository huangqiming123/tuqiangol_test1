import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage
from pages.set_up.set_up_page import SetUpPage


class TestCase122BlackCarAddressLibraryListOperation(unittest.TestCase):
    """
    用例第122条，黑车地址库-黑车地址库的操作（查看、编辑、删除）
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
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.set_up_page = SetUpPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)

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

    def test_case_122_black_car_address_library_list_operation(self):
        # 断言url
        expect_url_after_click_set_up = self.base_url + '/setup/toSetUp'
        self.assertEqual(expect_url_after_click_set_up, self.set_up_page.check_url_after_click_set_up(), 'url地址和实际不一致')

        # 点击黑车地址库
        self.set_up_page.click_set_up_page_lift_list('black_car_adress_library')
        sleep(2)

        # 断言右侧页面左上角的文本
        expect_text_after_click_black_car_address = '黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,
                         self.set_up_page.check_text_after_click_black_car_address())

        # 点击查看黑车地址库
        self.set_up_page.black_car_address_operation_look()
        sleep(3)

        # 断言列表的黑车地址名称和实际的是否一致
        expect_black_car_address_name = self.set_up_page.expect_black_car_address_name()
        actual_black_car_address_name_click_operation_look = self.set_up_page.check_title_text_black_car_address_operation_look()
        self.assertEqual(expect_black_car_address_name, actual_black_car_address_name_click_operation_look)

        # 点击关闭查看黑车地址库
        self.set_up_page.close_look_black_car_address()

        # 断言是否关闭成功
        expect_text_after_click_black_car_address = '黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,
                         self.set_up_page.check_text_after_click_black_car_address())

        # 点击编辑黑车地址库
        self.set_up_page.black_car_address_operation_edit()

        # 断言编辑是否打开
        sleep(3)
        expect_title_text_after_click_edit_black_car_address = '创建黑车地址'
        self.assertEqual(expect_title_text_after_click_edit_black_car_address,
                         self.set_up_page.check_title_text_after_click_edit_black_car_address())

        # 点击关闭编辑黑车地址库
        self.set_up_page.close_edit_black_car_address()

        # 断言是否关闭成功
        expect_text_after_click_black_car_address = '黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,
                         self.set_up_page.check_text_after_click_black_car_address())

        # 点击删除黑车地址库
        self.set_up_page.black_car_address_operation_delete()
        # 断言是否打开
        expect_text_after_click_delete_black_car_address = '确定'
        self.assertEqual(expect_text_after_click_delete_black_car_address,
                         self.set_up_page.check_title_text_after_click_delete_black_car_address())
        # 点击×
        self.set_up_page.close_delete_black_car_address()
        # 断言是否关闭成功
        expect_text_after_click_black_car_address = '黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,
                         self.set_up_page.check_text_after_click_black_car_address())

        # 点击删除黑车地址库
        self.set_up_page.black_car_address_operation_delete()
        # 断言是否打开
        expect_text_after_click_delete_black_car_address = '确定'
        self.assertEqual(expect_text_after_click_delete_black_car_address,
                         self.set_up_page.check_title_text_after_click_delete_black_car_address())
        # 点击取消删除
        self.set_up_page.cancel_delete_black_car_address()
        # 断言是否关闭成功
        expect_text_after_click_black_car_address = '黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,
                         self.set_up_page.check_text_after_click_black_car_address())

        # 点击删除黑车地址库
        self.set_up_page.black_car_address_operation_delete()
        # 断言是否打开
        expect_text_after_click_delete_black_car_address = '确定'
        self.assertEqual(expect_text_after_click_delete_black_car_address,
                         self.set_up_page.check_title_text_after_click_delete_black_car_address())
        # 点击确认
        self.set_up_page.cancel_delete_black_car_address()
        # 断言是否关闭成功
        expect_text_after_click_black_car_address = '黑车地址库'
        self.assertEqual(expect_text_after_click_black_car_address,
                         self.set_up_page.check_text_after_click_black_car_address())
