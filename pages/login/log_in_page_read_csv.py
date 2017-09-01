class LogInPageReadCsv(object):
    def read_csv(self, csv_name):
        csv_file = open('E:\git\\tuqiangol_test\data\login\\%s' % csv_name, 'r', encoding='utf8')
        return csv_file
