import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_complex_search_page import GlobalComplexSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-高级搜索-通过选择基本信息单一查找

# author:孙燕妮

class TestCase044GlobComplexSearchByBasicInfo(unittest.TestCase):
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

    def test_glob_complex_search_by_basic_info(self):
        '''测试全局搜索-高级搜索-通过选择基本信息单一查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 点击全局搜索栏-高级搜素按钮
        self.global_complex_search_page.click_complex_search()



        csv_file = open(r"E:\git\tuqiangol_test\data\global_search\global_complex_search_by_basic_info.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            basic_info = {
                "type" : row[0],
                "info": row[1]
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

            # 执行sql脚本查询当前登录账号的userId,fullParent
            get_id_sql = "select o.account,o.userId,r.fullParent from user_relation r inner join user_organize o on r.userId = o.userId where o.account = 'test_007' ;"
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


                # 执行sql脚本，通过当前所选基本信息查找所有匹配记录
                get_curr_type_sql = "select id from assets_device where " + basic_info["type"] + " like '%" + \
                                    basic_info["info"] + "%' and userId in " + str(lower_account_tuple) + ";"

                cur.execute(get_curr_type_sql)

                # 读取数据
                curr_dev = cur.fetchall()
                total_list = []
                for range1 in curr_dev:
                    for range2 in range1:
                        total_list.append(range2)

                # 从数据tuple中获取当前所选用户下的设备个数
                dev_count = len(total_list)

                print(basic_info["type"] + " = " + basic_info["info"] + "的设备共：" + str(dev_count) + "条!")



                # 编辑基本信息
                self.global_complex_search_page.complex_search_select_basic_info(basic_info["type"],basic_info["info"])

                # 点击搜索按钮
                self.global_complex_search_page.complex_search_click()
                self.driver.wait(3)

                # 获取当前共多少条搜索结果
                dev_num = self.global_complex_search_page.complex_search_result()

                # 验证当前搜索结果个数与数据库查询结果是否一致
                self.assertEqual(dev_count,dev_num,"当前搜索结果个数与数据库查询结果不一致")

                # 重置搜索条件
                self.global_complex_search_page.complex_search_reset()
                self.driver.wait()



        csv_file.close()


        # 关闭高级搜索对话框
        self.global_complex_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()


