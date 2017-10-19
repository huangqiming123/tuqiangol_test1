class SafeAreaSearchSql(object):
    def search_sql_in_test_case_129(self, name):
        sql = "SELECT description FROM `geozone_info` WHERE userid = 40409 AND flag = 0 AND geoname = '%s';" % name
        return sql

    def search_sql_in_test_case_131(self, name):
        sql = "SELECT description FROM `geozone_info` WHERE userid = 40409 AND flag = 1 AND geoname = '%s';" % name
        return sql

    def search_sql_in_test_case_138_01(self, geo_name):
        sql = "SELECT o.id FROM `geozone_info` o WHERE o.geoname = '" + geo_name + "';"
        return sql

    def search_sql_in_test_case_138_02(self, geo_id, account, data):
        sql = "SELECT t.imei AS imei FROM `alarm_configure` t " \
              "LEFT JOIN `equipment_mostly` tt ON tt.imei = t.imei " \
              "WHERE 1 = 1 AND t.geoId = '%s' AND tt.account = '%s'" % (geo_id, account)

        if data["search_type"] == 'imei':
            sql += " AND t.imei = '%s'" % data["search_content"]

        if data["search_type"] == '设备名':
            sql += "AND tt.deviceName = '%s'" % data["search_content"]

        sql += ';'
        return sql
