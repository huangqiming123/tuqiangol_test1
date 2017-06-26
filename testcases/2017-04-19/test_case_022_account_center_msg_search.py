import unittest

import pymysql
from pages.account_center.account_center_msg_center_page import AccountCenterMsgCenterPage

from automate_driver.automate_driver import AutomateDriver
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page import BasePage
from pages.login.login_page import LoginPage


# 账户中心-消息中心-根据搜索条件来搜索消息
# author:孙燕妮

class TestCase022AccountCenterMsgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_msg_center = AccountCenterMsgCenterPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_msg_search(self):
        '''通过mysql测试消息中心-根据搜索条件来搜索消息功能'''

        connect = pymysql.connect(host="172.16.0.100",
                                  port=3306,
                                  user="tracker",
                                  passwd="tracker",
                                  db="tracker-web-mimi")

        # 创建数据库游标
        cur = connect.cursor()

        # 执行sql脚本查询当前登录账号的消息-设备离线、已读、imei=868120132482941
        get_msg_sql = "select m.id from user_message m inner join user_organize o on o.userId = m.userId" \
                      " where o.account = 'jimitest' and m.type = '2' and m.readFlag = '1' and m.imeis = '868120145233604';"
        cur.execute(get_msg_sql)

        # 读取数据
        data = cur.fetchall()
        total_list = []
        for range1 in data:
            for range2 in range1:
                total_list.append(range2)
        msg_num = len(total_list)

        # 打开途强在线首页-登录页
        self.base_page.open_page()

        # 登录
        self.login_page.user_login("jimitest", "jimi123")

        # 进入消息中心
        self.account_center_page_msg_center.enter_msg_center()

        # 获取消息中心title
        msg_center_title = self.account_center_page_msg_center.get_msg_center_title()

        # 验证消息中心title是否正确显示
        self.assertIn("消息中心", msg_center_title, "消息中心title有误!")

        # 设置搜索条件，统计搜索结果
        # 选中已读
        self.account_center_page_msg_center.set_search_status_read()
        # 选中设备离线
        self.account_center_page_msg_center.set_search_type("设备离线")
        # 输入imei
        self.account_center_page_msg_center.set_search_imei("868120145233604")

        # 搜索结果
        self.account_center_page_msg_center.click_search()

        '''# 统计当前搜索结果列表共几条消息
        # 设置每页10条
        self.account_center_page_msg_center.select_per_page_number("10")
        # 获取当前共几页
        total_pages_num = self.account_center_page_msg_center.get_total_pages_num()
        # 获取最后一页有几条记录
        last_page_logs_num = self.account_center_page_msg_center.last_page_logs_num()
        # 计算搜索结果消息列表消息共几条
        count_search_msg_num = (int(total_pages_num) - 1) * 10 + last_page_logs_num'''
        count_search_msg_num = self.account_center_page_msg_center.get_total_unread_logs_num()
        # 验证搜索结果列表数据与数据库查询结果是否一致
        self.assertEqual(msg_num, count_search_msg_num, "搜索结果列表数据与数据库查询结果不一致")

        # 退出登录
        self.account_center_page_navi_bar.usr_logout()
        cur.close()
        connect.close()
