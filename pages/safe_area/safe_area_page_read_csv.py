class SafeAreaPageReadCsv(object):
    def read_csv(self, name):
        csv_file = open('E:\git\\tianyanzaixian_tuqiang\data\safe_area\\%s' % name, 'r', encoding='utf8')
        return csv_file
