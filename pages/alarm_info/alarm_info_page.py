import time
from time import sleep
import datetime

from pages.base.base_page import BasePage
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class AlarmInfoPage(BasePage):
    def click_control_after_click_alarm_info(self):
        # 点击控制台后点击指令管理
        current_handle = self.driver.get_current_window_handle()
        self.driver.click_element('x,//*[@id="index"]/a')
        sleep(2)

        all_handle = self.driver.get_all_window_handles()

        for handle in all_handle:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.driver.click_element('x,//*[@id="alarm"]/a')

    def actual_url_click_alarm(self):
        # 获取真实的url
        url = self.driver.get_current_url()
        return url

    def actual_text_alick_alarm(self):
        # 获取真实的文本
        text = self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[1]/b')
        return text

    def click_lift_list(self, param):
        if param == 'alarm_info':
            self.driver.click_element('x,//*[@id="alarm-ReportTab"]/ul/li[1]/a')

        elif param == 'alarm_set_up':
            self.driver.click_element('x,//*[@id="getPushSet"]')

        elif param == 'set_up_enclosure':
            self.driver.click_element('x,//*[@id="getGeozoneList"]')

        elif param == 'alarm_detail':
            self.driver.click_element('x,//*[@id="alarm-ReportTab"]/ul/li[2]/a')
        sleep(3)

    def actual_text_click_alarm_info(self):
        # 点击告警总览后，获取右侧页面的文本
        self.switch_to_alarm_overview_frame()
        text = self.driver.get_text('x,/html/body/div/div[1]/div/b')
        self.driver.default_frame()
        return text

    def click_alarm_info_type(self):
        # 点击选择告警类型
        self.driver.click_element(
            'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[2]/div[3]/div[2]/div[3]/table/thead/tr/th/span')
        sleep(3)

    def actual_text_after_alarm_type(self):
        # 获取文本
        text = self.driver.get_text('x,//*[@id="serAlarmTypeModal"]/div/div/div[1]/h4')
        return text

    def click_alarm_type(self, param):
        if param == 'close':
            self.driver.click_element('x,//*[@id="alarmOverviewColse"]')
        elif param == 'canal':
            self.driver.click_element('x,//*[@id="js-canal-alarm-item"]')
        elif param == 'ensure':
            self.driver.click_element('x,//*[@id="serAlarmTypeModal"]/div/div/div[3]/button[1]')
        sleep(3)

    def click_all_select(self):
        self.driver.click_element('x,//*[@id="serAlarmTypeModal"]/div/div/div[2]/div/div/div/label/div/ins')
        sleep(3)

    def get_total_alarm_type(self):
        # 获取所有的报警类型
        total_list = list(self.driver.get_elements('x,//*[@id="alarmTypeReport"]/li'))
        total = len(total_list)
        return total

    def actual_text_click_alarm_set_up(self):
        # 获取告警设置点击后的文本
        text = self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[1]/div/b')
        return text

    def click_menu(self, type):
        # 点击全部开启app推送
        if type == 'open_app':
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/form/div/div/button[1]')
        elif type == 'close_app':
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/form/div/div/button[2]')

        elif type == 'look_all':
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/form/div/div/button[3]')

        elif type == 'close_all':
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/form/div/div/button[4]')

        elif type == 'email':
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/form/div/div/button[5]')

        elif type == 'time':
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/form/div/div/button[6]')
        sleep(3)

    def get_total_number(self):
        tot = list(self.driver.get_elements('x,//*[@id="alarm_appSet_tbody"]/tr'))
        total = len(tot)
        return total

    def actual_text_ater_set_up_email(self):
        # 点击全部设置右键发送
        text = self.driver.get_text('x,//*[@id="mailAddressModal"]/div/div/div[1]/h4')
        return text

    def set_up_email_operation(self, param):
        # 全部设置邮箱发送界面的操作
        if param == 'close':
            self.driver.click_element('x,//*[@id="mailAddressModal"]/div/div/div[1]/button/span')
            sleep(2)
        if param == 'cancel':
            self.driver.click_element('x,//*[@id="mailAddressModal"]/div/div/div[3]/button[2]')
            sleep(2)
        if param == 'ensure':
            self.driver.click_element('x,//*[@id="emailSave"]')
            sleep(2)

    def add_email_to_set_up(self, param):
        # 增加邮箱
        self.driver.operate_input_element('x,//*[@id="firstEmail"]', param)
        self.driver.click_element(
            'x,//*[@id="mailAddressModal"]/div/div/div[2]/div[2]/div/div/form/div/div/ul/li/button')
        sleep(2)
        self.driver.click_element(
            'x,//*[@id="mailAddressModal"]/div/div/div[2]/div[2]/div/div/form/div/div/ul/li[2]/button')
        sleep(2)

    def actual_text_after_click_alarm_time(self):
        # 点击告警时间后，检查文本
        text = self.driver.get_text('x,//*[@id="setAlarmTimeModal"]/div/div/div[1]/h4')
        return text

    def set_up_alarm_time_operation(self, type):
        # 告警时间设置页面的操作
        if type == 'close':
            self.driver.click_element('x,//*[@id="setAlarmTimeModal"]/div/div/div[1]/button/span')
            sleep(2)
        if type == 'cancel':
            self.driver.click_element('x,//*[@id="setAlarmTimeModal"]/div/div/div[3]/button[2]')
            sleep(2)
        if type == 'ensure':
            self.driver.click_element('x,//*[@id="saveAlarmTime"]')
            sleep(2)

    def add_data_to_set_up_alarm_time(self, param, param1):
        self.driver.operate_input_element('x,//*[@id="offlineAlarmTime"]', param)
        self.driver.operate_input_element('x,//*[@id="stayAlertTime"]', param1)

    def circle_click_look_alarm(self):
        # 循环点击查看警告
        total = self.get_total_number()
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.driver.execute_script(
                    self.driver.get_element(
                        'x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[1]/div/ins' % number))
                self.driver.click_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[1]/div/ins' % number)
                sleep(3)

    def circle_click_app(self):
        total = self.get_total_number()
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.driver.execute_script(
                    self.driver.get_element(
                        'x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[2]/div/ins' % number))
                self.driver.click_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[2]/div/ins' % number)
                sleep(2)

    def circle_click_set_up_email(self):
        total = self.get_total_number()
        for number in range(total + 1):
            if number == 0:
                pass
            else:
                self.driver.execute_script(
                    self.driver.get_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[3]/a' % number))
                self.driver.click_element('x,//*[@id="alarm_appSet_tbody"]/tr[%s]/td[4]/label[3]/a' % number)
                sleep(3)
                self.driver.click_element('x,//*[@id="mailAddressModal"]/div/div/div[3]/button[2]')

    def actual_text_after_click_set_up_enclosure(self):
        # 点击围栏设置后 返回页面右上角的文本
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[4]/div[1]/div/b')
        return actual_text

    def click_add_enclosure(self):
        # 点击创建围栏
        self.driver.click_element('x,//*[@id="toMap"]')
        sleep(3)

    def actual_text_after_click_add_enclosure(self):
        # 点击创建围栏后，返回页面右上角的文本
        text = self.driver.get_text('x,//*[@id="createGeoLand"]')
        return text

    def click_close_add_enclosure(self):
        # 点击关闭创建围栏
        self.driver.click_element('x,//*[@id="createFenceModal"]/div/div/div[1]/button/span')
        sleep(3)

    def set_up_enclosure_list_operation(self, param):
        # 围栏设置列表操作
        try:
            if param == 'look':
                self.driver.click_element('x,//*[@id="geozoneList"]/tr[1]/td[5]/a[1]')

            elif param == 'edit':
                self.driver.click_element('x,//*[@id="geozoneList"]/tr[1]/td[5]/a[2]')

            elif param == 'delete':
                self.driver.click_element('x,//*[@id="geozoneList"]/tr[1]/td[5]/a[3]')

            elif param == 'set_up':
                self.driver.click_element('x,//*[@id="geozoneList"]/tr[1]/td[5]/a[4]')
            sleep(3)
        except:
            print('列表无数据！')

    def first_list_name_in_set_up_enclosure(self):
        # 获取围栏设置列表第一列的名称
        try:
            text = self.driver.get_text('x,//*[@id="geozoneList"]/tr[1]/td[2]')
            return text
        except:
            print('列表无数据！')

    def actaul_text_after_click_look(self):
        # 点击查看后，获取页面的title文本
        text = self.driver.get_text('x,//*[@id="checkGeo"]')
        return text

    def close_look_enclosure(self):
        # 点击关闭查看围栏
        self.driver.click_element('x,//*[@id="viewFenceModal"]/div/div/div[1]/button/span')
        sleep(3)

    def actual_text_after_click_edit(self):
        # 点击编辑后，返回编辑框title的文本
        return self.driver.get_text('x,//*[@id="myModalLabel"]')

    def click_edit_enclosure_operation(self, param):
        # 编辑框的操作
        if param == 'close':
            self.driver.click_element('x,//*[@id="editFenceModal"]/div/div/div[1]/button/span')
        elif param == 'cancel':
            self.driver.click_element('x,//*[@id="editFenceModal"]/div/div/div[3]/button[2]')
        elif param == 'ensure':
            self.driver.click_element('x,//*[@id="saveBtn"]')
        sleep(3)

    def add_data_to_edit_enclosure(self, param, param1):
        # 编辑围栏设置的数据
        self.driver.operate_input_element('x,//*[@id="geoname"]', param)
        self.driver.operate_input_element('x,//*[@id="description"]', param1)

    def actual_text_after_click_delete_list(self):
        # 点击删除后获取真实的文本
        return self.driver.get_text('x,/html/body/div[25]/div[3]/a[1]')

    def click_detele_enclosure_operation(self, param):
        # 　删除列表的框框的操作
        if param == 'close':
            self.driver.click_element('x,//*[@id="layui-layer2"]/span/a')
        elif param == 'cancel':
            self.driver.click_element('x,/html/body/div[25]/div[3]/a[2]')
        elif param == 'ensure':
            self.driver.click_element('x,/html/body/div[25]/div[3]/a[1]')
        sleep(3)

    def actual_text_after_click_set_up_alarm(self):
        # 点击告警设置后，返回title的文本
        return self.driver.get_text('x,//*[@id="setFenceModal"]/div/div/div[1]/h4')

    def click_set_up_alarm_operation(self, param):
        # 　设置告警框框的操作
        if param == 'close':
            self.driver.click_element('x,//*[@id="setFenceModal"]/div/div/div[1]/button/span')
        elif param == 'cancel':
            self.driver.click_element('x,//*[@id="setFenceModal"]/div/div/div[3]/button[2]')
        elif param == 'ensure':
            self.driver.click_element('x,//*[@id="setFenceModal"]/div/div/div[3]/button[1]')
        sleep(3)

    def add_data_to_set_up_alarm(self, set_up_alarm_data):
        # 告警设置增加数据去设置
        self.driver.click_element('x,//*[@id="delete-all"]')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="key"]', set_up_alarm_data['search'])
        self.driver.click_element('x,//*[@id="setFenceModal"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/i')
        sleep(2)
        self.driver.click_element(
            'x,//*[@id="geoTree_3_span"]')
        self.driver.click_element('x,//*[@id="chosen-node"]')

        self.driver.click_element('x,//*[@id="acc_configure_form"]/div[2]/div[1]/label/div/ins')
        self.driver.operate_input_element('x,//*[@id="stayTimeIn"]', set_up_alarm_data['time_01'])

        self.driver.click_element('x,//*[@id="acc_configure_form"]/div[2]/div[2]/label/div/ins')
        self.driver.operate_input_element('x,//*[@id="stayTimeOut"]', set_up_alarm_data['time_02'])

    def click_choose_date(self, param):
        # 选择日期
        if param == 'today':
            # 今天
            self.driver.click_element('x,//*[@id="qucikTime_alarmReport"]/button[1]')
        elif param == 'yesterday':
            # 昨天
            self.driver.click_element('x,//*[@id="qucikTime_alarmReport"]/button[2]')

        elif param == 'this_work':
            self.driver.click_element('x,//*[@id="qucikTime_alarmReport"]/button[3]')

        elif param == 'last_week':
            self.driver.click_element('x,//*[@id="qucikTime_alarmReport"]/button[4]')

        elif param == 'this_month':
            self.driver.click_element('x,//*[@id="qucikTime_alarmReport"]/button[5]')

        elif param == 'last_month':
            self.driver.click_element('x,//*[@id="qucikTime_alarmReport"]/button[6]')
        sleep(3)

    def get_cuurrent_time_year(self):
        # 获取当前的日期的年份
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        current_time_year = current_time.split('-')[0]
        return current_time_year + "年"

    def get_cuurrent_time_mouth(self):
        # 获取当前的日期的月份
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        current_time_mouth = current_time.split('-')[1]
        return current_time_mouth + "月"

    def get_cuurrent_time_day(self):
        # 获取当前的日期的月份
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        current_time_day = current_time.split('-')[2]
        return current_time_day

    def get_current_date_with_time(self):
        # 获取当前的时间
        current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        return current_time

    def get_current_date(self):
        # 获取当前的时间
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return current_time + " 00:00"

    def get_first_time(self):
        # 获取第一个时间
        js = "$('input[id=startTime_alarmReport]').attr('readonly','')"
        self.driver.execute_js(js)
        first_time = self.driver.get_element('x,//*[@id="startTime_alarmReport"]').get_attribute('value')
        return first_time

    def get_second_time(self):
        # 获取第二个时间
        js = "$('input[id=endTime_alarmReport]').attr('readonly','')"
        self.driver.execute_js(js)
        second_time = self.driver.get_element('x,//*[@id="endTime_alarmReport"]').get_attribute('value')
        return second_time

    def get_first_yesterday_day(self):
        # 获取昨天的开始时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        first = str(yes) + " 00:00"
        return first

    def get_second_yesterday_day(self):
        # 获取昨天的结束时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        second = str(yes) + " 23:59"
        return second

    def get_week_first_time(self):
        # 获取本周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.isoweekday() - 1))
        week = today - days_count
        return str(week) + ' 00:00'

    def get_week_sencond_time(self):
        # 获取本周的结束时间
        today = datetime.date.today()
        return str(today) + ' 23:59'

    def get_last_week_first_time(self):
        # 获取上周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count - datetime.timedelta(days=6)
        return str(week) + ' 00:00'

    def get_last_week_second_time(self):
        # 获取上周的结束时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count
        return str(week) + ' 23:59'

    def get_this_mouth_first_time(self):
        # 获取本月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.day - 1))
        this_month = today - days_count
        return str(this_month) + " 00:00"

    def get_last_month_second_time(self):
        # 获取上月的结束
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        return str(last_month) + " 23:59"

    def get_last_month_first_time(self):
        # 获取上月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        month = datetime.date(last_month.year, last_month.month, 1)
        return str(month) + " 00:00"

    def add_data_to_search_in_alarm_overview(self, data):
        # 输入数据去搜索
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        # 点击搜索
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[3]/div/div[1]/span/button')
        sleep(2)
        # 输入数据
        self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', data['user_name'])
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
        # 点击搜索的第一个
        sleep(2)
        self.driver.click_element('c,autocompleter-item')

        # 点击设备搜索
        self.driver.clear_input('x,//*[@id="imeiInput_alarmOverview"]')
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[4]/div/div[1]/div/div[1]/span/button')
        sleep(2)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_alarmOverview"]/li'))
        all_group_num = len(all_group_list)
        if all_group_num == 1:
            pass
        else:
            for n in range(1, all_group_num):
                sleep(1)
                self.driver.click_element(
                    'x,/html/body/div/div[2]/div[1]/form/div/div[4]/div/div[1]/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                        n + 1))

        # 选择全部设备
        self.driver.click_element('x,//*[@id="treeModal_alarmOverview"]/div[2]/label/div/ins')
        # 点击确定
        sleep(2)
        self.driver.click_element('x,//*[@id="treeModal_alarmOverview"]/div[2]/div/button[1]')
        sleep(2)
        # 选择日期
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/span[2]')
        sleep(2)
        if data['choose_date'] == 'today':
            # 今天
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[2]')
        elif data['choose_date'] == 'yesterday':
            # 昨天
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[3]')

        elif data['choose_date'] == 'this_work':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[4]')

        elif data['choose_date'] == 'last_week':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[5]')

        elif data['choose_date'] == 'this_month':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[6]')

        elif data['choose_date'] == 'last_month':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[7]')

        else:
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[1]')
            # 填写开始时
            js = 'document.getElementById("startTime_alarmReport").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="startTime_alarmReport"]', data['began_time'])

            # 填写结束时间
            js = 'document.getElementById("endTime_alarmReport").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_alarmReport"]', data['end_time'])
        sleep(3)
        # 点击选择报警类型
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[5]/button')
        sleep(5)
        self.driver.default_frame()

    def actual_text_after_click_alarm_detail(self):
        # 点击告警之后，返回页面左上角的文本
        return self.driver.get_text('x,/html/body/div[1]/div[1]/div/b')

    def add_data_to_search_alarm_detail(self, data):
        # 在搜索页面增加数据
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        # 点击搜索
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/span/button')
        # 输入数据
        self.driver.operate_input_element('x,//*[@id="cusTreeKey2"]', data['user_name'])
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn2"]')
        # 点击搜索的第一个
        self.driver.click_element('c,autocompleter-item')

        # 点击设备搜索
        self.driver.clear_input('x,//*[@id="imeiInput_alarmDetail"]')
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span/button')
        sleep(2)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_alarmDetail"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))

        # 选择全部设备
        self.driver.click_element('x,//*[@id="treeModal_alarmDetail"]/div[2]/label/div/ins')
        # 点击确定
        self.driver.click_element('x,//*[@id="treeModal_alarmDetail"]/div[2]/div/button[1]')
        sleep(2)

        # 选择型号
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div/div/span[2]')
        if data['type'] == 'all':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div/div/div/ul/li[1]')

        # 选择状态
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/span[2]')
        if data['status'] == 'all':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/div/ul/li[1]')
        elif data['status'] == '1':
            # 已读
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/div/ul/li[2]')
        elif data['status'] == '0':
            # 未读
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/div/ul/li[3]')

        # 填写告警时间段
        js = 'document.getElementById("startTime_alarmInfo").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="startTime_alarmInfo"]', data['alarm_begin_time'])

        js = 'document.getElementById("endTime_alarmInfo").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="endTime_alarmInfo"]', data['alarm_end_time'])

        # 填写定位时间段
        js = 'document.getElementById("startTime_position").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="startTime_position"]', data['push_begin_time'])

        js = 'document.getElementById("endTime_position").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('x,//*[@id="endTime_position"]', data['push_end_time'])
        self.driver.click_element('x,/html/body/div[1]/div[1]/div')
        # 选择是否包含下级
        if data['next_user'] == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[4]/label/div/ins')
        # 点击搜索
        sleep(2)
        self.driver.click_element('x,//*[@id="getAlertInfo_btn"]')
        sleep(5)
        self.driver.default_frame()

    def get_search_total(self):
        '''
        # 获取查询后页面的页数
        page1 = self.get_total_pages_num('x,//*[@id="alarm_info_paging"]')
        if page1 == 0:
            total = 0
        else:
            for n in range(100):
                page = self.get_total_pages_num('x,//*[@id="alarm_info_paging"]')
                self.driver.click_element('x,//*[@id="alarm_info_paging"]' + "/ul/li[" + str(int(page) + 1) + "]/a")
                try:
                    self.driver.get_text('l,下一页') == '下一页'
                    continue
                except:
                    break
            pages = self.get_actual_pages_number_with_serach('x,//*[@id="alarm_info_paging"]')
            # 获取最后一页有多少条记录
            num = self.last_page_logs_num_with_search('x,//*[@id="alarm_info_tbody"]', 'x,//*[@id="alarm_info_paging"]')
            # 计算总共有多少条记录
            if pages == 1:
                total = num
            else:
                total = int(pages) * 10 + num
        return total'''
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number('x,//*[@id="alarm_info_paging"]', 'x,//*[@id="alarm_info_tbody"]')
            return total
        except:
            return 0

    def get_web_total_in_overview_search(self):
        # 查询报警总览搜索出的条数
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        a = self.driver.get_element('x,//*[@id="alarm_report_nodata"]').get_attribute('style')
        if a == 'display: block;':
            self.driver.default_frame()
            return 0
        elif a == 'display: none;':
            number = len(list(self.driver.get_elements('x,//*[@id="alarm_report_tbody"]/tr')))
            self.driver.default_frame()
            return number

    def click_all_alarm_type(self):
        # 现在报警类型
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.driver.click_element('x,/html/body/div/div[2]/div[3]/div[2]/div[3]/table/thead/tr/th/span')
        sleep(1)
        self.driver.default_frame()
        self.driver.click_element('x,//*[@id="serAlarmTypeModal"]/div/label/div/ins')
        sleep(1)
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def get_alarm_first_time(self):
        # 获取第一个告警开始时间
        js = "$('input[id=startTime_position]').attr('readonly','')"
        self.driver.execute_js(js)
        return self.driver.get_element('x,//*[@id="startTime_position"]').get_attribute('value')

    def get_alarm_second_time(self):
        # 获取告警结束时间
        js = "$('input[id=endTime_position]').attr('readonly','')"
        self.driver.execute_js(js)
        return self.driver.get_element('x,//*[@id="endTime_position"]').get_attribute('value')

    def get_push_first_time(self):
        # 获取推送开始时间
        js = "$('input[id=startTime_alarmInfo]').attr('readonly','')"
        self.driver.execute_js(js)
        return self.driver.get_element('x,//*[@id="startTime_alarmInfo"]').get_attribute('value')

    def get_push_second_time(self):
        # 获取推送结束时间
        js = "$('input[id=endTime_alarmInfo]').attr('readonly','')"
        self.driver.execute_js(js)
        return self.driver.get_element('x,//*[@id="endTime_alarmInfo"]').get_attribute('value')

    def click_handle_meun(self, param):
        # 点击处理的菜单
        if param == 'all_read':
            # 全部标记为已读
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/button[1]')
        elif param == 'read':
            # 标记为已读
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/button[2]')
        elif param == 'all_handle':
            # 全部处理
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/button[3]')
        elif param == 'handle':
            # 处理
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/div/button[4]')
        sleep(4)

    def choose_select_result_first(self):
        # 勾选查询后的第一个数据
        try:
            self.driver.click_element('x,//*[@id="alarm_info_tbody"]/tr[1]/td[1]/span/div/ins')
        except:
            print("暂无数据！")

    def actual_text_after_click_handle(self):
        # 点击处理后 返回处理框的文本
        return self.driver.get_text('x,/html/body/div[22]/div/div/div[1]/h4')

    def add_data_to_handle(self, name, desc):
        # 增加处理信息
        self.driver.operate_input_element('x,/html/body/div[22]/div/div/div[2]/form/div[1]/div/input', name)
        self.driver.operate_input_element('x,/html/body/div[22]/div/div/div[2]/form/div[2]/div/textarea', desc)
        self.driver.click_element('x,/html/body/div[22]/div/div/div[3]/button[1]')
        sleep(3)

    def click_export_button(self):
        # 点击导出
        try:
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/table/thead/tr/th[1]/label/div/ins')
            sleep(2)
            self.driver.click_element(
                'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/button')
            sleep(2)
        except:
            print('无数据')

    def actual_text_after_click_handles(self):
        return self.driver.get_text('x,/html/body/div[23]/div/div/div[1]/h4')

    def add_data_to_handles(self, param, param1):
        self.driver.operate_input_element('x,/html/body/div[23]/div/div/div[2]/form/div[1]/div/input', param)
        self.driver.operate_input_element('x,/html/body/div[23]/div/div/div[2]/form/div[2]/div/textarea', param1)
        self.driver.click_element('x,/html/body/div[23]/div/div/div[3]/button[1]')
        sleep(3)

    def click_alarm_overview_list(self):
        self.driver.click_element('x,//*[@id="alarmOverview"]/a')
        sleep(2)

    def click_alarm_detail_list(self):
        self.driver.click_element('x,//*[@id="alarmDdetails"]/a')
        sleep(2)

    def switch_to_alarm_overview_frame(self):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
