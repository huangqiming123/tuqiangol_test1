class SearchSql(object):
    def search_dev_sql(self, lower_account_tuple, search_data):
        sql = "select d.imei from assets_device d where d.userId in " + str(lower_account_tuple)

        if search_data['dev_info'] != '':
            sql += " and ( d.imei like '%" + search_data['dev_info'] + "%' or d.driverName like '%" + search_data[
                'dev_info'] + "%' or d.vehicleNumber like '%" + search_data['dev_info'] + "%' or d.deviceName like '%" + \
                   search_data['dev_info'] + "%')"

        sql += ";"
        return sql

    def search_account_sql(self, lower_account_tuple, search_data):
        # 全局搜索，搜索用户的sql
        sql = "select o.id from user_organize o where o.userId in " + str(lower_account_tuple)

        if search_data['account_info'] != '':
            sql += " and ( o.nickName like '%" + search_data['account_info'] + "%' or o.account like '%" + search_data[
                'account_info'] + "%')"

        sql += ";"
        return sql

    def search_complex_sql(self, user_id, search_data):
        # 全局搜索 高级搜索
        sql = "select d.id from assets_device d where d.userId = '%s'" % user_id
        if search_data['base_info'] == 'imei':
            sql += " and d.imei like '%" + search_data['info'] + "%'"

        elif search_data['base_info'] == '车牌号':
            sql += " and d.vehicleNumber like '%" + search_data['info'] + "%'"

        elif search_data['base_info'] == '设备类型':
            sql += " and d.mcType like '%" + search_data['info'] + "%'"

        elif search_data['base_info'] == 'SN':
            sql += " and d.sn like '%" + search_data['info'] + "%'"

        elif search_data['base_info'] == '车架号':
            sql += " and d.carFrame like '%" + search_data['info'] + "%'"

        elif search_data['base_info'] == '设备SIM卡号':
            sql += " and d.sim like '%" + search_data['info'] + "%'"

        elif search_data['base_info'] == '设备名称':
            sql += " and d.deviceName like '%" + search_data['info'] + "%'"

        begin_time = search_data['date'].split('/')[0]
        end_time = search_data['date'].split('/')[1]
        if search_data['is_date'] == '':
            if search_data['date_type'] == '激活时间':
                if begin_time != '':
                    sql += " and DATEDIFF(d.activationTime,'" + begin_time + "') = 0"

            elif search_data['date_type'] == '平台到期时间':
                if begin_time != '':
                    sql += " and DATEDIFF(d.expiration,'" + begin_time + "') = 0"

        elif search_data['is_date'] == '1':
            if search_data['date_type'] == '激活时间':
                if begin_time != '':
                    sql += " and d.activationTime >= '%s'" % begin_time
                if end_time != '':
                    sql += " and d.activationTime <= '%s'" % end_time

            elif search_data['date_type'] == '平台到期时间':
                if begin_time != '':
                    sql += " and d.expiration >= '%s'" % begin_time
                if end_time != '':
                    sql += " and d.expiration <= '%s'" % end_time

        if search_data['arrearage'] != '':
            sql += " and d.expiration <= CURDATE()"

        if search_data['no_active'] != '':
            sql += " and d.activationTime is NULL"

        sql += ";"
        return sql
