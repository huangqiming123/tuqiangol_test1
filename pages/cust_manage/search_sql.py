from model.connect_sql import ConnectSql


class SearchSql(object):
    def search_current_account_data(self, user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_tuqiang_sql()
        cursor = connect.cursor()

        get_user_id_sql = "select u.userId,u.account,u.type from user_info u where u.account = '%s';" % user_account
        cursor.execute(get_user_id_sql)
        user_data_list = cursor.fetchall()

        list_data = []
        for range1 in user_data_list:
            for range2 in range1:
                list_data.append(range2)
        all_data = tuple(list_data)
        cursor.close()
        connect.close()
        return all_data


    def search_dev_sql(self, user_id, search_data):
        # 搜索设备的sql
        sql = "select o.id from assets_organize o inner join assets_device d on o.id = d.orgId where d.userId = '%s'" % user_id

        if search_data['group'] != '':
            sql += " and o.organizeName = '%s'" % search_data['group']

        if search_data['active'] == '未激活':
            sql += " and d.activationTime is null"

        elif search_data['active'] == '已激活':
            sql += " and d.activationTime is not null"

        if search_data['bound'] == '未绑定':
            sql += " and d.bindUserId is null"

        elif search_data['bound'] == '已绑定':
            sql += " and d.bindUserId is not null"

        if search_data['sim_or_imei'] == 'sim':
            sql += " and d.sim like '%" + search_data['info'] + "%'"

        elif search_data['sim_or_imei'] == 'imei':
            sql += " and d.imei like '%" + search_data['info'] + "%'"

        sql += ";"
        return sql

    def search_account_sql(self, lower_account_tuple, search_data):
        sql = ""
        if len(lower_account_tuple) == 0:
            sql = "select u.id from user_info u where u.userId in ('')"
        elif len(lower_account_tuple) == 1:
            sql = "select u.id from user_info u where u.userId in (" + str(lower_account_tuple[0]) + ")"

        elif len(lower_account_tuple) > 1:
            sql = "select u.id from user_info u where u.userId in %s" % str(lower_account_tuple)

        if search_data['account_type'] == '代理商':
            sql += " and u.type = '8'"

        elif search_data['account_type'] == '用户':
            sql += " and u.type = '9'"

        elif search_data['account_type'] == '销售':
            sql += " and u.type = '11'"

        if search_data['info'] != '':
            sql += " and (u.account like '%" + search_data['info'] + "%' or u.nickName like '%" + search_data[
                'info'] + "%')"

        sql += ";"
        return sql
