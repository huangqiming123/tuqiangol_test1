import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.dev_manage.dev_manage_page import DevManagePage

from pages.login.login_page import LoginPage


# 设备管理-设备搜索-by 激活状态

# author:孙燕妮

class TestCase093DevManageDevSearchByActiveStatus(unittest.TestCase):
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

    def test_dev_manage_dev_search_by_active_status(self):
        '''测试设备管理-设备搜索-by 激活状态'''

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

        # 执行sql脚本，通过当前登录账号获取其userId
        get_login_userId_sql = "select account,userId,nickName from user_organize where account = 'test_007'; "

        cur.execute(get_login_userId_sql)

        # 读取数据
        login_user_info = cur.fetchall()

        # 从数据tuple中获取当前登录账号的userId
        login_userId = login_user_info[0][1]

        # 执行sql脚本，通过当前所选设备激活状态-已激活 查找所有匹配记录
        get_result_sql_01 = "select id from assets_device where userId = '" + login_userId + \
                            "'  and activationTime is not NULL;"

        cur.execute(get_result_sql_01)

        # 读取数据
        curr_dev_01 = cur.fetchall()
        total_list = []
        for range1 in curr_dev_01:
            for range2 in range1:
                total_list.append(range2)

        # 从数据tuple中获取当前所选已过期状态的设备个数
        dev_count_01 = len(total_list)

        print("当前所选已激活状态的设备共：" + str(dev_count_01) + "条!")



        # 选择过期状态为已激活
        self.dev_manage_page.select_active_status("已激活")

        # 搜索
        self.dev_manage_page.click_search_btn()

        # 获取当前搜索结果设备个数
        dev_num_01 = self.dev_manage_page.count_curr_dev_num()

        # 验证当前搜索结果与数据库查询结果是否一致
        self.assertEqual(dev_count_01,dev_num_01,"当前搜索结果与数据库查询结果不一致")




        # 执行sql脚本，通过当前所选设备激活状态-未激活 查找所有匹配记录
        get_result_sql_02 = "select id from assets_device where userId = '" + login_userId + \
                            "'  and activationTime is NULL;"

        cur.execute(get_result_sql_02)

        # 读取数据
        curr_dev_02 = cur.fetchall()
        total_list = []
        for range1 in curr_dev_02:
            for range2 in range1:
                total_list.append(range2)

        # 从数据tuple中获取当前用户未激活状态的设备个数
        dev_count_02 = len(total_list)

        print("当前用户未激活状态的设备共：" + str(dev_count_02) + "条!")


        # 选择激活状态为未激活
        self.dev_manage_page.select_active_status("未激活")

        # 搜索
        self.dev_manage_page.click_search_btn()

        # 获取当前搜索结果设备个数
        dev_num_02 = self.dev_manage_page.count_curr_dev_num()

        # 验证当前搜索结果与数据库查询结果是否一致
        self.assertEqual(dev_count_02, dev_num_02, "当前搜索结果与数据库查询结果不一致")



        # 关闭游标和连接
        cur.close()
        connect.close()



        # 退出登录
        self.account_center_page_navi_bar.dev_manage_usr_logout()

