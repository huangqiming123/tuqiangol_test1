class SearchSql(object):
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
        sql = "select u.id from user_organize u where u.userId in %s" % str(lower_account_tuple)

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
