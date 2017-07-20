import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_complex_search_page import GlobalComplexSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-高级搜索-通过选择用户+基本信息+日期类型三组合查找

# author:孙燕妮

class TestCase053GlobComplexSearchByAccAndBasicInfoAndDateType(unittest.TestCase):
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

    def test_glob_complex_search_by_acc_and_basic_info_and_date_type(self):
        '''测试全局搜索-高级搜索-通过选择用户+基本信息+日期类型三组合查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 点击全局搜索栏-高级搜素按钮
        self.global_complex_search_page.click_complex_search()

        basic_info = {
            "imei": "123",
            "deviceName": "123"
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

        # 执行sql脚本，通过所选择的用户名称或账号获取当前所选择账户的userId
        get_curr_userId_sql = "select account,userId,nickName from user_organize where account = 'test_007'; "

        cur.execute(get_curr_userId_sql)

        # 读取数据
        curr_user_info = cur.fetchall()

        # 从数据tuple中获取当前所选用户的userId
        curr_userId = curr_user_info[0][1]

        # 执行sql脚本，通过当前所选用户+基本信息+激活时间查找所有匹配记录
        get_result_sql_01 = "select id from assets_device where userId = '" + curr_userId + \
                            "' and activationTime > '2016-09-01' and activationTime < '2016-11-02' and imei like '%" + \
                            basic_info["imei"] + "%';"

        cur.execute(get_result_sql_01)

        # 读取数据
        curr_dev_01 = cur.fetchall()
        total_list = []
        for range1 in curr_dev_01:
            for range2 in range1:
                total_list.append(range2)

        # 从数据tuple中获取当前所选用户+基本信息+激活时间匹配的设备个数
        dev_count_01 = len(total_list)

        print("当前所选用户+基本信息+激活时间匹配的设备共：" + str(dev_count_01) + "条!")

        # 执行sql脚本，通过当前所选用户+基本信息+平台到期时间查找所有匹配记录
        get_result_sql_03 = "select id from assets_device where userId = '" + curr_userId + \
                            "'  and deviceName like '%" + basic_info[
                                "deviceName"] + "%' and expiration > '2017-02-01' and expiration < '2037-10-23';"

        cur.execute(get_result_sql_03)

        # 读取数据
        curr_dev_03 = cur.fetchall()
        total_list = []
        for range1 in curr_dev_03:
            for range2 in range1:
                total_list.append(range2)

        # 从数据tuple中获取当前所选用户+基本信息+平台到期时间匹配的设备个数
        dev_count_03 = len(total_list)

        print("当前所选用户+基本信息+平台到期时间匹配的设备共：" + str(dev_count_03) + "条!")

        # 选择用户
        self.global_complex_search_page.complex_search_select_acc("test_007")

        # 编辑基本信息
        self.global_complex_search_page.complex_search_select_basic_info("imei", basic_info["imei"])

        # 编辑日期信息
        self.global_complex_search_page.complex_search_select_date_type("激活时间", "2016-09-01", "2016-11-02")

        # 点击搜索按钮
        self.global_complex_search_page.complex_search_click()
        self.driver.wait(3)

        # 获取当前共多少条搜索结果
        dev_num_01 = self.global_complex_search_page.complex_search_result()

        # 验证当前搜索结果个数与数据库查询结果是否一致
        self.assertEqual(dev_count_01, dev_num_01, "当前搜索结果个数与数据库查询结果不一致")

        # 重置搜索条件
        self.global_complex_search_page.complex_search_reset()

        self.driver.wait()

        # 选择用户
        self.global_complex_search_page.complex_search_select_acc("test_007")

        # 编辑基本信息
        self.global_complex_search_page.complex_search_select_basic_info("deviceName", basic_info["deviceName"])

        # 编辑日期信息
        self.global_complex_search_page.complex_search_select_date_type("平台到期时间", "2017-02-01", "2037-10-23")

        # 点击搜索按钮
        self.global_complex_search_page.complex_search_click()
        self.driver.wait(3)

        # 获取当前共多少条搜索结果
        dev_num_03 = self.global_complex_search_page.complex_search_result()

        # 验证当前搜索结果个数与数据库查询结果是否一致
        self.assertEqual(dev_count_03, dev_num_03, "当前搜索结果个数与数据库查询结果不一致")

        self.driver.wait()

        # 关闭当前高级搜索对话框
        self.global_complex_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()