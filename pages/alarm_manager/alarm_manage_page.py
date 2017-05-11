from time import sleep

from pages.base.base_page import BasePage


class AlarmManagePage(BasePage):
    def click_alarm_icon(self):
        self.driver.click_element('x,//*[@id="gaojing"]')
        sleep(2)

    def get_text_after_click_alarm_icon(self):
        return self.driver.get_text('x,//*[@id="alarmMessage"]/div[1]/h5')

    def click_alarm_alarm_set_up(self):
        self.driver.click_element('x,//*[@id="alarmPushSet_a"]')
        sleep(2)

    def get_text_after_click_alarm_set_up(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        text = self.driver.get_text('x,//*[@id="alarmConfigModal"]/div/div/div[1]/h4')
        self.driver.default_frame()
        return text

    def click_close_alarm_set_up(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        self.driver.click_element('x,/html/body/div[1]/div/div/div[1]/button')
        self.driver.default_frame()

    def click_cancel_alarm_set_up(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        self.driver.click_element('x,//*[@id="alarmConfigModal"]/div/div/div[3]/button[2]')
        self.driver.default_frame()

    def click_save_alarm_set_up(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')

        self.driver.operate_input_element('x,//*[@id="offlineAlarmTime"]', '100')
        self.driver.click_element('x,//*[@id="baseSetForm"]/div[1]/div/label/div/ins')
        self.driver.operate_input_element('x,//*[@id="stayAlertTime"]', '100')
        self.driver.click_element('x,//*[@id="baseSetForm"]/div[2]/div/label/div/ins')
        self.driver.click_element('x,//*[@id="lowerDiv"]/div/label/div/ins')

        self.driver.click_element('x,//*[@id="alarmSetSubmit"]')

        self.driver.default_frame()

    def click_push_setting_button(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        self.driver.click_element('x,//*[@id="pushSetLi"]')
        sleep(2)
        self.driver.default_frame()

    def get_number_alarm_set_up(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        number = len(list(self.driver.get_elements('x,//*[@id="alarm_appSet_tbody"]/tr')))
        sleep(2)
        self.driver.default_frame()
        return number

    def click_all_set_up_email(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')

        self.driver.click_element('x,//*[@id="alarmTableHeader"]/thead/tr/th[4]/a')

        self.driver.default_frame()

    def get_text_after_click_all_set_up_email(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        text = self.driver.get_text('x,//*[@id="alarmEmailModal"]/div/div/div[1]/h4')
        self.driver.default_frame()
        return text

    def click_cancel_all_set_up_email(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        self.driver.click_element('x,//*[@id="alarmEmailModal"]/div/div/div[3]/button[2]')
        self.driver.default_frame()

    def click_close_all_set_up_email(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        self.driver.click_element('x,//*[@id="alarmEmailModal"]/div/div/div[1]/button/span')
        self.driver.default_frame()

    def click_save_all_set_up_email(self):
        self.driver.switch_to_frame('x,//*[@id="alarmModalFrame"]')
        self.driver.operate_input_element('x,//*[@id="modalBody"]/div/div/ul/li/input', '123@123.123')
        self.driver.click_element('x,//*[@id="alarmMailSetSubmit"]')
        sleep(2)
        self.driver.default_frame()

    def click_save_set_up_email(self):
        self.driver.operate_input_element('x,//*[@id="modalBody"]/div/div/ul/li/input', '123@123.123')
        self.driver.click_element('x,//*[@id="alarmMailSetSubmit"]')
        sleep(2)

    def get_first_imei_value(self):
        text = self.driver.get_text('x,//*[@id="alarmInfoTable"]/tr[1]/td[2]/a')
        self.driver.click_element('x,//*[@id="alarmInfoTable"]/tr[1]/td[2]/a')
        sleep(2)
        return text

    def get_text_after_click_first_imei(self):
        text = self.driver.get_text('x,/html/body/div[17]/div/div/div[1]/h4')

        return text

    def get_imei_after_click_imei(self):
        self.driver.switch_to_frame('x,//*[@id="commModal_iframe"]')
        text = self.driver.get_element('x,//*[@id="device_info_a"]/fieldset/div[1]/div[1]/input[2]').get_attribute(
            'value')
        self.driver.default_frame()
        return text

    def close_edit_dev_details(self):
        self.driver.click_element('x,//*[@id="commModal"]/div/div/div[1]/button/span')

    def cancel_edit_dev_details(self):
        self.driver.click_element('x,//*[@id="commModal"]/div/div/div[3]/button[2]')
        sleep(2)

    def cancel_save_dev_details(self):
        self.driver.switch_to_frame('x,//*[@id="commModal_iframe"]')

        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[1]/input', '我的设备')
        self.driver.operate_input_element('x,//*[@id="device_info_a"]/fieldset/div[2]/div[2]/input', 'sim123')
        self.driver.operate_input_element('x,//*[@id="reMark"]', '备注')

        self.driver.click_element('x,/html/body/div[1]/ul/li[2]/a')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[1]/div[1]/input', '张三')
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/div[1]/div[2]/input', '妖妖灵')
        self.driver.operate_input_element('x,//*[@id="device_info_b"]/fieldset/fieldset/fieldset/div[1]/div[2]/input',
                                          '深圳')

        self.driver.default_frame()

        self.driver.click_element('x,//*[@id="commModal_submit_btn"]')
        sleep(3)

    def click_alarm_handle_button(self):
        self.driver.click_element('x,/html/body/div[7]/div[2]/div[2]/table/tbody/tr[1]/td[8]/a')
        sleep(2)

    def get_text_after_click_alarm_handle(self):
        return self.driver.get_text('x,//*[@id="alarmDealModal_deal"]/div/div/div[1]/h4')

    def close_alarm_handle(self):
        self.driver.click_element('x,//*[@id="alarmDealModal_deal"]/div/div/div[1]/button/span')
        sleep(2)

    def cancel_alarm_handle(self):
        self.driver.click_element('x,//*[@id="alarmDealModal_deal"]/div/div/div[3]/button[2]')
        sleep(2)

    def save_alarm_handle(self):
        self.driver.operate_input_element('x,//*[@id="alarmDealModal_deal_inputDealUserName"]', '张三')
        self.driver.operate_input_element('x,//*[@id="alarmDealModal_deal_dealContent"]', '这是备注')
        self.driver.click_element('x,//*[@id="saveAlarmDealBtn"]')
        sleep(3)
