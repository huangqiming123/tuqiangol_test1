import csv
import unittest


from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-验证当前选中客户的实际下级客户数与“下级客户”数

# author:孙燕妮

class TestCase066CustManageCurrLowerAcc(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page  = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page  = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_curr_lower_acc(self):
        '''客户管理-验证当前选中客户的实际下级客户数与“下级客户”数'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 获取当前登录用户的下级客户数
        login_lower_num = self.cust_manage_cust_list_page.get_curr_login_lower_acc()
        print(login_lower_num)

        # 点击进入“下级客户”
        self.cust_manage_lower_account_page.enter_lower_acc()

        # 获取当前登录用户“下级客户”下共有多少条数据
        login_acc = self.cust_manage_lower_account_page.count_curr_lower_acc()
        print(login_acc)

        # 验证当前选中客户的库存数与“我的设备”数是否一致
        self.assertEqual(login_lower_num, login_acc, "当前登录用户的下级客户数不一致")


        csv_file = open(r"E:\git\tuqiangol_test\data\cust_manage\acc_exact_search.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "keyword": row[0]
            }

            # 左侧客户列表搜索并选中唯一客户
            self.cust_manage_cust_list_page.acc_exact_search(search_info["keyword"])

            self.driver.wait(3)

            # 获取当前选中客户的下级客户数
            curr_lower_num = self.cust_manage_cust_list_page.get_curr_lower_acc()
            print(curr_lower_num)

            # 获取当前选中客户“下级客户”下共有多少条数据
            my_acc = self.cust_manage_lower_account_page.count_curr_lower_acc()
            print(my_acc)

            # 验证当前选中客户的库存数与“我的设备”数是否一致
            self.assertEqual(curr_lower_num,my_acc,"当前选中客户的下级客户数不一致")



        csv_file.close()


        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()


