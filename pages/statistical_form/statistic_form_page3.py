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
        if a == '0':
            return 0
        else:
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

    def get_total_page_in_over_speed_form(self):
        a = self.driver.get_element('x,//*[@id="paging-overspeed"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page('x,//*[@id="paging-overspeed"]')
            return total
        else:
            return 0

    def get_over_speed_report_form_begin_time(self):
        return self.driver.get_element('x,//*[@id="startTime_overspeed"]').get_attribute('value') + ':00'

    def get_over_speed_report_form_end_time(self):
        return self.driver.get_element('x,//*[@id="endTime_overspeed"]').get_attribute('value') + ':00'

    def get_total_number_per_page_in_over_speed_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="overspeed-tbody"]/tr')))

    def get_imei_in_over_speed_form(self, n):
        return self.driver.get_text('x,//*[@id="overspeed-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_speed_in_over_speed_form(self, n):
        return int(self.driver.get_text('x,//*[@id="overspeed-tbody"]/tr[%s]/td[6]' % str(n + 1)))

    def get_addr_in_over_speed_form(self, n):
        return self.driver.get_text('x,//*[@id="overspeed-tbody"]/tr[%s]/td[7]' % str(n + 1))

    def get_time_in_over_speed_form(self, n):
        return self.driver.get_text('x,//*[@id="overspeed-tbody"]/tr[%s]/td[5]' % str(n + 1))

    def get_lat_in_over_speed_form(self, n):
        return float(self.driver.get_text('x,//*[@id="overspeed-tbody"]/tr[%s]/td[8]' % str(n + 1)).split('/')[1])

    def get_lng_in_over_speed_form(self, n):
        return float(self.driver.get_text('x,//*[@id="overspeed-tbody"]/tr[%s]/td[8]' % str(n + 1)).split('/')[0])

    def add_data_to_search_in_alarm_overview(self, data):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')

        # 选择时间
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/span[2]')
        sleep(2)
        if data['choose_date'] == 'today':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[2]')

        elif data['choose_date'] == 'yesterday':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[3]')

        elif data['choose_date'] == 'this_week':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[4]')

        elif data['choose_date'] == 'last_week':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[5]')

        elif data['choose_date'] == 'this_month':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[6]')

        elif data['choose_date'] == 'last_month':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[7]')

        elif data['choose_date'] == '':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[1]')
            sleep(2)
            # 填写开始时
            js1 = 'document.getElementById("startTime_alarmReport").removeAttribute("readonly")'
            self.driver.execute_js(js1)
            self.driver.operate_input_element('x,//*[@id="startTime_alarmReport"]', data['began_time'])
            # 填写结束时间
            js = 'document.getElementById("endTime_alarmReport").removeAttribute("readonly")'
            self.driver.execute_js(js)
            self.driver.operate_input_element('x,//*[@id="endTime_alarmReport"]', data['end_time'])

        # 选择用户
        # 点击搜索
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[3]/div/div[1]/span/button')
        sleep(2)
        # 输入数据
        self.driver.operate_input_element('x,//*[@id="cusTreeKey"]', data['user_name'])
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
        # 点击搜索的第一个
        sleep(2)
        self.driver.click_element('c,autocompleter-item')

        # 填写是否包含下级
        input_style = self.driver.get_element('x,//*[@id="alarmForm"]/div/div[5]/div/label/div/input').is_selected()
        if input_style == True and data['is_next'] == '0':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[5]/div/label/div/ins')

        elif input_style == False and data['is_next'] == '1':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[5]/div/label/div/ins')

        # 选择是否输入设备
        self.driver.clear_input('x,//*[@id="imeiInput_alarmOverview"]')
        sleep(2)
        if data['is_enter_dev'] == '1':
            self.driver.click_element('x,//*[@id="alarmForm"]/div/div[4]/div/div/div/div[1]/span/button')
            sleep(3)
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
            self.driver.click_element('x,//*[@id="treeModal_alarmOverview"]/div[2]/label/div/ins')
            sleep(1)
            self.driver.click_element('x,//*[@id="treeModal_alarmOverview"]/div[2]/div/button[1]')
            sleep(2)
        # 点击搜索
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[6]/button')
        sleep(5)

    def select_all_alarm_type_in_alarm_overview_search(self):
        self.driver.switch_to_frame('x,//*[@id="alarmOverviewFrame"]')
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[3]/div[2]/div[3]/table/thead/tr/th/span')
        sleep(3)
        self.driver.default_frame()
        input_style = self.driver.get_element('x,//*[@id="allCheck"]').is_selected()
        if input_style == False:
            self.driver.click_element('x,//*[@id="serAlarmTypeModal"]/div/label/div/ins')
            sleep(2)
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def get_alarm_overview_form_begin_time(self):
        return self.driver.get_element('x,//*[@id="startTime_alarmReport"]').get_attribute('value') + ':00'

    def get_alarm_overview_form_end_time(self):
        return self.driver.get_element('x,//*[@id="endTime_alarmReport"]').get_attribute('value') + ':00'

    def get_no_data_display_in_alarm_overview(self):
        a = self.driver.get_element('x,//*[@id="alarm_report_nodata"]').get_attribute('style')
        return a

    def get_web_total_number_alarm_overview(self):
        return len(list(self.driver.get_elements('x,//*[@id="alarm_report_tbody"]/tr')))

    def get_imei_in_alarm_overview(self, n):
        return self.driver.get_text('x,//*[@id="alarm_report_tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_sos_number_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[1]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[1]' % str(n + 1))
        return int(number)

    def get_blind_area_enter_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[2]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[2]' % str(n + 1))
        return int(number)

    def get_blind_area_exit_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[3]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[3]' % str(n + 1))
        return int(number)

    def booting_notification_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[4]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[4]' % str(n + 1))
        return int(number)

    def first_fix_notification_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[5]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[5]' % str(n + 1))
        return int(number)

    def get_low_external_power_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[6]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[6]' % str(n + 1))
        return int(number)

    def get_low_power_protection_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[7]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[7]' % str(n + 1))
        return int(number)

    def get_sim_card_change_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[8]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[8]' % str(n + 1))
        return int(number)

    def get_over_speed_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[9]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[9]' % str(n + 1))
        return int(number)

    def get_power_off_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[10]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[10]' % str(n + 1))
        return int(number)

    def airplane_mode_after_low_power_protection_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[11]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[11]' % str(n + 1))
        return int(number)

    def disassembly_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[12]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[12]' % str(n + 1))
        return int(number)

    def get_cut_power_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[13]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[13]' % str(n + 1))
        return int(number)

    def get_vibration_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[14]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[14]' % str(n + 1))
        return int(number)

    def get_movement_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[15]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[15]' % str(n + 1))
        return int(number)

    def get_low_power_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[16]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[16]' % str(n + 1))
        return int(number)

    def get_exit_geozone_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[18]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[18]' % str(n + 1))
        return int(number)

    def enter_geozone_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[19]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[19]' % str(n + 1))
        return int(number)

    def rearview_mirror_vibration_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[22]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[22]' % str(n + 1))
        return int(number)

    def get_enter_terminal_geozone_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[24]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[24]' % str(n + 1))
        return int(number)

    def get_exit_terminal_geozone_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[25]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[25]' % str(n + 1))
        return int(number)

    def get_off_line_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[26]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[26]' % str(n + 1))
        return int(number)

    def get_voice_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[27]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[27]' % str(n + 1))
        return int(number)

    def get_acc_open_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[28]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[28]' % str(n + 1))
        return int(number)

    def get_acc_shut_down_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[30]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[30]' % str(n + 1))
        return int(number)

    def get_long_time_not_out_fence_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[29]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[29]' % str(n + 1))
        return int(number)

    def get_long_time_not_into_fence_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[31]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[31]' % str(n + 1))
        return int(number)

    def get_stay_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[32]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[32]' % str(n + 1))
        return int(number)

    def get_linger_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[33]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[33]' % str(n + 1))
        return int(number)

    def get_illegal_mobile_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[34]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[34]' % str(n + 1))
        return int(number)

    def insufficient_battery_back_up_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[36]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[36]' % str(n + 1))
        return int(number)

    def get_over_step_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[37]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[37]' % str(n + 1))
        return int(number)

    def get_sensitive_areas_fence_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[38]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[38]' % str(n + 1))
        return int(number)

    def get_over_speed_platform_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[39]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[39]' % str(n + 1))
        return int(number)

    def select_all_alarm_type_in_alarm_detail_search(self):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        self.driver.click_element('x,//*[@id="alarmTitle"]/button')
        sleep(1)
        self.driver.default_frame()
        a = self.driver.get_element('x,//*[@id="allCheck"]').is_selected()
        if a == False:
            self.driver.click_element('x,//*[@id="serAlarmTypeModal"]/div/label/div/ins')
            sleep(1)
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def add_data_to_search_alarm_detail(self, data):
        self.driver.switch_to_frame('x,//*[@id="alarmDdetailsFrame"]')
        # 点击搜索
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/span/button')
        sleep(2)
        # 输入数据
        self.driver.operate_input_element('x,//*[@id="cusTreeKey2"]', data['user_name'])
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn2"]')
        # 点击搜索的第一个
        sleep(2)
        self.driver.click_element('c,autocompleter-item')

        # 选择查询的设备型号
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div/div/span[2]')
        sleep(2)
        if data['type'] == 'all':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div/div/div/ul/li[1]')
            sleep(1)

        # 选择是否未读还是已读
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/span[2]')
        sleep(2)
        if data['status'] == 'all':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/div/ul/li[1]')
            sleep(1)
        elif data['status'] == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/div/ul/li[2]')
            sleep(1)
        elif data['status'] == '0':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[3]/div[2]/div/div/div/ul/li[3]')
            sleep(1)

        # 选择是否输入设备
        self.driver.clear_input('x,//*[@id="imeiInput_alarmDetail"]')
        if data['is_input_dev'] == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[1]/span/button')
            sleep(2)
            all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_alarmDetail"]/li'))
            all_group_num = len(all_group_list)
            if all_group_num == 1:
                pass
            else:
                for n in range(1, all_group_num):
                    sleep(1)
                    self.driver.click_element(
                        'x,/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                            n + 1))
            self.driver.click_element('x,//*[@id="treeModal_alarmDetail"]/div[2]/label/div/ins')
            sleep(1)
            self.driver.click_element('x,//*[@id="treeModal_alarmDetail"]/div[2]/div/button[1]')
            sleep(2)

        # 填写告警时间
        js1 = 'document.getElementById("startTime_alarmInfo").removeAttribute("readonly")'
        self.driver.execute_js(js1)
        self.driver.operate_input_element('x,//*[@id="startTime_alarmInfo"]', data['alarm_begin_time'])

        js2 = 'document.getElementById("endTime_alarmInfo").removeAttribute("readonly")'
        self.driver.execute_js(js2)
        self.driver.operate_input_element('x,//*[@id="endTime_alarmInfo"]', data['alarm_end_time'])

        # 填写定位时间
        js3 = 'document.getElementById("startTime_position").removeAttribute("readonly")'
        self.driver.execute_js(js3)
        self.driver.operate_input_element('x,//*[@id="startTime_position"]', data['push_begin_time'])

        js4 = 'document.getElementById("endTime_position").removeAttribute("readonly")'
        self.driver.execute_js(js4)
        self.driver.operate_input_element('x,//*[@id="endTime_position"]', data['push_end_time'])

        self.driver.click_element('x,//*[@id="getAlertInfo_btn"]')
        sleep(5)

    def get_alarm_begin_time_in_alarm_detail_page(self):
        return self.driver.get_element('x,//*[@id="startTime_alarmInfo"]').get_attribute('value') + ':00'

    def get_alarm_end_time_in_alarm_detail_page(self):
        return self.driver.get_element('x,//*[@id="endTime_alarmInfo"]').get_attribute('value') + ':00'

    def get_push_begin_time_in_alarm_detail_page(self):
        return self.driver.get_element('x,//*[@id="startTime_position"]').get_attribute('value') + ':00'

    def get_push_end_time_in_alarm_detail_page(self):
        return self.driver.get_element('x,//*[@id="endTime_position"]').get_attribute('value') + ':00'

    def get_web_total_number_in_alarm_detail_page(self):
        return len(list(self.driver.get_elements('x,//*[@id="alarm_info_tbody"]/tr')))

    def get_imei_in_alarm_detail(self, n):
        return self.driver.get_text('x,//*[@id="alarm_info_tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_creat_time_in_alarm_detail(self, n):
        return self.driver.get_text('x,//*[@id="alarm_info_tbody"]/tr[%s]/td[7]' % str(n + 1))

    def get_push_time_in_alarm_detail(self, n):
        return self.driver.get_text('x,//*[@id="alarm_info_tbody"]/tr[%s]/td[8]' % str(n + 1))

    def get_addr_in_alarm_detail(self, n):
        return self.driver.get_text('x,//*[@id="alarm_info_tbody"]/tr[%s]/td[10]' % str(n + 1))

    def get_read_status_in_alarm_detail(self, n):
        a = self.driver.get_text('x,//*[@id="alarm_info_tbody"]/tr[%s]/td[12]' % str(n + 1))
        if a == '未读':
            return -1
        elif a == '已读':
            return 0

    def get_web_total_in_mile_form_with_search_mile(self):
        return self.driver.get_text('x,//*[@id="allmileages"]')

    def get_web_total_in_mile_form_with_search_day(self):
        return self.driver.get_text('x,//*[@id="allmileages-day"]')

    def get_web_total_in_tracel_form_with_search_mile(self):
        return self.driver.get_text('x,//*[@id="allmileages"]')

    def get_web_total_time_in_tracel_form_with_search_mile(self):
        return self.driver.get_text('x,//*[@id="allmileageshours"]')

    def get_web_total_in_tracel_form_with_search_day(self):
        return self.driver.get_text('x,//*[@id="allmileages-day"]')

    def get_risk_point_alert_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[35]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[35]' % str(n + 1))
        return int(number)

    def change_time_format(self, web_total_time):
        a = web_total_time
        hour = int(a.split('小')[0])
        min = int(a.split('时')[1].split('分')[0])
        sec = int(a.split('分')[1].split('秒')[0])
        return hour * 3600 + min * 60 + sec

    def open_conver_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[20]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[20]' % str(n + 1))
        return int(number)

    def low_power_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[21]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[21]' % str(n + 1))
        return int(number)

    def sleep_alarm_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[23]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[23]' % str(n + 1))
        return int(number)

    def get_door_alarm_in_alarm_overview(self, n):
        self.driver.execute_script(self.driver.get_element('x,//*[@id="tableXScrollCon"]/table/tbody/tr[1]/td[17]'))
        sleep(1)
        number = self.driver.get_text('x,//*[@id="tableXScrollCon"]/table/tbody/tr[%s]/td[17]' % str(n + 1))
        return int(number)
