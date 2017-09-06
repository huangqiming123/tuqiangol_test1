from time import sleep

from pages.base.base_page import BasePage
from pages.base.new_paging import NewPaging


class StatisticFormPage3(BasePage):
    def request_base_url(self):
        return 'http://119.23.160.20:9080/api/gpscontroll/v1'
        # return 'http://172.16.0.105:9080/api/gpscontroll/v1'

    def change_dev_imei_format(self, imeis):
        imei_list = []
        for imei in imeis:
            imei_list.append(int(imei))
        a = (str(imei_list).split('[')[1].split(']')[0]).replace(" ", '')
        return a

    def get_sport_overview_form_begin_time(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_sport"]').get_attribute('value')
        return begin_time + ':00'

    def get_sport_overview_form_end_time(self):
        end_time = self.driver.get_element('x,//*[@id="endTime_sport"]').get_attribute('value')
        return end_time + ':00'

    def get_web_search_total_number_sport_overview(self):
        return len(list(self.driver.get_elements('x,//*[@id="run-tbody"]/tr')))

    def get_imei_in_sport_overview(self, n):
        return self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_mileage_in_sport_overview(self, n):
        return int(float(self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[5]' % str(n + 1))) * 1000)

    def get_over_speed_times_in_sport_overview(self, n):
        return int(self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[6]' % str(n + 1)))

    def get_stop_times_in_sport_overview(self, n):
        return int(self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[7]' % str(n + 1)))

    def get_mile_report_form_begin_time(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_mileage"]').get_attribute('value')
        return begin_time + ':00'

    def get_mile_report_form_end_time(self):
        end_time = self.driver.get_element('x,//*[@id="endTime_mileage"]').get_attribute('value')
        return end_time + ':00'

    def get_total_page_in_mile_report_form(self):
        a = self.driver.get_element('x,//*[@id="paging-mileage"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-mileage"]')
            return total
        else:
            return 0

    def get_total_number_per_page_in_mile_report_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileage-tbody"]/tr')))

    def get_imei_in_mile_report_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_start_time_in_mile_report_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[5]' % str(n + 1))

    def get_end_time_in_mile_report_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[6]' % str(n + 1))

    def get_distance_in_mile_report_form(self, n):
        return float(self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[7]' % str(n + 1)))

    def click_per_page_in_mile_report_form(self, i):
        self.driver.click_element('l,%s' % str(i + 1))
        sleep(3)

    def get_total_page_in_mile_report_form_with_day(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-day"]')
            return total
        else:
            return 0

    def get_total_number_per_page_in_mile_report_form_with_day(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileage-day-tbody"]/tr')))

    def get_imei_in_mile_report_form_with_day(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_distance_in_mile_report_form_with_day(self, n):
        return float(self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[6]' % str(n + 1)))

    def get_at_day_time_in_mile_report_form_with_day(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[5]' % str(n + 1))

    def get_total_page_in_tracel_report_form(self):
        a = self.driver.get_element('x,//*[@id="paging-mileage"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-mileage"]')
            return total
        else:
            return 0

    def get_tracel_report_form_begin_time(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_travel"]').get_attribute('value')
        return begin_time + ':00'

    def get_tracel_report_form_end_time(self):
        end_time = self.driver.get_element('x,//*[@id="endTime_travel"]').get_attribute('value')
        return end_time + ':00'

    def get_total_number_per_page_in_tracel_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileage-tbody"]/tr')))

    def get_imei_in_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_distance_in_tracel_form(self, n):
        return float(self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[9]' % str(n + 1)))

    def get_start_time_in_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[5]' % str(n + 1))

    def get_end_time_in_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[6]' % str(n + 1))

    def get_start_addr_in_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[7]' % str(n + 1))

    def get_end_addr_in_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[8]' % str(n + 1))

    def get_avg_speed_in_tracel_form(self, n):
        return float(self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[12]' % str(n + 1)))

    def get_run_time_second_in_tracel_form(self, n):
        a = self.driver.get_text('x,//*[@id="mileage-tbody"]/tr[%s]/td[10]' % str(n + 1))
        hour = int(a.split('小')[0])
        min = int(a.split('时')[1].split('分')[0])
        sec = int(a.split('分')[1].split('秒')[0])
        return hour * 3600 + min * 60 + sec

    def get_tracel_form_begin_time(self):
        return

    def get_total_page_in_tracel_form_with_day(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-day"]')
            return total
        else:
            return 0

    def get_total_number_per_page_in_tracel_report_form_with_day(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileage-day-tbody"]/tr')))

    def get_imei_in_tracel_form_with_day(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_distance_in_tracel_report_form_with_day(self, n):
        return float(self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[6]' % str(n + 1)))

    def get_at_day_time_in_tracel_report_form_with_day(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[5]' % str(n + 1))
