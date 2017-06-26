import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 设备管理-包含下级的设备搜索-by 设备过期状态

# author:孙燕妮

class TestCase089DevManageCurrAndLowerDevSearchByDevExpiredStatus(unittest.TestCase):
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

    def test_dev_manage_curr_and_lower_dev_search_by_dev_expired_status(self):
        '''测试设备管理-包含下级的设备搜索-by 设备过期状态'''

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

        '''connect = pymysql.connect(host="120.24.75.214",
                                  port=3306,
                                  user="jimi_test",
                                  passwd="jimi_test",
                                  db="tracker-web")

        # 创建数据库游标
        cur = connect.cursor()

        # 执行sql脚本查询当前登录账号的userId,fullParent
        get_id_sql = "select o.account,o.userId,r.fullParent from user_relation r inner join user_organize o on r.userId = o.userId where o.account = 'jimitest' ;"
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

            # 执行sql脚本，通过当前所选设备过期状态-已过期 查找所有匹配记录
            get_result_sql_01 = "select count(*) from assets_device_expiration where userId in " + str(
                lower_account_tuple) + "  and CURDATE() > expiration;"

            cur.execute(get_result_sql_01)

            # 读取数据
            curr_dev_01 = cur.fetchall()

            # 从数据tuple中获取当前所选已过期状态的设备个数
            dev_count_01 = curr_dev_01[0][0]

            print("当前所选已过期状态的设备共：" + str(dev_count_01) + "条!")'''

        # 选择过期状态为已过期
        self.dev_manage_page.select_expired_status("已过期")

        # 选中“包含下级”复选框
        self.dev_manage_page.contain_lower_dev()

        # 搜索
        self.dev_manage_page.click_search_btn()

        '''# 获取当前搜索结果设备个数
        dev_num_01 = self.dev_manage_page.count_curr_dev_num()

        # 验证当前搜索结果与数据库查询结果是否一致
        self.assertEqual(dev_count_01,dev_num_01,"当前搜索结果与数据库查询结果不一致")




            # 执行sql脚本，通过当前所选设备过期状态-即将过期 查找所有匹配记录
            get_result_sql_02 = "select count(*) from ( select a.imei,a.expiration,CURDATE()," \
                                "DATEDIFF(a.expiration,CURDATE()) as DiffDate from assets_device a  where a.userId in "\
                                + str(lower_account_tuple) + ") b where b.DiffDate < '30' ;"

            cur.execute(get_result_sql_02)

            # 读取数据
            curr_dev_02 = cur.fetchall()

            # 从数据tuple中获取当前所选即将过期状态的设备个数
            dev_count_02 = curr_dev_02[0][0]

            print("当前所选即将过期状态的设备共：" + str(dev_count_02) + "条!")'''

        # 选择过期状态为即将过期
        self.dev_manage_page.select_expired_status("即将过期")

        # 选中“包含下级”复选框
        self.dev_manage_page.contain_lower_dev()

        # 搜索
        self.dev_manage_page.click_search_btn()

        '''# 获取当前搜索结果设备个数
        dev_num_02 = self.dev_manage_page.count_curr_dev_num()

        # 验证当前搜索结果与数据库查询结果是否一致
        self.assertEqual(dev_count_02, dev_num_02, "当前搜索结果与数据库查询结果不一致")



            # 关闭游标和连接
            cur.close()
            connect.close()'''

        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()
