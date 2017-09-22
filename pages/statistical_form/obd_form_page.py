from time import sleep

from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.base.new_paging import NewPaging


class ObdFormPage(BasePage):
    def click_obd_form_mileage_statistical_button(self):
        self.driver.click_element('x,//*[@id="OBDmileageReport"]/a')
        sleep(3)

    def switch_to_obd_mileage_statistical_frame(self):
        self.driver.switch_to_frame('x,//*[@id="OBDmileageReportFrame"]')
        sleep(1)

    def add_data_to_search_obd_mileage_statistical_form(self, search_data):
        # 选择时间
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        if search_data['choose_date'] == '':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="startTime_travel"]', search_data['begin_time'])
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="endTime_travel"]', search_data['end_time'])

        elif search_data['choose_date'] == 'today':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif search_data['choose_date'] == 'yesterday':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')

        elif search_data['choose_date'] == 'this_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')

        elif search_data['choose_date'] == 'last_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')

        elif search_data['choose_date'] == 'this_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')

        elif search_data['choose_date'] == 'last_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')

        sleep(2)

        # 选择用户
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[3]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_data['user_name'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(3)

        # TODO:obd form choose imei
        # 输入设备imei
        self.driver.operate_input_element('x,//*[@id="imei"]', self.search_imei())

        # 点击搜索按钮
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[5]/button')
        sleep(5)

    def search_imei(self):
        return '868120145148729'

    def get_dev_name_in_obd_mileage_statistical_form(self):
        return self.driver.get_text('x,//*[@id="deviceName"]')

    def get_dev_total_mile_obd_mileage_statistical_form(self):
        return self.driver.get_text('x,//*[@id="accumulatedMileage"]')

    def get_dev_avg_oil_obd_mileage_statistical_form(self):
        return self.driver.get_text('x,//*[@id="averageFuelConsumption"]')

    def get_avg_oil_obd_mileage_statistical_form(self):
        return self.driver.get_text('x,//*[@id="averageFuelConsumption"]')

    def get_dev_total_oil_obd_mileage_statistical_form(self):
        return self.driver.get_text('x,//*[@id="totalFuel"]')

    def click_obd_form_tracel_statistical_button(self):
        self.driver.click_element('x,//*[@id="OBDtracelReport"]/a')

    def switch_to_obd_tracel_statistical_frame(self):
        self.driver.switch_to_frame('x,//*[@id="OBDtracelReportFrame"]')

    def add_data_to_search_obd_tracel_statistical_form(self, data):
        # 选择时间
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        if data['choose_date'] == '':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="startTime_travel"]', data['begin_time'])
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="endTime_travel"]', data['end_time'])

        elif data['choose_date'] == 'today':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif data['choose_date'] == 'yesterday':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')

        elif data['choose_date'] == 'this_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')

        elif data['choose_date'] == 'last_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')

        elif data['choose_date'] == 'this_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')

        elif data['choose_date'] == 'last_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')

        sleep(2)

        # 选择用户
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[3]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', data['user_name'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(3)

        # TODO:obd form choose imei
        # 输入设备imei
        self.driver.operate_input_element('x,//*[@id="imei"]', self.search_imei())

        # 点击搜索按钮
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_dev_name_in_obd_tracel_statistical_form(self):
        return self.driver.get_text('x,//*[@id="deviceName"]')

    def get_dev_total_mile_obd_tracel_statistical_form(self):
        return self.driver.get_text('x,//*[@id="accumulatedMileage"]')

    def get_dev_avg_oil_obd_tracel_statistical_form(self):
        return self.driver.get_text('x,//*[@id="averageFuelConsumption"]')

    def get_avg_oil_obd_tracel_statistical_form(self):
        return self.driver.get_text('x,//*[@id="averageSpeed"]')

    def get_dev_total_oil_obd_tracel_statistical_form(self):
        return self.driver.get_text('x,//*[@id="totalFuel"]')

    def get_dev_name_in_sql(self, param):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cousor = connect.cursor()
        sql = "SELECT deviceName FROM equipment_mostly WHERE imei = '%s';" % param
        cousor.execute(sql)
        dev_name = cousor.fetchall()[0][0]
        cousor.close()
        connect.close()
        return dev_name

    def get_obd_list_total_page_number(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_page('x,//*[@id="paging-day"]')
        else:
            return 0

    def get_per_page_total_number(self):
        return len(list(self.driver.get_elements('x,//*[@id="mileage-day-tbody"]/tr')))

    def get_per_mile_in_obd_mileage_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[n]/td[3]' % str(n + 1))

    def get_per_oil_in_obd_mileage_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[n]/td[4]' % str(n + 1))

    def click_per_page(self, i):
        self.driver.click_element('l,%s' % str(i + 1))

    def get_sql_total_number(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_travel"]').get_attribute('value')
        end_time = self.driver.get_element('x,//*[@id="endTime_travel"]').get_attribute('value')

        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_form()
        cursor = connect.cursor()
        sql = "select DATE_FORMAT(CREATE_TIME,'%Y-%m-%d') FROM gt_obd_trip WHERE DEVICE_IMEI = '" + self.search_imei() + "' and (START_TIME BETWEEN '" + begin_time + "' and '" + end_time + "' or END_TIME BETWEEN '" + begin_time + "' and '" + end_time + "' or (START_TIME<='" + begin_time + "' and END_TIME >= '" + end_time + "')) GROUP BY DATE_FORMAT(CREATE_TIME,'%Y-%m-%d');"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(data)

    def get_web_total_number(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_page = NewPaging(self.driver, self.base_url)
            return new_page.get_total_number('x,//*[@id="paging-day"]', 'x,//*[@id="mileage-day-tbody"]')
        else:
            return 0

    def get_sql_total_number_in_tracel_form(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_travel"]').get_attribute('value')
        end_time = self.driver.get_element('x,//*[@id="endTime_travel"]').get_attribute('value')

        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_form()
        cursor = connect.cursor()
        sql = "select DEVICE_IMEI FROM gt_obd_trip WHERE DEVICE_IMEI = '" + self.search_imei() + "' and (START_TIME BETWEEN '" + begin_time + "' and '" + end_time + "' or END_TIME BETWEEN '" + begin_time + "' and '" + end_time + "' or (START_TIME<='" + begin_time + "' and END_TIME >= '" + end_time + "'));"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(data)

    def get_web_total_number_in_tracel_form(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_page = NewPaging(self.driver, self.base_url)
            return new_page.get_total_number('x,//*[@id="paging-day"]', 'x,//*[@id="mileage-day-tbody"]')
        else:
            return 0

    def get_per_mile_in_obd_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[5]' % str(n + 1))

    def get_per_oil_in_obd_tracel_form(self, n):
        return self.driver.get_text('x,//*[@id="mileage-day-tbody"]/tr[%s]/td[6]' % str(n + 1))

    def click_obd_vehicle_condition_condition_form_button(self):
        self.driver.click_element('x,//*[@id="OBDcarConditionReport"]/a')
        sleep(2)

    def switch_to_obd_vehicle_condition_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="OBDcarConditionReportFrame"]')

    def add_data_to_search_obd_vehicle_condition_form(self, data):
        # 选择时间
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        if data['choose_date'] == '':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="startTime_travel"]', data['begin_time'])
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="endTime_travel"]', data['end_time'])

        elif data['choose_date'] == 'today':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif data['choose_date'] == 'yesterday':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')

        elif data['choose_date'] == 'this_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')

        elif data['choose_date'] == 'last_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')

        elif data['choose_date'] == 'this_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')

        elif data['choose_date'] == 'last_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')

        sleep(2)

        # 选择用户
        self.driver.click_element('x,//*[@id="CarConditionFrom"]/div[1]/div[3]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', data['user_name'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(3)

        # TODO:obd form choose imei
        # 输入设备imei
        self.driver.operate_input_element('x,//*[@id="imei"]', self.search_imei())

        # 点击搜索按钮
        self.driver.click_element('x,//*[@id="CarConditionFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_dev_name_in_obd_vehicle_condition_form(self):
        return self.driver.get_text('x,//*[@id="deviceName"]')

    def get_dev_total_mile_obd_vehicle_condition_form(self):
        return self.driver.get_text('x,//*[@id="averageFuelConsumption"]')

    def get_dev_avg_oil_obd_vehicle_condition_form(self):
        return self.driver.get_text('x,//*[@id="averageFuelConsumption"]')

    def get_avg_oil_obd_vehicle_condition_form(self):
        return self.driver.get_text('x,//*[@id="averageSpeed"]')

    def get_dev_total_oil_obd_vehicle_condition_form(self):
        return self.driver.get_text('x,//*[@id="totalFuel"]')

    def get_sql_total_number_in_obd_vehicel_condition_form(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_travel"]').get_attribute('value')
        end_time = self.driver.get_element('x,//*[@id="endTime_travel"]').get_attribute('value')

        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_form()
        cursor = connect.cursor()
        sql = "SELECT DEVICE_IMEI FROM gt_obd_his WHERE DEVICE_IMEI = '" + self.search_imei() + "' and CREATE_TIME BETWEEN '" + begin_time + "' and '" + end_time + "' and ERROR_CODE is NULL and RAPID_ACCELERATION = 0 and RAPID_DECELERATION = 0;"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(data)

    def get_web_total_number_in_vehicel_condition_form(self):
        a = self.driver.get_element('x,//*[@id="paging-day"]').get_attribute('style')
        if a == 'display: block;':
            new_page = NewPaging(self.driver, self.base_url)
            return new_page.get_total_number('x,//*[@id="paging-day"]', 'x,//*[@id="mileage-day-tbody"]')
        else:
            return 0

    def click_obd_trouble_form_button(self):
        self.driver.click_element('x,//*[@id="OBDfailureReport"]/a')
        sleep(2)

    def switch_to_obd_trouble_form_frame(self):
        self.driver.switch_to_frame('x,//*[@id="OBDfailureReportFrame"]')

    def add_data_to_search_obd_trouble_form(self, data):
        # 选择时间
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        if data['choose_date'] == '':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[1]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="startTime_travel"]', data['begin_time'])
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="endTime_travel"]', data['end_time'])

        elif data['choose_date'] == 'today':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[2]')

        elif data['choose_date'] == 'yesterday':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[3]')

        elif data['choose_date'] == 'this_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[4]')

        elif data['choose_date'] == 'last_week':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[5]')

        elif data['choose_date'] == 'this_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')

        elif data['choose_date'] == 'last_month':
            self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[7]')

        sleep(2)

        # 选择用户
        self.driver.click_element('x,//*[@id="FailureFrom"]/div[1]/div[3]/div/div[1]/span/button')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', data['user_name'])
        self.driver.click_element('x,//*[@id="search_user_btn"]')
        sleep(3)
        self.driver.click_element('c,autocompleter-item')
        sleep(3)

        # TODO:obd form choose imei
        # 输入设备imei
        self.driver.operate_input_element('x,//*[@id="imei"]', self.search_imei())

        # 点击搜索按钮
        self.driver.click_element('x,//*[@id="FailureFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_sql_total_number_in_obd_trouble_form(self):
        begin_time = self.driver.get_element('x,//*[@id="startTime_travel"]').get_attribute('value')
        end_time = self.driver.get_element('x,//*[@id="endTime_travel"]').get_attribute('value')

        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_form()
        cursor = connect.cursor()
        sql = "SELECT DEVICE_IMEI FROM gt_obd_his WHERE DEVICE_IMEI = '" + self.search_imei() + "' and CREATE_TIME BETWEEN '" + begin_time + "' and '" + end_time + "' and ERROR_CODE is not NULL;"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(data)
