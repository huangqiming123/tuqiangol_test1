import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览  总进货数
# author:zhangao

class TestCase154AccountCenterOverviewTotal(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_total(self):
        self.base_page.open_page()
        self.log_in_base.log_in()
        # 获取登录账号的用户名
        current_account = self.log_in_base.get_log_in_account()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()
        expect_total = self.account_center_page_details.get_current_account_total_equipment()

        # 点击库存
        self.account_center_page_details.account_overview('总进货数')
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                self.driver.switch_to_window(handle)
                sleep(2)
                expect_url = self.driver.get_current_url()
                connect = self.connect_sql.connect_tuqiang_sql()
                # 创建数据库游标
                cur = connect.cursor()
                # 执行sql脚本查询当前登录账号的userId,fullParent
                get_id_sql = "select userId from user_organize where account = '" + current_account + "' ;"
                cur.execute(get_id_sql)
                # 读取数据
                user_relation = cur.fetchall()
                user_id = user_relation[0][0]
                actual_url = self.base_url + '/customer/toSearch?userId=%s' % user_id
                self.assertEqual(expect_url, actual_url, '点击总进货数后，实际的url和期望的不一样！')

                # 执行sql脚本查询当前登录账号的userId,fullParent
                get_id_sql = "select o.account,o.userId,r.fullParent from user_relation r inner join user_organize o on r.userId = o.userId where o.account = '" + current_account + "' ;"
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
                # 执行sql脚本，通过当前所选设备激活状态-未激活 查找所有匹配记录
                get_result_sql = "select id from assets_device where userId in " + str(lower_account_tuple) + " ;"
                cur.execute(get_result_sql)
                # 读取数据
                curr_dev = cur.fetchall()
                total_list = []
                for range1 in curr_dev:
                    for range2 in range1:
                        total_list.append(range2)
                # 从数据tuple中获取当前用户及其下级账户未激活状态的设备个数
                dev_count = len(total_list)
                self.assertEqual(expect_total, str(dev_count), '当前总进货数和实际数据库不一致！')
                cur.close()
                connect.close()
                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
