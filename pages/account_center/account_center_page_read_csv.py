class AccountCenterPageReadCsv(object):
    def read_csv(self, csv_file_name):
        csv_file = open('E:\git\\tuqiangol_test\data\\account_center\\%s' % csv_file_name, 'r', encoding='utf8')
        return csv_file
