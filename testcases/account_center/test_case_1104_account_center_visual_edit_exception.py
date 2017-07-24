import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from pages.account_center.account_center_page_read_csv import AccountCenterPageReadCsv
from pages.account_center.account_center_visual_account_page import AccountCenterVisualAccountPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer


# 账户中心-虚拟账户管理---修改异常处理
# author:戴招利
class TestCase1104AccountCenterVisualEditException(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.visual_account_page = AccountCenterVisualAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.account_center_page_read_csv = AccountCenterPageReadCsv()
        self.log_in_base = LogInBaseServer(self.driver, self.base_page)
        self.base_page.open_page()
        self.assert_text = AssertText()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def test_visual_account_edit_exception(self):
        '''虚拟账户修改，异常错误提示'''

        # 登录
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        # 进入虚拟账户管理
        self.visual_account_page.enter_visual_account()
        # 添加虚拟账号、保存
        self.visual_account_page.add_visual_account("xnhtj001", "jimi123")
        self.visual_account_page.save_add_info()
        # 点击编辑
        self.visual_account_page.click_editor()

        # 虚拟账号添加与编辑方法
        # 长度不够
        prompt = self.visual_account_page.get_visu_account_error_prompt("edit", "12", "")
        self.assertEqual(self.assert_text.account_center_page_password_len_text(), prompt["pwd_error_prompt"],
                         "修改虚拟账号密码，提示不一致")
        self.assertEqual(self.assert_text.account_center_page_password_unlike(), prompt["pwd2_error_prompt"],
                         "虚拟账号的确认密码，提示不一致")

        # 格式错误
        prompt = self.visual_account_page.get_visu_account_error_prompt("edit", "abcdefgh", "")
        self.assertEqual(self.assert_text.account_center_page_password_formart_text(), prompt["pwd_error_prompt"],
                         "修改虚拟账号密码，提示不一致")
        self.assertEqual(self.assert_text.account_center_page_password_unlike(), prompt["pwd2_error_prompt"],
                         "虚拟账号的确认密码，提示不一致")

        # 密码相同，长度不够
        prompt = self.visual_account_page.get_visu_account_error_prompt("edit", "123", "123")
        self.assertEqual(self.assert_text.account_center_page_password_len_text(), prompt["pwd_error_prompt"],
                         "修改虚拟账号密码，提示不一致")
        self.assertEqual(self.assert_text.account_center_page_password_len_text(), prompt["pwd2_error_prompt"],
                         "虚拟账号的确认密码，提示不一致")

        # 密码不一致
        prompt = self.visual_account_page.get_visu_account_error_prompt("edit", "jimi123", "123")
        self.assertEqual("", prompt["pwd_error_prompt"], "修改虚拟账号密码，提示不一致")
        self.assertEqual(self.assert_text.account_center_page_password_unlike(), prompt["pwd2_error_prompt"],
                         "虚拟账号的确认密码，提示不一致")

        # 验证密码输入长度
        self.assertEqual(16, self.visual_account_page.get_visual_add_and_edit_len(), "密码限制长度显示不一致")
        # 点取消
        self.visual_account_page.dis_save_add_info()
        self.driver.wait(1)
        # 删除
        self.visual_account_page.del_visu_account()
        self.driver.wait()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()

    def tearDown(self):
        self.driver.quit_browser()
