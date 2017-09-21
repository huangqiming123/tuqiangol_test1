from time import sleep

from pages.base.base_page import BasePage


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
        return '868120145233604'

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
