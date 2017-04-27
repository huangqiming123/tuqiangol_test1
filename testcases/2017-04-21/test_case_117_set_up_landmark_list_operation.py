import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.set_up.set_up_page import SetUpPage


class TestCase117SetUpLandmarkListOperation(unittest.TestCase):
    """
    用例第117条，编辑地标位置（查看、编辑、删除）
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

    def test_case_117_set_up_landmark_add_landmark(self):
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

        # 点击查看地标
        self.set_up_page.set_up_landmark_operation_click_look()

        # 断言实际的地标名称和打开的是否一致
        self.assertEqual(self.set_up_page.expect_landmark_text(),
                         self.set_up_page.check_title_text_after_click_look_button(), '实际地标名字和期望的不一致')
        # 点击关闭
        self.set_up_page.close_landmark()
        # 断言是否关闭成功
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '右侧页面标题文本和实际不一致')

        csv_file = open('E:\git\\tuqiangol_test\data\set_up\set_up_landmark_edit_data.csv', 'r', encoding='utf8')
        csv_data = csv.reader(csv_file)

        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            set_up_landmark_edit_data = {
                'landmark_name': row[0],
                'landmark_desc': row[1]
            }
            # 点击编辑
            self.set_up_page.set_up_landmark_operation_click_edit()
            sleep(2)

            # 断言 编辑框是否打开
            expect_title_text_after_click_edit = '编辑'
            self.assertEqual(expect_title_text_after_click_edit,
                             self.set_up_page.check_title_text_after_click_edit_button(), '编辑框没有正常打开')

            # 输入参数，点击保存
            self.set_up_page.edit_landmark(set_up_landmark_edit_data)
            sleep(2)

            # 断言 是否修改成功
            self.assertEqual(self.set_up_page.expect_landmark_text(), set_up_landmark_edit_data['landmark_name'],
                             '编辑不成功！')
            sleep(2)
        csv_file.close()

        # 点击编辑
        self.set_up_page.set_up_landmark_operation_click_edit()
        sleep(2)

        # 断言 编辑框是否打开
        expect_title_text_after_click_edit = '编辑'
        self.assertEqual(expect_title_text_after_click_edit,
                         self.set_up_page.check_title_text_after_click_edit_button(), '编辑框没有正常打开')

        # 点击关闭编辑框
        self.set_up_page.close_landmark_edit()

        # 断言是否正常关闭
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '右侧页面标题文本和实际不一致')
        sleep(2)

        # 点击编辑
        self.set_up_page.set_up_landmark_operation_click_edit()
        sleep(2)

        # 断言 编辑框是否打开
        expect_title_text_after_click_edit = '编辑'
        self.assertEqual(expect_title_text_after_click_edit,
                         self.set_up_page.check_title_text_after_click_edit_button(), '编辑框没有正常打开')

        # 点击取消编辑框
        self.set_up_page.cancel_landmark_edit()

        # 断言是否正常关闭
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '右侧页面标题文本和实际不一致')
        sleep(2)

        # 点击删除地标
        self.set_up_page.set_up_landmark_operation_click_delete()
        sleep(2)

        # 断言 提示是否删除框是否打开
        expect_text_after_click_detele = '确定'
        self.assertEqual(expect_text_after_click_detele, self.set_up_page.check_text_after_click_delete(), '删除框没有打开！')

        # 点击确认
        self.set_up_page.ensure_detele_landmark()

        # 断言，判断删除框是否关闭
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '删除框没有关闭！')

        sleep(2)
        # 点击删除地标
        self.set_up_page.set_up_landmark_operation_click_delete()
        sleep(1)

        # 断言 提示是否删除框是否打开
        expect_text_after_click_detele = '确定'
        self.assertEqual(expect_text_after_click_detele, self.set_up_page.check_text_after_click_delete(), '删除框没有打开！')

        # 点击取消
        self.set_up_page.cancel_delete_landmark()

        # 断言，判断删除框是否关闭
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '删除框没有关闭！')

        sleep(2)
        # 点击删除地标
        self.set_up_page.set_up_landmark_operation_click_delete()
        sleep(1)

        # 断言 提示是否删除框是否打开
        expect_text_after_click_detele = '确定'
        self.assertEqual(expect_text_after_click_detele, self.set_up_page.check_text_after_click_delete(), '删除框没有打开！')

        # 点击取消
        self.set_up_page.close_delete_landmark()

        # 断言，判断删除框是否关闭
        expect_title_text_after_click_set_up_landmark = '地标设置'
        self.assertEqual(expect_title_text_after_click_set_up_landmark,
                         self.set_up_page.check_title_text_after_click_set_up_landmark(), '删除框没有关闭！')
