import datetime
from time import sleep

from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.new_paging import NewPaging


class ClockInPage(BasePage):
    def click_clock_in_form_button(self):
        self.driver.click_element('x,//*[@id="punchTheClockReport"]/a')
        sleep(2)

    def switch_to_click_in_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="punchTheClockReportFrame"]')

    def add_data_to_search_click_in_form(self, data):
        # 点击清空
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[2]/button')
        sleep(2)
        # 选择时间
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        if data['date_type'] == '':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="startTime_travel"]', data['begin_time'])
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="endTime_travel"]', data['end_time'])

        elif data['date_type'] == 'today':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif data['date_type'] == 'yesterday':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')

        elif data['date_type'] == 'this_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')

        elif data['date_type'] == 'last_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')

        elif data['date_type'] == 'this_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')

        elif data['date_type'] == 'last_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')

        sleep(2)
        # 输入设备imei
        self.driver.operate_input_element('x,//*[@id="imeis"]', self.get_dev_imei())

        # 输入设备型号
        self.driver.operate_input_element('x,//*[@id="deviceName"]', data['dev_type'])
        # 选择打卡类型
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[4]/div/div/div/span[2]')
        sleep(1)
        if data['clock_in_type'] == 'all':
            self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[4]/div/div/div/div/ul/li[1]')

        elif data['clock_in_type'] == '1':
            self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[4]/div/div/div/div/ul/li[2]')

        elif data['clock_in_type'] == '2':
            self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[4]/div/div/div/div/ul/li[3]')

        sleep(2)

        # 点击搜索
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[1]/button')
        sleep(5)

    def get_page_number_after_search_clock_in_form(self):
        a = self.driver.get_element('x,//*[@id="punchTheClock-day-noData"]').get_attribute('style')
        if a == 'display: block;':
            return 0
        else:
            new_page = NewPaging(self.driver, self.base_url)
            number = new_page.get_total_page('x,//*[@id="paging-day"]')
            return number

    def get_no_data_text_in_clock_form(self):
        return self.driver.get_text('x,//*[@id="punchTheClock-day-noData"]/div/span')

    def get_sql_data_in_clock_in_form(self, data):
        begin_time = self.driver.get_element('startTime_travel').get_attribute('value')
        end_time = self.driver.get_element('endTime_travel').get_attribute('value')
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_form()
        cursor = connect.cursor()
        sql = "SELECT DEVICE_IMEI,GPS_TIME,ON_OFF FROM clock_on_off WHERE DEVICE_IMEI = '" + self.get_dev_imei() + "' and GPS_TIME BETWEEN '" + begin_time + "' and '" + end_time + "'"
        if data['clock_in_type'] != 'all':
            sql += " and ON_OFF = '" + data['clock_in_type'] + "'"
        sql += " order by GPS_TIME desc;"
        cursor.execute(sql)
        data = cursor.fetchall()
        data_list = []
        for range in data:
            # TODO:mqsql plus 8 hours
            data_list.append({
                'imei': range[0],
                'time': str(range[1]),
                'on_off': range[2]
            })
        cursor.close()
        connect.close()
        return data_list

    def get_per_page_number_in_clock_in_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="punchTheClock-day-tbody"]/tr')))

    def get_imei_in_clock_in_form(self, n):
        return self.driver.get_text('x,//*[@id="punchTheClock-day-tbody"]/tr[%s]/td[2]' % str(n + 1))

    def get_time_in_clock_form(self, n):
        return self.driver.get_text('x,//*[@id="punchTheClock-day-tbody"]/tr[%s]/td[4]' % str(n + 1))

    def get_on_off_in_clock_form(self, n):
        a = self.driver.get_text('x,//*[@id="punchTheClock-day-tbody"]/tr[%s]/td[5]' % str(n + 1))
        if a == '上班':
            return 1
        elif a == '下班':
            return 2

    def click_per_page(self, n):
        self.driver.click_element('l,%s' % str(n + 1))
        sleep(2)

    def get_begin_time_in_clock_in_form(self):
        return self.driver.get_element('startTime_travel').get_attribute('value') + ':00'

    def get_end_time_in_clock_in_form(self):
        return self.driver.get_element('endTime_travel').get_attribute('value') + ':00'

    def get_dev_imei(self):
        return '860123456788888'

    def get_addr_in_clock_form(self, n):
        return self.driver.get_text('x,//*[@id="punchTheClock-day-tbody"]/tr[%s]/td[6]' % str(n + 1))
