import os
from time import sleep

from model.read_excel import open_excel
from pages.base.base_page import BasePage


class FormExportPage(BasePage):
    def find_expect_file(self):
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

    def click_export_button_in_sport_overview(self):
        # 点击导出的按钮
        self.driver.click_element('x,//*[@id="Export"]')
        sleep(2)

    def get_sport_overview_export_div_number(self):
        # 运动总览导出页面的div标签数
        return len(list(self.driver.get_elements('x,//*[@id="exportsModal"]/div/div')))

    def get_input_style_select_in_sport_overview_export(self, m):
        # 获取客户信息和基本信息全选的勾是否被勾选
        return self.driver.get_element(
            'x,//*[@id="exportsModal"]/div/div[%s]/div[1]/div/label/div/input' % str(m + 1)).is_selected()

    def click_per_in_sport_overview_export(self, m):
        # 点击每一个基本信息和客户信息的全选框
        self.driver.click_element('x,//*[@id="exportsModal"]/div/div[%s]/div[1]/div/label/div/ins' % str(m + 1))
        sleep(1)

    def click_search_button_in_sport_overview(self):
        # 点击运动总览页面的搜索按钮
        self.driver.click_element('x,//*[@id="runForm"]/div[4]/button')
        sleep(5)

    def click_create_task_button_in_sport_overview_export(self):
        # 点击运动总览页面的生成任务按钮
        self.driver.click_element('x,//*[@id="addTaskBtn"]')
        sleep(10)
        self.driver.click_element('x,//*[@id="taskList"]/div[1]/ul/li/a')
        sleep(5)

    def get_data_total_number_in_sport_overview(self):
        # 获取运动总览查询出来的数据条数
        return len(list(self.driver.get_elements('x,//*[@id="table"]/tbody/tr')))

    def get_per_line_data(self, i):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[11]' % str(i + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[12]' % str(i + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[13]' % str(i + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[14]' % str(i + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[15]' % str(i + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[16]' % str(i + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[1]' % str(i + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[2]' % str(i + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[3]' % str(i + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[4]' % str(i + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[5]' % str(i + 1)),
            '型号': self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[6]' % str(i + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[7]' % str(i + 1)),
            '总里程(KM)': float(self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[8]' % str(i + 1))),
            '超速(次)': float(self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[9]' % str(i + 1))),
            '停留(次)': float(self.driver.get_text('x,//*[@id="table"]/tbody/tr[%s]/td[10]' % str(i + 1))),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_mileage_data(self):
        # 搜索里程报表的数据
        # 选择本月
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(1)
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
        sleep(2)

        # 选择全部设备
        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_mileageReport"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_mileageReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_mileageReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_mileageReport"]/div[2]/div/button[1]')

        # 搜索
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[2]/div[3]/button')
        sleep(5)

    def get_per_line_data_mileage(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver == '-':
            driver = ''
        oil = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[11]' % str(a + 1))
        if oil == '-':
            oil = '-'
        else:
            '''oil = '%.3f' % (float(
                self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[10]' % str(a + 1))) / 100 * 8)'''
            oil = oil

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '开始时间': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '结束时间': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '总里程(KM)': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '总油耗': oil,
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def click_export_button_in_mileage(self):
        # 点击导出按钮在里程报表里
        self.driver.click_element('x,//*[@id="Export"]')
        sleep(6)

    def select_day_in_mileage_form(self):
        # 选择天查询
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[3]/label[3]/div/ins')
        sleep(1)

    def get_per_line_data_mileage_with_day(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[10]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[11]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver == '-':
            driver = ''
        day = self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[8]' % str(a + 1))
        if len(day) == 9:
            day = day.split('-')[0] + '-' + day.split('-')[1] + "-" + '0' + day.split('-')[2]

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '日期': day,
            '总里程(KM)': self.driver.get_text('x,//*[@id="dayTableHeader"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_travel_data(self):
        # 搜索行程报表数据
        # 搜索里程报表的数据
        # 选择本月
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(1)
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
        sleep(2)

        # 选择全部设备
        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_travelReport"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_travelReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_travelReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_travelReport"]/div[2]/div/button[1]')

        # 搜索
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[3]/button')
        sleep(5)

    def get_per_line_data_travel(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[20]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[21]' % str(a + 1))
        if driver == '-':
            driver = ''

        oil = self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if oil == '-':
            oil = '-'
        else:
            '''oil = '%.3f' % (float(
                self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[12]' % str(a + 1))) / 100 * 8)'''
            oil = oil

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '开始时间': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '结束时间': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '起点': 0.0,
            '终点': 0.0,
            '总里程(KM)': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[12]' % str(a + 1)),
            '总用时(时间)': self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '总油耗': oil,
            '平均速度(KM/H)': float(
                self.driver.get_text('x,//*[@id="mileageTableHeader"]/tbody/tr[%s]/td[15]' % str(a + 1))),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def click_day_button_in_travel_form(self):
        # 点击按天查询
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[3]/label[3]/div/ins')
        sleep(2)

    def search_travel_data_with_day(self):
        # 搜索行程报表数据
        # 搜索里程报表的数据
        # 选择本月
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(1)
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/div/ul/li[6]')
        sleep(2)

        # 选择全部设备
        # 选择设备
        self.driver.clear_input('x,//*[@id="imeiInput_travelReport"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_travelReport"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_travelReport"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_travelReport"]/div[2]/div/button[1]')

        # 搜索
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[2]/div[3]/button')
        sleep(5)

    def get_per_line_data_travel_with_day(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[10]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[11]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver == '-':
            driver = ''

        day = self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[8]' % str(a + 1))
        if len(day) == 9:
            day = day.split('-')[0] + '-' + day.split('-')[1] + "-" + '0' + day.split('-')[2]

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '日期': day,
            '总里程(KM)': self.driver.get_text('x,//*[@id="travelDayTableHeader"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_stay_data(self):
        # 搜索停留报表数据
        # 搜索里程报表的数据
        # 选择本月
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/span[2]')
        sleep(1)
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[1]/div[1]/div/div/div/div/ul/li[6]')
        sleep(2)

        # 选择全部设备
        # 选择设备
        self.driver.operate_input_element('x,//*[@id="imeiInput_stopCar"]', '867414030000066')
        '''self.driver.clear_input('x,//*[@id="imeiInput_stopCar"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_stopCar"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_stopCar"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_stopCar"]/div[2]/div/button[1]')
        '''
        # 搜索
        self.driver.click_element('x,//*[@id="StopCarFrom"]/div[2]/div[3]/button')
        sleep(5)

    def get_per_line_data_stay(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '设备IMEI': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '状态': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '开始时间': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '结束时间': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '地址': 0.0,
            '经纬度': 0.0,
            '停留时间': self.driver.get_text('x,//*[@id="stayTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def click_close_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    def switch_export_frame(self):
        self.driver.switch_to_iframe('x,/html/body/div[5]/div[2]/iframe')

    def click_create_task_button_in_sport_overview_export_stay(self):
        self.driver.click_element('x,//*[@id="addTaskBtn"]')
        sleep(10)
        self.driver.click_element('x,//*[@id="exportsModal"]/div/div[3]/div[2]/ul/div[1]/li/div[2]/a')
        sleep(10)
