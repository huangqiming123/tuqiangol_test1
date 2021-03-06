import time
import datetime
from model.connect_sql import ConnectSql
from pages.statistical_form.statistical_form_page import StatisticalFormPage


class SearchSql(StatisticalFormPage):
    def get_today_begin_date(self):
        # 获取今天的开始时间
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return current_time + " 00:00:00"

    def get_today_end_time(self):
        # 今天的结束时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def get_yesterday_begin_time(self):
        # 获取昨天的开始时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        first = str(yes) + " 00:00:00"
        return first

    def get_yesterday_end_time(self):
        # 获取昨天的结束时间
        today = datetime.date.today()
        yes = today - datetime.timedelta(days=1)
        second = str(yes) + " 23:59:59"
        return second

    def get_this_week_begin_time(self):
        # 获取本周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.isoweekday() - 1))
        week = today - days_count
        return str(week) + ' 00:00:00'

    def get_this_week_end_time(self):
        # 获取本周的结束时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def get_last_week_begin_time(self):
        # 获取上周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count - datetime.timedelta(days=6)
        return str(week) + ' 00:00:00'

    def get_last_week_end_time(self):
        # 获取上周的结束时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count
        return str(week) + ' 23:59:59'

    def get_this_month_begin_time(self):
        # 获取本月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=(today.day - 1))
        this_month = today - days_count
        return str(this_month) + " 00:00:00"

    def get_this_month_end_time(self):
        # 获取本月的开始时间
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def get_last_month_begin_time(self):
        # 获取上月的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        month = datetime.date(last_month.year, last_month.month, 1)
        return str(month) + " 00:00:00"

    def get_last_month_end_time(self):
        # 获取上月的结束
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.day)
        last_month = today - days_count
        return str(last_month) + " 23:59:59"

    def search_current_account_equipment(self, user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()

        get_user_id_sql = "select u.userId from user_info u where u.account = '%s';" % user_account
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        user_id = user_id_list[0][0]

        get_account_dev_sql = "select a.imei from equipment_mostly a LEFT JOIN equipment_expiration e on a.imei = e.imei where a.userId = '%s' and a.status = 'NORMAL' and DATEDIFF(a.expiration,CURDATE())>=0 and (e.expiration is NULL OR (e.expiration is not null and DATEDIFF(e.expiration,CURDATE())>=0)) and (e.userId is null or (e.userId is not null and e.userId = '%s')) and a.activationTime is not null;" % (
            user_id, user_id)
        # get_account_dev_sql = "select a.imei from equipment_mostly a where a.userId = '%s' and a.status = 'NORMAL' and DATEDIFF(a.expiration,CURDATE())>=0;" % user_id
        cursor.execute(get_account_dev_sql)
        get_all_dev = cursor.fetchall()
        dev_list = []
        for range1 in get_all_dev:
            for range2 in range1:
                dev_list.append(range2)
        all_dev = tuple(dev_list)
        cursor.close()
        connect.close()
        return all_dev

    def search_sport_overview_sql(self, account_dev, search_data):
        sql = "select b.IMEI from (SELECT s.IMEI FROM day_run_summary AS s WHERE s.IMEI IN %s" % str(account_dev)

        if search_data['choose_date'] == '':
            sql += " and s.ATDAY BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "'"

        elif search_data['choose_date'] == 'yesterday':
            sql += " and s.ATDAY BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "'"

        elif search_data['choose_date'] == 'this_week':
            sql += " and s.ATDAY BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "'"

        elif search_data['choose_date'] == 'last_week':
            sql += " and s.ATDAY BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "'"

        elif search_data['choose_date'] == 'this_month':
            sql += " and s.ATDAY BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "'"

        elif search_data['choose_date'] == 'last_month':
            sql += " and s.ATDAY BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "'"

        sql += " GROUP BY s.IMEI) b;"
        return sql

    def search_sum_sport_overview_sql(self, account_dev, search_data):
        sql = "SELECT s.MILEAGE,s.OVERSPEEDTIMES,s.STOPTIMES FROM day_run_summary AS s WHERE s.IMEI IN %s" % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " and s.ATDAY BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "'"

        elif search_data['choose_date'] == 'yesterday':
            sql += " and s.ATDAY BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "'"

        elif search_data['choose_date'] == 'this_week':
            sql += " and s.ATDAY BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "'"

        elif search_data['choose_date'] == 'last_week':
            sql += " and s.ATDAY BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "'"

        elif search_data['choose_date'] == 'this_month':
            sql += " and s.ATDAY BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "'"

        elif search_data['choose_date'] == 'last_month':
            sql += " and s.ATDAY BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "'"

        sql += ";"
        return sql

    def search_sport_mile_sql(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"

        elif search_data['type'] == 'day':
            sql += "SELECT m.DISTANCE FROM day_mileage_summary AS m WHERE m.IMEI IN %s" % str(account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_mile_sql_01(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_01 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_02(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_02 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_03(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_03 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_04(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_04 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_05(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_05 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_06(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_06 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_07(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_07 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_08(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_08 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_09(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_09 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_10(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_10 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_11(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_11 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_mile_sql_12(self, account_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE,m.RUNTIMESECOND FROM report_track_segment_12 AS m WHERE m.IMEI IN %s" % str(
                account_dev)
            if search_data['choose_date'] == '':
                sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                           'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                       search_data['end_time'] + "'))"

            elif search_data['choose_date'] == 'today':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                       self.get_today_end_time() + "'))"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_yesterday_end_time() + "'))"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_week_end_time() + "'))"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_week_end_time() + "'))"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_this_month_end_time() + "'))"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                       self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                       self.get_last_month_end_time() + "'))"
        sql += ";"
        return sql

    def search_sport_over_speed_sql(self, account_dev, search_data):
        sql = "SELECT t.IMEI FROM report_track_segment AS t INNER JOIN day_run_summary AS r ON t.IMEI = r.IMEI WHERE r.OVERSPEEDTIMES IS NOT NULL and t.IMEI in %s" % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND t.CREATETIME BETWEEN '" + search_data['begin_time'] + "' AND '" + search_data['end_time'] + "'"

        elif search_data['choose_date'] == 'today':
            sql += " AND t.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' AND '" + self.get_today_end_time() + "'"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND t.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' AND '" + self.get_yesterday_end_time() + "'"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND t.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' AND '" + self.get_this_week_end_time() + "'"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND t.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' AND '" + self.get_last_week_end_time() + "'"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND t.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' AND '" + self.get_this_month_end_time() + "'"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND t.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' AND '" + self.get_last_month_end_time() + "'"

        if search_data['speed'] != '':
            sql += " AND t.AVGSPEED >= '%s'" % search_data['speed']

        sql += ";"
        return sql

    def search_sport_stay_sql(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment AS m WHERE m.IMEI in %s" % str(account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[   'end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_01(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_01 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_02(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_02 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data'end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_03(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_03 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_04(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_04 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_05(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_05 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_06(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_06 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_07(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_07 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_08(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_08 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_09(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_09 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_10(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_10 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_11(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_11 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_sql_12(self, account_dev, search_data):
        sql = "SELECT m.STARTTIME,m.DURSECOND FROM report_stop_segment_12 AS m WHERE m.IMEI in %s" % str(account_dev)
        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data['end_time'] + "' "
        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' "

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' "

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' "

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' "

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' "

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"
            # sql += " and m.CREATETIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' "

        sql += " AND m.ACC = '0';"
        return sql

    def search_sport_stay_not_shut_down_sql(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_01(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_01 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_02(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_02 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_03(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_03 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_04(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_04 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_05(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_05 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_06(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_06 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_07(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_07 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_08(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_08 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_09(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_09 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_10(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_10 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_11(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_11 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_sport_stay_not_shut_down_sql_12(self, account_dev, search_data):
        sql = "SELECT m.IMEI,m.DURSECOND FROM report_stop_segment_12 AS m WHERE m.IMEI in %s and m.acc = '1' " % str(
            account_dev)

        if search_data['choose_date'] == '':
            sql += " AND (m.STARTTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or m.ENDTIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (m.STARTTIME <= '" + search_data['begin_time'] + "' and m.ENDTIME >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (m.STARTTIME <= '" + self.get_today_begin_date() + "' and m.ENDTIME >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (m.STARTTIME <= '" + self.get_yesterday_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (m.STARTTIME <= '" + self.get_this_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (m.STARTTIME <= '" + self.get_last_week_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (m.STARTTIME <= '" + self.get_this_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (m.STARTTIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or m.ENDTIME BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (m.STARTTIME <= '" + self.get_last_month_begin_time() + "' and m.ENDTIME >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_01(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_01 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_02(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_02 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_03(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_03 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_04(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_04 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_05(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_05 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_06(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_06 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_07(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_07 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_08(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_08 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_09(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_09 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_10(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_10 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_11(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_11 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_acc_sql_12(self, account_dev, search_data):
        sql = "SELECT a.IMEI,a.ACC,a.DURATION FROM report_acc_segment_12 AS a WHERE a.IMEI in %s" % str(account_dev)

        if search_data['status'] != '':
            sql += " and a.acc = '%s'" % search_data['status']

        if search_data['choose_date'] == '':
            sql += " AND (a.START BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                'end_time'] + "' or a.END BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                       'end_time'] + "' or (a.START <= '" + search_data['begin_time'] + "' and a.END >= '" + \
                   search_data['end_time'] + "'))"

        elif search_data['choose_date'] == 'today':
            sql += " AND (a.START BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or a.END BETWEEN '" + \
                   self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "' or (a.START <= '" + self.get_today_begin_date() + "' and a.END >= '" + \
                   self.get_today_end_time() + "'))"

        elif search_data['choose_date'] == 'yesterday':
            sql += " AND (a.START BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or a.END BETWEEN '" + \
                   self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "' or (a.START <= '" + self.get_yesterday_begin_time() + "' and a.END >= '" + \
                   self.get_yesterday_end_time() + "'))"

        elif search_data['choose_date'] == 'this_week':
            sql += " AND (a.START BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "' or (a.START <= '" + self.get_this_week_begin_time() + "' and a.END >= '" + \
                   self.get_this_week_end_time() + "'))"

        elif search_data['choose_date'] == 'last_week':
            sql += " AND (a.START BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "' or (a.START <= '" + self.get_last_week_begin_time() + "' and a.END >= '" + \
                   self.get_last_week_end_time() + "'))"

        elif search_data['choose_date'] == 'this_month':
            sql += " AND (a.START BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "' or (a.START <= '" + self.get_this_month_begin_time() + "' and a.END >= '" + \
                   self.get_this_month_end_time() + "'))"

        elif search_data['choose_date'] == 'last_month':
            sql += " AND (a.START BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or a.END BETWEEN '" + \
                   self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "' or (a.START <= '" + self.get_last_month_begin_time() + "' and a.END >= '" + \
                   self.get_last_month_end_time() + "'))"

        sql += ";"
        return sql

    def search_alarm_details_sql(self, user_id, account_dev, data):
        sql = "SELECT a.imei FROM alarm_info AS a WHERE a.imei in " + str(
            account_dev)
        if data['next_user'] == '':
            sql += " and a.USER_ID = '%s'" % user_id
            if data['alarm_begin_time'] != '':
                sql += " and a.CREATETIME >= '%s'" % data['alarm_begin_time']

            if data['alarm_end_time'] != '':
                sql += " and a.CREATETIME <= '%s'" % data['alarm_end_time']

            if data['push_begin_time'] != '':
                sql += " and a.PUSHTIME >= '%s'" % data['push_begin_time']

            if data['push_end_time'] != '':
                sql += " and a.PUSHTIME <= '%s'" % data['push_end_time']

            if data['status'] != '':
                sql += " and a.READ_STATUS = '%s'" % data['status']
        elif data['next_user'] == '1':
            if data['alarm_begin_time'] != '':
                sql += " and a.CREATETIME >= '%s'" % data['alarm_begin_time']

            if data['alarm_end_time'] != '':
                sql += " and a.CREATETIME <= '%s'" % data['alarm_end_time']

            if data['push_begin_time'] != '':
                sql += " and a.PUSHTIME >= '%s'" % data['push_begin_time']

            if data['push_end_time'] != '':
                sql += " and a.PUSHTIME <= '%s'" % data['push_end_time']

            if data['status'] != '':
                sql += " and a.READ_STATUS = '%s'" % data['status']
        sql += ";"
        return sql

    def search_sport_mile_report_sql_01(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_01 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_02(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_02 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_03(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_03 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_04(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_04 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_05(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_05 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_06(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_06 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_07(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_07 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_08(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_08 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_09(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_09 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_10(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_10 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_11(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_11 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_12(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum_12 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_01(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_01 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_02(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_02 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_03(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_03 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_04(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_04 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_05(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_05 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_06(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_06 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_07(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_07 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_08(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_08 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_09(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_09 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_10(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_10 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_11(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_11 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total_12(self, all_dev, search_data):
        begin_time = self.get_begin_time_in_mile_report_page()
        end_time = self.get_end_time_in_mile_report_page()
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum_12 AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.START_TIME > '" + begin_time + "' and m.END_TIME < '" + end_time + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def get_total_electric_report_sql(self, all_user_dev, all_dev, search_data):
        sql = "SELECT e.imei FROM equipment_electricity e INNER JOIN equipment_detail d on e.imei = d.imei"
        if search_data['next'] == '':
            sql += " where e.imei in %s" % str(all_dev)
            if search_data['electric'] != '':
                sql += " and e.electricity <= '%s'" % search_data['electric']
        elif search_data['next'] == '1':
            sql += " where e.imei in %s" % str(all_user_dev)
            if search_data['electric'] != '':
                sql += " and e.electricity <= '%s'" % search_data['electric']
        sql += ";"
        return sql

    def search_current_account_equipment_and_next(self, param):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()

        get_user_id_sql = "select u.userId,u.fullParentId from user_info u where u.account = '%s';" % param
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        user_id = user_id_list[0][0]
        user_full_id = user_id_list[0][1]

        get_lower_account_sql = "select userId from user_info where fullParentId like '" + user_full_id + user_id + ",%'" + ";"
        cursor.execute(get_lower_account_sql)
        # 读取数据
        lower_account = cursor.fetchall()
        lower_account_list = [user_id]
        for range1 in lower_account:
            for range2 in range1:
                lower_account_list.append(range2)
        lower_account_tuple = tuple(lower_account_list)

        get_account_dev_sql = "select a.imei from equipment_mostly a LEFT JOIN equipment_expiration e on a.imei = e.imei where a.userId in %s and a.status = 'NORMAL' and DATEDIFF(a.expiration,CURDATE())>=0 and (e.expiration is NULL OR (e.expiration is not null and DATEDIFF(e.expiration,CURDATE())>=0)) and (e.userId is null or (e.userId is not null and e.userId in %s));" % (
            str(lower_account_tuple), str(lower_account_tuple))
        # get_account_dev_sql = "select a.imei from equipment_mostly a where a.userId in %s and a.status = 'NORMAL' and DATEDIFF(a.expiration,CURDATE())>=0;" % str(
        #    lower_account_tuple)
        cursor.execute(get_account_dev_sql)
        get_all_dev = cursor.fetchall()
        dev_list = []
        for range1 in get_all_dev:
            for range2 in range1:
                dev_list.append(range2)
        all_dev = tuple(dev_list)
        cursor.close()
        connect.close()
        return all_dev

    def search_current_account(self, user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()

        get_user_id_sql = "select u.userId from user_info u where u.account = '%s';" % user_account
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        user_id = user_id_list[0][0]
        cursor.close()
        connect.close()
        return user_id

    def get_total_electric_report_sqls(self, all_user_dev, all_dev, search_data):
        sql = "SELECT d.deviceName,e.electricity,d.imei,d.account FROM equipment_electricity e INNER JOIN equipment_mostly d on e.imei = d.imei"
        if search_data['next'] == '':
            sql += " where e.imei in %s" % str(all_dev)
            if search_data['electric'] != '':
                sql += " and e.electricity < '%s'" % search_data['electric']
        elif search_data['next'] == '1':
            sql += " where e.imei in %s" % str(all_user_dev)
            if search_data['electric'] != '':
                sql += " and e.electricity < '%s'" % search_data['electric']
        sql += ";"
        return sql

    def get_total_and_times_sql(self, all_dev, all_user_dev, search_data):
        begin_time = self.get_begin_time_in_guide_machine_report_page()
        end_time = self.get_end_time_in_guide_machine_report_page()
        sql = "select m.DEVICE_IMEI,min(r.USABLE_NUMS),sum(r.DAY_USED_NUMS) from guide_machine m inner join guide_machine_report r on m.DEVICE_IMEI= r.DEVICE_IMEI"
        if search_data['status'] == '0':
            sql += " where m.DEVICE_IMEI in %s" % str(all_dev)
        elif search_data['status'] == '1':
            sql += " where m.DEVICE_IMEI in %s" % str(all_user_dev)

        sql += " and r.UP_TIME between '" + begin_time + "' and '" + end_time + "' group by m.DEVICE_IMEI;"
        return sql

    def get_oil_report_total_sql(self, all_dev):
        begin_time = self.get_begin_time_in_oil_report()
        end_time = self.get_end_time_in_oil_report()

        sql = "select o.id from oil_his_201705 o where o.DEVICE_IMEI in " + str(
            all_dev) + " and o.RECORD_TIME between '" + begin_time + "' and '" + end_time + "';"

        return sql

    def get_today_end_times(self):
        return (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H") + ':00'

    def search_current_account_user_id(self, param):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_user_id_sql = "select u.userId from user_info u where u.account = '%s';" % param
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        user_id = user_id_list[0][0]
        cursor.close()
        connect.close()
        return user_id

    def search_current_account_user_full_id(self, param):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_user_id_sql = "select u.userId,u.fullParentId from user_info u where u.account = '%s';" % param
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        full_id = user_id_list[0][1] + user_id_list[0][0]
        cursor.close()
        connect.close()
        return full_id

    def get_imei_account_is_band(self, imei):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()
        get_user_id_sql = "SELECT m.bindUserId FROM equipment_mostly m WHERE m.imei = '%s';" % imei
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        cursor.close()
        connect.close()
        if user_id_list[0][0] == None:
            return 1
        else:
            return 2
