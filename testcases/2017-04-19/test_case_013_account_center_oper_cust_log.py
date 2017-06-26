import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 账户中心招呼栏业务日志-客户管理日志查询
# author:孙燕妮

class TestCase013AccountCenterOperCustLog(unittest.TestCase):
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

    def test_account_center_oper_cust_log(self):
        '''测试招呼栏业务日志-客户管理日志查询功能'''

        connect = pymysql.connect(host="172.16.0.100",
                                  port=3306,
                                  user="tracker",
                                  passwd="tracker",
                                  db="tracker-web-mimi")

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
            print("select * from operation_log l where l.created_by in " + str(lower_account_tuple) \
                  + "and l.serviceType = '1' AND l.operType = '5';")

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，获取其客户（2）+ 修改（1）记录
            get_cust_modify_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) \
                                  + " and l.serviceType = '2' and l.operType = '1';"
            cur.execute(get_cust_modify_sql)
            # 读取数据
            get_cust_modify_log = cur.fetchall()
            total_list = []
            for range1 in get_cust_modify_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_cust_modify_log_count = len(total_list)

            print("当前登录账户与其所有下级账户的客户修改记录共：" + str(get_cust_modify_log_count) + "条!")

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，获取其客户（2）+ 添加（0）记录
            get_cust_add_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) + " and l.serviceType = '2' and l.operType = '0';"
            cur.execute(get_cust_add_sql)
            # 读取数据
            get_cust_add_log = cur.fetchall()
            total_list = []
            for range1 in get_cust_add_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_cust_add_log_count = len(total_list)

            print("当前登录账户与其所有下级账户的客户新增记录共：" + str(get_cust_add_log_count) + "条!")

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，获取其客户（2）+ 删除（2）记录
            get_cust_del_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) + " and l.serviceType = '2' and l.operType = '2';"
            cur.execute(get_cust_del_sql)
            # 读取数据
            get_cust_del_log = cur.fetchall()
            total_list = []
            for range1 in get_cust_del_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_cust_del_log_count = len(total_list)

            print("当前登录账户与其所有下级账户的客户删除记录共：" + str(get_cust_del_log_count) + "条!")

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，获取其客户（2）+ 修改密码（3）记录
            get_cust_edit_passwd_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) + " and l.serviceType = '2' and l.operType = '3';"
            cur.execute(get_cust_edit_passwd_sql)
            # 读取数据
            get_cust_edit_passwd_log = cur.fetchall()
            total_list = []
            for range1 in get_cust_edit_passwd_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_cust_edit_passwd_log_count = len(total_list)

            print("当前登录账户与其所有下级账户的客户修改密码记录共：" + str(get_cust_edit_passwd_log_count) + "条!")

            # 执行sql脚本获取当前系统时间
            cur.execute("select curdate();")
            sys_time = cur.fetchall()
            print(sys_time)
            sys_date = sys_time[0][0]
            print(sys_date)

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，搜索其在当前系统日期的20时为止
            # 账号为当前登录账户的客户（2）+ 重置密码（4）记录
            get_cust_reset_passwd_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) + " and l.serviceType = '2' and l.operType = '4' and " \
                                       "l.creation_date >= '2017-02-07 00:00' and l.creation_date <= '" + \
                                        str(sys_date) + " 20:00' and l.created_by = '" + user_relation_id[
                                            "userId"] + "';"
            cur.execute(get_cust_reset_passwd_sql)
            # 读取数据
            get_cust_reset_passwd_log = cur.fetchall()
            total_list = []
            for range1 in get_cust_reset_passwd_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_cust_reset_passwd_log_count = len(total_list)

            print("在当前系统日期的20时为止操作人为当前登录账户的客户重置密码记录共：" + str(get_cust_reset_passwd_log_count) + "条!")

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

            # 点击客户管理（默认-修改）
            self.account_center_page_operation_log.log_cust_modify()
            self.driver.wait(3)
            # 获取当前客户修改日志列表客户修改记录共几条
            total_cust_modify_num = self.account_center_page_operation_log.count_curr_busi_cust_log_num()

            # 通过对比当前页面显示的客户修改记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_cust_modify_log_count, total_cust_modify_num, "数据库查询结果与页面展示结果不一致")

            # 回到第一页
            self.account_center_page_operation_log.click_cust_log_first_page()
            self.driver.wait(3)

            # 当前日志列表点击客户管理-添加
            self.account_center_page_operation_log.log_cust_add()
            self.driver.wait(3)
            # 获取当前客户添加日志列表客户添加记录共几条
            total_cust_add_num = self.account_center_page_operation_log.count_curr_busi_cust_log_num()

            # 通过对比当前页面显示的客户添加记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_cust_add_log_count, total_cust_add_num, "数据库查询结果与页面展示结果不一致")

            # 回到第一页
            self.account_center_page_operation_log.click_cust_log_first_page()
            self.driver.wait(2)

            # 当前日志列表点击客户管理-删除
            self.account_center_page_operation_log.log_cust_delete()
            self.driver.wait(2)
            # 获取当前客户删除日志列表客户删除记录共几条
            total_cust_del_num = self.account_center_page_operation_log.count_curr_busi_cust_log_num()

            # 通过对比当前页面显示的客户删除记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_cust_del_log_count, total_cust_del_num, "数据库查询结果与页面展示结果不一致")

            # 回到第一页
            self.account_center_page_operation_log.click_cust_log_first_page()
            self.driver.wait(2)

            # 当前日志列表点击客户管理-修改密码
            self.account_center_page_operation_log.log_cust_modify_passwd()
            self.driver.wait(2)
            # 获取当前客户修改密码日志列表客户修改密码记录共几条
            total_cust_modify_passwd_num = self.account_center_page_operation_log.count_curr_busi_cust_log_num()

            # 通过对比当前页面显示的客户修改密码记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_cust_edit_passwd_log_count, total_cust_modify_passwd_num, "数据库查询结果与页面展示结果不一致")

            # 回到第一页
            self.account_center_page_operation_log.click_cust_log_first_page()
            self.driver.wait(2)

            # 在当前列表输入搜索条件
            # 结束时间 系统日期 20:00
            # 搜索输入 操作人 web_autotest
            # 当前日志列表点击客户管理-重置密码
            self.account_center_page_operation_log.log_cust_reset_passwd()
            self.account_center_page_operation_log.search_cust_log("test_007")
            self.driver.wait(2)
            # 获取客户重置密码日志列表客户重置密码记录共几条
            total_cust_reset_passwd_num = self.account_center_page_operation_log.count_curr_busi_cust_log_num()

            # 通过对比当前页面显示的客户重置密码记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_cust_reset_passwd_log_count, total_cust_reset_passwd_num, "数据库查询结果与页面展示结果不一致")

            # 退出登录
            self.account_center_page_navi_bar.usr_logout()
        cur.close()
        connect.close()
