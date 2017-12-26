from time import sleep

from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer


class UserCenterPage(BasePageServer):
    def get_account_info(self, user_account):
        # 获取当前登录账号的客户信息
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "SELECT o.nickName,o.phone,o.email FROM user_info o WHERE o.account = '%s';" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()
        data_list = []
        for range in data:
            for range1 in range:
                data_list.append(range1)
        cursor.close()
        connect.close()
        return data_list

    def click_user_center_button(self):
        # 点击个人中心
        self.driver.click_element('x,//*[@id="userCenter"]')
        sleep(2)

    def click_modify_user_info(self):
        # 点击修改资料
        self.driver.click_element('x,//a[@class="js-edit-information"]')
        sleep(2)

    def get_user_account_in_modify_page(self):
        return self.driver.get_element('x,//*[@id="edit-modal-account"]').get_attribute('value')

    def get_user_name_in_modify_page(self):
        return self.driver.get_element('x,//*[@id="edit-modal-nickName"]').get_attribute('value')

    def get_user_phone_in_modify_page(self):
        return self.driver.get_element('x,//*[@id="edit-modal-phone"]').get_attribute('value')

    def get_user_email_in_modify_page(self):
        return self.driver.get_element('x,//*[@id="edit-modal-email"]').get_attribute('value')

    def click_cancel_button(self):
        self.driver.click_element('c,layui-layer-btn1')
        sleep(2)

    def click_close_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def add_data_to_modify_info(self, user_to_modify_info):
        # 填写数据
        self.driver.operate_input_element('x,//*[@id="edit-modal-nickName"]', user_to_modify_info['username'])
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="edit-modal-phone"]', user_to_modify_info['phone'])
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="edit-modal-email"]', user_to_modify_info['email'])
        sleep(1)

    def click_ensure_button(self):
        self.driver.click_element('c,layui-layer-btn0')
        sleep(2)

    def input_user_name_in_modify_info(self, special_char):
        self.driver.operate_input_element('x,//*[@id="edit-modal-nickName"]', special_char)
        sleep(1)

    def input_user_phone_in_modify_info(self, special_char):
        self.driver.operate_input_element('x,//*[@id="edit-modal-phone"]', special_char)
        sleep(1)

    def get_user_name_in_main_page(self):
        return self.driver.get_text('x,//*[@id="topusername"]')

    def get_user_phone_in_main_page(self):
        return self.driver.get_text('x,//*[@id="topuserphone"]')

    def get_user_name_exception_in_modify_info_page(self):
        return self.driver.get_text('x,//label[@for="edit-modal-nickName"]')

    def input_user_email_in_modify_info(self, email_format):
        self.driver.operate_input_element('x,//*[@id="edit-modal-email"]', email_format)
        sleep(1)

    def get_user_email_exception_in_modify_info_page(self):
        return self.driver.get_text('x,//label[@for="edit-modal-email"]')

    def click_dev_management_button(self):
        # 点击设备管理按钮
        self.driver.click_element('x,//*[@id="device"]/a')
        sleep(2)

    def get_dev_list_first_imei(self):
        return self.driver.get_text('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[4]')

    def click_edit_dev_button(self):
        # 点击编辑的按钮
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[1]')
        sleep(2)

    def click_help_button(self):
        self.driver.click_element('x,//*[@id="js-toHelp"]')
        sleep(2)

    def switch_to_business_frame(self):
        self.driver.switch_to_frame('x,//*[@id="servicelogReportFrame"]')

    def get_operation_in_business_log(self):
        return self.driver.get_text('x,//*[@id="logslist_xf"]/tr[1]/td[1]')

    def get_target_account_in_business_log(self):
        return self.driver.get_text('x,//*[@id="logslist_xf"]/tr[1]/td[3]')

    def get_operation_platform_in_business_log(self):
        return self.driver.get_text('x,//*[@id="logslist_xf"]/tr[1]/td[4]')

    def get_desc_in_business_log(self):
        return self.driver.get_text('x,//*[@id="logslist_xf"]/tr[1]/td[5]/span')

    def click_sale_button(self):
        self.driver.click_element('x,//*[@id="deviceTableContent"]/tbody/tr[1]/td[13]/a[2]')
        sleep(4)
        # 点击客户树第一个
        self.driver.click_element('x,//*[@id="treeDemo_device_sale_id_1_span"]')
        sleep(2)
        # 点击销售
        self.driver.click_element('x,//*[@id="device_sale_id"]/div[3]/div[2]/button[3]')
        sleep(2)

    def search_dev_sale_in_business_log(self):
        self.driver.click_element('x,//span[@title="设备修改"]')
        sleep(2)
        self.driver.click_element('x,//li[@title="设备分配"]')
        sleep(2)

    def click_search_button_in_business_log(self):
        self.driver.click_element('x,//*[@id="search_xf"]')
        sleep(5)