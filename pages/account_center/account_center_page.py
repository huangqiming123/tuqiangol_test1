import datetime
from time import sleep
import time

from model.connect_sql import ConnectSql
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class AccountCenterPage(BasePageServer):
    def switch_to_account_info_frame(self):
        self.driver.switch_to_frame('x,//*[@id="usercenterFrame"]')
        sleep(1)

    def get_account_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="topusername"]')

    def get_account_type_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="topusertype"]')

    def get_account_telephone_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="topuserphone"]')

    def get_account_01_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="userAccount"]')

    def get_account_type_01_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="userType"]')

    def get_account_telephone_01_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="userPhone"]')

    def get_telephone_alarm_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="phoneRecord"]')

    def get_massage_alarm_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="infoRecord"]')

    def get_telephone_and_massage_alarm_number_in_mysql(self, account):
        conncet_sql = ConnectSql()
        conncet = conncet_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()
        sql = "SELECT v.phoneRecord,v.infoRecord FROM rc_recharge_card_stock v INNER JOIN user_info u on v.userId = u.userId WHERE u.account = '%s';" % account
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conncet.close()
        return data

    def get_year_card_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="yearCard"]')

    def get_life_card_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="lifetimeCard"]')

    def get_year_and_life_card_number_in_mysql(self, account):
        conncet_sql = ConnectSql()
        conncet = conncet_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()
        sql = "SELECT v.yearCard,v.lifetimeCard FROM rc_recharge_card_stock v INNER JOIN user_info u on v.userId = u.userId WHERE u.account = '%s';" % account
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conncet.close()
        return data

    def get_consume_massage_alarm_number(self):
        return self.driver.get_text(
            'x,/html/body/div[1]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/div/div[1]/p[1]')

    def get_consume_massage_alarm_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="yesterdayinfo"]')

    def get_consume_telephone_alarm_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="yesterdayphone"]')

    def get_consume_year_card_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="yesterdayyear"]')

    def get_consume_life_card_number_in_account_info_page(self):
        return self.driver.get_text('x,//*[@id="yesterdaylife"]')

    def get_bengin_time(self, param):
        if param == '昨天':
            today = datetime.date.today()
            yes = today - datetime.timedelta(days=1)
            first = str(yes) + " 00:00"
            return first

        elif param == '本月':
            today = datetime.date.today()
            days_count = datetime.timedelta(days=(today.day - 1))
            this_month = today - days_count
            return str(this_month) + " 00:00"

        elif param == '上月':
            today = datetime.date.today()
            days_count = datetime.timedelta(days=today.day)
            last_month = today - days_count
            month = datetime.date(last_month.year, last_month.month, 1)
            return str(month) + " 00:00"

    def get_end_time(self, param):
        if param == '昨天':
            today = datetime.date.today()
            yes = today - datetime.timedelta(days=1)
            second = str(yes) + " 23:59"
            return second

        elif param == '本月':
            current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
            return current_time

        elif param == '上月':
            today = datetime.date.today()
            days_count = datetime.timedelta(days=today.day)
            last_month = today - days_count
            return str(last_month) + " 23:59"

    def get_consume_number_in_mysql(self, begin_time, end_time, account):
        data = []
        conncet_sql = ConnectSql()
        conncet = conncet_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()

        massage_sql = "SELECT b.amount FROM vs_bill b INNER JOIN user_info o on b.userId = o.userId WHERE o.account = '" + account + "' and b.alarmPushType = 4 and b.creationDate BETWEEN '" + begin_time + "' and '" + end_time + "';"
        cursor.execute(massage_sql)
        massage_data = cursor.fetchall()
        data.append(massage_data[0][0])

        telephone_sql = "SELECT b.amount FROM vs_bill b INNER JOIN user_info o on b.userId = o.userId WHERE o.account = '" + account + "' and b.alarmPushType = 3 and b.creationDate BETWEEN '" + begin_time + "' and '" + end_time + "';"
        cursor.execute(telephone_sql)
        telephone_data = cursor.fetchall()
        data.append(telephone_data[0][0])

        year_card_sql = "SELECT b.imei FROM rc_recharge b INNER JOIN user_info o on b.userId = o.userId WHERE o.account = '" + account + "' and b.cardType = 1 and b.creationDate BETWEEN '" + begin_time + "' and '" + end_time + "';"
        cursor.execute(year_card_sql)
        year_card_data = cursor.fetchall()
        data.append(len(year_card_data))

        life_card_sql = "SELECT b.imei FROM rc_recharge b INNER JOIN user_info o on b.userId = o.userId WHERE o.account = '" + account + "' and b.cardType = 2 and b.creationDate BETWEEN '" + begin_time + "' and '" + end_time + "';"
        cursor.execute(life_card_sql)
        life_card_data = cursor.fetchall()
        data.append(len(life_card_data))

        cursor.close()
        conncet.close()
        return data

    def click_this_month_in_account_page(self):
        self.driver.click_element('x,/html/body/div[1]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/ul/li[2]/a')
        sleep(1)

    def click_last_month_in_account_page(self):
        self.driver.click_element('x,/html/body/div[1]/div/div[2]/div[1]/div[1]/div[4]/div/div[2]/div/ul/li[3]/a')
        sleep(1)

    def switch_to_bill_list_frame(self):
        self.driver.switch_to_frame('x,//*[@id="vsBillFrame"]')
        sleep(1)

    def add_data_to_search_bill_list_in_bill_list_page(self, search_data):
        # 点击清空
        self.driver.click_element('x,//*[@id="clearBtn"]')
        sleep(2)
        # 选择时间
        self.driver.click_element('x,//*[@id="qryForm"]/div/div[1]/div/div/div/span[2]')
        sleep(2)

        if search_data['date_type'] == '今天':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[1]/div/div/div/div/ul/li[1]')

        elif search_data['date_type'] == '本周':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[1]/div/div/div/div/ul/li[2]')

        elif search_data['date_type'] == '本月':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[1]/div/div/div/div/ul/li[3]')

        elif search_data['date_type'] == '上月':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[1]/div/div/div/div/ul/li[4]')

        elif search_data['date_type'] == '自定义':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[1]/div/div/div/div/ul/li[5]')

            self.driver.operate_input_element('x,//*[@id="startTime"]', search_data['begin_time'])
            self.driver.operate_input_element('x,//*[@id="endTime"]', search_data['end_time'])
        sleep(2)
        # 输入告警的imei
        self.driver.operate_input_element('x,//*[@id="imei"]', search_data['imei'])

        # 输入告警的电话
        self.driver.operate_input_element('x,//*[@id="phone"]', search_data['telephone'])

        # 选择告警接收方式 3:电话，4:短信
        self.driver.click_element('x,//*[@id="qryForm"]/div/div[5]/div/div/div/span[2]')
        sleep(2)
        if search_data['alarm_type'] == '3':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[5]/div/div/div/div/ul/li[2]')

        elif search_data['alarm_type'] == '4':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[5]/div/div/div/div/ul/li[3]')

        elif search_data['alarm_type'] == '':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[5]/div/div/div/div/ul/li[1]')
        sleep(2)

        # 选择处理结果 0:失败1:成功
        self.driver.click_element('x,//*[@id="qryForm"]/div/div[6]/div/div/div/span[2]')
        sleep(2)
        if search_data['result'] == '':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[6]/div/div/div/div/ul/li[1]')

        elif search_data['result'] == '0':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[6]/div/div/div/div/ul/li[3]')

        elif search_data['result'] == '1':
            self.driver.click_element('x,//*[@id="qryForm"]/div/div[6]/div/div/div/div/ul/li[2]')
        sleep(2)

        # 点击搜索
        self.driver.click_element('x,//*[@id="qryBtn"]')
        sleep(5)

    def clcik_bill_button_in_account_info_page(self):
        self.driver.click_element('x,//*[@id="vsBill"]/a')
        sleep(2)

    def get_sql_number_after_click_search_button(self, account, search_data):
        conncet_sql = ConnectSql()
        conncet = conncet_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()

        sql = "SELECT b.id FROM vs_bill b INNER JOIN user_info o on b.userId = o.userId WHERE o.account = '" + account + "'"
        if search_data['date_type'] == '今天':
            sql += " and b.creationDate BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "'"

        elif search_data['date_type'] == '本周':
            sql += " and b.creationDate BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_month_end_time() + "'"

        elif search_data['date_type'] == '本月':
            sql += " and b.creationDate BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "'"

        elif search_data['date_type'] == '上月':
            sql += " and b.creationDate BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "'"

        elif search_data['date_type'] == '自定义':
            sql += " and b.creationDate BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "'"

        if search_data['imei'] != '':
            sql += " and b.imei like '%" + search_data['imei'] + "%'"

        if search_data['telephone'] != '':
            sql += " and b.phone like '%" + search_data['telephone'] + "%'"

        if search_data['alarm_type'] != '':
            sql += " and b.alarmPushType = '" + search_data['alarm_type'] + "'"

        if search_data['result'] != '':
            sql += " and b.status = '" + search_data['result'] + "'"

        sql += ";"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conncet.close()
        return len(data)

    def get_today_begin_date(self):
        # 获取今天的开始时间
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return current_time + " 00:00"

    def get_today_end_time(self):
        # 今天的结束时间
        current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        return current_time

    def get_yesterday_begin_time(self):
        # 获取昨天的开始时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        first = str(yes) + " 00:00"
        return first

    def get_yesterday_end_time(self):
        # 获取昨天的结束时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        second = str(yes) + " 23:59"
        return second

    def get_this_week_begin_time(self):
        # 获取本周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.isoweekday()) - 1)
        week = today - days_count
        return str(week) + ' 00:00'

    def get_this_week_end_time(self):
        # 获取本周的结束时间
        current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        return current_time

    def get_last_week_begin_time(self):
        # 获取上周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count - datetime.timedelta(days=6)
        return str(week) + ' 00:00'

    def get_last_week_end_time(self):
        # 获取上周的结束时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count
        return str(week) + ' 23:59'

    def get_this_month_begin_time(self):
        # 获取本月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.day - 1))
        this_month = today - days_count
        return str(this_month) + " 00:00"

    def get_this_month_end_time(self):
        # 获取本月的开始时间
        current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))
        return current_time

    def get_last_month_begin_time(self):
        # 获取上月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        month = datetime.date(last_month.year, last_month.month, 1)
        return str(month) + " 00:00"

    def get_last_month_end_time(self):
        # 获取上月的结束
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        return str(last_month) + " 23:59"

    def get_web_number_after_click_search_button(self):
        a = self.driver.get_element('x,//*[@id="mileage_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="mileage_paging"]', 'x,//*[@id="mileage_body"]')
            return total
        else:
            return 0

    def clcik_order_manage_button_in_account_info_page(self):
        self.driver.click_element('x,//*[@id="ordermanager"]/a')
        sleep(2)

    def switch_to_order_manage_frame(self):
        self.driver.switch_to_frame('x,//*[@id="ordermanagerFrame"]')

    def add_data_to_search_order_manage_in_bill_list_page(self, search_data):
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[3]/button[2]')
        sleep(1)
        # 输入订单编号
        self.driver.operate_input_element('x,//*[@id="orderNo"]', search_data['order_id'])
        # 选择订单查询日期类型
        if search_data['date_type'] != '':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div/div/div/span[2]')
            sleep(2)
            if search_data['date_type'] == '创建时间':
                self.driver.click_element(
                    'x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div/ul/li[1]')
            elif search_data['date_type'] == '支付时间':
                self.driver.click_element(
                    'x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[2]/div/div/div/div/ul/li[2]')
            sleep(2)
            self.driver.operate_input_element('x,//*[@id="startTime_order"]', search_data['begin_time'])
            self.driver.operate_input_element('x,//*[@id="endTime_order"]', search_data['end_time'])

        # 输入商品名称
        self.driver.operate_input_element('x,//*[@id="productName"]', search_data['goods_name'])
        # 选择订单类型
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/span[2]')
        sleep(2)
        if search_data['order_type'] == '':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div/ul/li[1]')

        elif search_data['order_type'] == '3':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div/ul/li[3]')

        elif search_data['order_type'] == '4':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div/ul/li[2]')

        sleep(2)

        # 选择订单状态
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div/div/span[2]')
        sleep(2)
        if search_data['is_order'] == '':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div/ul/li[1]')

        elif search_data['is_order'] == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div/ul/li[3]')

        elif search_data['is_order'] == '0':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[3]/div/div/div/div/ul/li[2]')
        sleep(2)

        # 选择支付方式
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div/div/span[2]')
        sleep(2)
        if search_data['is_pay'] == '':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div/div/div/ul/li[1]')

        elif search_data['is_pay'] == '0':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div/div/div/ul/li[3]')

        elif search_data['is_pay'] == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[4]/div/div/div/div/ul/li[2]')
        sleep(2)

        # 点击搜索
        self.driver.click_element('x,//*[@id="queryorderinfo"]')
        sleep(5)

    def get_sql_number_after_click_order_manage_search_button(self, account, search_data):
        begin_time = self.driver.get_element('x,//*[@id="startTime_order"]').get_attribute('value')
        end_time = self.driver.get_element('x,//*[@id="endTime_order"]').get_attribute('value')
        conncet_sql = ConnectSql()
        conncet = conncet_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()

        sql = "SELECT t.id FROM t_order t INNER JOIN user_info u on t.createBy = u.userId WHERE u.account = '%s'" % account

        if search_data['date_type'] == '创建时间':
            sql += " and t.createDate BETWEEN '" + begin_time + "' and '" + end_time + "'"

        if search_data['date_type'] == '支付时间':
            sql += " and t.transPayTime BETWEEN '" + begin_time + "' and '" + end_time + "'"

        if search_data['goods_name'] != '':
            sql += " and t.productName LIKE '%" + search_data['goods_name'] + "%'"

        if search_data['order_id'] != '':
            sql += " and t.orderNo LIKE '%" + search_data['order_id'] + "%'"

        if search_data['order_type'] != '':
            sql += " and t.orderType = '%s'" % search_data['order_type']

        if search_data['is_order'] != '':
            sql += " and t.payStatus = '%s'" % search_data['is_order']

        if search_data['is_pay'] != '':
            sql += " and t.payType = '%s' and t.payStatus = '1'" % search_data['is_pay']

        sql += ";"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conncet.close()
        return len(data)

    def get_web_number_after_click_order_manage_search_button(self):
        a = self.driver.get_element('x,//*[@id="order_info_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="order_info_paging"]', 'x,//*[@id="orderinfobody"]')
            return total
        else:
            return 0

    def get_consume_massage_alarm_number_in_account_info_page_this_month(self):
        return self.driver.get_text('x,//*[@id="currentinfo"]')

    def get_consume_telephone_alarm_number_in_account_info_page_this_month(self):
        return self.driver.get_text('x,//*[@id="currentphone"]')

    def get_consume_year_card_number_in_account_info_page_this_month(self):
        return self.driver.get_text('x,//*[@id="currentyear"]')

    def get_consume_life_card_number_in_account_info_page_this_month(self):
        return self.driver.get_text('x,//*[@id="currentlife"]')

    def get_consume_massage_alarm_number_in_account_info_page_last_month(self):
        return self.driver.get_text('x,//*[@id="upinfo"]')

    def get_consume_telephone_alarm_number_in_account_info_page_last_month(self):
        return self.driver.get_text('x,//*[@id="upphone"]')

    def get_consume_year_card_number_in_account_info_page_last_month(self):
        return self.driver.get_text('x,//*[@id="upyear"]')

    def get_consume_life_card_number_in_account_info_page_last_month(self):
        return self.driver.get_text('x,//*[@id="uplife"]')

    def clcik_massage_and_telephone_alarm_button_in_account_info_page(self):
        self.driver.click_element('x,//*[@id="vsAlarmSetList"]/a')
        sleep(2)

    def switch_to_massage_and_telephone_alarm_frame(self):
        self.driver.switch_to_frame('x,//*[@id="vsAlarmSetListFrame"]')

    def add_data_to_search_massage_and_telephone_alarm_in_set_page(self, search_data):
        # 清空
        self.driver.click_element('x,//*[@id="clearBtn"]')
        sleep(2)
        self.driver.operate_input_element('x,//*[@id="alarmSetName"]', search_data['alarm_name'])

        # 选择告警类型 3：电话 4：短信
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div/div/span[2]')
        sleep(2)

        if search_data['alarm_type'] == '':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div/div/div/ul/li[1]')

        elif search_data['alarm_type'] == '3':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div/div/div/ul/li[2]')

        elif search_data['alarm_type'] == '4':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div/div/div/ul/li[3]')

        sleep(2)

        self.driver.click_element('x,//*[@id="qryBtn"]')
        sleep(5)

    def get_sql_number_after_click_massage_and_telephone_alarm_set_search_button(self, account, search_data):
        conncet_sql = ConnectSql()
        conncet = conncet_sql.connect_tuqiang_sql()
        cursor = conncet.cursor()

        sql = "SELECT t.id FROM vs_alarm_set t INNER JOIN user_info u on t.createdBy = u.userId WHERE u.account = '%s'" % account

        if search_data['alarm_name'] != '':
            sql += " and t.alarmSetName like '%" + search_data['alarm_name'] + "%'"

        if search_data['alarm_type'] != "":
            sql += " and t.alarmPushType = '%s'" % search_data['alarm_type']

        sql += ";"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conncet.close()
        return len(data)

    def get_web_number_after_click_massage_and_telephone_alarm_search_button(self):
        a = self.driver.get_element('x,//*[@id="alarm_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="alarm_paging"]', 'x,//*[@id="alarm_body"]')
            return total
        else:
            return 0
