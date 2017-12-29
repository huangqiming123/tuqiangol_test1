from time import sleep

from pages.base.base_page import BasePage
from pages.base.new_paging import NewPaging


class StatisticFormPage4(BasePage):
    def request_base_url(self):
        return 'http://119.23.160.20:9080/api/gpscontroll/v1'
        # return 'http://172.16.0.105:9080/api/gpscontroll/v1'

    # 停留报表页面数
    def get_total_page_in_over_stay_form(self):
        a = self.driver.get_element('x,//*[@id="paging-stopCar"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-stopCar"]')
            return total
        else:
            return 0

    # 页面开始时间
    def get_over_stay_report_form_begin_time(self):
        return self.driver.get_element('x,//*[@id="startTime_stopCar"]').get_attribute('value') + ':00'

    # 页面结束时间
    def get_over_stay_report_form_end_time(self):
        return self.driver.get_element('x,//*[@id="endTime_stopCar"]').get_attribute('value') + ':00'

    # 每页行数
    def get_total_number_per_page_in_over_stay_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="stayTableContent"]/tbody/tr')))

    # 列表imei
    def get_imei_in_over_stay_form(self, n):
        return self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[3]' % str(n + 1))

    # 列表状态
    def get_state_in_over_stay_form(self, n):
        return self.driver.get_text('x,//*[@id="stopCar-tbody"]/tr[%s]/td[5]' % str(n + 1))

    # 开始时间
    def get_start_time_in_over_stay_form(self, n):
        return self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[6]' % str(n + 1))

    # 结束时间
    def get_end_time_in_over_stay_form(self, n):
        return self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[7]' % str(n + 1))

    # 列表地址
    def get_addr_in_over_stay_form(self, n):
        return self.driver.get_text('x,//*[@id="stopCar-tbody"]/tr[%s]/td[8]' % str(n + 1))

    # 经度
    def get_lng_in_over_stay_form(self, n):
        return float(
            self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[9]' % str(n + 1)).split('/')[0])

    # 纬度
    def get_lat_in_over_stay_form(self, n):
        return float(
            self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[9]' % str(n + 1)).split('/')[1])

    # 总计停留时间
    def get_total_stay_time_in_over_stay_form(self):
        return self.driver.get_text("x,//*[@id='stopCar-alltimes']")

    # acc报表页面数
    def get_total_page_in_over_acc_form(self):
        a = self.driver.get_element('x,//*[@id="paging-accReport"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-accReport"]')
            return total
        else:
            return 0

    # acc页面开始时间
    def get_over_acc_report_form_begin_time(self):
        return self.driver.get_element('startTime_acc').get_attribute('value') + ':00'

    # 页面结束时间
    def get_over_acc_report_form_end_time(self):
        return self.driver.get_element('endTime_acc').get_attribute('value') + ':00'

    # 页面acc状态
    def get_over_acc_report_form_acc_state(self):
        state = self.driver.get_text('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[3]/div/span/div/span[2]')
        if state == "打开":
            return "on"
        elif state == "关闭":
            return "off"
        else:
            return "all"

    # 每页行数
    def get_total_number_per_page_in_over_acc_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="accTableContent"]/tbody/tr')))

    # 列表imei
    def get_imei_in_over_acc_form(self, n):
        return self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[3]' % str(n + 1))

    # 列表状态
    def get_state_in_over_acc_form(self, n):
        # return self.driver.get_text('x,//*[@id="accTable"]/tr[%s]/td[5]' % str(n + 1))
        state = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[5]' % str(n + 1))
        if state == "打开":
            return "1"
        elif state == "关闭":
            return "0"

    # 开始时间
    def get_start_time_in_over_acc_form(self, n):
        return self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[6]' % str(n + 1))

    # 结束时间
    def get_end_time_in_over_acc_form(self, n):
        return self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[7]' % str(n + 1))

    # 总用时
    def get_total_time_in_over_acc_form(self):
        return self.driver.get_text('aCCTotalTime')

    # 打开次数
    def get_total_time_in_open_count_acc_form(self):
        return self.driver.get_text('aCCOn')

    # 关闭次数
    def get_total_time_in_close_count_acc_form(self):
        return self.driver.get_text('aCCOff')

    def get_total_page_in_over_stay_not_shut_down_form(self):
        a = self.driver.get_element('x,//*[@id="paging-stopNotOff"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-stopNotOff"]')
        else:
            return 0

    def get_total_number_per_page_in_over_stay_not_shut_down_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="stopNotOffTableContent"]/tbody/tr')))

    def get_total_page_in_acc(self):
        a = self.driver.get_element('x,//*[@id="paging-accReport"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-accReport"]')
        else:
            return 0

    def get_total_number_per_page_in_acc(self):
        return len(list(self.driver.get_elements('x,//*[@id="accTableContent"]/tbody/tr')))

    def get_total_page_in_status(self):
        a = self.driver.get_element('x,//*[@id="paging-offLine"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-offLine"]')
        else:
            return 0

    def get_total_number_per_page_in_status(self):
        return len(list(self.driver.get_elements('x,//*[@id="offlineTableContent"]/tbody/tr')))

    def get_total_page_in_electric(self):
        a = self.driver.get_element('x,//*[@id="paging-electric"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-electric"]')
        else:
            return 0

    def get_total_number_per_page_in_electric(self):
        return len(list(self.driver.get_elements('x,//*[@id="electricTableContent"]/tbody/tr')))

    def get_total_number_per_page_in_alarm_overview(self):
        a = len(list(self.driver.get_elements('x,//*[@id="alarmReportTable"]/tbody/tr')))
        if 1 == a:
            try:
                b = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr/td')
                if '暂无数据' == b:
                    return 0
            except:
                return 1
        else:
            return a

    def get_total_page_in_alarm_detail(self):
        a = self.driver.get_element('x,//*[@id="alarm_info_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="alarm_info_paging"]')
        else:
            return 0

    def get_total_number_per_page_in_alarm_detail(self):
        return len(list(self.driver.get_elements('x,//*[@id="alarmTableContent"]/tbody/tr')))

    def get_total_page_in_obd_mileage(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-day"]')
        else:
            return 0

    def get_total_number_per_page_in_obd_mileage(self):
        return len(list(self.driver.get_elements('x,//*[@id="travelDayTableContent"]/tbody/tr')))

    def get_total_page_in_obd_travel(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-day"]')
        else:
            return 0

    def get_total_number_per_page_in_obd_travel(self):
        return len(list(self.driver.get_elements('x,//*[@id="travelDayTableContent"]/tbody/tr')))

    def get_total_page_in_obd_car_condition(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-day"]')
        else:
            return 0

    def get_total_number_per_page_in_obd_car_condition(self):
        return len(list(self.driver.get_elements('x,//*[@id="travelDayTableContent"]/tbody/tr')))
