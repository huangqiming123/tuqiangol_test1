import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.base.lon_in_base import LogInBase
from pages.console.console_page import ConsolePage
from pages.console.console_page_read_csv import ConsolePageReadCsv
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 控制台-车辆列表-模糊搜索

# author:孙燕妮

class TestCase111ConsoleVehicleListLikeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.console_page = ConsolePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.log_in_base = LogInBase(self.driver, self.base_url)
        self.console_page_read_csv = ConsolePageReadCsv()
        self.connect_sql = ConnectSql()
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_console_vehicle_list_like_search(self):
        '''测试控制台-车辆列表-模糊搜索'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.log_in_base.log_in()
        current_account = self.log_in_base.get_log_in_account()

        # 获取当前窗口句柄
        account_center_handle = self.driver.get_current_window_handle()

        # 点击进入控制台
        self.dev_manage_page.enter_console()

        # 获取当前所有窗口句柄
        all_handles = self.driver.get_all_window_handles()
        for handle in all_handles:
            if handle != account_center_handle:
                # 切换到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait(1)
                # 关闭账户中心窗口
                self.driver.close_current_page()
                # 回到控制台窗口
                self.driver.switch_to_window(handle)
                self.driver.wait()

        csv_file = self.console_page_read_csv.read_csv('search_dev.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "like_keyword": row[0]
            }

            connect = self.connect_sql.connect_tuqiang_sql()

            # 创建数据库游标
            cur = connect.cursor()

            # 执行sql脚本，通过当前登录账号获取其userId
            get_login_userId_sql = "select account,userId,nickName from user_organize where account = '" + current_account + "'; "

            cur.execute(get_login_userId_sql)

            # 读取数据
            login_user_info = cur.fetchall()

            # 从数据tuple中获取当前登录账号的userId
            login_userId = login_user_info[0][1]

            # 执行sql脚本，通过当前登录账号userId查找该用户下符合搜索条件的所有设备记录
            get_login_user_dev_sql = "select id from assets_device where userId = '" + login_userId + \
                                     "' and (imei like '%" + search_info["like_keyword"] + \
                                     "%' or deviceName like '%" + search_info["like_keyword"] + \
                                     "%' or vehicleNumber like '%" + search_info["like_keyword"] + \
                                     "%' or driverName  like '%" + search_info["like_keyword"] + "%');"

            cur.execute(get_login_user_dev_sql)

            # 读取数据
            login_user_dev = cur.fetchall()
            total_list = []
            for range1 in login_user_dev:
                for range2 in range1:
                    total_list.append(range2)

            # 从数据tuple中获取当前登录账号符合搜索条件的设备个数
            login_user_dev_count = len(total_list)

            print("当前登录账户下符合搜索条件的设备共：" + str(login_user_dev_count) + "条!")

            # 车辆列表输入模糊关键字搜索设备
            self.console_page.search_dev(search_info["like_keyword"])

            # 获取搜索结果设备总数
            sleep(5)
            dev_num = self.console_page.count_all_group_dev()

            # 验证搜索结果总数与数据库搜索结果数是否一致
            self.assertEqual(login_user_dev_count, dev_num, "搜索结果总数与数据库搜索结果数不一致")
            cur.close()
            connect.close()

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
