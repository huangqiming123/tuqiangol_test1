class CustManagePageReadCsv(object):
    def read_csv(self, csv_file_name):
        csv_file = open('E:\git\\tianyanzaixian_tuqiang\data\cust_manage\\%s' % csv_file_name, 'r', encoding='utf8')
        return csv_file
