import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.cust_manage.cust_manage_basic_info_and_add_cust_page import CustManageBasicInfoAndAddCustPage
from pages.cust_manage.cust_manage_cust_list_page import CustManageCustListPage
from pages.cust_manage.cust_manage_my_dev_page import CustManageMyDevPage
from pages.cust_manage.cust_manage_page_read_csv import CustManagePageReadCsv

from pages.login.login_page import LoginPage


# 客户管理-左侧用户列表搜索客户

# author:孙燕妮

class TestCase064CustManageLikeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.cust_manage_basic_info_and_add_cust_page = CustManageBasicInfoAndAddCustPage(self.driver, self.base_url)
        self.cust_manage_cust_list_page = CustManageCustListPage(self.driver, self.base_url)
        self.cust_manage_my_dev_page = CustManageMyDevPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.cust_manage_page_read_csv = CustManagePageReadCsv()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_cust_manage_like_search(self):
        '''测试客户管理-模糊搜索客户'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()
        current_account = self.log_in_base.get_log_in_account()
        # 进入客户管理页面
        self.cust_manage_basic_info_and_add_cust_page.enter_cust_manage()

        csv_file = self.cust_manage_page_read_csv.read_csv('acc_like_search.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "keyword": row[0]
            }

            connect = self.connect_sql.connect_tuqiang_sql()

            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = "select o.account,o.userId,r.fullParent from user_relation r inner join user_organize o on" \
                         " r.userId = o.userId where o.account = '" + current_account + "';"
            cur.execute(get_id_sql)

            # 读取数据
            user_relation = cur.fetchall()

            # 遍历数据
            for row in user_relation:
                user_relation_id = {
                    "account": row[0],
                    "userId": row[1],
                    "fullParent": row[2]
                }

                # 执行sql脚本，根据当前登录账号的userId,fullParent查询出当前账户的所有下级账户
                get_lower_account_sql = "select userId from user_relation where fullParent like" + \
                                        "'" + user_relation_id["fullParent"] + user_relation_id["userId"] + "%'" + ";"
                cur.execute(get_lower_account_sql)

                # 读取数据
                lower_account = cur.fetchall()

                lower_account_list = [user_relation_id["userId"]]

                for range1 in lower_account:
                    for range2 in range1:
                        lower_account_list.append(range2)

                lower_account_tuple = tuple(lower_account_list)

                print(lower_account_tuple)

                # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，匹配搜索条件-账户名/用户名，获取其搜索结果
                dev_search01_sql = "select id from user_organize where userId in " + str(
                    lower_account_tuple) + "and (account like '%" + search_info["keyword"] + \
                                   "%' or nickName like '%" + search_info["keyword"] + "%');"
                cur.execute(dev_search01_sql)
                # 读取数据
                dev_search01_data = cur.fetchall()
                total_list = []
                for range1 in dev_search01_data:
                    for range2 in range1:
                        total_list.append(range2)
                # 从数据tuple中获取最终查询结果统计条数
                dev_search01_count = len(total_list)
                print("当前搜索关键词为" + search_info["keyword"] + "的结果共：" + str(dev_search01_count) + "条!")
                # 左侧客户列表搜索关键词,并统计查询结果列表共多少条
                num = self.cust_manage_cust_list_page.acc_like_search(search_info["keyword"])
                # 判断模糊搜索结果列表是否与数据库查询结果一致
                self.assertEqual(dev_search01_count, num, "模糊查找结果不准确")
        csv_file.close()
        # 进入账户中心页面
        self.cust_manage_basic_info_and_add_cust_page.enter_account_center()
        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
