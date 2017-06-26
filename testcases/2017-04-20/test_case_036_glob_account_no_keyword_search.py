import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_account_search_page import GlobalAccountSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-搜索栏用户不输入搜索信息查找功能
# author:孙燕妮

class TestCase027GlobAccountNoKeywordSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_account_search_page = GlobalAccountSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_global_account_no_keyword_search(self):
        '''测试全局搜索-搜索栏用户不输入搜索信息查找功能'''

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

        # 执行sql脚本查询当前登录账号的userId,fullParent
        get_id_sql = "select o.account,o.userId,r.fullParent from user_relation r inner join user_organize o on" \
                     " r.userId = o.userId where o.account = 'test_007' ;"
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

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，无搜索条件下获取其搜索结果
            acc_search01_sql = "select id from user_organize where userId in " + str(
                lower_account_tuple) + ";"
            cur.execute(acc_search01_sql)
            # 读取数据
            acc_search_data = cur.fetchall()
            total_list = []
            for range1 in acc_search_data:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            acc_search_count = len(total_list)

            print("当前登录账户与其所有下级账户中搜有设备共：" + str(acc_search_count) + "!")

            # 打开途强在线首页-登录页
            self.base_page.open_page()

            # 登录
            self.login_page.user_login("test_007", "jimi123")

            # 不输入搜索关键词点击“用户”搜索按钮

            self.global_account_search_page.click_account_search()

            # 不输入搜索关键词点击用户搜索对话框-用户搜索按钮
            self.global_account_search_page.click_account_dial_search()

            # 获取搜索结果总数
            result_num = self.global_account_search_page.easy_search_result()

            # 验证搜索结果与数据库查询结果是否一致
            self.assertEqual(acc_search_count, result_num, "不输入搜索条件时搜索的结果与数据库查询结果总数不一致")

            # 关闭当前设备搜索对话框
            self.global_account_search_page.close_dev_search()

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()
