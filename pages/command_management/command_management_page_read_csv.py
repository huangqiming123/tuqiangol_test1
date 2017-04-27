class CommandManagementPageReadCsv(object):
    def read_csv(self, csv_file_name):
        csv_file = open('E:\git\\tuqiangol_test\data\command_management\\%s' % csv_file_name, 'r', encoding='utf8')
        return csv_file
