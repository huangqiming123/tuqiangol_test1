class HelpPageSql(object):
    # 搜索设备管理的sql
    def equipment_manager_search_sql(self, lower_account_tuple, search_data):
        sql = "select l.id from operation_log l INNER JOIN user_info o ON l.created_by = o.userId where l.created_by in %s and l.serviceType = '1'" % str(
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

    # 搜索客户管理日志的sql
    def search_cus_manager_sql(self, lower_account_tuple, search_data):

        sql = "select l.id from operation_log l INNER JOIN user_info o ON l.created_by = o.userId where l.created_by in " + str(
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

    # 搜索登录日志的sql
    def search_log_in_sql(self, lower_account_tuple, search_data):
        # 搜索登录日志的sql
        sql = "select id from user_login_log where loginUserId in %s" % str(lower_account_tuple)

        if search_data['account'] != '':
            sql += " and loginAccount like '%" + search_data['account'] + "%'"

        if search_data['begin_time'] != '':
            sql += " and loginTime >= '%s'" % search_data['begin_time']

        if search_data['end_time'] != '':
            sql += " and loginTime <= '%s'" % search_data['end_time']

        sql += ";"
        print(sql)
        return sql

    # 业务日志sql
    def business_log_sql(self, lower_account_tuple, search_data):
        sql = "select l.id from operation_aop_log l INNER JOIN user_info o " \
              "ON l.created_by = o.userId " \
              "where l.created_by in %s and l.enabled_flag = 1" % str(lower_account_tuple)

        if search_data["search_type"] == '设备管理-设备修改':
            sql += " and l.serviceType = 1 and l.operType = 1"

        if search_data["search_type"] == '设备管理-取消指令':
            sql += " and l.serviceType = 1 and l.operType = 3"

        if search_data["search_type"] == '设备管理-设备分配':
            sql += " and l.serviceType = 1 and l.operType = 5"

        if search_data["search_type"] == '客户管理-新增客户':
            sql += " and l.serviceType = 2 and l.operType = 0"

        if search_data["search_type"] == '客户管理-修改用户信息':
            sql += " and l.serviceType = 2 and l.operType = 1"

        if search_data["search_type"] == '客户管理-删除用户信息':
            sql += " and l.serviceType = 2 and l.operType = 2"

        if search_data["search_type"] == '客户管理-修改密码':
            sql += " and l.serviceType = 2 and l.operType = 3"

        if search_data["search_type"] == '客户管理-重置密码':
            sql += " and l.serviceType = 2 and l.operType = 4"

        if search_data["search_type"] == '客户管理-转移客户':
            sql += " and l.serviceType = 2 and l.operType = 5"

        if search_data["search_type"] == '安全区域-新增、编辑区域':
            sql += " and l.serviceType = 3 and l.operType = 1"

        if search_data["search_type"] == '安全区域-删除区域':
            sql += " and l.serviceType = 3 and l.operType = 2"

        if search_data["search_type"] == '安全区域-关联设备':
            sql += " and l.serviceType = 3 and l.operType = 3"

        if search_data["search_type"] == '告警设置-推送设置':
            sql += " and l.serviceType = 4 and l.operType = 1"

        if search_data['begin_time'] != '':
            sql += " and l.creation_date >= '%s'" % search_data['begin_time']

        if search_data['end_time'] != '':
            sql += " and l.creation_date <= '%s'" % search_data['end_time']

        if search_data['account'] != '':
            sql += " and o.account = '" + search_data['account'] + "'"

        if search_data['operation_account'] != "":
            sql += " and l.account = '" + search_data['operation_account'] + "'"

        if search_data['imei'] != "":
            sql += " and l.imei = '" + search_data['imei'] + "'"

        sql += ';'
        return sql
