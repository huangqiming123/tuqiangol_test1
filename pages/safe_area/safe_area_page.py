from time import sleep

from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer


class SafeAreaPage(BasePageServer):
    def click_control_after_click_safe_area(self):
        # 点击安全区域
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
        sleep(2)

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
            if a is False:
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
            'x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[3]/div[2]/div[1]/table/thead/tr/th[1]/label/div/ins')
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
        self.driver.click_element('x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[2]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[2]/div[1]/div/div/div/ul/li[2]')
        sleep(2)

    def get_per_number(self):
        number = len(list(self.driver.get_elements('x,//*[@id="areatbody"]/tr')))
        return number

    def get_text_safe_area_type(self, m):
        text = self.driver.get_text('x,//*[@id="areatbody"]/tr[%s]/td[2]' % str(m + 1))
        return text

    def click_select_black_address_button(self):
        self.driver.click_element('x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[2]/div[1]/div/div/span[2]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[2]/div[1]/div/div/div/ul/li[3]')
        sleep(2)

    def get_page(self):
        text = self.driver.get_text('x,//*[@id="areapage"]')
        return text

    def get_text_after_click_delete(self):
        return self.driver.get_text('c,layui-layer-content')

    def click_ensure(self):
        self.driver.click_element('c,layui-layer-btn0')
        # self.driver.click_element('l,保存')
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

    # 获取第一个围栏名称文本
    def get_first_fence_name_text(self):
        text = self.driver.get_element('x,//*[@id="areatbody"]/tr[1]/td[1]').get_attribute('title')
        return text

    # 获取第一个地标名称文本
    def get_first_mark_name_text(self):
        text = self.driver.get_element('x,//*[@id="marktbody"]/tr[1]/td[1]').get_attribute('title')
        return text

    ########################################################################################################################

    # 获取围栏关联的设备总数
    def get_total_num_of_dev_relation_fences(self):
        num = self.driver.get_text('x,//*[@id="devNumber"]')
        return int(num)

    # 获取当前围栏实际关联设备数
    def get_all_num_of_dev_relation_fences(self):
        ele_list = self.driver.get_elements('x,//*[@id="checkList"]/li')

        # 获取最后一页总共有多少条记录
        number = len(ele_list)
        if number == '0':
            return '0'
        else:
            return number

    # 点击围栏编辑页面中的选择用户下拉框
    def click_fences_edit_select_users(self):
        self.driver.click_element('x,//*[@id="alarmconfiginfo"]/div[1]/div/div[1]/div[1]/span/button')
        sleep(2)

    # 围栏编辑页面点击删除
    def fences_edit_page_click_delete(self):
        self.driver.click_element('x,//*[@id="alarmconfiginfo"]/div[1]/div/div[2]/div/span/div/button[2]')
        sleep(1)

    # 围栏编辑页面搜索用户
    def fences_edit_pages_search_user(self, search_user):
        self.driver.operate_input_element('x,//*[@id="search_user_text"]', search_user)
        sleep(1)
        self.driver.click_element('x,//*[@id="search_user_btn"]')

    # 围栏编辑页面搜索设备
    def fences_edit_page_search_dev(self, data):
        self.driver.operate_input_element('x,//*[@id="search_text"]', data["account"])
        sleep(2)
        self.driver.click_element('x,//*[@id="alarmconfiginfo"]/div[1]/div/div[3]/div/div/div/div/span[3]')
        sleep(1)
        if data["search_type"] == 'imei':
            self.driver.click_element('x,//*[@id="alarmconfiginfo"]/div[1]/div/div[3]/div/div/div/div/div/ul/li[1]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="searchtext"]', data["search_content"])
            sleep(1)
            self.driver.click_element('x,//*[@id="searchAlarmConfigInfoBtn"]')
            sleep(2)
        if data["search_type"] == '设备名':
            self.driver.click_element('x,//*[@id="alarmconfiginfo"]/div[1]/div/div[3]/div/div/div/div/div/ul/li[2]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="searchtext"]', data["search_content"])
            sleep(1)
            self.driver.click_element('x,//*[@id="searchAlarmConfigInfoBtn"]')
            sleep(2)
        if data["search_type"] == '':
            self.driver.click_element('x,//*[@id="searchtext"]')
            sleep(1)
            self.driver.operate_input_element('x,//*[@id="searchtext"]', data["search_content"])
            sleep(1)
            self.driver.click_element('x,//*[@id="searchAlarmConfigInfoBtn"]')
            sleep(2)

    # 获取搜索到的该围栏关联的设备数
    def get_fence_relation_dev_num(self):
        ele = self.driver.get_elements('x,//*[@id="alarmconfiginfobody"]/tr')
        num = len(ele)
        return num

    # 获取当前编辑的围栏名称
    def get_fence_name_of_cur_edit(self):
        name = self.driver.get_element('x,//*[@id="areatbody"]/tr[1]/td[1]').get_attribute('title')
        return name

    # 点击围栏编辑页面关联设备列表中的删除
    def click_del_in_fences_edit_page(self):
        self.driver.click_element('x,//*[@id="alarmconfiginfo"]/div[1]/div/div[3]/div/span/div/button[2]')
        sleep(1)

    # 围栏编辑页面关联设备列表点击删除之后的文本获取
    def get_text_in_fence_edit_page_after_click_del(self):
        text = self.driver.get_text('x,/html/body/div[12]/div[2]')
        return text

    def click_close_detele_buttons(self):
        self.driver.click_element('x,/html/body/div[12]/span[1]/a')
        sleep(2)

    def click_account_center(self):
        self.driver.click_element('x,//*[@id="accountCenter"]/a')
        sleep(2)

    def get_current_account_in_account_center(self):
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        a = self.driver.get_text('x,//*[@id="userAccount"]')
        self.driver.default_frame()
        return a

    def add_data_to_search_defence_in_safe_area(self, data):
        self.driver.operate_input_element('x,//*[@id="queryareaname"]', data['defence_name'])
        sleep(1)
        self.driver.click_element('x,//*[@id="querycondition"]/button')
        sleep(4)

    def get_web_total_after_click_search(self):
        total_page = int(self.driver.get_text('x,//*[@id="areapage"]').split('/')[1])
        if total_page == 0:
            return 0
        elif total_page == 1:
            return len(list(self.driver.get_elements('x,//*[@id="areatbody"]/tr')))
        else:
            for n in range(total_page - 1):
                self.driver.click_element('x,//*[@id="areaTablePage"]/a[3]')
                sleep(3)
            return (10 * (total_page - 1) + len(list(self.driver.get_elements('x,//*[@id="areatbody"]/tr'))))

    def get_sql_total_after_click_search(self, data, account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "SELECT o.id FROM geozone_info o INNER JOIN user_info u on o.userid = u.userId WHERE u.account = '" + account + "' and o.flag = 0"
        if data['defence_name'] != '':
            sql += " and o.geoname like '%" + data['defence_name'] + "%'"
        sql += ";"
        print(sql)
        cursor.execute(sql)
        sql_data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(sql_data)

    def click_risk_point_share_button(self):
        self.driver.click_element('x,//*[@id="sharetab"]')
        sleep(3)

    def add_data_to_search_risk_point_in_safe_area(self, data):
        self.driver.operate_input_element('x,//*[@id="queryareaname"]', data['risk_name'])
        sleep(1)
        self.driver.click_element('x,//*[@id="querycondition"]/button')
        sleep(3)

    def get_web_total_after_click_search_risk_share(self):
        total_page = int(self.driver.get_text('x,//*[@id="sharepage"]').split('/')[1])
        if total_page == 0:
            return 0
        elif total_page == 1:
            return len(list(self.driver.get_elements('x,//*[@id="sharetbody"]/tr')))
        else:
            for n in range(total_page - 1):
                self.driver.click_element('x,//*[@id="shareTablePage"]/a[3]')
                sleep(3)
            return (10 * (total_page - 1) + len(list(self.driver.get_elements('x,//*[@id="sharetbody"]/tr'))))

    def get_sql_total_after_click_search_risk_share(self, data):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "SELECT t.id FROM t_share_area t WHERE t.name LIKE '%" + data['risk_name'] + "%';"
        print(sql)
        cursor.execute(sql)
        sql_data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(sql_data)
