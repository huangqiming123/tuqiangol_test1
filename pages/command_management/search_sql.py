class SearchSql(object):
    def search_work_task_manager_sql(self, user_id, search_data):
        sql = "select c.id from command_issued_template c where c.createdBy = '%s'" % user_id
        if search_data['number'] != '':
            sql += " and c.id like '%" + search_data['number'] + "%'"
        if search_data['name'] != '':
            sql += " and c.name like '%" + search_data['name'] + "%'"
        sql += ";"
        return sql

    def search_issued_work_template_sql(self, param, search_data):
        sql = "select c.id from command_issued_stage c where c.createdBy = '%s'" % param

        if search_data['batch'] != "":
            sql += " and c.issuedTemplateId like '%" + search_data['batch'] + "%'"

        if search_data['execute_state'] != '':
            sql += " and c.exectueState = '%s'" % search_data['execute_state']

        if search_data['state'] == '1':
            sql += " and DATEDIFF(c.endTime,CURDATE())<0"

        if search_data['imei'] != '':
            sql += " and c.imei = '%s'" % search_data['imei']

        sql += ";"
        return sql

    def search_issued_command_task_management_sql(self, current_user_next, search_data):
        sql = "SELECT t.id FROM command_task AS t WHERE t.createdBy IN " + str(current_user_next)

        if search_data['batch'] != "":
            sql += " and t.id like '%" + search_data['batch'] + "%'"

        if search_data['name'] != "":
            sql += " and t.insName like '%" + search_data['name'] + "%'"

        sql += ";"
        return sql

    def search_sql_for_issued_command_management_search(self, user_id, search_data):
        sql_01 = "SELECT l.id FROM user_info u LEFT JOIN business_command_logs l " \
                 "ON l.createdBy = u.userId WHERE l.id IS NOT NULL " \
                 "AND (u.userId = '" + user_id + "' OR u.fullParentId LIKE CONCAT('1," + user_id + "',',','%'))"

        sql_02 = " UNION ALL SELECT l.id FROM equipment_mostly d LEFT JOIN business_command_logs l " \
                 "ON d.bindUserId = l.createdBy AND d.imei = l.receiveDevice WHERE l.id IS NOT NULL " \
                 "AND (d.userId = '" + user_id + "' OR d.fullParentId LIKE CONCAT('1," + user_id + "',',','%'))"

        if search_data['batch'] == '':
            sql_01 = sql_01
            sql_02 = sql_02

            if search_data['imei'] != '':
                sql_01 += " and c.receiveDevice = '%s'" % search_data['imei']
                sql_02 += " and c.receiveDevice = '%s'" % search_data['imei']

            if search_data['statue'] == '5':
                sql_01 += " and c.isOffLine = '0'"
                sql_02 += " and c.isOffLine = '0'"

            if search_data['statue'] == '6':
                sql_01 += " and c.isOffLine = '1'"
                sql_02 += " and c.isOffLine = '1'"

            if search_data['statue'] != '5' and search_data['statue'] != '6' and search_data['statue'] != '':
                sql_02 += " and c.IsExecute = '%s'" % search_data['statue']
                sql_02 += " and c.IsExecute = '%s'" % search_data['statue']

        elif search_data['batch'] != '':
            sql_01 += " and c.taskId like '%" + search_data['batch'] + "%'"
            sql_02 += " and c.taskId like '%" + search_data['batch'] + "%'"

            if search_data['imei'] != '':
                sql_01 += " and c.receiveDevice = '%s'" % search_data['imei']
                sql_02 += " and c.receiveDevice = '%s'" % search_data['imei']

            if search_data['statue'] == '5':
                sql_01 += " and c.isOffLine = '0'"
                sql_02 += " and c.isOffLine = '0'"

            if search_data['statue'] == '6':
                sql_01 += " and c.isOffLine = '1'"
                sql_02 += " and c.isOffLine = '1'"

            if search_data['statue'] != '5' and search_data['statue'] != '6' and search_data['statue'] != '':
                sql_01 += " and c.IsExecute = '%s'" % search_data['statue']
                sql_02 += " and c.IsExecute = '%s'" % search_data['statue']

        sql = sql_01 + sql_02 + ";"
        return sql
