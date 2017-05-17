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
