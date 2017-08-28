import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.assert_text2 import AssertText2
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.login.login_page import LoginPage


# 登录--用户账户修改默认密码
# author:戴招利
class TestCase128LoginAccountEditDefaultPassword(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.assert_text2 = AssertText2()
        self.base_page.open_page()
        sleep(2)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_login_edit_default_password_success(self):
        # 用户账号修改默认密码

        data = ["用户", "有默认密码的账号123", "yonghuzh0123", "13129561000", "233234@qq.com", "用户1", "测试公司名称", "888888",
                "jimi123"]

        self.log_in_base.log_in()
        sleep(2)
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        self.cust_manage_basic_info_and_add_cust_page.add_acc()
        self.cust_manage_basic_info_and_add_cust_page.cancel_add_account()
        self.cust_manage_basic_info_and_add_cust_page.add_acc()
        sleep(2)

        # 选择客户类型、添加客户数据
        self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
        self.cust_manage_basic_info_and_add_cust_page.acc_type_choose(data[0])
        self.cust_manage_basic_info_and_add_cust_page.add_default_password_acc(data[1], data[2],
                                                                               data[3], data[4],
                                                                               data[5], data[6])
        self.driver.default_frame()
        self.cust_manage_basic_info_and_add_cust_page.acc_add_save()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
        # 登录（刚添加的下级账号：yonghuzh01,888888）
        self.log_in_base.log_in_with_csv(data[2], data[7])
        sleep(1)
        # 编辑用户默认密码(jimi123)
        self.cust_manage_basic_info_and_add_cust_page.user_default_password_edit(data[8])
        sleep(2)
        # 获取密码修改成功
        status = self.cust_manage_basic_info_and_add_cust_page.user_default_password_edit_prompt()
        self.assertIn(self.assert_text2.home_page_edit_password_success(), status, "修改密码失败！")
        sleep(2)
        self.assertEqual(self.base_url + "/", self.driver.get_current_url(), "修改默认密码后，没有返回到登录页")

        # 再次登录、并删除新建的用户
        sleep(2)
        self.log_in_base.log_in()
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        # 搜索新增客户名称（有默认密码的账号）
        self.cust_manage_lower_account_page.input_search_info(data[1])

        # 搜索
        self.cust_manage_lower_account_page.click_search_btn()

        # 删除该新增客户
        self.cust_manage_lower_account_page.delete_acc()

        # 确定删除
        self.cust_manage_lower_account_page.delete_acc_ensure()

        # 获取删除操作状态
        del_status = self.cust_manage_lower_account_page.get_del_status()

        # 验证是否操作成功
        self.assertIn(self.assert_text.account_center_page_operation_done(), del_status, "操作失败")
