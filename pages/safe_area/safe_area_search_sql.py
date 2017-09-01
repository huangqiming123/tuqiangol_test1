class SafeAreaSearchSql(object):
    def search_sql_in_test_case_129(self, name):
        sql = "SELECT description FROM `geozone_info` WHERE userid = 40409 AND flag = 0 AND geoname = '%s';" % name
        return sql

    def search_sql_in_test_case_131(self, name):
        sql = "SELECT description FROM `geozone_info` WHERE userid = 40409 AND flag = 1 AND geoname = '%s';" % name
        return sql