import unittest

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.global_search.global_complex_search_page import GlobalComplexSearchPage
from pages.login.login_page import LoginPage


# 全局搜索-高级搜索-通过选择用户-基本信息+日期类型+设备状态全组合查找

# author:孙燕妮

class TestCase057GlobComplexSearchByAllCondi(unittest.TestCase):
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

    def test_glob_complex_search_by_all_condi(self):
        '''测试全局搜索-高级搜索-通过选择用户-基本信息+日期类型+设备状态全组合查找功能'''

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("test_007", "jimi123")

        # 点击全局搜索栏-高级搜素按钮
        self.global_complex_search_page.click_complex_search()

        basic_info = {
            "imei": "12"
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

        # 执行sql脚本，通过当前所选基本信息+激活时间+设备状态-欠费 查找所有匹配记录
        get_result_sql_01 = "select e.id from assets_device_expiration  e " \
                            "left join assets_device d  on e.imei = d.imei where d.userId = '" + curr_userId + \
                            "'  and CURDATE() > e.expiration and d.activationTime > '2016-02-08' and d.activationTime < '2017-02-24'" \
                            "and d.imei like '%" + basic_info["imei"] + "%' group by d.imei;"

        cur.execute(get_result_sql_01)

        # 读取数据
        curr_dev_01 = cur.fetchall()
        total_list = []
        for range1 in curr_dev_01:
            for range2 in range1:
                total_list.append(range2)

        # 从数据tuple中获取当前所选基本信息+激活时间+欠费状态的设备个数
        dev_count_01 = len(total_list)

        print("当前所选基本信息+激活时间+欠费状态的设备共：" + str(dev_count_01) + "条!")

        # 选择用户
        self.global_complex_search_page.complex_search_select_acc("test_007")

        # 编辑基本信息
        self.global_complex_search_page.complex_search_select_basic_info("imei", basic_info["imei"])

        # 编辑日期信息
        self.global_complex_search_page.complex_search_select_date_type("激活时间", "2016-02-08", "2017-02-24")

        # 勾选设备状态-欠费
        self.global_complex_search_page.complex_search_select_dev_status("欠费")

        # 点击搜索按钮
        self.global_complex_search_page.complex_search_click()
        self.driver.wait(3)

        # 获取当前共多少条搜索结果
        dev_num_01 = self.global_complex_search_page.complex_search_result()

        # 验证当前搜索结果个数与数据库查询结果是否一致
        self.assertEqual(dev_count_01, dev_num_01, "当前搜索结果个数与数据库查询结果不一致")

        # 关闭当前高级搜索对话框
        self.global_complex_search_page.close_dev_search()

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
