import time

import datetime

from model.connect_sql import ConnectSql


class SearchSql(object):
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
        days_count = datetime.timedelta(days=(today.isoweekday() - 1))
        week = today - days_count
        return str(week) + ' 00:00'

    def get_this_week_end_time(self):
        # 获取本周的结束时间
        today = datetime.date.today()
        return str(today) + ' 23:59'

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
        current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        return current_time + " 23:59"

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

    def search_current_account_equipment(self, user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()

        get_user_id_sql = "select u.userId from user_info u where u.account = '%s';" % user_account
        cursor.execute(get_user_id_sql)
        user_id_list = cursor.fetchall()
        user_id = user_id_list[0][0]

        get_account_dev_sql = "select a.imei from equipment_mostly a where a.userId = '%s' and a.status = 'NORMAL' and DATEDIFF(a.expiration,CURDATE())>=0;" % user_id
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

    def search_alarm_details_sql(self, user_id, account_dev, data):
        sql = "SELECT a.imei FROM alarm_info_user AS a WHERE a.imei in " + str(
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

    def search_sport_mile_report_sql(self, all_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DISTANCE FROM report_distance_sum AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.CREATE_TIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "'"
        sql += ";"
        return sql

    def search_sport_mile_report_sql_get_total(self, all_dev, search_data):
        sql = ""
        if search_data['type'] == 'mile':
            sql += "SELECT m.DEVICE_IMEI FROM report_distance_sum AS m WHERE m.DEVICE_IMEI IN %s" % str(
                all_dev)
            if search_data['choose_date'] == '':
                sql += " AND m.CREATE_TIME BETWEEN '" + search_data['begin_time'] + "' and '" + search_data[
                    'end_time'] + "'"
            elif search_data['choose_date'] == 'today':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_today_begin_date() + "' and '" + self.get_today_end_time() + "'"

            elif search_data['choose_date'] == 'yesterday':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_yesterday_begin_time() + "' and '" + self.get_yesterday_end_time() + "'"

            elif search_data['choose_date'] == 'this_week':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_this_week_begin_time() + "' and '" + self.get_this_week_end_time() + "'"

            elif search_data['choose_date'] == 'last_week':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_last_week_begin_time() + "' and '" + self.get_last_week_end_time() + "'"

            elif search_data['choose_date'] == 'this_month':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_this_month_begin_time() + "' and '" + self.get_this_month_end_time() + "'"

            elif search_data['choose_date'] == 'last_month':
                sql += " AND m.CREATE_TIME BETWEEN '" + self.get_last_month_begin_time() + "' and '" + self.get_last_month_end_time() + "'"

            sql += " group by m.DEVICE_IMEI"
        sql += ";"
        return sql

    def get_total_electric_report_sql(self, all_dev, search_data):
        sql = "SELECT e.imei FROM equipment_electricity e INNER JOIN equipment_detail d on e.imei = d.imei WHERE d.equipType = 'WIRELESS'"
        sql += " and e.imei in %s" % str(all_dev)
        if search_data['electric'] != '':
            sql += " and e.electricity < '%s'" % search_data['electric']
        sql += ";"
        return sql
