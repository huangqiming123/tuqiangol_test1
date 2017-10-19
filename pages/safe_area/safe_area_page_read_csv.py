class SafeAreaPageReadCsv(object):
    def read_csv(self, name):
        csv_file = open('D:\git\\tuqiangol_test\data\safe_area\\%s' % name, 'r', encoding='utf8')
        return csv_file