import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.account_center.account_center_operation_log_page import AccountCenterOperationLogPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 账户中心招呼栏业务日志-设备管理日志查询
# author:孙燕妮

class TestCase012AccountCenterOperDeviceLog(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_operation_log = AccountCenterOperationLogPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.connect_sql = ConnectSql()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_oper_device_log(self):
        '''测试招呼栏业务日志-设备管理日志查询功能'''
        connect = self.connect_sql.connect_tuqiang_sql()
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

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，获取其设备（1）+ 分配（5）记录
            get_device_assign_sql = "select l.id from operation_log l where l.created_by in " + str(lower_account_tuple) \
                                    + " and l.serviceType = '1' and l.operType = '5' ;"
            cur.execute(get_device_assign_sql)
            # 读取数据
            get_device_assign_log = cur.fetchall()
            # 从数据tuple中获取最终查询记录统计条数
            total_list = []
            for range1 in get_device_assign_log:
                for range2 in range1:
                    total_list.append(range2)
            get_device_assign_log_count = len(total_list)
            print("当前登录账户与其所有下级账户的设备分配记录共：" + str(get_device_assign_log_count) + "条!")

            # 执行sql脚本获取当前系统时间
            cur.execute("select curdate();")
            sys_time = cur.fetchall()
            print(sys_time)
            sys_date = sys_time[0][0]
            print(sys_date)

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，搜索其在当前系统日期的20时为止
            # 操作人为当前登录账户的设备（1）+ 分配（5）记录

            search_device_assign_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) + " and l.serviceType = '1' and l.operType = '5' and " \
                                       "l.creation_date  <= '" + \
                                       str(sys_date) + " 20:00' and l.created_by = '" + user_relation_id[
                                           "userId"] + "';"

            cur.execute(search_device_assign_sql)
            # 读取数据
            search_device_assign_log = cur.fetchall()
            total_list = []
            for range1 in search_device_assign_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            search_device_assign_log_count = len(total_list)

            print("在当前系统日期的20时为止操作人为当前登录账户的设备分配记录共："
                  + str(search_device_assign_log_count) + "条!")

            # 执行sql脚本，根据获取的当前登录账户id与其所有下级账户id，搜索其在当前系统日期的20时为止
            # 操作人为当前登录账户的设备（1）+ 修改（1）记录
            get_device_modify_sql = "select l.id from operation_log l where l.created_by in " + str(
                lower_account_tuple) + " and l.serviceType = '1' and l.operType = '1' and " \
                                       "l.creation_date  <= '" + \
                                    str(sys_date) + " 20:00' and l.created_by = '" + user_relation_id["userId"] + "';"
            cur.execute(get_device_modify_sql)
            # 读取数据
            get_device_modify_log = cur.fetchall()
            total_list = []
            for range1 in get_device_modify_log:
                for range2 in range1:
                    total_list.append(range2)
            # 从数据tuple中获取最终查询记录统计条数
            get_device_modify_log_count = len(total_list)

            print("在当前系统日期的20时为止操作人为当前登录账户的设备修改记录共：" + str(get_device_modify_log_count) + "条!")

            # 打开途强在线首页-登录页
            self.base_page.open_page()

            # 登录账号
            self.login_page.user_login("test_007", "jimi123")

            sleep(2)

            # 点击招呼栏-业务日志
            self.account_center_page_operation_log.business_log()
            # 判断当前页面是否正确跳转至业务日志页面
            expect_url = self.base_url + "/business/ConmmandLogs/toBusinessLog"
            self.assertEqual(expect_url, self.driver.get_current_url(), "当前页面跳转错误")

            sleep(4)

            # 获取当前设备分配日志列表设备分配记录共几条
            total_assign_logs_num = self.account_center_page_operation_log.count_curr_busi_log_num()

            # 通过对比当前页面显示的设备分配记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_device_assign_log_count, total_assign_logs_num, "数据库查询结果与页面展示结果不一致")
            # 回到第一页
            self.account_center_page_operation_log.click_dev_log_first_page()
            sleep(4)
            # 在当前列表输入搜索条件
            # 结束时间 系统日期 20:00
            # 搜索输入 操作人 web_autotest
            self.account_center_page_operation_log.search_device_log("test_007")
            sleep(4)
            # 获取当前通过搜索条件搜索出的日志列表设备分配记录共几条
            total_search_logs_num = self.account_center_page_operation_log.count_curr_busi_log_num()
            # 通过对比当前页面显示的设备分配记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(search_device_assign_log_count, total_search_logs_num, "数据库查询结果与页面展示结果不一致")
            # 回到第一页
            self.account_center_page_operation_log.click_dev_log_first_page()
            sleep(4)
            # 当前日志列表点击设备管理-修改
            self.account_center_page_operation_log.log_device_modify()
            sleep(4)
            # 获取当前设备修改日志列表设备分配记录共几条
            total_modify_logs_num = self.account_center_page_operation_log.count_curr_busi_log_num()
            # 通过对比当前页面显示的设备修改记录总数 与 数据库查询结果统计总数 做对比 判断结果是否一致
            self.assertEqual(get_device_modify_log_count, total_modify_logs_num, "数据库查询结果与页面展示结果不一致")
            # 退出登录
            self.account_center_page_navi_bar.usr_logout()
        cur.close()
        connect.close()
