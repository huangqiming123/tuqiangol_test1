from time import sleep
import time

import datetime

import math

from pages.base.base_page import BasePage
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class StatisticalFormPage(BasePage):
    '''
    控制台统计报表页面的page
    author:zhangAo
    :return
    '''

    def click_control_after_click_statistical_form_page(self):
        # 点击控制中心之后点击设置

        self.driver.click_element('x,//*[@id="reportsManagement"]/a')
        sleep(2)

    def actual_url_after_statistical_form(self):
        # 获取真实的url ，点击统计报表之后
        actual_url = self.driver.get_current_url()
        return actual_url

    def add_user_name_or_account_to_search(self, search_data):
        # 填写要搜索的用户名称或者账号搜索
        self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['name_or_account'])
        # 点击搜索
        sleep(2)
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
        sleep(5)

    def get_web_search_total_number(self):
        # 获取页面搜索出的条数
        try:
            # 通过classname获取搜索结果列表
            ele_list = self.driver.get_elements("c,autocompleter-item")
            search_result_num = len(ele_list)
            return search_result_num

        except:
            print("当前模糊查找无结果")
            return 0

    def switch_to_sport_overview_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="sportOverviewFrame"]')

    def actual_text_after_click_sport_overview(self):
        # 获取页面右侧左上角的文本
        self.switch_to_sport_overview_form_frame()
        actual_text = self.driver.get_text('x,/html/body/div/div[1]/div/b')
        self.driver.default_frame()
        return actual_text

    def add_data_to_search_sport_overview(self, search_data):
        # 搜索用户
        # self.driver.switch_to_frame('x,//*[@id="sportOverviewFrame"]')
        self.switch_to_sport_overview_form_frame()
        # 搜索用户
        self.driver.click_element('x,//*[@id="runForm"]/div[3]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        sleep(2)
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/span[2]')
        sleep(2)
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/div/ul/li[2]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/div/ul/li[3]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/div/ul/li[4]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/div/ul/li[5]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/div/ul/li[6]')
        elif search_data['choose_date'] == '':
            # 填写
            self.driver.click_element('x,//*[@id="runForm"]/div[1]/div/div/div/div/ul/li[1]')
            self.driver.operate_input_element('x,//*[@id="startTime_sport"]', search_data['begin_time'])
            # 填写结束时间
            self.driver.operate_input_element('x,//*[@id="endTime_sport"]', search_data['end_time'])

        self.driver.click_element('x,//*[@id="runForm"]/div[4]/button')
        sleep(10)

        self.driver.default_frame()
        '''
        # 选择要搜索的日期去搜索运动总览
        if search_data['search_user'] != '':
            self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['search_user'])
            sleep(2)
            self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
            sleep(1)
            self.driver.click_element('c,autocompleter-item')

        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element('x,//*[@id="Yesterday_mileage"]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element('x,//*[@id="ThisWeek_mileage"]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element('x,//*[@id="LastWeek_mileage"]')
        elif search_data['choose_date'] == 'this_mouth':
            # 本月
            self.driver.click_element('x,//*[@id="ThisMonth_mileage"]')
        elif search_data['choose_date'] == 'last_mouth':
            # 上月
            self.driver.click_element('x,//*[@id="LastMonth_mileage"]')
        elif search_data['choose_date'] == '':
            # 填写
            # 填写开始时间
            js = 'document.getElementById("startTime_sport").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_sport"]', search_data['begin_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_sport").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_sport"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="runForm"]/div[2]/button')
        sleep(5)'''

    def get_today_begin_date(self):
        # 获取今天的开始时间
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return current_time + " 00:00"

    def get_today_end_time(self):
        # 今天的结束时间
        current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        return current_time

    def get_yesterday_begin_time(self):
        # 获取昨天的开始时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        first = str(yes) + " 00:00"
        return first

    def get_yesterday_end_time(self):
        # 获取昨天的结束时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        second = str(yes) + " 23:59"
        return second

    def get_this_week_begin_time(self):
        # 获取本周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.isoweekday() - 1))
        week = today - days_count
        return str(week) + ' 00:00'

    def get_this_week_end_time(self):
        # 获取本周的结束时间
        today = datetime.date.today()
        return str(today) + ' 23:59'

    def get_last_week_begin_time(self):
        # 获取上周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count - datetime.timedelta(days=6)
        return str(week) + ' 00:00'

    def get_last_week_end_time(self):
        # 获取上周的结束时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count
        return str(week) + ' 23:59'

    def get_this_month_begin_time(self):
        # 获取本月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.day - 1))
        this_month = today - days_count
        return str(this_month) + " 00:00"

    def get_this_month_end_time(self):
        # 获取今天的开始时间
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return current_time + " 23:59"

    def get_last_month_begin_time(self):
        # 获取上月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        month = datetime.date(last_month.year, last_month.month, 1)
        return str(month) + " 00:00"

    def get_last_month_end_time(self):
        # 获取上月的结束
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        return str(last_month) + " 23:59"

    def get_total_search_sport_overview(self):
        # 获取页面的总条数
        try:
            last_page_logs = list(self.driver.get_elements('x,//*[@id="run-tbody"]/tr'))
            last_page_logs_num = len(last_page_logs)
            return last_page_logs_num
        except:
            return 0

    def export_sport_overview_data(self):
        total = self.get_total_search_sport_overview()
        if total == 0:
            pass
        else:
            self.driver.click_element('x,//*[@id="runForm"]/div[5]/button')
            sleep(3)

    def click_mileage_form_button(self):
        # 点击里程报表按钮
        self.driver.click_element('x,//*[@id="tracelReport"]/a')
        sleep(3)

    def switch_to_tracel_report_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="tracelReportFrame"]')

    def actual_text_after_click_mileage_form_button(self):
        # 点击里程报表后，获取页面左上角的文本
        self.switch_to_tracel_report_form_frame()
        actual_text = self.driver.get_text('x,/html/body/div/div[1]/div/b')
        self.driver.default_frame()
        return actual_text

    def add_data_to_search_mileage_form(self, search_data):
        # self.driver.switch_to_frame('x,//*[@id="tracelReportFrame"]')
        self.switch_to_tracel_report_form_frame()
        # 选择用户
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_travelReport"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_travelReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_travelReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_travelReport"]/div[2]/div/button[1]')

        # 选择类型
        if search_data['type'] == 'day':
            self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[3]/label[3]/div/ins')

        # 选择日期
        if search_data['type'] == 'mile':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
            sleep(2)
            if search_data['choose_date'] == 'yesterday':
                # 选择昨天
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')
            elif search_data['choose_date'] == 'this_week':
                # 选择这周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')
            elif search_data['choose_date'] == 'last_week':
                # 上周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')
            elif search_data['choose_date'] == 'this_month':
                # 本月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
            elif search_data['choose_date'] == 'last_month':
                # 上月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')
            elif search_data['choose_date'] == '':
                # 填写
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
                # 填写开始时间
                self.driver.operate_input_element('x,//*[@id="startTime_travel"]', search_data['begin_time'])
                # 填写结束时间
                self.driver.operate_input_element('x,//*[@id="endTime_travel"]', search_data['end_time'])
            elif search_data['choose_date'] == 'today':
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif search_data['type'] == 'day':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
            sleep(2)
            if search_data['choose_date'] == 'yesterday':
                # 选择昨天
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')
            elif search_data['choose_date'] == 'this_week':
                # 选择这周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')
            elif search_data['choose_date'] == 'last_week':
                # 上周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')
            elif search_data['choose_date'] == 'this_month':
                # 本月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')
            elif search_data['choose_date'] == 'last_month':
                # 上月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
            elif search_data['choose_date'] == '':
                # 填写
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
                # 填写开始时间
                self.driver.operate_input_element('x,//*[@id="startTime_travel"]', search_data['begin_time'])
                # 填写结束时间
                self.driver.operate_input_element('x,//*[@id="endTime_travel"]', search_data['end_time'])

        # 点击搜索
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[3]/button')
        sleep(5)
        self.driver.default_frame()
        '''
        # 填写要搜索的数据去搜索里程报表
        if search_data['search_user'] != '':
            self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['search_user'])
            sleep(2)
            self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
            sleep(1)
            self.driver.click_element('c,autocompleter-item')

        # 点击搜索设备
        self.driver.clear_input('x,//*[@id="imeiInput_mileageReport"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[1]/div/div/div/div[1]/span/button/i')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_mileageReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))

        self.driver.click_element('x,//*[@id="treeModal_mileageReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_mileageReport"]/div[2]/div/button[1]')
        sleep(3)

        # 选择类型
        if search_data['type'] == 'day':
            self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[2]/label[3]/div/ins')

        # 选择日期
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[2]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[3]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[4]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[5]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[6]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[1]')
        elif search_data['choose_date'] == '':
            # 填写
            # 填写开始时间
            js = 'document.getElementById("startTime_mileage").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_mileage"]', search_data['begin_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_mileage").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_mileage"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[2]/button')
        sleep(5)'''

    def get_total_search_mileage_form(self):
        # 计算里程报表查询出来的总条数
        try:
            self.new_paging = NewPaging(self.driver, self.base_url)
            num = self.new_paging.get_total_number('x,//*[@id="paging-mileage"]', 'x,//*[@id="mileage-tbody"]')
            return num
        except:
            return 0

    def get_total_search_mileage_form_with_day(self):
        # 计算里程报表查询出来的总条数
        try:
            self.new_paging = NewPaging(self.driver, self.base_url)
            num = self.new_paging.get_total_number('x,//*[@id="paging-day"]', 'x,//*[@id="mileage-day-tbody"]')
            return num
        except:
            return 0

    def click_over_speed_button(self):
        # 　点击超速报表
        self.driver.click_element('x,//*[@id="speedingReport"]/a')
        sleep(5)

    def switch_to_speeding_report_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="speedingReportFrame"]')

    def actual_text_after_click_over_speed_button(self):
        # 点击超速报警后，获取页面右侧的文本
        self.switch_to_speeding_report_form_frame()
        actual_text = self.driver.get_text('x,/html/body/div/div[1]/div/b')
        self.driver.default_frame()
        return actual_text

    def add_data_to_search_over_speed(self, search_data):
        # 选择用户
        # self.driver.switch_to_frame('x,//*[@id="speedingReportFrame"]')
        self.switch_to_speeding_report_form_frame()
        # 选择用户
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_overSpeedReport"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_overSpeedReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_overSpeedReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_overSpeedReport"]/div[2]/div/button[1]')

        # 填写超速的速度
        self.driver.operate_input_element('x,//*[@id="OverspeedFrom"]/div[1]/div[3]/input', search_data['speed'])
        # 选择日期
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/span[2]')
        sleep(2)
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[3]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[4]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[5]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[6]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[7]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[2]')
        elif search_data['choose_date'] == '':
            # 填写
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div[1]/div/div/div/div/ul/li[1]')
            # 填写开始时间
            self.driver.operate_input_element('x,//*[@id="startTime_overspeed"]', search_data['begin_time'])
            # 填写结束时间
            self.driver.operate_input_element('x,//*[@id="endTime_overspeed"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[3]/button')
        sleep(5)

        self.driver.default_frame()
        # 添加数据去搜索超速
        '''
        if search_data['search_user'] != '':
            self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['search_user'])
            sleep(2)
            self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
            sleep(1)
            self.driver.click_element('c,autocompleter-item')

        # 点击搜索设备
        self.driver.clear_input('x,//*[@id="imeiInput_overSpeedReport"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[1]/div/div/div/div/div[1]/span/button/i')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_overSpeedReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[1]/div/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                            n + 1))

        self.driver.click_element('x,//*[@id="treeModal_overSpeedReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_overSpeedReport"]/div[2]/div/button[1]')
        sleep(3)

        # 填写超速的速度
        self.driver.operate_input_element('x,//*[@id="OverspeedFrom"]/div[1]/div/input', search_data['speed'])
        # 选择日期
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[2]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[3]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[4]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[5]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[6]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/form/div[2]/div[1]/div[1]/button[1]')
        elif search_data['choose_date'] == '':
            # 填写
            # 填写开始时间
            js = 'document.getElementById("startTime_overspeed").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_overspeed"]', search_data['begin_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_overspeed").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_overspeed"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[2]/button')
        sleep(5)'''

    def get_total_search_over_speed_number(self):
        # 获取搜索出来的超速的条数
        try:
            total = self.total_num(self.get_actual_pages_number(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[3]/div[1]'),
                self.last_page_logs_num(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[3]/table/tbody',
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[3]/div[2]/div[3]/div[1]'))
            return total

        except:
            return 0

    def click_stay_form_button(self):
        # 点击停留报表
        self.driver.click_element('x,//*[@id="stayReport"]/a')
        sleep(5)

    def switch_to_stay_report_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="stayReportFrame"]')

    def actual_text_after_click_stay_form_button(self):
        # 点击停留报表后，获取页面左上角的文本
        self.switch_to_stay_report_form_frame()
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return actual_text

    def add_data_to_search_stay_form(self, search_data):
        # 输入数据去搜索 停留的报表
        # 选择用户
        # self.driver.switch_to_frame('x,//*[@id="stayReportFrame"]')
        self.switch_to_stay_report_form_frame()
        # 选择用户
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_stopCar"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_stopCar"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_stopCar"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_stopCar"]/div[2]/div/button[1]')
        # 选择日期
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/span[2]')
        sleep(2)
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[3]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[4]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[5]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[6]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[7]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[2]')
        elif search_data['choose_date'] == '':
            # 填写
            self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[1]')
            # 填写开始时间
            self.driver.operate_input_element('x,//*[@id="startTime_stopCar"]', search_data['begin_time'])
            # 填写结束时间
            self.driver.operate_input_element('x,//*[@id="endTime_stopCar"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[3]/button')
        sleep(5)

        self.driver.default_frame()
        '''

        if search_data['search_user'] != '':
            self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['search_user'])
            sleep(2)
            self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
            sleep(1)
            self.driver.click_element('c,autocompleter-item')

        # 点击搜索设备
        self.driver.clear_input('x,//*[@id="imeiInput_stopCar"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div[1]/span/button/i')
        sleep(1)
        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_stopCar"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                            n + 1))
        self.driver.click_element('x,//*[@id="treeModal_stopCar"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_stopCar"]/div[2]/div/button[1]')
        sleep(3)

        # 选择日期
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopCar"]/button[2]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopCar"]/button[3]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopCar"]/button[4]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopCar"]/button[5]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopCar"]/button[6]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopCar"]/button[1]')
        elif search_data['choose_date'] == '':
            # 填写
            # 填写开始时间
            js = 'document.getElementById("startTime_stopCar").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_stopCar"]', search_data['begin_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_stopCar").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_stopCar"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[2]/button')
        sleep(5)'''

    def get_total_search_stay_form_number(self):
        # 获取搜索出来的停留的条数
        try:
            self.new_paging = NewPaging(self.driver, self.base_url)
            total = self.new_paging.get_total_number('x,//*[@id="paging-stopCar"]', 'x,//*[@id="stopCar-tbody"]')
            return total

        except:
            return 0

    def click_paking_not_shut_down_form_button(self):
        # 点击停车位熄火报警
        self.driver.click_element('x,//*[@id="parkingReport"]/a')
        sleep(3)

    def switch_to_parking_report_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="parkingReportFrame"]')

    def actual_text_after_click_paking_not_shut_down_button(self):
        # 点击停车未熄火报表后，返回右侧页面抬头的文字
        self.switch_to_parking_report_form_frame()
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return actual_text

    def add_data_to_search_paking_not_shut_down_form(self, search_data):
        # 输入数据去搜索 停留的报表
        # 选择用户
        # self.driver.switch_to_frame('x,//*[@id="parkingReportFrame"]')
        self.switch_to_parking_report_form_frame()
        # 选择用户
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_stopNotOff"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_stopNotOff"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(2)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_stopNotOff"]/div[2]/label/div/ins')
        sleep(2)
        self.driver.click_element('x,//*[@id="treeModal_stopNotOff"]/div[2]/div/button[1]')
        # 选择日期
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/span[2]')
        sleep(2)
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[3]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[4]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[5]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[6]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[7]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[2]')
        elif search_data['choose_date'] == '':
            # 填写
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[1]')
            # 填写开始时间
            self.driver.operate_input_element('x,//*[@id="startTime_stopNotOff"]', search_data['begin_time'])
            # 填写结束时间
            self.driver.operate_input_element('x,//*[@id="endTime_stopNotOff"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[3]/button')
        sleep(5)
        self.driver.default_frame()
        '''
        if search_data['search_user'] != '':
            self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['search_user'])
            sleep(2)
            self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
            sleep(1)
            self.driver.click_element('c,autocompleter-item')

        # 点击搜索设备
        self.driver.clear_input('x,//*[@id="imeiInput_stopNotOff"]')
        sleep(1)
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div[1]/span/button/i')
        sleep(1)
        all_group_list = list(self.driver.get_elements(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                            n + 1))
        self.driver.click_element('x,//*[@id="treeModal_stopNotOff"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_stopNotOff"]/div[2]/div/button[1]')
        sleep(3)

        # 选择日期
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopNotOff"]/button[2]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopNotOff"]/button[3]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopNotOff"]/button[4]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopNotOff"]/button[5]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopNotOff"]/button[6]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element(
                    'x,//*[@id="qucikTime_stopNotOff"]/button[1]')
        elif search_data['choose_date'] == '':
            # 填写
            # 填写开始时间
            js = 'document.getElementById("startTime_stopNotOff").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_stopNotOff"]', search_data['begin_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_stopNotOff").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_stopNotOff"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[2]/button')
        sleep(5)'''

    def get_total_search_paking_not_shut_down_number(self):
        # 获取停车未熄火查询出的条数
        try:
            self.new_paging = NewPaging(self.driver, self.base_url)
            num = self.new_paging.get_total_number('x,//*[@id="paging-stopNotOff"]', 'x,//*[@id="stopNotOff-tbody"]')
            return num
        except:
            return 0

    def click_acc_form_button(self):
        # 点击acc报表
        self.driver.click_element('x,//*[@id="AccReport"]/a')
        sleep(3)

    def switch_to_acc_report_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="AccReportFrame"]')

    def actual_text_after_click_acc_button(self):
        # 点击acc报表
        self.switch_to_acc_report_form_frame()
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return actual_text

    def add_data_to_search_acc_form(self, search_data):
        # 　输入数据去搜索acc报表
        # 选择用户
        # self.driver.switch_to_frame('x,//*[@id="AccReportFrame"]')
        self.switch_to_acc_report_form_frame()
        # 选择用户
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[1]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_acc"]')
        sleep(1)
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/span/button/i')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_acc"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_acc"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_acc"]/div[2]/div/button[1]')
        # 选择日期
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/span[2]')
        sleep(1)
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[3]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[4]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[5]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[6]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[7]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[2]')
        elif search_data['choose_date'] == '':
            # 填写
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[1]')
            # 填写开始时间
            self.driver.operate_input_element('x,//*[@id="startTime_acc"]', search_data['begin_time'])
            # 填写结束时间
            self.driver.operate_input_element('x,//*[@id="endTime_acc"]', search_data['end_time'])

            # 选择状态
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[3]/div/span/div/span[2]')
        sleep(1)
        if search_data['status'] == '':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[3]/div/span/div/div/ul/li[1]')

        elif search_data['status'] == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[3]/div/span/div/div/ul/li[2]')

        elif search_data['status'] == '0':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[3]/div/span/div/div/ul/li[3]')
        # 点击搜索
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[3]/button')
        sleep(5)
        self.driver.default_frame()
        '''
        if search_data['search_user'] != '':
            self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', search_data['search_user'])
            sleep(2)
            self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
            sleep(1)
            self.driver.click_element('c,autocompleter-item')

        # 点击搜索设备
        self.driver.clear_input('x,//*[@id="imeiInput_acc"]')
        sleep(1)
        self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[1]/span/button/i')
        sleep(1)

        all_group_list = list(self.driver.get_elements(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                            n + 1))

        self.driver.click_element('x,//*[@id="treeModal_acc"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_acc"]/div[2]/div/button[1]')
        sleep(3)

        # 选择状态
        self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[2]/div/span/div/span[2]')
        sleep(1)
        if search_data['status'] == '':
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[2]/div/span/div/div/ul/li[1]')

        elif search_data['status'] == '1':
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[2]/div/span/div/div/ul/li[2]')

        elif search_data['status'] == '0':
            self.driver.click_element(
                    'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[1]/div[2]/div/span/div/div/ul/li[3]')

        sleep(1)

        # 选择日期
        if search_data['choose_date'] == 'yesterday':
            # 选择昨天
            self.driver.click_element(
                    'x,//*[@id="qucikTime_acc"]/button[2]')
        elif search_data['choose_date'] == 'this_week':
            # 选择这周
            self.driver.click_element(
                    'x,//*[@id="qucikTime_acc"]/button[3]')
        elif search_data['choose_date'] == 'last_week':
            # 上周
            self.driver.click_element(
                    'x,//*[@id="qucikTime_acc"]/button[4]')
        elif search_data['choose_date'] == 'this_month':
            # 本月
            self.driver.click_element(
                    'x,//*[@id="qucikTime_acc"]/button[5]')
        elif search_data['choose_date'] == 'last_month':
            # 上月
            self.driver.click_element(
                    'x,//*[@id="qucikTime_acc"]/button[6]')
        elif search_data['choose_date'] == 'today':
            # 今天
            self.driver.click_element(
                    'x,//*[@id="qucikTime_acc"]/button[1]')
        elif search_data['choose_date'] == '':
            # 填写
            # 填写开始时间
            js = 'document.getElementById("startTime_acc").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_acc"]', search_data['begin_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_acc").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_acc"]', search_data['end_time'])
        # 点击搜索
        self.driver.click_element(
                'x,/html/body/div[2]/div[5]/div/div[1]/div[2]/div[1]/div[6]/div[2]/div[1]/form/div[2]/div[2]/button')
        sleep(5)'''

    def get_total_search_acc_form_number(self):
        # 获取搜索出来的acc报表的条数
        try:
            self.new_paging = NewPaging(self.driver, self.base_url)
            return self.new_paging.get_last_page_number('x,//*[@id="accTable"]')
        except:
            return 0

    def get_total_search_mile_total(self):
        # 运动总览页面获取总的里程数
        try:
            actual = self.driver.get_text('x,//*[@id="allmileage"]')
            return actual
        except:
            return 0

    def get_total_search_over_speed_total(self):
        # 运动总览页面获取总的超速次数
        try:
            actual = self.driver.get_text('x,//*[@id="alloverSpeedTimes"]')
            return actual
        except:
            return 0

    def get_total_search_stay_total(self):
        # 运动总览页面获取总的停留次数
        try:
            actual = self.driver.get_text('x,//*[@id="allstopTimes"]')
            return actual
        except:
            return 0

    def get_mileage_all_mile(self):
        # 获取里程报表，里程查询的总里程
        try:
            actual = self.driver.get_text('x,//*[@id="allmileages"]')
            return actual
        except:
            return 0

    def get_mileage_all_time(self):
        # 获取总时间，里程查询的总时间
        try:
            actual = self.driver.get_text('x,//*[@id="allmileageshours"]')
            return actual
        except:
            return 0

    def get_mileage_total_oil(self):
        # 获取总油耗，里程查询的总时间
        try:
            actual = self.driver.get_text('x,//*[@id="allfuel"]')
            return actual
        except:
            return 0

    def get_mileage_with_day_total_mile(self):
        # 查询类型为天，获取总的里程数
        try:
            actual = self.driver.get_text('x,//*[@id="allmileages-day"]')
            return actual
        except:
            return 0

    def get_total_stay_form_time(self):
        # 获取页面中总的停留时间
        try:
            actual = self.driver.get_text('x,//*[@id="stopCar-alltimes"]')
            return actual
        except:
            return 0

    def get_total_stay_form_time_with_acc_on(self):
        # 获取停车未熄火的总时间
        try:
            actual = self.driver.get_text('x,//*[@id="stopNotOff-alltimes"]')
            return actual
        except:
            return 0

    def get_total_search_acc_open(self):
        # 获取acc打开几次
        try:
            actual = self.driver.get_text('x,//*[@id="aCCOn"]')
            return actual
        except:
            return 0

    def get_total_search_acc_close(self):
        # 获取acc关闭几次
        try:
            actual = self.driver.get_text('x,//*[@id="aCCOff"]')
            return actual
        except:
            return 0

    def get_total_search_all_time(self):
        # 获取acc报表页面的总时间
        try:
            actual = self.driver.get_text('x,//*[@id="aCCTotalTime"]')
            return actual
        except:
            return 0

    def change_sec_time(self, sec):
        # 将所有的秒换成 小时分秒的形式
        if sec == 0:
            return '0'
        else:
            hours = sec / 3600
            all_min_and_second = sec % 3600
            mins = all_min_and_second / 60
            seconds = all_min_and_second % 60
            return "%d小时%d分%d秒" % (int(hours), int(mins), int(seconds))

    def click_export_mileage_form(self):
        # 点击导出里程报表
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[4]/button')
        sleep(3)

    def click_export_over_form(self):
        # 点击导出超速报表
        try:
            self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[4]/button')
            sleep(3)
        except:
            print('查询无数据，无法导出')

    def click_export_stay_form(self):
        # 点击导出停留报表

        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[4]/button')
        sleep(3)

    def click_export_paking_not_shut_down(self):
        # 点击停车未熄火报表
        try:
            self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[4]/button')
            sleep(3)
        except:
            print('查询无数据，无法导出')

    def click_export_acc_form(self):
        # 点击导出acc报表
        try:
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[4]/button')
            sleep(3)
        except:
            print('查询无数据，无法导出')

    def click_customer_in_mile_form(self, n):
        self.switch_to_tracel_report_form_frame()
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button(self):
        self.switch_to_tracel_report_form_frame()
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_mile_form(self):
        self.switch_to_tracel_report_form_frame()
        a = self.driver.get_element('x,//*[@id="dev_tree_travelReport"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_travelReport"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_mile_form(self):
        self.switch_to_tracel_report_form_frame()
        self.driver.click_element('x,//*[@id="dev_tree_travelReport_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_mile_form(self, m):
        self.switch_to_tracel_report_form_frame()
        text = self.driver.get_text(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_mile_form(self, m):
        self.switch_to_tracel_report_form_frame()
        self.driver.click_element(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_mile_form(self, m):
        self.switch_to_tracel_report_form_frame()
        number = len(list(self.driver.get_elements(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_customer_in_over_speed_form(self, n):
        self.switch_to_speeding_report_form_frame()
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button_in_over_speed_form(self):
        self.switch_to_speeding_report_form_frame()
        self.driver.click_element('x,//*[@id="OverspeedFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_over_speed_form(self):
        self.switch_to_speeding_report_form_frame()
        a = self.driver.get_element('x,//*[@id="dev_tree_overSpeedReport"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_overSpeedReport"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_over_speed_form(self):
        self.switch_to_speeding_report_form_frame()
        self.driver.click_element('x,//*[@id="dev_tree_overSpeedReport_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_over_speed_form(self, m):
        self.switch_to_speeding_report_form_frame()
        text = self.driver.get_text(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_over_speed_form(self, m):
        self.switch_to_speeding_report_form_frame()
        self.driver.click_element(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_over_speed_form(self, m):
        self.switch_to_speeding_report_form_frame()
        number = len(list(self.driver.get_elements(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_customer_in_stay_form(self, n):
        self.switch_to_stay_report_form_frame()
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button_in_stay_form(self):
        self.switch_to_stay_report_form_frame()
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_stay_form(self):
        self.switch_to_stay_report_form_frame()
        a = self.driver.get_element('x,//*[@id="dev_tree_stopCar"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_stopCar"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_stay_form(self):
        self.switch_to_stay_report_form_frame()
        self.driver.click_element('x,//*[@id="dev_tree_stopCar_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_stay_form(self, m):
        self.switch_to_stay_report_form_frame()
        text = self.driver.get_text(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_stay_form(self, m):
        self.switch_to_stay_report_form_frame()
        self.driver.click_element(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_stay_form(self, m):
        self.switch_to_stay_report_form_frame()
        number = len(list(self.driver.get_elements(
            'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_customer_in_stay_not_shut_down_form(self, n):
        self.switch_to_parking_report_form_frame()
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button_in_stay_not_shut_down(self):
        self.switch_to_parking_report_form_frame()
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_stay_not_shut_down(self):
        self.switch_to_parking_report_form_frame()
        a = self.driver.get_element('x,//*[@id="dev_tree_stopNotOff"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_stopNotOff"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_stay_not_shut_down(self):
        self.switch_to_parking_report_form_frame()
        self.driver.click_element('x,//*[@id="dev_tree_stopNotOff_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_stay_not_shut_down(self, m):
        self.switch_to_parking_report_form_frame()
        text = self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_stay_not_shut_down(self, m):
        self.switch_to_parking_report_form_frame()
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_stay_not_shut_down(self, m):
        self.switch_to_parking_report_form_frame()
        number = len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_customer_in_acc_form(self, n):
        self.switch_to_acc_report_form_frame()
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[1]/div/div[1]/span/button')
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button_in_acc_form(self):
        self.switch_to_acc_report_form_frame()
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_acc_form(self):
        self.switch_to_acc_report_form_frame()
        a = self.driver.get_element('x,//*[@id="dev_tree_acc"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_acc"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_acc_form(self):
        self.switch_to_acc_report_form_frame()
        self.driver.click_element('x,//*[@id="dev_tree_acc_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_acc_form(self, m):
        self.switch_to_acc_report_form_frame()
        text = self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_acc_form(self, m):
        self.switch_to_acc_report_form_frame()
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_acc_form(self, m):
        self.switch_to_acc_report_form_frame()
        number = len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_customer_in_alarm_overview(self, n):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[3]/div/div[1]/span/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="treeDemo_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button_alarm_form(self):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[4]/div/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_alarm_overview_form(self):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        a = self.driver.get_element('x,//*[@id="dev_tree_alarmOverview"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_alarmOverview"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_alarm_overview_form(self):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.driver.click_element('x,//*[@id="dev_tree_alarmOverview_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_alarm_overview_form(self, m):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        text = self.driver.get_text(
            'x,/html/body/div/div[2]/div[1]/form/div/div[4]/div/div[1]/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_alarm_overview_form(self, m):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.driver.click_element(
            'x,/html/body/div/div[2]/div[1]/form/div/div[4]/div/div[1]/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_alarm_overview_form(self, m):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        number = len(list(self.driver.get_elements(
            'x,/html/body/div/div[2]/div[1]/form/div/div[4]/div/div[1]/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_customer_in_alarm_detail_form(self, n):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.click_element('x,//*[@id="treeDemo2_%s_span"]' % str(n + 1))
        sleep(2)
        self.driver.default_frame()

    def click_search_dev_button_in_alarm_detail(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span/button')
        sleep(2)
        self.driver.default_frame()

    def get_group_number_in_alarm_detail_form(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        a = self.driver.get_element('x,//*[@id="dev_tree_alarmDetail"]').get_attribute('style')
        if a == 'display: block;':
            number = len(list(self.driver.get_elements('x,//*[@id="dev_tree_alarmDetail"]/li')))
            self.driver.default_frame()
            return number
        else:
            self.driver.default_frame()
            return 0

    def click_defalut_group_in_alarm_detail_form(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.driver.click_element('x,//*[@id="dev_tree_alarmDetail_1_switch"]')
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_in_alarm_detail_form(self, m):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        text = self.driver.get_text(
            'x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[%s]/a/span[2]' % str(
                m + 1))
        number = text.split('(')[1].split(')')[0]
        self.driver.default_frame()
        return number

    def click_per_group_in_alarm_detail_form(self, m):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.driver.click_element(
            'x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                m + 1))
        sleep(2)
        self.driver.default_frame()

    def get_dev_number_list_in_alarm_detail_form(self, m):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        number = len(list(self.driver.get_elements(
            'x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[%s]/ul/li' % str(
                m + 1))))
        self.driver.default_frame()
        return number

    def click_off_line_form_button(self):
        self.driver.click_element('x,//*[@id="offlineReport"]/a')
        sleep(2)

    def get_text_after_click_off_line_form_button(self):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return text

    def add_off_time_in_off_line_form(self, off_time):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        self.driver.operate_input_element('x,//*[@id="customizeDay"]', off_time)
        self.driver.default_frame()

    def click_search_button_in_off_line_form(self):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        self.driver.click_element('x,//*[@id="OffLineFrom"]/div[2]/div[3]/button[1]')
        sleep(2)
        self.driver.default_frame()

    def get_text_after_click_search(self):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        text = self.driver.get_text('c,layui-layer-content')
        self.driver.default_frame()
        return text

    def click_customer_in_off_line(self, n):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 2))
        sleep(2)
        self.driver.default_frame()

    def add_data_to_search_customer_in_off_line(self, search_data):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        self.driver.click_element('x,//*[@id="OffLineFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data)
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.default_frame()

    def get_text_after_click_search_in_off_line(self):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        text = self.driver.get_text('x,//*[@id="OffLineFrom"]/div[2]/div[1]/div/div[2]/div[1]/div/span')
        self.driver.default_frame()
        return text

    def click_on_line_form_button(self):
        self.driver.click_element('x,//*[@id="onlineReport"]/a')
        sleep(2)

    def get_text_after_click_on_line_form_button(self):
        self.driver.switch_to_frame('x,//*[@id="onlineReportFrame"]')
        text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return text

    def click_customer_in_on_line(self, n):
        self.driver.switch_to_frame('x,//*[@id="onlineReportFrame"]')
        self.driver.click_element('x,//*[@id="tree_%s_span"]' % str(n + 2))
        sleep(2)
        self.driver.default_frame()

    def add_data_to_search_customer_in_on_line(self, param):
        self.driver.switch_to_frame('x,//*[@id="onlineReportFrame"]')
        self.driver.click_element('x,//*[@id="OnLineFrom"]/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', param)
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.default_frame()

    def get_text_after_click_search_in_on_line(self):
        self.driver.switch_to_frame('x,//*[@id="onlineReportFrame"]')
        text = self.driver.get_text('x,//*[@id="OnLineFrom"]/div[1]/div/div[2]/div[1]/div/span')
        self.driver.default_frame()
        return text

    def click_mileage_form_buttons(self):
        self.driver.click_element('x,//*[@id="mileageReport"]/a')
        sleep(2)

    def switch_to_mile_report_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')

    def actual_text_after_click_mileage_form_buttons(self):
        # self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')
        self.switch_to_mile_report_form_frame()
        text = self.driver.get_text('x,/html/body/div/div[1]/div/b')
        self.driver.default_frame()
        return text

    def add_datas_to_search_mileage_form(self, search_data):
        # self.driver.switch_to_frame('x,//*[@id="mileageReportFrame"]')
        self.switch_to_mile_report_form_frame()
        # 选择用户
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_mileageReport"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_mileageReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_mileageReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_mileageReport"]/div[2]/div/button[1]')

        # 选择类型
        if search_data['type'] == 'day':
            self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[3]/label[3]/div/ins')

        # 选择日期
        if search_data['type'] == 'mile':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
            sleep(2)
            if search_data['choose_date'] == 'yesterday':
                # 选择昨天
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')
            elif search_data['choose_date'] == 'this_week':
                # 选择这周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')
            elif search_data['choose_date'] == 'last_week':
                # 上周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')
            elif search_data['choose_date'] == 'this_month':
                # 本月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
            elif search_data['choose_date'] == 'last_month':
                # 上月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')
            elif search_data['choose_date'] == '':
                # 填写
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
                # 填写开始时间
                self.driver.operate_input_element('x,//*[@id="startTime_mileage"]', search_data['begin_time'])
                # 填写结束时间
                self.driver.operate_input_element('x,//*[@id="startTime_mileage"]', search_data['end_time'])
            elif search_data['choose_date'] == 'today':
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif search_data['type'] == 'day':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
            sleep(2)
            if search_data['choose_date'] == 'yesterday':
                # 选择昨天
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')
            elif search_data['choose_date'] == 'this_week':
                # 选择这周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')
            elif search_data['choose_date'] == 'last_week':
                # 上周
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')
            elif search_data['choose_date'] == 'this_month':
                # 本月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')
            elif search_data['choose_date'] == 'last_month':
                # 上月
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
            elif search_data['choose_date'] == '':
                # 填写
                self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
                # 填写开始时间
                self.driver.operate_input_element('x,//*[@id="startTime_mileage"]', search_data['begin_time'])
                # 填写结束时间
                self.driver.operate_input_element('x,//*[@id="startTime_mileage"]', search_data['end_time'])

        # 点击搜索
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[3]/button')
        sleep(5)
        self.driver.default_frame()

    def click_electric_report_form_buttons(self):
        self.driver.click_element('x,//*[@id="electricityReport"]/a')
        sleep(2)

    def switch_to_electricity_report_frame(self):
        self.driver.switch_to_frame('x,//*[@id="electricityReportFrame"]')

    def actual_text_after_click_electric_report_buttons(self):
        # self.driver.switch_to_frame('x,//*[@id="electricityReportFrame"]')
        self.switch_to_electricity_report_frame()
        text = self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')
        self.driver.default_frame()
        return text

    def add_data_to_search_electric_report(self, search_data):
        # self.driver.switch_to_frame('x,//*[@id="electricityReportFrame"]')
        self.switch_to_electricity_report_frame()
        # 搜索用户
        self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[1]/div/div[1]/span/button')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['search_user'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        # 选择低于的电量
        self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/span[2]')
        sleep(2)
        if search_data['electric'] == '100':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[1]')
        elif search_data['electric'] == '90':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[2]')
        elif search_data['electric'] == '80':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[3]')
        elif search_data['electric'] == '70':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[4]')
        elif search_data['electric'] == '60':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[5]')
        elif search_data['electric'] == '50':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[6]')
        elif search_data['electric'] == '40':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[7]')
        elif search_data['electric'] == '30':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[8]')
        elif search_data['electric'] == '20':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[9]')
        elif search_data['electric'] == '10':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[2]/div/span/div/div/ul/li[10]')

        # 选择型号
        self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[3]/div/div/div/span[2]')
        sleep(2)
        if search_data['dev_type']:
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[3]/div/div/div/div/ul/li[1]')

        # 选择下级
        a = self.driver.get_element('x,//*[@id="icheckContainSub"]').is_selected()
        if a == True and search_data['next'] == '':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[4]/label/div/ins')
        elif a == True and search_data['next'] == '1':
            pass
        elif a == False and search_data['next'] == '1':
            self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[4]/label/div/ins')
        elif a == False and search_data['next'] == '':
            pass

        # 点击搜索
        self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[5]/button[1]')
        sleep(5)

        self.driver.default_frame()

    def get_web_total_electric_report(self):
        # self.driver.switch_to_frame('x,//*[@id="electricityReportFrame"]')
        self.switch_to_electricity_report_frame()
        a = self.driver.get_element('x,//*[@id="paging-electric"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="paging-electric"]', 'x,//*[@id="electricTable"]')
            self.driver.default_frame()
            return total
        else:
            self.driver.default_frame()
            return 0

    def get_no_data_text_in_alarm_overview_page(self):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        text = self.driver.get_text('x,//*[@id="alarm_report_nodata"]/div/span')
        self.driver.default_frame()
        return text

    def get_sos_total_alarm_number(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[1]

    def get_list_sos_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[1]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[1]' % str(n + 1))
        return number

    def get_enter_satellite_dead_zone_alarm_total(self):
        text = self.driver.get_text('x,//*[@id="alarmTableTotal"]')
        return text.split(' ')[3]

    def get_list_enter_satellite_dead_zone_alarm_total_number(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[2]'))
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[2]' % str(n + 1))
        return number

    def get_begin_time_in_mile_report_page(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_mileage"]').get_attribute('value')
        return begin_time

    def get_end_time_in_mile_report_page(self):
        begin_time = self.driver.get_element('x,//*[@id="endTime_mileage"]').get_attribute('value')
        return begin_time

    def get_select_account_in_on_line_form(self, n):
        self.driver.switch_to_frame('x,//*[@id="onlineReportFrame"]')
        self.driver.click_element('x,//*[@id="OnLineFrom"]/div[1]/div/div[1]/span/button')
        sleep(2)
        text = self.driver.get_text('x,//*[@id="tree_%s_span"]' % str(n + 2))
        self.driver.default_frame()
        return text

    def get_search_input_account_in_on_line_form(self):
        self.driver.switch_to_frame('x,//*[@id="onlineReportFrame"]')
        text = self.driver.get_element('x,//*[@id="search_text"]').get_attribute('value')
        self.driver.default_frame()
        return text

    def get_select_account_off_line_form(self, n):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        self.driver.click_element('x,//*[@id="OffLineFrom"]/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        text = self.driver.get_text('x,//*[@id="tree_%s_span"]' % str(n + 2))
        self.driver.default_frame()
        return text

    def get_search_input_account_in_off_line_form(self):
        self.driver.switch_to_frame('x,//*[@id="offlineReportFrame"]')
        text = self.driver.get_element('x,//*[@id="search_text"]').get_attribute('value')
        self.driver.default_frame()
        return text

    def get_web_page_electric_report(self):
        a = self.driver.get_element('x,//*[@id="paging-electric"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-electric"]')
            return total
        else:
            return 0

    def get_web_page_list_electric_report(self):
        new_paging = NewPaging(self.driver, self.base_url)
        total = new_paging.get_last_page_number('x,//*[@id="electricTable"]')
        return total

    def get_dev_name_in_electric_report(self, n):
        return self.driver.get_text('x,/html/body/div[1]/div[2]/div[3]/table/tbody/tr[%s]/td[2]' % str(n + 1))

    def click_per_page_in_electric_report_form(self, n):
        self.driver.click_element('l,%s' % str(n + 1))
        sleep(2)

    def get_dev_electricity_web_in_electric_report(self, x):
        return self.driver.get_text('x,/html/body/div[1]/div[2]/div[3]/table/tbody/tr[%s]/td[6]' % str(x + 1))

    def get_dev_imei_web_in_electric_report(self, x):
        return self.driver.get_text('x,/html/body/div[1]/div[2]/div[3]/table/tbody/tr[%s]/td[3]' % str(x + 1))

    def get_dev_type_web_in_electric_report(self, x):
        return self.driver.get_text('x,/html/body/div[1]/div[2]/div[3]/table/tbody/tr[%s]/td[4]' % str(x + 1))

    def get_dev_user_name_web_in_electric_report(self, x):
        return self.driver.get_text('x,/html/body/div[1]/div[2]/div[3]/table/tbody/tr[%s]/td[5]' % str(x + 1))

    def get_headers_for_post_request(self):
        headers = {
            'Cookie': 'JSESSIONID=DA4D4C232AE4097C30F48D9000642050'
        }
        return headers

    def get_start_time_in_alarm_overview(self):
        return self.driver.get_element('x,//*[@id="startTime_alarmReport"]').get_attribute('value')

    def get_end_time_in_alarm_overview(self):
        return self.driver.get_element('x,//*[@id="endTime_alarmReport"]').get_attribute('value')

    def get_dev_name_in_alarm_overview(self):
        return self.driver.get_text('x,//*[@id="alarm_report_tbody"]/tr[1]/td[2]')

    def get_dev_type_in_alarm_overview(self):
        return self.driver.get_text('x,//*[@id="alarm_report_tbody"]/tr[1]/td[4]')

    def get_dev_imei_in_alarm_overview(self):
        return self.driver.get_text('x,//*[@id="alarm_report_tbody"]/tr[1]/td[3]')
