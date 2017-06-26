import csv
import unittest
from time import sleep

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 设备管理-包含下级的设备搜索-by 设备类型+车牌号

# author:孙燕妮

class TestCase098DevManageDevSearchByDevTypeAndCarFrame(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.dev_manage_page = DevManagePage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_manage_dev_search_by_dev_type_and_car_frame(self):
        '''测试设备管理-包含下级的设备搜索-by 设备类型+车牌号'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

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

        # 点击进入设备管理
        self.dev_manage_page.enter_dev_manage()

        # 点击更多筛选条件
        self.dev_manage_page.more_search_info()

        # 选中包含下级设备
        self.dev_manage_page.contain_lower_dev()

        csv_file = open(r"E:\git\tuqiangol_test\data\dev_manage\single_search_info.csv",
                        'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            search_info = {
                "imei": row[0],
                "dev_name": row[1],
                "login_user_dev_type": row[2],
                "user_select": row[3],
                "select_user_dev_type": row[4],
                "vehicle_number": row[5],
                "car_frame": row[6],
                "SIM": row[7],
                "active_start_time": row[8],
                "active_end_time": row[9],
                "plat_expired_start_time": row[10],
                "plat_expired_end_time": row[11],
                "dev_use_range": row[12]
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

            # 执行sql脚本，通过当前登录账号及其下级用户查找该用户下符合搜索条件的所有设备记录
            get_login_user_dev_sql = "select a.id from assets_device a where a.userId in " + str(lower_account_tuple) + \
                                     " and a.mcType = '" + search_info["login_user_dev_type"] + \
                                     "' and a.carFrame like '%" + search_info["car_frame"] + "%';"

            cur.execute(get_login_user_dev_sql)

            # 读取数据
            login_user_dev = cur.fetchall()
            total_list = []
            for range1 in login_user_dev:
                for range2 in range1:
                    total_list.append(range2)

                    # 从数据tuple中获取当前登录账号下的设备个数
            login_user_dev_count = len(total_list)

            print("当前登录账户下符合搜索条件的设备共：" + str(login_user_dev_count) + "条!")

            # 选择机型名称
            sleep(3)
            self.dev_manage_page.select_dev_type(search_info["login_user_dev_type"])

            # 输入车架号
            self.dev_manage_page.input_car_frame(search_info["car_frame"])

            # 搜索
            self.dev_manage_page.click_search_btn()

            # 获取当前搜索结果设备个数
            login_user_dev_num = self.dev_manage_page.count_curr_dev_num()

            # 验证搜索结果与数据库查询结果是否一致
            self.assertEqual(login_user_dev_count, login_user_dev_num, "搜索结果与数据库查询结果不一致")

            # 关闭游标和连接
            cur.close()
            connect.close()

        csv_file.close()

        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
