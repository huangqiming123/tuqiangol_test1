class SearchSql(object):
    def search_dev_sql(self, user_id, lower_account_tuple, search_data):
        # 查询设备的sql
        sql = "select d.id from assets_device d where"
        if search_data['next'] == '':
            sql += " d.userId = '%s'" % user_id

            if search_data['dev_name'] != '':
                sql += " and d.deviceName like '%" + search_data['dev_name'] + "%'"

            if search_data['dev_type'] != '':
                sql += " and d.mcType like '%" + search_data['dev_type'] + "%'"

            if search_data['past_due'] == '即将过期':
                sql += " and DATEDIFF(d.expiration,CURDATE())<= 30 and DATEDIFF(d.expiration,CURDATE())>= 0"
            elif search_data['past_due'] == '已过期':
                sql += " and DATEDIFF(d.expiration,CURDATE())<= 0"

            if search_data['plate_numbers'] != '':
                sql += " and d.vehicleNumber like '%" + search_data['plate_numbers'] + "%'"

            if search_data['frame_number'] != '':
                sql += " and d.carFrame like '%" + search_data['frame_number'] + "%'"

            if search_data['sim'] != '':
                sql += " and d.sim like '%" + search_data['sim'] + "%'"

            if search_data['active'] == '已激活':
                sql += " and d.activationTime is not null"
            elif search_data['active'] == '未激活':
                sql += " and d.activationTime is null"

            if search_data['choose_time'] == '激活时间':
                if search_data['begin_time'] != '':
                    sql += " and d.activationTime >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and d.activationTime <= '%s'" % search_data['end_time']
            elif search_data['choose_time'] == '平台到期时间':
                if search_data['begin_time'] != '':
                    sql += " and d.expiration >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and d.expiration <= '%s'" % search_data['end_time']

        elif search_data['next'] == '1':
            sql += " d.userId in %s" % str(lower_account_tuple)

            if search_data['dev_name'] != '':
                sql += " and d.deviceName like '%" + search_data['dev_name'] + "%'"

            if search_data['dev_type'] != '':
                sql += " and d.mcType like '%" + search_data['dev_type'] + "%'"

            if search_data['past_due'] == '即将过期':
                sql += " and DATEDIFF(d.expiration,CURDATE())<= 30 and DATEDIFF(d.expiration,CURDATE())>= 0"
            elif search_data['past_due'] == '已过期':
                sql += " and DATEDIFF(d.expiration,CURDATE())<= 0"

            if search_data['plate_numbers'] != '':
                sql += " and d.vehicleNumber like '%" + search_data['plate_numbers'] + "%'"

            if search_data['frame_number'] != '':
                sql += " and d.carFrame like '%" + search_data['frame_number'] + "%'"

            if search_data['sim'] != '':
                sql += " and d.sim like '%" + search_data['sim'] + "%'"

            if search_data['active'] == '已激活':
                sql += " and d.activationTime is not null"
            elif search_data['active'] == '未激活':
                sql += " and d.activationTime is null"

            if search_data['choose_time'] == '激活时间':
                if search_data['begin_time'] != '':
                    sql += " and d.activationTime >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and d.activationTime <= '%s'" % search_data['end_time']
            elif search_data['choose_time'] == '平台到期时间':
                if search_data['begin_time'] != '':
                    sql += " and d.expiration >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and d.expiration <= '%s'" % search_data['end_time']

        sql += ";"
        return sql
