import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_lower_account_page import CustManageLowerAccountPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage

from pages.login.login_page import LoginPage


# 客户管理-下级客户不同类型-搜索

# author:孙燕妮

class TestCase079CustManageLowerAccountTypeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.cust_manage_lower_account_page = CustManageLowerAccountPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_lower_account_type_search(self):
        '''客户管理-下级客户不同类型-搜索'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        # 点击进入下级客户
        self.cust_manage_lower_account_page.enter_lower_acc()

        csv_file = open(r"E:\git\tuqiangol_test\data\cust_manage\acc_type.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            type_info = {
                "type": row[0],
                "type_number": row[1]
            }

            connect = pymysql.connect(host="172.16.0.100",
                                      port=3306,
                                      user="tracker",
                                      passwd="tracker",
                                      db="tracker-web-mimi")

            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本，通过所登录的账号获取当前所选择账户的userId
            get_curr_userId_sql = "select account,userId,nickName from user_organize where account = 'test_007';"

            cur.execute(get_curr_userId_sql)

            # 读取数据
            curr_user_info = cur.fetchall()

            # 从数据tuple中获取当前所选用户的userId
            curr_userId = curr_user_info[0][1]

            # 执行sql脚本，通过当前用户userId查找该用户下级客户中客户类型为type_info["type"]的用户
            get_acc_sql = "select r.id from user_relation r inner join user_organize o on r.userId = o.userId  " \
                          "where  r.parentId = '" + curr_userId + "' and o.type = '" + type_info["type_number"] + "';"

            cur.execute(get_acc_sql)

            # 读取数据
            curr_acc = cur.fetchall()
            total_list = []
            for range1 in curr_acc:
                for range2 in range1:
                    total_list.append(range2)

            # 从数据tuple中获取当前所选用户下的设备个数
            acc_count = len(total_list)

            print("当前登录用户符合搜索条件的下级客户共：" + str(acc_count) + "条!")

            # 点击各个用户类型查看搜索结果
            self.cust_manage_lower_account_page.click_acc_type(type_info["type"])

            # 获取搜索结果个数
            acc_num = self.cust_manage_lower_account_page.count_curr_lower_acc()

            # 验证搜索结果个数与数据库查询结果是否一致
            self.assertEqual(acc_count, acc_num, "搜索结果个数与数据库查询结果不一致")

        csv_file.close()

        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
