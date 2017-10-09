import os
from time import sleep

import xlrd

from model.read_excel import open_excel
from pages.base.base_page import BasePage


class Page(BasePage):
    def click_expect_button(self):
        self.driver.click_element('x,//*[@id="runForm"]/div[5]/button')
        sleep(5)

    def find_expect_file_after_click_expect_button(self):
        base_dir = "C:\\Users\\Administrator\\Downloads"
        lists = os.listdir(base_dir)
        # 重新按时间对目录下的文件进行排序
        lists.sort(key=lambda fn: os.path.getmtime(base_dir + "\\" + fn))
        # List[-1]取到的就是最新生成的文件或文件夹
        file_new = os.path.join(base_dir, lists[-1])
        return file_new

    def read_excel_file_by_index(self, file, col_name_index=0, by_index=0):
        excel_file = open_excel(file)
        # table = excel_file.sheets[by_index]
        table = excel_file.sheet_by_index(by_index)
        # 列数
        number_rows = table.nrows
        # 每一列总共有多少个值
        colnames = table.row_values(col_name_index)

        list = []
        for rownum in range(1, number_rows):

            row = table.row_values(rownum)
            if row:
                data = {}
                for i in range(len(colnames)):
                    data[colnames[i]] = row[i]
                list.append(data)
        return list

    def get_number_in_sport_overview_form(self):
        return len(list(self.driver.get_elements('x,//*[@id="run-tbody"]/tr')))

    def get_xuhao(self, n):
        a = self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[1]' % str(n + 1))
        if float(a).is_integer():
            return float('%.1f' % float(a))

    def get_dev_type(self, n):
        return self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[4]' % str(n + 1))

    def get_stay_times(self, n):
        a = self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[7]' % str(n + 1))
        if float(a).is_integer():
            return float('%.1f' % float(a))

    def get_total_mile(self, n):
        a = self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[5]' % str(n + 1))
        if float(a).is_integer():
            return float('%.1f' % float(a))
        else:
            return float(a)

    def get_over_speed_times(self, n):
        a = self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[6]' % str(n + 1))
        if float(a).is_integer():
            return float('%.1f' % float(a))

    def get_imei(self, n):
        return self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[3]' % str(n + 1))

    def get_dev_name(self, n):
        return self.driver.get_text('x,//*[@id="run-tbody"]/tr[%s]/td[2]' % str(n + 1))
