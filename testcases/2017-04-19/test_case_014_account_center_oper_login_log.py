import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 账户中心招呼栏业务日志-登录日志查询
# author:孙燕妮

class TestCase014AccountCenterOperLoginLog(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_login_log(self):
        '''测试招呼栏业务日志-登录日志查询功能'''

        connect = pymysql.connect(host="172.16.0.100",
                                  port=3306,
                                  user="tracker",
                                  passwd="tracker",
                                  db="tracker-web-mimi",
                                  charset='utf8')

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

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，获取其登录日志
            get_login_log_sql = "select id from user_login_log where loginUserId in " + str(
                lower_account_tuple) + ";"
            cur.execute(get_login_log_sql)
            # 读取数据
            get_login_log = cur.fetchall()
            total_list = []
            for range1 in get_login_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_login_log_count = len(total_list)

            print("当前登录账户与其所有下级账户的登录记录共：" + str(get_login_log_count) + "条!")

            # 执行sql脚本获取当前系统时间
            cur.execute("select curdate();")
            sys_time = cur.fetchall()
            print(sys_time)
            sys_date = sys_time[0][0]
            print(sys_date)

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，搜索其在2017-02-07到当前系统日期的20时内
            # 账号为当前登录账户的登录记录

            search_login_log_sql = "select id from user_login_log where loginUserId in " + str(
                lower_account_tuple) + " and loginTime >= '2017-02-07 00:00' and loginTime <= '" + \
                                   str(sys_date) + " 20:00' and loginAccount = '" + "test_007';"

            cur.execute(search_login_log_sql)
            # 读取数据
            search_login_log = cur.fetchall()
            total_list = []
            for range1 in search_login_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            search_login_log_count = len(total_list)

            print("在2017-02-07到当前系统日期的20时内账户为当前登录账户的登录记录共："
                  + str(search_login_log_count) + "条!")

            # 打开途强在线首页-登录页
            self.base_page.open_page()

            # 登录账号
            self.login_page.user_login("test_007", "jimi123")

            self.driver.wait()

            # 点击招呼栏-业务日志
            self.account_center_page_operation_log.business_log()
            # 判断当前页面是否正确跳转至业务日志页面
            expect_url = self.base_url + "/business/ConmmandLogs/toBusinessLog"
            self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")

            # 点击登录日志
            self.account_center_page_operation_log.login_log()
            sleep(4)

            '''# 获取当前记录列表底部的分页条，设置每页10条
            self.account_center_page_operation_log.select_login_per_page_number("10")
            # 获取当前共几页
            total_login_pages_num = self.account_center_page_operation_log.get_total_login_pages_num()
            # 获取最后一页有几条记录
            last_login_page_logs_num = self.account_center_page_operation_log.last_login_page_logs_num()
            # 计算当前登录日志列表登录记录共几条
            total_login_logs_num = (int(total_login_pages_num) - 1) * 10 + last_login_page_logs_num'''

            total_login_logs_num = self.account_center_page_operation_log.get_log_in_log_total()
            # 通过对比当前页面显示的登录日志总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_login_log_count + 1, total_login_logs_num, "数据库查询结果与页面展示结果不一致")

            # 输入搜索条件来查询登录日志
            self.account_center_page_operation_log.search_login_log("test_007")
            sleep(4)
            '''
            # 获取当前记录列表底部的分页条，设置每页10条
            self.account_center_page_operation_log.select_login_per_page_number("10")
            # 获取当前共几页
            total_login_pages_num = self.account_center_page_operation_log.get_total_login_pages_num()
            # 获取最后一页有几条记录
            last_login_page_logs_num = self.account_center_page_operation_log.last_login_page_logs_num()
            # 计算当前登录日志列表登录记录共几条
            search_login_logs_num = (int(total_login_pages_num) - 1) * 10 + last_login_page_logs_num'''

            search_login_logs_num = self.account_center_page_operation_log.get_log_in_log_total()
            # 通过对比当前页面显示的登录日志总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(search_login_log_count + 1, search_login_logs_num, "数据库查询结果与页面展示结果不一致")

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()

        cur.close()
        connect.close()
