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
