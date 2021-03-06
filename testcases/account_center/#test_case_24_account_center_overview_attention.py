import unittest
from time import sleep
from automate_driver.automate_driver_server import AutomateDriverServer
from model.assert_text import AssertText
from model.connect_sql import ConnectSql
from pages.account_center.account_center_details_page import AccountCenterDetailsPage
from pages.account_center.account_center_navi_bar_page import AccountCenterNaviBarPage
from pages.base.base_page_server import BasePageServer
from pages.base.lon_in_base_server import LogInBaseServer
from pages.login.login_page import LoginPage


# 账户中心-账户详情-账户总览   重点关注车辆
# author:zhangao

class TestCase24AccountCenterOverviewAttention(unittest.TestCase):
    def setUp(self):
        self.driver = AutomateDriverServer(choose='chrome')
        self.base_url = self.driver.base_url
        self.base_page = BasePageServer(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.account_center_page_details = AccountCenterDetailsPage(self.driver, self.base_url)
        self.account_center_page_navi_bar = AccountCenterNaviBarPage(self.driver, self.base_url)
        self.driver.set_window_max()
        self.log_in_base = LogInBaseServer(self.driver, self.base_url)
        self.assert_text = AssertText()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_account_center_overview_attention(self):
        # 打开途强在线首页-登录页
        self.base_page.open_page()
        # 登录账号
        self.log_in_base.log_in()
        self.account_center_page_navi_bar.click_account_center_button()
        current_account = self.log_in_base.get_log_in_account()
        sleep(2)
        account_center_handle = self.driver.get_current_window_handle()

        self.account_center_page_details.account_center_iframe()
        actual_total_attention = self.account_center_page_details.get_actual_total_attention()
        # 点击库存
        self.account_center_page_details.account_overview('重点关注车辆')
        self.driver.default_frame()

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
                get_id_sql = "select userId from user_info where account = '" + current_account + "' ;"
                cur.execute(get_id_sql)
                # 读取数据
                user_relation = cur.fetchall()
                print(user_relation)
                user_id = user_relation[0][0]
                # actual_url = self.base_url + '/console?userId=%s&viewFlag=4' % user_id
                actual_url = self.base_url + '/console?viewFlag=4'
                cur.close()
                connect.close()
                self.assertEqual(expect_url, actual_url, '点击重点关注车辆后，实际的url和期望的不一样！')
                sleep(2)

                # 断言已关注被选中
                self.assertEqual('active', self.driver.get_element('x,//*[@id="FOLLOW"]').get_attribute('class'))

                expect_total_inactive = self.account_center_page_details.get_total_all_attention_equipment()
                self.assertEqual(actual_total_attention, expect_total_inactive, '账号重点关注车辆数量错误')

                # 查看控制台告警设置能否打开
                self.account_center_page_navi_bar.click_alarm_button_in_console()
                # 断言
                get_text = self.account_center_page_navi_bar.get_text_after_click_alarm_button()
                self.assertEqual(self.assert_text.account_center_page_alarm_manager_text(), get_text)
                self.account_center_page_navi_bar.close_alarm_in_console()

                self.driver.close_current_page()
                # 回到账户中心窗口
                self.driver.switch_to_window(account_center_handle)
                self.driver.wait()

        # 退出登录
                # self.account_center_page_navi_bar.usr_logout()
