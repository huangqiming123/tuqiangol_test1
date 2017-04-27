class SearchSql(object):
    def search_equipment_manager_sql(self, lower_account_tuple, search_data):
        # 搜索设备管理的sql语句
        sql = "select l.id from operation_log l INNER JOIN user_organize o ON l.created_by = o.userId where l.created_by in %s and l.serviceType = '1'" % str(
            lower_account_tuple)
        if search_data['type'] == '5':
            sql += " and l.operType = '5'"
            if search_data['begin_time'] != '':
                sql += " and l.creation_date >= '%s'" % search_data['begin_time']

            if search_data['end_time'] != '':
                sql += " and l.creation_date <= '%s'" % search_data['end_time']

            if search_data['more'] != '':
                sql += " and (o.account like '%" + search_data['more'] + "%' or l.imei like '%" + search_data[
                    'more'] + "%' or l.account like '%" + search_data['more'] + "%')"

        elif search_data['type'] == '1':
            sql += " and l.operType = '1'"
            if search_data['begin_time'] != '':
                sql += " and l.creation_date >= '%s'" % search_data['begin_time']

            if search_data['end_time'] != '':
                sql += " and l.creation_date <= '%s'" % search_data['end_time']

            if search_data['more'] != '':
                sql += " and (o.account like '%" + search_data['more'] + "%' or l.imei like '%" + search_data[
                    'more'] + "%' or l.account like '%" + search_data['more'] + "%')"
        sql += ";"
        return sql

    def search_cus_manager_sql(self, lower_account_tuple, search_data):
        # 客户管理日志
        sql = "select l.id from operation_log l INNER JOIN user_organize o ON l.created_by = o.userId where l.created_by in " + str(
            lower_account_tuple) + " and l.serviceType = '2' and l.operType = '" + search_data['type'] + "'"

        if search_data['begin_time'] != '':
            sql += " and l.creation_date >= '%s'" % search_data['begin_time']

        if search_data['end_time'] != '':
            sql += " and l.creation_date <= '%s'" % search_data['end_time']

        if search_data['more'] != '':
            sql += " and (l.account like '%" + search_data['more'] + "%' or o.account like '%" + search_data[
                'more'] + "%')"

        sql += ";"
        return sql

    def search_log_in_sql(self, lower_account_tuple, search_data):
        # 搜索登录日志的sql
        sql = "select id from user_login_log where loginUserId in " + str(lower_account_tuple)

        if search_data['account'] != '':
            sql += " and loginAccount like '%" + search_data['account'] + "%'"

        if search_data['begin_time'] != '':
            sql += " and loginTime >= '%s'" % search_data['begin_time']

        if search_data['end_time'] != '':
            sql += " and loginTime <= '%s'" % search_data['end_time']

        sql += ";"
        return sql

    def search_massage_sql(self, current_account, search_data):
        # 搜索消息的sql
        sql = "select m.id from user_message m inner join user_organize o on o.userId = m.userId where o.account = '%s'" % current_account

        if search_data['imei'] != '':
            sql += " and m.imeis like '%" + search_data['imei'] + "%'"

        if search_data['type'] != '':
            sql += " and m.type = '%s'" % search_data['type']

        if search_data['status'] != '':
            sql += " and m.readFlag = '%s'" % search_data['status']

        sql += ";"
        return sql
