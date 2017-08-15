import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_pages import AccountCenterNaviBarPages
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.global_search.global_search_page_read_csv import GlobleSearchPageReadCsv
from pages.global_search.search_sql import SearchSql


class TestCase116UserSearchModifyWebDevEditAuthority(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver(choose='firefox')
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPages(self.driver, self.base_url)
        self.driver.set_window_max()
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.global_search_page_read_csv = GlobleSearchPageReadCsv()
        self.search_sql = SearchSql()
        self.driver.wait(1)
        self.connect_sql = ConnectSql()
        self.assert_text = AssertText()
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_user_search_modify_web_dev_edit_authority(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()

        # 选择用户搜索
        self.global_dev_search_page.click_dev_search()
        self.global_dev_search_page.click_search_buttons()

        # 获取列表中第二个用户的账号
        self.global_dev_search_page.swith_to_search_frame()
        get_second_user_account = self.global_account_search_page.get_second_user_account_after_search_user()
        # 点击详情
        self.global_account_search_page.click_user_detail_button()
        # 点击用户信息
        self.global_account_search_page.click_user_info_in_user_detail()

        # 获取用户信息页面登录账号名字
        current_account = self.global_account_search_page.get_current_account_in_user_detail()
        self.assertEqual(get_second_user_account, current_account)

        # 获取各个权限input的select属性
        web_login_authority = self.global_account_search_page.get_web_login_authority_input_select_in_user_detail()
        app_login_authority = self.global_account_search_page.get_app_login_authorith_input_select_in_user_detail()

        batch_issued_command_authority = self.global_account_search_page.batch_issued_command_authority_in_user_detail()
        batch_issued_work_type_authority = self.global_account_search_page.batch_issued_work_type_authority_in_user_detail()

        web_modify_authority = self.global_account_search_page.get_web_modify_authority_in_user_detail()
        app_modify_authority = self.global_account_search_page.get_app_modify_authority_in_user_detail()

        if web_modify_authority == True:
            # 点击web修改设备的权限
            self.global_account_search_page.click_web_modify_dev_authority_in_user_detail()
            # 点击保存
            self.global_account_search_page.click_ensuer_button_in_user_detail()
            # 点击关闭
            self.driver.default_frame()
            self.global_account_search_page.click_close_button()

            # 退出登录
            self.global_account_search_page.logout()

            # 登录刚刚修改过的账号
            self.global_account_search_page.log_in_user(get_second_user_account, 'jimi123')
            # 进入设备管理页面
            self.global_account_search_page.click_dev_manage_page()
            sleep(2)
            # 点击编辑设备
            self.global_account_search_page.click_edit_dev_in_dev_manage_page()
            # 点击保存
            self.global_account_search_page.click_ensuer_button()
            # 获取提示语
            text = self.global_account_search_page.get_no_authority_text()
            self.assertIn(self.assert_text.no_authority_text(), text)

            # 关闭设备编辑页面
            self.global_account_search_page.close_dev_edit()
            # 退出登录的账号
            self.global_account_search_page.click_account_manage_page()
            self.global_account_search_page.logout()
            # 登录web_autotest
            self.log_in_base.log_in()
            self.log_in_base.click_account_center_button()
            self.global_dev_search_page.click_easy_search()
            # 关闭
            self.global_dev_search_page.close_search()
            sleep(2)
            self.global_dev_search_page.click_easy_search()
            # 选择用户搜索
            self.global_dev_search_page.click_dev_search()
            self.global_dev_search_page.click_search_buttons()
            # 点击详情
            self.global_dev_search_page.swith_to_search_frame()
            self.global_account_search_page.click_user_detail_button()
            # 点击用户信息
            self.global_account_search_page.click_user_info_in_user_detail()

            self.global_account_search_page.click_web_modify_dev_authority_in_user_detail()
            # 点击保存
            self.global_account_search_page.click_ensuer_button_in_user_detail()
            # 点击关闭
            self.driver.default_frame()
            self.global_account_search_page.click_close_button()

            # 退出登录
            self.global_account_search_page.logout()

            # 登录刚刚修改过的账号
            self.global_account_search_page.log_in_user(get_second_user_account, 'jimi123')
            # 进入设备管理页面
            self.global_account_search_page.click_dev_manage_page()
            # 点击编辑设备
            self.global_account_search_page.click_edit_dev_in_dev_manage_page()
            # 点击保存
            self.global_account_search_page.click_ensuer_button()
            # 获取提示语
            text = self.global_account_search_page.get_authority_text()
            self.assertIn(self.assert_text.account_center_page_operation_done(), text)

        elif web_modify_authority == False:
            # 点击web修改设备的权限
            self.global_account_search_page.click_web_modify_dev_authority_in_user_detail()
            # 点击保存
            self.global_account_search_page.click_ensuer_button_in_user_detail()
            # 点击关闭
            self.driver.default_frame()
            self.global_account_search_page.click_close_button()

            # 退出登录
            self.global_account_search_page.logout()

            # 登录刚刚修改过的账号
            self.global_account_search_page.log_in_user(get_second_user_account, 'jimi123')
            # 进入设备管理页面
            self.global_account_search_page.click_dev_manage_page()
            # 点击编辑设备
            self.global_account_search_page.click_edit_dev_in_dev_manage_page()
            # 点击保存
            self.global_account_search_page.click_ensuer_button()
            # 获取提示语
            text = self.global_account_search_page.get_authority_text()
            self.assertIn(self.assert_text.account_center_page_operation_done(), text)

            # 关闭设备编辑页面
            self.global_account_search_page.close_dev_edit()
            # 退出登录的账号
            self.global_account_search_page.click_account_manage_page()
            sleep(2)
            self.global_account_search_page.logout()
            # 登录web_autotest
            self.log_in_base.log_in()
            self.log_in_base.click_account_center_button()
            self.global_dev_search_page.click_easy_search()
            # 关闭
            self.global_dev_search_page.close_search()
            sleep(2)
            self.global_dev_search_page.click_easy_search()
            # 选择用户搜索
            self.global_dev_search_page.click_dev_search()
            self.global_dev_search_page.click_search_buttons()
            # 点击详情
            self.global_dev_search_page.swith_to_search_frame()
            self.global_account_search_page.click_user_detail_button()
            # 点击用户信息
            self.global_account_search_page.click_user_info_in_user_detail()

            self.global_account_search_page.click_web_modify_dev_authority_in_user_detail()
            # 点击保存
            self.global_account_search_page.click_ensuer_button_in_user_detail()
            # 点击关闭
            self.driver.default_frame()
            self.global_account_search_page.click_close_button()

            # 退出登录
            self.global_account_search_page.logout()

            # 登录刚刚修改过的账号
            self.global_account_search_page.log_in_user(get_second_user_account, 'jimi123')
            # 进入设备管理页面
            self.global_account_search_page.click_dev_manage_page()
            # 点击编辑设备
            self.global_account_search_page.click_edit_dev_in_dev_manage_page()
            # 点击保存
            self.global_account_search_page.click_ensuer_button()
            # 获取提示语
            text = self.global_account_search_page.get_no_authority_text()
            self.assertIn(self.assert_text.no_authority_text(), text)
