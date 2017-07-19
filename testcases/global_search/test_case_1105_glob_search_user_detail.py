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


class TestCase1105GlobSearchUserDetail(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
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

    def test_case_1105_global_search_user_detail(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        self.log_in_base.log_in_jimitest()
        self.log_in_base.click_account_center_button()
        self.global_dev_search_page.click_easy_search()
        # 关闭
        self.global_dev_search_page.close_search()
        sleep(2)

        self.global_dev_search_page.click_easy_search()

        # 选择用户搜索
        self.global_dev_search_page.click_dev_search()
        self.global_dev_search_page.click_search_buttons()

        user_name = self.global_dev_search_page.get_user_name_in_user_search()
        user_type = self.global_dev_search_page.get_user_type_in_user_search()
        user_account = self.global_dev_search_page.get_user_account_in_user_search()
        # 点用户详情
        self.global_dev_search_page.click_detail_in_user_search()

        # 用户信息
        self.global_dev_search_page.click_user_info_in_user_detail()
        # 获取用户信息中用户名称，用户类型、用户账号、上级用户
        user_name_in_detail = self.global_dev_search_page.get_user_name_in_detail()
        self.assertIn(user_name, user_name_in_detail)

        user_type_in_detail = self.global_dev_search_page.get_user_type_in_detail()
        self.assertEqual(user_type, user_type_in_detail)

        uesr_account_in_detail = self.global_dev_search_page.get_user_account_in_detail()
        self.assertEqual(user_account, uesr_account_in_detail)
        user_account_input_value = self.global_dev_search_page.get_user_account_input_value_in_detail()
        self.assertEqual('true', user_account_input_value)

        get_up_user_name = self.global_dev_search_page.get_up_user_name_in_detail()
        get_up_user_input_value = self.global_dev_search_page.get_up_user_input_value_in_detail()
        self.assertEqual('true', get_up_user_input_value)

        # 查询选中用户的上级
        connect = self.connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_up_account_sql = "select parentId from user_info where account = '%s';" % user_account
        cursor.execute(get_up_account_sql)
        get_up_account = cursor.fetchall()
        up_account_id = get_up_account[0][0]
        get_up_name_sql = "select nickName from user_info where userId = '%s';" % up_account_id
        cursor.execute(get_up_name_sql)
        get_up_name = cursor.fetchall()
        up_account = get_up_name[0][0]
        cursor.close()
        connect.close()
        self.assertEqual(get_up_user_name, up_account)

        # 验证右侧的客户数是否可以搜索
        # 搜索没有的数据
        text = self.global_dev_search_page.search_user_in_user_info('无数据')
        self.assertIn(self.assert_text.account_center_page_no_data_text(), text)

        # 循环点击五次
        for n in range(5):
            self.driver.switch_to_frame('x,/html/body/div[14]/div[2]/iframe')
            self.driver.click_element('x,//*[@id="complex_userInfo_tree_complexUpdate_%s_span"]' % str(n + 3))
            get_up_user_name = self.global_dev_search_page.get_up_user_name_in_details()
            select_up_name = self.driver.get_text(
                'x,//*[@id="complex_userInfo_tree_complexUpdate_%s_span"]' % str(n + 3))
            self.assertEqual(get_up_user_name, select_up_name)
            sleep(2)
            self.driver.default_frame()

        # 点击销售设备
        self.global_dev_search_page.click_sale_dev_in_user_info()
        # 获取销售的对象
        sale_user_name = self.global_dev_search_page.get_sale_user_name()
        self.assertEqual(user_name, sale_user_name)

        # 点击新增客户
        self.global_dev_search_page.click_add_user_in_user_info()
        # 获取新增客户默认的上级
        up_user_in_add_user = self.global_dev_search_page.get_up_user_in_add_user()
        self.assertIn(user_name, up_user_in_add_user)

        # 验证账号
        # 为空
        self.global_dev_search_page.check_add_user_account_input_in_user_info('')
        self.global_dev_search_page.click_save_add_user()
        text = self.global_dev_search_page.get_text_account_input_expertion()
        self.assertEqual(self.assert_text.cust_page_user_account_not_null(), text)

        # 小于3位
        self.global_dev_search_page.check_add_user_account_input_in_user_info('12')
        self.global_dev_search_page.click_save_add_user()
        text = self.global_dev_search_page.get_text_account_input_expertion()
        self.assertEqual(self.assert_text.cust_page_user_account_len(), text)

        # 验证最大长度
        get_user_account_input_max_len = self.global_dev_search_page.get_user_account_input_max_len()
        self.assertEqual('30', get_user_account_input_max_len)

        # 验证客户名称
        # 为空
        self.global_dev_search_page.check_add_user_name_input_in_user_info('')
        self.global_dev_search_page.click_save_add_user()
        text = self.global_dev_search_page.get_text_name_input_expertion()
        self.assertEqual(self.assert_text.cust_page_user_name_not_null(), text)

        # 小于3位
        self.global_dev_search_page.check_add_user_name_input_in_user_info('12')
        self.global_dev_search_page.click_save_add_user()
        text = self.global_dev_search_page.get_text_name_input_expertion()
        self.assertEqual(self.assert_text.cust_page_user_name_more_than_3(), text)

        # 密码
        # 为空
        self.global_dev_search_page.click_add_user_password_first_input_in_user_info('')
        self.global_dev_search_page.click_save_add_user()
        get_first_password_text = self.global_dev_search_page.get_first_password_text()
        self.assertEqual(self.assert_text.cust_page_user_password_not_null(), get_first_password_text)

        # 小于6位
        self.global_dev_search_page.click_add_user_password_first_input_in_user_info('12qw')
        self.global_dev_search_page.click_add_user_password_second_input_in_user_info('12qw')
        self.global_dev_search_page.click_save_add_user()
        get_first_password_text = self.global_dev_search_page.get_first_password_text()
        self.assertEqual(self.assert_text.cust_page_user_password_len(), get_first_password_text)

        # 全数字
        self.global_dev_search_page.click_add_user_password_first_input_in_user_info('121212')
        self.global_dev_search_page.click_add_user_password_second_input_in_user_info('121212')
        self.global_dev_search_page.click_save_add_user()
        get_first_password_text = self.global_dev_search_page.get_first_password_text()
        self.assertEqual(self.assert_text.account_center_page_password_formart_text(), get_first_password_text)

        # 全字母
        self.global_dev_search_page.click_add_user_password_first_input_in_user_info('qwerqw')
        self.global_dev_search_page.click_add_user_password_second_input_in_user_info('qwerqw')
        self.global_dev_search_page.click_save_add_user()
        get_first_password_text = self.global_dev_search_page.get_first_password_text()
        self.assertEqual(self.assert_text.account_center_page_password_formart_text(), get_first_password_text)
        # 两次密码不一致
        self.global_dev_search_page.click_add_user_password_first_input_in_user_info('qwerqw123')
        self.global_dev_search_page.click_add_user_password_second_input_in_user_info('qwerqw2324')
        self.global_dev_search_page.click_save_add_user()
        get_second_password_text = self.global_dev_search_page.get_second_password_text()
        self.assertEqual(self.assert_text.cust_page_password_unlike(), get_second_password_text)
