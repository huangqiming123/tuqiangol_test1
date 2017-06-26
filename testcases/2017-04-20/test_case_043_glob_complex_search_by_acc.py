import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_complex_search_page import GlobalComplexSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-高级搜索-通过选择用户单一查找

# author:孙燕妮

class TestCase043GlobComplexSearchByAcc(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_complex_search_page = GlobalComplexSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_glob_complex_search_by_acc(self):
        '''测试全局搜索-高级搜索-通过选择用户单一查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 点击全局搜索栏-设备搜索按钮
        self.global_complex_search_page.click_easy_search()

        # 点击设备搜索对话框-高级搜索按钮
        self.global_complex_search_page.click_dev_dial_complex_search()

        # 点击高级搜索对话框-返回按钮
        self.global_complex_search_page.dev_dial_complex_search_back()

        # 关闭当前对话框
        self.global_complex_search_page.close_dev_search()

        # 点击全局搜索栏-高级搜素按钮
        self.global_complex_search_page.click_complex_search()

        csv_file = open(r"E:\git\tuqiangol_test\data\global_search\global_complex_search_by_acc.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            acc = {
                "account": row[0]
            }

            connect = pymysql.connect(
                host='172.16.0.100',
                port=3306,
                user='tracker',
                passwd='tracker',
                db='tracker-web-mimi',
                charset='utf8'
            )

            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本，通过所选择的用户名称或账号获取当前所选择账户的userId
            get_curr_userId_sql = "select account,userId,nickName from user_organize where account = '" + acc[
                "account"] + "'; "

            cur.execute(get_curr_userId_sql)

            # 读取数据
            curr_user_info = cur.fetchall()

            # 从数据tuple中获取当前所选用户的userId
            curr_userId = curr_user_info[0][1]

            # 执行sql脚本，通过当前所选用户userId查找该用户下的所有设备记录
            get_curr_user_dev_sql = "select id from assets_device where userId = '" + curr_userId + "';"

            cur.execute(get_curr_user_dev_sql)

            # 读取数据
            curr_user_dev = cur.fetchall()
            total_list = []
            for range1 in curr_user_dev:
                for range2 in range1:
                    total_list.append(range2)

            # 从数据tuple中获取当前所选用户下的设备个数
            dev_count = len(total_list)

            print("用户" + acc["account"] + "的设备共：" + str(dev_count) + "条!")

            # 选择用户
            self.global_complex_search_page.complex_search_select_acc(acc["account"])

            # 点击搜索按钮
            self.global_complex_search_page.complex_search_click()

            # 获取当前共多少条搜索结果
            dev_num = self.global_complex_search_page.complex_search_result()

            # 验证当前搜索结果个数与数据库查询结果是否一致
            self.assertEqual(dev_count, dev_num, "当前搜索结果个数与数据库查询结果不一致")

            # 重置搜索条件
            self.global_complex_search_page.complex_search_reset()
            self.driver.wait()

        csv_file.close()

        # 关闭高级搜索对话框
        self.global_complex_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
