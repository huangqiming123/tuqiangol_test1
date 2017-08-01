from time import sleep

from pages.base.base_page import BasePage
from pages.base.base_page_server import BasePageServer


class SafeAreaPage(BasePageServer):
    def click_control_after_click_safe_area(self):
        # 点击控制台后点击指令管理
        self.driver.click_element('x,//*[@id="geozone"]/a')
        sleep(2)

    def click_all_select_button(self):
        # 点击列表的全选按钮
        self.driver.click_element('x,//*[@id="areaTableHeader"]/thead/tr/th[1]/label/div/ins')

    def click_delete_button(self):
        self.driver.click_element('x,//*[@id="deletesafe"]')
        sleep(2)

    def click_cancel_detele_button(self):
        self.driver.click_element('c,layui-layer-btn1')

    def click_close_detele_button(self):
        self.driver.click_element('c,layui-layer-ico')

    def click_list_edit_button(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a[1]')
        sleep(2)
        self.driver.click_element('l,编辑')
        sleep(2)

    def get_text_after_click_edit(self):
        return self.driver.get_text('x,/html/body/div[2]/div[1]')

    def ensure_edit_list(self, param, param1):
        self.driver.operate_input_element('x,//*[@id="geonameHtml"]', param)
        self.driver.operate_input_element('x,//*[@id="descriptionHtml"]', param1)
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def click_cancel_edit(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def click_close_edit(self):
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[1]/button/span')
        sleep(2)

    def click_list_delete_button(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a[1]')
        sleep(2)
        self.driver.click_element('l,删除')

    def click_relevance_button(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a[1]')
        sleep(2)
        self.driver.click_element('l,关联')
        sleep(2)

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
            a = self.driver.get_element('x,//*[@id="accEmailSend"]').is_selected()
            if a == False:
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
        sleep(2)

    def click_detele_button_with_mark(self):
        self.driver.click_element('x,//*[@id="deletesafe"]')
        sleep(2)

    def click_edit_button_in_list(self):
        self.driver.click_element('x,//*[@id="marktbody"]/tr[1]/td[2]/a')
        sleep(2)
        self.driver.click_element('l,编辑')
        sleep(2)

    def click_ensure_edit_in_list(self, param, param1):
        self.driver.operate_input_element('x,//*[@id="geonameHtml"]', param)
        self.driver.operate_input_element('x,//*[@id="descriptionHtml"]', param1)
        self.driver.click_element('c,layui-layer-btn0')
        sleep(4)

    def click_cancel_edit_in_list(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def click_close_edit_in_list(self):
        self.driver.click_element('x,//*[@id="createModal"]/div/div/div[1]/button/span')
        sleep(2)

    def click_delete_button_in_list(self):
        self.driver.click_element('x,//*[@id="marktbody"]/tr[1]/td[2]/a')
        sleep(2)
        self.driver.click_element('l,删除')
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

    def click_select_fence_button(self):
        self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div[1]/div/div/div/ul/li[2]')
        sleep(2)

    def get_per_number(self):
        number = len(list(self.driver.get_elements('x,//*[@id="areatbody"]/tr')))
        return number

    def get_text_safe_area_type(self, m):
        text = self.driver.get_text('x,//*[@id="areatbody"]/tr[%s]/td[2]' % str(m + 1))
        return text

    def click_select_black_address_button(self):
        self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/div[1]/div/div/div/ul/li[3]')
        sleep(2)

    def get_page(self):
        text = self.driver.get_text('x,//*[@id="areapage"]')
        return text

    def get_text_after_click_delete(self):
        return self.driver.get_text('c,layui-layer-content')

    def click_ensure(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def click_close(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def click_creat_map(self):
        self.driver.click_element('x,//*[@id="createsafe"]')
        sleep(2)

    def get_text_after_create_map(self):
        text = self.driver.get_text('c,popover-content')
        return text

    def get_first_list_black_address_name(self):
        return self.driver.get_element('x,//*[@id="areatbody"]/tr[1]/td[1]').get_attribute('title')

    def click_edit_black_address(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a[1]')
        sleep(2)
        self.driver.click_element('l,编辑')
        sleep(2)

    def get_black_address_after_click_edit(self):
        return self.driver.get_element('x,//*[@id="geonameHtml"]').get_attribute('value')

    def get_black_address_input_value(self):
        value = self.driver.get_element('x,//*[@id="blackcar"]').is_selected()
        return value

    def get_text_after_ensure(self):
        text = self.driver.get_text('c,layui-layer-content')
        return text

    def get_first_list_fence_name(self):
        return self.driver.get_element('x,//*[@id="areatbody"]/tr[1]/td[1]').get_attribute('title')

    def click_edit_fence(self):
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a[1]')
        sleep(2)
        self.driver.click_element('l,编辑')
        sleep(2)

    def get_fence_name_after_edit(self):
        return self.driver.get_element('x,//*[@id="geonameHtml"]').get_attribute('value')

    def click_customer(self, n):
        self.driver.click_element('x,//*[@id="ud_userTree_%s_span"]' % str(n + 1))
        sleep(2)

    def search_user_in_customer(self, data):
        self.driver.operate_input_element('x,//*[@id="key"]', data)
        self.driver.click_element('x,//*[@id="cusTreeSearchBtn"]')
        sleep(3)

    def get_text_after_search_no_data(self):
        return self.driver.get_text('x,//*[@id="setdevicecontext"]/div[1]/div/div[1]/div/span')

    def get_no_data_attribute(self):
        return self.driver.get_element('x,//*[@id="ud_deviceTree"]').get_attribute('style')

    def get_text_no_data(self):
        return self.driver.get_element('x,//*[@id="ud_deviceTree_nodata"]/span').text

    def click_close_default_group(self):
        self.driver.click_element('x,//*[@id="ud_deviceTree_1_switch"]')
        sleep(2)

    def get_total_group(self):
        return len(list(self.driver.get_elements('x,//*[@id="ud_deviceTree"]/li')))

    def click_open_per_group(self, m):
        self.driver.click_element(
            'x,/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[%s]/span[1]' % str(m + 1))
        sleep(2)

    def get_total_dev_in_per_group(self, m):
        text = self.driver.get_text(
            'x,/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[%s]/a/span[2]' % str(m + 1))
        print(text)
        dev_number = text.split('(')[1].split(')')[0]
        return dev_number

    def get_list_dev_in_per_group(self, m):
        return len(list(self.driver.get_elements(
            'x,/html/body/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[%s]/ul/li' % str(m + 1))))

    def get_total_dev_in_per_groups(self, m, list_total_dev):
        text = self.driver.get_text('x,//*[@id="ud_deviceTree_%s_span"]' % str(m + 1 + list_total_dev))
        print(text)
        dev_number = text.split('(')[1].split(')')[0]
        return dev_number

    def get_total_page_num_mark_page(self):
        a = self.driver.get_text('x,//*[@id="markpage"]')
        number = a.split('/')[1]
        return number

    def get_page_in_mark_page(self):
        text = self.driver.get_text('x,//*[@id="markpage"]')
        return text

    def click_next_page_in_mark_page(self):
        self.driver.click_element('x,//*[@id="markTablePage"]/a[3]')
        sleep(2)

    def get_per_number_in_mark_page(self):
        return len(list(self.driver.get_elements('x,//*[@id="marktbody"]/tr')))

    def click_ago_page_in_mark_page(self):
        self.driver.click_element('x,//*[@id="markTablePage"]/a[2]')
        sleep(2)

    def get_first_name_in_mark_point_list(self):
        return self.driver.get_element('x,//*[@id="marktbody"]/tr[1]/td[1]').get_attribute('title')

    def click_edit_button_in_mark_point(self):
        self.driver.click_element('x,//*[@id="marktbody"]/tr[1]/td[2]/a[1]')
        sleep(2)
        self.driver.click_element('l,编辑')
        sleep(2)

    def get_name_after_click_edit(self):
        return self.driver.get_element('x,//*[@id="geonameHtml"]').get_attribute('value')

    def click_create_mark_point(self):
        self.driver.click_element('x,//*[@id="createsafe"]')
        sleep(2)

    def click_delete_in_mark_point(self):
        self.driver.click_element('x,//*[@id="deletesafe"]')
        sleep(2)

    def get_count_dev_number(self):
        return self.driver.get_text('x,//*[@id="devNumber"]')

    def get_list_total_number(self):
        return len(list(self.driver.get_elements('x,//*[@id="checkList"]/li')))

    def get_send_email_button_value(self):
        return self.driver.get_element('x,//*[@id="accEmailSend"]').is_selected()

    def click_send_email_button(self):
        self.driver.click_element('x,//*[@id="accEmailSend"]')
        sleep(2)

    def get_email_style(self):
        text = self.driver.get_element('x,//*[@id="acc_configure_form"]/div[3]/div/ul').get_attribute('style')
        a = text.split(' ')[1].split(';')[0]
        return a

    def add_email_to_check_email_type(self, email):
        self.driver.operate_input_element('x,//*[@id="acc_configure_form"]/div[3]/div/ul/li[1]/input', email)

    def add_email_to_check_second_email_type(self, param):
        self.driver.operate_input_element('x,//*[@id="acc_configure_form"]/div[3]/div/ul/li[2]/input', param)

    def add_email_to_check_third_email_type(self, param):
        self.driver.operate_input_element('x,//*[@id="acc_configure_form"]/div[3]/div/ul/li[3]/input', param)

    def get_text_after_ensures(self):
        return self.driver.get_text('c,layui-layer-setwin')
