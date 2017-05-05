from time import sleep

from pages.base.base_page import BasePage


class SafeAreaPage(BasePage):
    def click_control_after_click_safe_area(self):
        # 点击控制台后点击指令管理
        current_handle = self.driver.get_current_window_handle()
        self.driver.click_element('x,//*[@id="index"]/a')
        sleep(2)

        all_handle = self.driver.get_all_window_handles()

        for handle in all_handle:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.driver.click_element('x,//*[@id="safetyManagement"]/a')

    def click_all_select_button(self):
        # 点击列表的全选按钮
        self.driver.click_element('x,//*[@id="areaTableHeader"]/thead/tr/th[1]/label/div/ins')

    def click_delete_button(self):
        self.driver.click_element('x,//*[@id="deletesafe"]')

    def click_cancel_detele_button(self):
        self.driver.click_element('x,/html/body/div[10]/div[3]/a[2]')

    def click_close_detele_button(self):
        self.driver.click_element('x,/html/body/div[10]/span/a')

    def click_list_edit_button(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[2]/a[1]')
        sleep(2)

    def get_text_after_click_edit(self):
        return self.driver.get_text('x,/html/body/div[2]/div/div/div[1]/h4')

    def ensure_edit_list(self, param, param1):
        self.driver.operate_input_element('x,//*[@id="geonameHtml"]', param)
        self.driver.operate_input_element('x,//*[@id="descriptionHtml"]', param1)
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[3]/button[1]')
        sleep(2)

    def click_cancel_edit(self):
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[3]/button[3]')
        sleep(2)

    def click_close_edit(self):
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[1]/button/span')
        sleep(2)

    def click_list_delete_button(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[2]/a[2]')
        sleep(2)

    def click_relevance_button(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[2]/a[3]')

    def search_account_click_equipment(self, current_account):
        self.driver.operate_input_element('x,//*[@id="key"]', current_account)
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)

        self.driver.click_element('x,//*[@id="ud_deviceTree_1_check"]')
        sleep(2)

    def add_data(self, data):
        self.driver.operate_input_element('x,//*[@id="key"]', data['search_acc'])
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
        sleep(2)
        self.driver.click_element('c,autocompleter-item')
        sleep(2)
        self.driver.click_element('x,//*[@id="setdevicecontext"]/div[3]/div[1]/a')

        self.driver.click_element('x,//*[@id="ud_deviceTree_1_check"]')
        sleep(2)

        el = self.driver.get_element('x,//*[@id="accEmailSend"]')
        self.driver.execute_script(el)

        self.driver.operate_input_element('x,//*[@id="stayTimeIn"]', data['time_01'])
        self.driver.operate_input_element('x,//*[@id="stayTimeOut"]', data['time_02'])

        if data['email'] == '1':
            self.driver.click_element('x,//*[@id="acc_configure_form"]/div[3]/div/label/div/ins')
            self.driver.operate_input_element('x,//*[@id="acc_configure_form"]/div[3]/div/ul/li[1]/input',
                                              '123@123.com')

        self.driver.click_element('x,//*[@id="setdeviceModal"]/div/div/div[3]/button[1]')
        sleep(2)

    def get_current_page_number(self):
        a = self.driver.get_text('x,//*[@id="areapage"]')
        number = a.split('/')[0]
        return number

    def get_total_page_num(self):
        a = self.driver.get_text('x,//*[@id="areapage"]')
        number = a.split('/')[1]
        return number

    def click_next_page(self):
        self.driver.click_element('x,//*[@id="areaTablePage"]/a[3]')
        sleep(2)

    def click_ago_page(self):
        self.driver.click_element('x,//*[@id="areaTablePage"]/a[2]')
        sleep(2)

    def click_last_page(self):
        self.driver.click_element('x,//*[@id="areaTablePage"]/a[4]')
        sleep(2)

    def clcik_first_page(self):
        self.driver.click_element('x,//*[@id="areaTablePage"]/a[1]')
        sleep(1)

    def click_mark_button(self):
        self.driver.click_element('x,//*[@id="marktab"]')
        sleep(2)

    def click_all_select_button_with_mark(self):
        self.driver.click_element(
            'x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div[1]/table/thead/tr/th[1]/label/div/ins')

    def click_detele_button_with_mark(self):
        self.driver.click_element('x,//*[@id="deletesafe"]')
        sleep(2)

    def click_edit_button_in_list(self):
        self.driver.click_element('x,//*[@id="marktbody"]/tr[1]/td[2]/a[1]')
        sleep(2)

    def click_ensure_edit_in_list(self, param, param1):
        self.driver.operate_input_element('x,//*[@id="geonameHtml"]',param)
        self.driver.operate_input_element('x,//*[@id="descriptionHtml"]',param1)
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[3]/button[1]')
        sleep(2)

    def click_cancel_edit_in_list(self):
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[3]/button[3]')
        sleep(2)

    def click_close_edit_in_list(self):
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[1]/button/span')
        sleep(2)

    def click_delete_button_in_list(self):
        self.driver.click_element('x,//*[@id="marktbody"]/tr[1]/td[2]/a[2]')
        sleep(2)

    def get_total_page_number_mark(self):
        a = self.driver.get_text('x,//*[@id="markpage"]')
        number = a.split('/')[1]
        return number

    def get_current_page_number_mark(self):
        a = self.driver.get_text('x,//*[@id="markpage"]')
        number = a.split('/')[0]
        return number

    def click_next_page_mark(self):
        self.driver.click_element('x,//*[@id="markTablePage"]/a[3]')
        sleep(2)

    def click_ago_page_mark(self):
        self.driver.click_element('x,//*[@id="markTablePage"]/a[2]')
        sleep(2)

    def click_last_page_mark(self):
        self.driver.click_element('x,//*[@id="markTablePage"]/a[4]')
        sleep(2)

    def clcik_first_page_mark(self):
        self.driver.click_element('x,//*[@id="markTablePage"]/a[1]')
        sleep(2)

