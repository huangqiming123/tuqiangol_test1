class SearchSql(object):
    def search_dev_sql(self, user_id, lower_account_tuple, search_data):
        # 查询设备的sql
        sql = "select d.id from equipment_detail d, equipment_mostly m, assets_organize o where d.imei = m.imei and o.id = m.orgId"
        if search_data['next'] == '':
            sql += " and m.userId = '%s'" % user_id

            if search_data['dev_name'] != '':
                sql += " and m.deviceName like '%" + search_data['dev_name'] + "%'"

            if search_data['dev_type'] != '':
                sql += " and m.mcType like '%" + search_data['dev_type'] + "%'"

            if search_data['past_due'] == '即将过期':
                sql += " and DATEDIFF(m.expiration,CURDATE())<= 30 and DATEDIFF(m.expiration,CURDATE())>= 0"
            elif search_data['past_due'] == '已过期':
                sql += " and DATEDIFF(m.expiration,CURDATE())<= 0"

            if search_data['plate_numbers'] != '':
                sql += " and d.vehicleNumber like '%" + search_data['plate_numbers'] + "%'"

            if search_data['frame_number'] != '':
                sql += " and d.carFrame like '%" + search_data['frame_number'] + "%'"

            if search_data['sim'] != '':
                sql += " and m.sim like '%" + search_data['sim'] + "%'"

            if search_data['active'] == '已激活':
                sql += " and m.activationTime is not null"
            elif search_data['active'] == '未激活':
                sql += " and m.activationTime is null"

            if search_data['choose_time'] == '激活时间':
                if search_data['begin_time'] != '':
                    sql += " and m.activationTime >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and m.activationTime <= '%s'" % search_data['end_time']
            elif search_data['choose_time'] == '平台到期时间':
                if search_data['begin_time'] != '':
                    sql += " and m.expiration >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and m.expiration <= '%s'" % search_data['end_time']

            if search_data['band_status'] == '已绑定':
                sql += " and m.bindUserId is not null"
            elif search_data['band_status'] == '未绑定':
                sql += " and m.bindUserId is null"

            if search_data['dev_mold'] == '有线':
                pass
            elif search_data['dev_mold'] == '电池':
                pass

            if search_data['dev_group'] == '默认组':
                sql += " and o.organizeName = '" + search_data['dev_group'] + "'"

            if search_data['sn'] != "":
                sql += " and d.sn like '" + search_data['sn'] + "'"

        elif search_data['next'] == '1':
            sql += " and m.userId in %s" % str(lower_account_tuple)

            if search_data['dev_name'] != '':
                sql += " and m.deviceName like '%" + search_data['dev_name'] + "%'"

            if search_data['dev_type'] != '':
                sql += " and m.mcType like '%" + search_data['dev_type'] + "%'"

            if search_data['past_due'] == '即将过期':
                sql += " and DATEDIFF(m.expiration,CURDATE())<= 30 and DATEDIFF(m.expiration,CURDATE())>= 0"
            elif search_data['past_due'] == '已过期':
                sql += " and DATEDIFF(m.expiration,CURDATE())<= 0"

            if search_data['plate_numbers'] != '':
                sql += " and d.vehicleNumber like '%" + search_data['plate_numbers'] + "%'"

            if search_data['frame_number'] != '':
                sql += " and d.carFrame like '%" + search_data['frame_number'] + "%'"

            if search_data['sim'] != '':
                sql += " and m.sim like '%" + search_data['sim'] + "%'"

            if search_data['active'] == '已激活':
                sql += " and m.activationTime is not null"
            elif search_data['active'] == '未激活':
                sql += " and m.activationTime is null"

            if search_data['choose_time'] == '激活时间':
                if search_data['begin_time'] != '':
                    sql += " and m.activationTime >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and m.activationTime <= '%s'" % search_data['end_time']
            elif search_data['choose_time'] == '平台到期时间':
                if search_data['begin_time'] != '':
                    sql += " and m.expiration >= '%s'" % search_data['begin_time']
                if search_data['end_time'] != '':
                    sql += " and m.expiration <= '%s'" % search_data['end_time']

            if search_data['band_status'] == '已绑定':
                sql += " and m.bindUserId is not null"
            elif search_data['band_status'] == '未绑定':
                sql += " and m.bindUserId is null"

            if search_data['dev_mold'] == '有线':
                pass
            elif search_data['dev_mold'] == '电池':
                pass

            if search_data['dev_group'] == '默认组':
                sql += " and o.organizeName = '" + search_data['dev_group'] + "'"

            if search_data['sn'] != "":
                sql += " and d.sn like '" + search_data['sn'] + "'"

        sql += ";"
        return sql
