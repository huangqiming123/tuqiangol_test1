from time import sleep

from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class MassageCenterPage(BasePageServer):
    def click_massage_center_button(self):
        # 点击消息中心的按钮
        self.driver.click_element('x,//a[@href="/customer/sendUserMessage"]')
        sleep(3)

    def add_data_search_massage_data(self, search_data):
        # 填写imei
        self.driver.operate_input_element('x,//*[@id="remainSearchDeviceInput"]', search_data['imei'])
        # 选择消息类型
        self.driver.click_element('x,/html/body/div[6]/div[2]/div[1]/form/div[2]/span[1]/div/span[2]')
        sleep(2)
        if search_data['massage_type'] == '':
            self.driver.click_element('x,//li[@title="消息类型"]')

        elif search_data['massage_type'] == '设备离线':
            self.driver.click_element('x,//li[@title="设备离线"]')

        elif search_data['massage_type'] == "设备到期":
            self.driver.click_element('x,//li[@title="设备到期"]')

        elif search_data['massage_type'] == '导游播报':
            self.driver.click_element('x,//li[@title="导游播报"]')

        elif search_data['massage_type'] == '电量过低':
            self.driver.click_element('x,//li[@title="电量过低"]')
        sleep(2)

        # 选择已读未读状态
        self.driver.click_element('x,/html/body/div[6]/div[2]/div[1]/form/div[2]/span[2]/div/span[2]')
        sleep(2)
        if search_data['is_read'] == '':
            self.driver.click_element('x,//li[@title="状态"]')

        elif search_data['is_read'] == '未读':
            self.driver.click_element('x,//li[@title="未读"]')

        elif search_data['is_read'] == '已读':
            self.driver.click_element('x,//li[@title="已读"]')
        sleep(2)
        self.driver.click_element('x,//button[@title="搜索"]')
        sleep(10)

    def get_sql_total_search_center_massage(self, search_data, all_user_id):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        sql = "SELECT u.id FROM user_message u WHERE u.userId in %s" % str(all_user_id)
        ###########################################################

        if search_data['imei'] != "":
            sql += " and u.imeis = %s" % search_data['imei']

        ###########################################################

        if search_data['massage_type'] == '设备离线':
            sql += " and u.type = 2"
        elif search_data['massage_type'] == "设备到期":
            sql += " and u.type = 1"
        elif search_data['massage_type'] == '导游播报':
            sql += " and u.type = 3"
        elif search_data['massage_type'] == '电量过低':
            sql += " and u.type = 4"

        ###########################################################

        if search_data['is_read'] == '未读':
            sql += " and u.readFlag = 0"
        elif search_data['is_read'] == '已读':
            sql += " and u.readFlag = 1"

        ###########################################################
        sql += ";"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return len(data)

    def get_web_total_search_center_massage(self):
        ###########################################################
        ##获取页面上搜索用户消息的数据条数
        ###########################################################
        a = self.driver.get_element('x,//*[@id="msg_paging"]').get_attribute('style')
        if a == "display: block;":
            new_paging = NewPaging(self.driver, self.base_url)
            return new_paging.get_total_number('x,//*[@id="msg_paging"]', 'x,//*[@id="msg_tbody"]')
        else:
            return 0
