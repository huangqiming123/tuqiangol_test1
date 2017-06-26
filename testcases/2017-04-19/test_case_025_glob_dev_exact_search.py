import csv
import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_dev_search_page import GlobalDevSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-搜索栏设备精确查找
# author:孙燕妮

class TestCase025GlobDevExactSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.global_dev_search_page = GlobalDevSearchPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_global_dev_exact_search(self):
        '''通过csv测试全局搜索-搜索栏设备精确查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        csv_file = open(r"E:\git\tuqiangol_test\data\global_search\dev_search_keyword.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            dev_search = {
                "dev_name": row[0],
                "dev_imei": row[1]
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

                # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，匹配搜索条件-设备名称，获取其搜索结果
                dev_search01_sql = "select id from assets_device where userId in " + str(
                    lower_account_tuple) + "and deviceName = '" + dev_search["dev_name"] + "';"
                cur.execute(dev_search01_sql)
                # 读取数据
                dev_search01_data = cur.fetchall()
                total_list = []
                for range1 in dev_search01_data:
                    for range2 in range1:
                        total_list.append(range2)
                # 从数据tuple中获取最终查询记录统计条数
                dev_search01_count = len(total_list)

                print("当前登录账户与其所有下级账户中设备名称为" + dev_search["dev_name"] + "的记录共：" + str(dev_search01_count) + "条!")

                # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，匹配搜索条件-设备imei，获取其搜索结果
                dev_search02_sql = "select id from assets_device where userId in " + str(
                    lower_account_tuple) + "and imei = '" + dev_search["dev_imei"] + "';"
                cur.execute(dev_search02_sql)
                # 读取数据
                dev_search02_data = cur.fetchall()
                total_list = []
                for range1 in dev_search02_data:
                    for range2 in range1:
                        total_list.append(range2)
                # 从数据tuple中获取最终查询记录统计条数
                dev_search02_count = len(total_list)

                print("当前登录账户与其所有下级账户中设备imei为" + dev_search["dev_imei"] + "的记录共：" + str(dev_search02_count) + "条!")

                # 在全局搜索栏输入搜索关键词-设备名称
                self.global_dev_search_page.device_easy_search(dev_search["dev_name"])

                # 获取搜索结果总数
                result_num01 = self.global_dev_search_page.easy_search_result()

                # 验证搜索结果与数据库查询结果是否一致
                self.assertEqual(dev_search01_count, result_num01, "通过设备名称搜索的结果与数据库查询结果总数不一致")

                # 在设备搜索对话框输入搜索关键词-设备imei
                self.global_dev_search_page.dev_dial_search(dev_search["dev_imei"])

                # 获取搜索结果总数
                result_num02 = self.global_dev_search_page.easy_search_result()

                # 验证搜索结果与数据库查询结果是否一致
                self.assertEqual(dev_search02_count, result_num02, "通过设备名称搜索的结果与数据库查询结果总数不一致")

                # 关闭当前设备搜索对话框
                self.global_dev_search_page.close_dev_search()

                self.driver.wait(1)

            cur.close()
            connect.close()

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
