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

    def click_customer_mangement(self):
        # 点击客户管理
        self.driver.click_element('x,//*[@id="customer"]/a')
        sleep(3)

    def click_add_new_customer_buttons(self):
        self.driver.click_element('x,//*[@id="AddCustomer"]')
        sleep(2)

    def switch_to_add_new_customer_frame(self):
        # 切换到新增客户的frame
        self.driver.switch_to_frame('x,//*[@id="layui-layer-iframe1"]')

    def add_user_name_and_user_account(self, new_customer_data):
        self.driver.operate_input_element('x,//*[@id="nickName"]', new_customer_data[0])
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="account"]', new_customer_data[1])
        sleep(1)

    def search_user_in_customer_management(self, param):
        self.driver.operate_input_element('x,//*[@id="searchaccount"]', param)
        sleep(1)
        self.driver.click_element('x,//button[@title="搜索"]')
        sleep(3)

    def click_edit_customer_button(self):
        # 点击编辑用户信息
        self.driver.click_element('x,//*[@id="customertablecontent"]/tbody/tr[1]/td[9]/a[2]')
        sleep(2)

    def click_reset_password_button(self):
        # 点击重置密码的按钮
        self.driver.click_element('x,//*[@id="customertablecontent"]/tbody/tr[1]/td[9]/a[4]')
        sleep(2)

    def click_transfer_customer_button(self):
        # 点击转移客户
        self.driver.click_element('x,//*[@id="customertablecontent"]/tbody/tr[1]/td[9]/a[5]')
        sleep(2)

    def click_delete_customer_button(self):
        self.driver.click_element('x,//*[@id="customertablecontent"]/tbody/tr[1]/td[9]/a[3]')
        sleep(2)

    def select_customer_management_condition(self):
        # 选择客户管理的查询条件
        self.driver.click_element('x,//*[@id="serviceType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="客户管理"]')
        sleep(2)

    def select_add_new_customer_log(self):
        # 选择新增客户的查询添加
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="新增客户"]')
        sleep(2)

    def select_edit_customer_log(self):
        # 选择新增客户的查询添加
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="修改用户信息"]')
        sleep(2)

    def select_delete_customer_log(self):
        # 选择新增客户的查询添加
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="删除用户信息"]')
        sleep(2)

    def select_reset_password_log(self):
        # 选择新增客户的查询添加
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="重置密码"]')
        sleep(2)

    def select_transfer_customer_log(self):
        # 选择新增客户的查询添加
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="转移客户"]')
        sleep(2)

    def click_safe_area_button(self):
        # 点击安全区域
        self.driver.click_element('x,//*[@id="geozone"]/a')

    def search_platform_fence(self):
        sleep(3)
        self.driver.click_element('x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[2]/div[2]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="平台围栏"]')
        sleep(2)

    def get_first_fence_name(self):
        return self.driver.get_element('x,//*[@id="areatbody"]/tr[1]/td[1]').get_attribute('title')

    def click_edit_fence_button(self):
        # 点击编辑围栏的按钮
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a')
        sleep(1)
        self.driver.click_element('l,编辑')
        sleep(2)

    def click_relevance_fence_button(self):
        # 点击编辑围栏的按钮
        self.driver.click_element('x,//*[@id="areatbody"]/tr[1]/td[3]/a')
        sleep(1)
        self.driver.click_element('l,关联')
        sleep(2)

    def click_dev_relevance_fence(self):
        self.driver.click_element('x,//*[@id="ud_deviceTree_2_check"]')
        sleep(1)
        a = self.driver.get_element('x,//input[@class="geozone-geolist-checkbox inOut"]').is_selected()
        if a == False:
            self.driver.click_element('x,//ins[@class="iCheck-helper]"')
        sleep(1)
        imei = self.driver.get_text('x,//*[@id="ud_deviceTree_2_span"]')
        return imei.split('[')[1].split(']')[0]

    def select_safe_area_search(self):
        self.driver.click_element('x,//*[@id="serviceType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="安全区域"]')
        sleep(2)

    def select_edit_safe_area_search(self):
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="新增、编辑区域"]')
        sleep(5)

    def select_relevant_safe_area_search(self):
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="关联设备"]')
        sleep(5)

    def select_delete_relevant_safe_area_search(self):
        self.driver.click_element('x,//*[@id="logType"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="删除关联"]')
        sleep(5)
