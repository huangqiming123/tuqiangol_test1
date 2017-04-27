class StatisticalFormPageReadCsv(object):
    def read_csv(self, name):
        csv_file = open('E:\git\\tuqiangol_test\data\statistical_form\\%s' % name, 'r', encoding='utf8')
        return csv_file
