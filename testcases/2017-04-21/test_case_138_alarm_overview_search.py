import csv
import unittest

import time

import pymysql

from automate_driver.automate_driver import AutomateDriver
from pages.alarm_info.alarm_info_page import AlarmInfoPage
from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.command_management.command_management_page import CommandManagementPage
from pages.login.login_page import LoginPage


class TestCase138AlarmOverviewSearch(unittest.TestCase):
    '''
    用例第138条，告警总览页面搜索
    author：zhangAo
    '''

    def setUp(self):
        # 前置条件
        # 实例化对象
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.log_in_page = LoginPage(self.driver, self.base_url)
        self.command_management_page = CommandManagementPage(self.driver, self.base_url)
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
        self.alarm_info_page = AlarmInfoPage(self.driver, self.base_url)

        # 打开页面，填写用户名、密码、点击登录
        self.base_page.open_page()
        self.driver.set_window_max()
        self.driver.implicitly_wait(5)
        self.driver.clear_cookies()
        self.log_in_page.account_input('jimitest')
        self.log_in_page.password_input('jimi123')
        self.log_in_page.remember_me()
        self.log_in_page.login_button_click()
        self.driver.implicitly_wait(5)

        # 登录之后点击控制台，然后点击指令管理
        self.alarm_info_page.click_control_after_click_alarm_info()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit_browser()

    def test_case_138_alarm_overview_search(self):
        # 断言url
        expect_url = self.base_url + '/alarmInfo/toAlarmInfo'
        self.assertEqual(expect_url, self.alarm_info_page.actual_url_click_alarm())
        # 断言文本
        expect_text = '告警'
        self.assertEqual(expect_text, self.alarm_info_page.actual_text_alick_alarm())

        # 点击告警总览
        self.alarm_info_page.click_lift_list('alarm_info')
        # 断言文本
        expect_text_after_click_alarm = '告警总览'
        self.assertEqual(expect_text_after_click_alarm, self.alarm_info_page.actual_text_click_alarm_info())
        # 测试日期
        self.alarm_info_page.click_choose_date('today')
        # 断言第一个时间
        self.assertEqual(self.alarm_info_page.get_current_date(), self.alarm_info_page.get_first_time())
        # 断言第二个时间
        self.assertEqual(self.alarm_info_page.get_current_date_with_time(), self.alarm_info_page.get_second_time())

        # 点击昨天
        self.alarm_info_page.click_choose_date('yesterday')
        # 断言第一个时间
        self.assertEqual(self.alarm_info_page.get_first_yesterday_day(), self.alarm_info_page.get_first_time())
        self.assertEqual(self.alarm_info_page.get_second_yesterday_day(), self.alarm_info_page.get_second_time())

        # 点击本周
        self.alarm_info_page.click_choose_date('this_work')
        # 断言
        self.assertEqual(self.alarm_info_page.get_week_first_time(), self.alarm_info_page.get_first_time())
        self.assertEqual(self.alarm_info_page.get_week_sencond_time(), self.alarm_info_page.get_second_time())

        # 点击上周
        self.alarm_info_page.click_choose_date('last_week')
        self.assertEqual(self.alarm_info_page.get_last_week_first_time(), self.alarm_info_page.get_first_time())
        self.assertEqual(self.alarm_info_page.get_last_week_second_time(), self.alarm_info_page.get_second_time())

        # 本月
        self.alarm_info_page.click_choose_date('this_month')
        self.assertEqual(self.alarm_info_page.get_this_mouth_first_time(), self.alarm_info_page.get_first_time())
        self.assertEqual(self.alarm_info_page.get_week_sencond_time(), self.alarm_info_page.get_second_time())

        # 上月
        self.alarm_info_page.click_choose_date('last_month')
        self.assertEqual(self.alarm_info_page.get_last_month_first_time(), self.alarm_info_page.get_first_time())
        self.assertEqual(self.alarm_info_page.get_last_month_second_time(), self.alarm_info_page.get_second_time())
        # 选择报警类型
        time.sleep(2)
        self.alarm_info_page.click_all_alarm_type()
        time.sleep(2)
        # 输入数据搜索
        csv_file = open('E:\git\\tuqiangol_test\data\\alarm_info\\alarm_overview_search_data.csv', 'r',
                        encoding='utf8')
        csv_data = csv.reader(csv_file)
        is_header = True
        for row in csv_data:
            if is_header:
                is_header = False
                continue
            data = {
                'user_name': row[0],
                'choose_date': row[1],
                'began_time': row[2],
                'end_time': row[3]
            }
            self.alarm_info_page.add_data_to_search_in_alarm_overview(data)
            # 连接数据库
            connect = pymysql.connect(
                host='172.16.0.100',
                port=3306,
                user='tracker',
                passwd='tracker',
                db='tracker-web-mimi',
                charset='utf8'
            )
            # 创建游标
            cursor = connect.cursor()
            # 查询搜索用户的uesrID
            get_user_id_sql = "SELECT user_organize.userId FROM user_organize WHERE user_organize.account ='" + data[
                'user_name'] + "';"
            # 执行sql
            cursor.execute(get_user_id_sql)
            get_user_id = cursor.fetchall()
            user_id = get_user_id[0][0]

            # 当前用户下设置
            get_current_user_all_equipment = "SELECT a.imei FROM assets_device AS a WHERE a.userId = " + user_id + " and a.expiration > CURDATE();"
            cursor.execute(get_current_user_all_equipment)
            all_equipment = cursor.fetchall()

            all_equipment_list = []
            for range1 in all_equipment:
                for range2 in range1:
                    all_equipment_list.append(range2)

            current_user_all_equipment = tuple(all_equipment_list)

            cursor.close()
            connect.close()
            time.sleep(5)
            # 连接另一个数据库
            connect_02 = pymysql.connect(
                host='172.16.0.116',
                port=8066,
                user='jimi',
                passwd='jimi',
                db='his',
                charset='utf8'
            )
            # 创建游标
            cursor_02 = connect_02.cursor()

            get_total_sql = "SELECT b.imei FROM(SELECT a.IMEI,a.CREATETIME FROM alarm_info AS a WHERE a.CREATETIME BETWEEN  '" + self.alarm_info_page.get_first_time() + "' AND  '" + self.alarm_info_page.get_second_time() + "' and a.imei in " + str(
                current_user_all_equipment) + " and a.USER_ID = " + user_id + " GROUP BY a.IMEI) b"
            # 执行sql
            cursor_02.execute(get_total_sql)
            get_total = cursor_02.fetchall()
            total_list = []
            for range1 in get_total:
                for range2 in range1:
                    total_list.append(range2)
            total = len(total_list)

            # 查询web端的总条数
            web_total = self.alarm_info_page.get_web_total_in_overview_search()
            # 断言
            self.assertEqual(total, web_total)
            cursor_02.close()
            connect_02.close()
        csv_file.close()
