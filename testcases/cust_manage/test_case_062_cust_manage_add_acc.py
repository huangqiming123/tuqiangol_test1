import csv
import unittest
from time import sleep

from automate_driver.automate_driver_server import AutomateDriverServer
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


# 客户管理-新增用户

# author:孙燕妮

class TestCase062CustManageAddAcc(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer()
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
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_add_acc(self):
        '''测试客户管理-新增用户'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        self.cust_manage_basic_info_and_add_cust_page.add_acc()
        self.cust_manage_basic_info_and_add_cust_page.close_add_account()

        csv_file = self.cust_manage_page_read_csv.read_csv('acc_add.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            add_info = {
                "keyword": row[0],
                "acc_type": row[1],
                "acc_name": row[2],
                "account": row[3],
                "passwd": row[4],
                "phone": row[5],
                "email": row[6],
                "conn": row[7],
                "com": row[8]
            }

            # 左侧客户列表搜索并选中唯一客户
            self.cust_manage_cust_list_page.acc_exact_search(add_info["keyword"])

            # 点击新增用户
            self.cust_manage_basic_info_and_add_cust_page.add_acc()
            sleep(2)
            # 右侧搜索栏中搜索并选中作为上级用户
            self.cust_manage_basic_info_and_add_cust_page.acc_search(add_info["keyword"])
            # 选择客户类型
            self.driver.switch_to_frame('x,/html/body/div[7]/div[2]/iframe')
            self.cust_manage_basic_info_and_add_cust_page.acc_type_choose(add_info["acc_type"])
            # 编辑用户输入框信息
            self.cust_manage_basic_info_and_add_cust_page.add_acc_input_info_edit(add_info["acc_name"],
                                                                                  add_info["account"],
                                                                                  add_info["passwd"],
                                                                                  add_info["phone"],
                                                                                  add_info["email"],
                                                                                  add_info["conn"],
                                                                                  add_info["com"])
            # 修改用户登录权限
            self.cust_manage_basic_info_and_add_cust_page.acc_login_limit_modi()
            self.driver.default_frame()
            self.cust_manage_basic_info_and_add_cust_page.acc_add_save()

            # 获取保存操作状态
            status = self.cust_manage_basic_info_and_add_cust_page.acc_info_save_status()
            # 验证是否操作成功
            self.assertIn("操作成功", status, "操作失败")


            # 搜索新增客户
            self.cust_manage_lower_account_page.input_search_info(add_info["account"])

            # 搜索
            self.cust_manage_lower_account_page.click_search_btn()

            # 删除该新增客户
            self.cust_manage_lower_account_page.delete_acc()

            # 确定删除
            self.cust_manage_lower_account_page.delete_acc_ensure()

            # 获取删除操作状态
            del_status = self.cust_manage_lower_account_page.get_del_status()

            # 验证是否操作成功
            self.assertIn("操作成功", del_status, "操作失败")

        csv_file.close()
