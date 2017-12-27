import unittest
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv

from pages.login.login_page import LoginPage


class TestCase408CustomerManagementAddUserExpection(unittest.TestCase):
    # 测试新增客户--异常操作验证
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.assert_text = AssertText()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_customer_management_add_user_exception(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        self.cust_manage_basic_info_and_add_cust_page.add_acc()
        self.cust_manage_basic_info_and_add_cust_page.cancel_add_account()

        self.cust_manage_basic_info_and_add_cust_page.add_acc()

        # 验证上级客户input的属性是否为readonly
        readonly_value = self.cust_manage_basic_info_and_add_cust_page.get_up_account_value()
        self.assertEqual('true', readonly_value)

        # 验证新增客户的名称
        # 1 为空
        self.cust_manage_basic_info_and_add_cust_page.add_account_name('')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()
        text = self.cust_manage_basic_info_and_add_cust_page.get_add_account_name_exception_text()
        self.assertEqual(self.assert_text.cust_page_user_name_not_null(), text)

        # 2 长度小于三位
        self.cust_manage_basic_info_and_add_cust_page.add_account_name('1')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()
        text = self.cust_manage_basic_info_and_add_cust_page.get_add_account_name_exception_text()
        self.assertEqual(self.assert_text.cust_page_user_name_more_than_3(), text)

        # 3 验证最大长度
        max_len = self.cust_manage_basic_info_and_add_cust_page.get_account_name_max_len()
        self.assertEqual('50', max_len)

        # 验证新增客户账号
        # 1 为空
        self.cust_manage_basic_info_and_add_cust_page.add_account('')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()
        text = self.cust_manage_basic_info_and_add_cust_page.get_add_account_exception_text()
        self.assertEqual(self.assert_text.cust_page_user_account_not_null(), text)

        # 2 长度小于3位
        self.cust_manage_basic_info_and_add_cust_page.add_account('1')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()
        text = self.cust_manage_basic_info_and_add_cust_page.get_add_account_exception_text()
        self.assertEqual(self.assert_text.cust_page_user_account_len(), text)

        # 3 验证最大长度
        account_max_len = self.cust_manage_basic_info_and_add_cust_page.get_account_max_len()
        self.assertEqual('30', account_max_len)

        # 验证密码
        # 1 为空
        self.cust_manage_basic_info_and_add_cust_page.add_password_first('')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        get_password_first_text = self.cust_manage_basic_info_and_add_cust_page.get_text_first_password()
        self.assertEqual(self.assert_text.cust_page_user_password_not_null(), get_password_first_text)

        # 2 小于6位
        self.cust_manage_basic_info_and_add_cust_page.add_password_first('12e')
        self.cust_manage_basic_info_and_add_cust_page.add_password_second('12e')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        get_password_first_text = self.cust_manage_basic_info_and_add_cust_page.get_text_first_password()
        self.assertEqual(self.assert_text.cust_page_user_password_len(), get_password_first_text)

        # 3 全字母
        self.cust_manage_basic_info_and_add_cust_page.add_password_first('abcdefg')
        self.cust_manage_basic_info_and_add_cust_page.add_password_second('abcdefg')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        get_password_first_text = self.cust_manage_basic_info_and_add_cust_page.get_text_first_password()
        self.assertEqual(self.assert_text.cust_page_user_password_formate(), get_password_first_text)

        # 4 全数字
        self.cust_manage_basic_info_and_add_cust_page.add_password_first('123456')
        self.cust_manage_basic_info_and_add_cust_page.add_password_second('123456')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        get_password_first_text = self.cust_manage_basic_info_and_add_cust_page.get_text_first_password()
        self.assertEqual(self.assert_text.cust_page_user_password_formate(), get_password_first_text)

        # 5 只输入确认密码
        self.cust_manage_basic_info_and_add_cust_page.add_password_first('')
        self.cust_manage_basic_info_and_add_cust_page.add_password_second('a123456')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        get_password_first_text = self.cust_manage_basic_info_and_add_cust_page.get_text_second_password()
        self.assertEqual(self.assert_text.cust_page_password_unlike(), get_password_first_text)

        # 6两次密码不一致
        self.cust_manage_basic_info_and_add_cust_page.add_password_first('123456ee')
        self.cust_manage_basic_info_and_add_cust_page.add_password_second('123456ff')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()

        get_password_first_text = self.cust_manage_basic_info_and_add_cust_page.get_text_second_password()
        self.assertEqual(self.assert_text.cust_page_password_unlike(), get_password_first_text)

        # 验证电话、邮箱、联系人、公司名的最大长度
        phone_max_len = self.cust_manage_basic_info_and_add_cust_page.get_phone_max_len()
        self.assertEqual('20', phone_max_len)

        email_max_len = self.cust_manage_basic_info_and_add_cust_page.get_email_max_len()
        self.assertEqual('50', email_max_len)
        # 验证邮箱格式
        self.cust_manage_basic_info_and_add_cust_page.add_email_format('123123')
        self.cust_manage_basic_info_and_add_cust_page.click_ensure()
        get_text_email = self.cust_manage_basic_info_and_add_cust_page.get_text_email_text()
        self.assertEqual(self.assert_text.cust_page_user_email_formate_error(), get_text_email)

        connect_max_len = self.cust_manage_basic_info_and_add_cust_page.get_connect_max_len()
        self.assertEqual('50', connect_max_len)

        comp_max_len = self.cust_manage_basic_info_and_add_cust_page.get_comp_max_len()
        self.assertEqual('50', comp_max_len)
