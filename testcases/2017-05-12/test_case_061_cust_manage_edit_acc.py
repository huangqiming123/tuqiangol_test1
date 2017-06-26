import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv

from pages.login.login_page import LoginPage


# 客户管理-编辑用户

# author:孙燕妮

class TestCase061CustManageEditAcc(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_edit_acc(self):
        '''测试客户管理-编辑用户'''
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录
        self.log_in_base.log_in()
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()
        csv_file = self.cust_manage_page_read_csv.read_csv('acc_edit.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            edit_info = {
                "keyword": row[0],
                "higher": row[1],
                "acc_type": row[2],
                "acc_name": row[3],
                "phone": row[4],
                "email": row[5],
                "conn": row[6],
                "com": row[7]
            }

            # 左侧客户列表搜索并选中唯一客户
            self.cust_manage_cust_list_page.acc_exact_search(edit_info["keyword"])

            # 点击编辑用户
            self.cust_manage_basic_info_and_add_cust_page.edit_acc()
            # 右侧搜索栏中搜索并选中作为上级用户
            sleep(3)
            self.cust_manage_basic_info_and_add_cust_page.acc_search(edit_info["higher"])
            # 选择客户类型
            self.cust_manage_basic_info_and_add_cust_page.acc_type_choose(edit_info["acc_type"])
            # 编辑用户输入框信息
            self.cust_manage_basic_info_and_add_cust_page.acc_input_info_edit(edit_info["acc_name"],
                                                                              edit_info["phone"],
                                                                              edit_info["email"],
                                                                              edit_info["conn"],
                                                                              edit_info["com"])
            # 修改用户登录权限
            self.cust_manage_basic_info_and_add_cust_page.acc_login_limit_modi()
            # 修改用户指令权限
            self.cust_manage_basic_info_and_add_cust_page.acc_instr_limit_modi()
            # 修改用户修改权限
            self.cust_manage_basic_info_and_add_cust_page.acc_modi_limit_modi()
            # 保存
            self.cust_manage_basic_info_and_add_cust_page.acc_info_save()
            # 获取保存操作状态
            status = self.cust_manage_basic_info_and_add_cust_page.acc_info_save_status()
            # 验证是否操作成功
            self.assertIn("操作成功", status, "操作失败")

        csv_file.close()
        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
