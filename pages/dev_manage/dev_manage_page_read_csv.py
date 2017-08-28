class DevManagePageReadCsv(object):
    def read_csv(self, file_name):
        csv_file = open('E:\git\\tianyanzaixian_tuqiang\data\dev_manage\\%s' % file_name, 'r', encoding='utf8')
        return csv_file
