class SearchSql(object):
    def search_work_task_manager_sql(self, user_id, search_data):
        sql = "select c.id from command_issued_template c where c.createdBy = '%s'" % user_id
        if search_data['number'] != '':
            sql += " and c.id like '%" + search_data['number'] + "%'"
        if search_data['name'] != '':
            sql += " and c.name like '%" + search_data['name'] + "%'"
        sql += ";"
        return sql
