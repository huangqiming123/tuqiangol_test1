from model.connect_sql import ConnectSql


class SearchSql(object):
    # 获取当前登录账号数据（id、账号、类型）
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


    # 搜索设备管理的sql语句
    def search_equipment_manager_sql(self, lower_account_tuple, search_data):
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

    def search_cus_manager_sql(self, lower_account_tuple, search_data):
        # 客户管理日志
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

    def search_log_in_sql(self, lower_account_tuple, search_data):
        # 搜索登录日志的sql
        sql = "select id from user_login_log where loginUserId = '%s'" % lower_account_tuple

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
        sql = "select m.id from user_message m where m.userId in %s" % str(current_account)

        if search_data['imei'] != '':
            #sql += " and m.imeis like '%" + search_data['imei'] + "%'"
            sql += " and m.imeis=" + search_data['imei']

        if search_data['type'] != '':
            sql += " and m.type = '%s'" % search_data['type']

        if search_data['status'] != '':
            sql += " and m.readFlag = '%s'" % search_data['status']

        sql += ";"
        return sql

    # 搜索充值卡--申请记录的sql   根据状态搜索
    def search_apply_record_sql(self, id, state):
        sql = "select status from rc_recharge_card_order where userid=%s" % id
        if state != "":
            sql += " and status=%s" % state

        sql += ";"
        return sql

    # 搜索充值卡--转移记录的sql
    def search_transfer_record_sql(self, id, state):
        sql = "select creationDate from rc_recharge_card_transfer where userId=%s" % id
        if state != "":
            sql += " and `inOut` =%s" % state

        sql += ";"
        return sql

    # 搜索充值卡--充值记录的sql
    def search_refill_record_sql(self, id, data):
        sql = "select imei from rc_recharge where userId=%s" % id
        if data["refill_type"] != "":
            sql += " and cardType=%s" % data["refill_type"]

        if data['device_imei'] != '':
            #多个imei，精确搜索
            if "/" in data['device_imei']:
                imeis = data['device_imei'].split("/")
                device_imei = tuple(imeis)
                sql += " and imei in" + str(device_imei)
                print(sql)

            # 一个imei模糊搜索
            else:
                sql += " and imei like '%" + data['device_imei'] + "%'"

        sql += ";"
        return sql

    # 充值记录的sql--最新时间
    def search_refill_record_reill_time_sql(self, id, imei):
        sql = "select max(updationDate) from rc_recharge where userId='%s' and imei='%s' ORDER BY updationDate DESC;" % (
        id, imei)
        print(sql)
        return sql

    # 充值记录的sql--最后时间
    def search_refill_record_expire_time_sql(self, time):
        sql = "select max(newExpiration) from rc_recharge where updationDate='%s';" % time
        print(sql)
        return sql
