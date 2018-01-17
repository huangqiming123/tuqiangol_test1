import datetime
import os
from time import sleep

from model.read_excel import open_excel
from pages.base.base_page import BasePage


class FormExportPage(BasePage):
    def find_expect_file(self):
        # C:\Users\Administrator\Downloads
        base_dir = "C:\\Users\\Administrator\\Downloads"
        lists = os.listdir(base_dir)
        # 重新按时间对目录下的文件进行排序
        lists.sort(key=lambda fn: os.path.getmtime(base_dir + "\\" + fn))
        # List[-1]取到的就是最新生成的文件或文件夹
        file_new = os.path.join(base_dir, lists[-1])
        return file_new

    def read_excel_file_by_index(self, file, col_name_index=0, by_index=0, n=1):
        excel_file = open_excel(file)
        # table = excel_file.sheets[by_index]
        table = excel_file.sheet_by_index(by_index)
        # 列数
        number_rows = table.nrows
        # 每一列总共有多少个值
        colnames = table.row_values(col_name_index)

        list = []
        for rownum in range(n, number_rows):

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
        sleep(15)
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
        self.driver.click_element('x,//li[@title="上月"]')
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
        self.driver.click_element('x,//li[@title="上月"]')
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
        sleep(20)

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
        self.driver.click_element('x,//li[@title="上月"]')
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
        sleep(8)

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
        # self.driver.operate_input_element('x,//*[@id="imeiInput_stopCar"]', '867414030000066')
        self.driver.clear_input('x,//*[@id="imeiInput_stopCar"]')
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
        self.driver.switch_to_iframe('x,//*[@id="layui-layer-iframe1"]')

    def click_create_task_button_in_sport_overview_export_stay(self):
        self.driver.click_element('x,//*[@id="addTaskBtn"]')
        sleep(10)
        self.driver.click_element('x,//*[@id="exportsModal"]/div/div[3]/div[2]/ul/div[1]/li/div[2]/a')
        sleep(10)

    def search_stay_not_shut_down_data(self):
        # 搜索停留报表数据
        # 搜索里程报表的数据
        # 选择本月
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/span[2]')
        sleep(1)
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[1]/div[1]/div/div/div/div/ul/li[6]')
        sleep(2)

        # 选择全部设备
        # 选择设备
        # self.driver.operate_input_element('x,//*[@id="imeiInput_stopCar"]', '867414030000066')
        self.driver.clear_input('x,//*[@id="imeiInput_stopNotOff"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_stopNotOff"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_stopNotOff"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_stopNotOff"]/div[2]/div/button[1]')

        # 搜索
        self.driver.click_element('x,//*[@id="stopNotOffFrom"]/div[2]/div[3]/button')
        sleep(5)

    def get_per_line_data_stay_not_shut_down(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '设备IMEI': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '状态': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '开始时间': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '结束时间': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '地址': 0.0,
            '经纬度': 0.0,
            '停留时间': self.driver.get_text('x,//*[@id="stopNotOffTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_acc_data(self):
        # 搜索停留报表数据
        # 搜索里程报表的数据
        # 选择本月
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/span[2]')
        sleep(1)
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[1]/div[1]/div/div/div/div/ul/li[6]')
        sleep(2)

        # 选择全部设备
        # 选择设备
        # self.driver.operate_input_element('x,//*[@id="imeiInput_stopCar"]', '867414030000066')
        self.driver.clear_input('x,//*[@id="imeiInput_acc"]')
        sleep(2)
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[1]/span/button')
        sleep(1)

        all_group_list = list(self.driver.get_elements('x,//*[@id="dev_tree_acc"]/li'))
        all_group_num = len(all_group_list)
        for n in range(1, all_group_num):
            sleep(1)
            self.driver.click_element(
                'x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[2]/div/div/div/div[2]/div[1]/ul/li[%s]/span[1]' % str(
                    n + 1))
        self.driver.click_element('x,//*[@id="treeModal_acc"]/div[2]/label/div/ins')
        self.driver.click_element('x,//*[@id="treeModal_acc"]/div[2]/div/button[1]')

        # 搜索
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[1]/form/div[2]/div[3]/button')
        sleep(5)

    def get_per_line_data_acc(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '所属账号': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '设备IMEI': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '状态': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '开始时间': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '结束时间': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '总用时': self.driver.get_text('x,//*[@id="accTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_status_data(self):
        self.driver.click_element('x,//*[@id="OffLineFrom"]/div[3]/div[5]/button[1]')
        sleep(5)

    def get_per_line_data_status(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_number = self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备SIM卡号': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '所属用户': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '联系电话': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '设备状态': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '时间': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '经纬度': 0.0,
            '地址': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1)),
            '时长': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="offlineTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1)),
            '司机名称': driver_name,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_electric_data(self):
        # 点击包含下级、搜索
        self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[4]/label/div/ins')
        sleep(1)
        self.driver.click_element('x,//*[@id="ElectricFrom"]/div/div[5]/button[1]')
        sleep(10)

    def get_per_line_data_electric(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '型号': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '所属账号': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '剩余电量': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_alarm_overview_data(self):
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/span[2]')
        sleep(1)
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[1]/div/div/div/div/ul/li[7]')
        sleep(2)
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[5]/div/label/div/ins')
        sleep(1)
        self.driver.click_element('x,//*[@id="alarmForm"]/div/div[6]/button')
        sleep(6)

    def get_per_line_data_alarm_overview(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[8]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[9]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[10]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[11]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '所属用户': self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
            'SOS求救': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[14]' % str(a + 1))),
            '进卫星盲区报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[15]' % str(a + 1))),
            '出卫星盲区报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[16]' % str(a + 1))),
            '开机报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[17]' % str(a + 1))),
            '后视镜震动报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[18]' % str(a + 1))),
            '卫星第一次定位报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[19]' % str(a + 1))),
            '外电低电报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[20]' % str(a + 1))),
            '外电低电保护报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[21]' % str(a + 1))),
            '换卡报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[22]' % str(a + 1))),
            '关机报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[23]' % str(a + 1))),
            '外电低电保护后飞行模式报警': float(
                self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[24]' % str(a + 1))),
            '拆卸报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[25]' % str(a + 1))),
            '非法移动告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[26]' % str(a + 1))),
            '后备电池电量不足告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[27]' % str(a + 1))),
            '越界告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[28]' % str(a + 1))),
            '断电报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[29]' % str(a + 1))),
            '门报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[30]' % str(a + 1))),
            '声控报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[31]' % str(a + 1))),
            '伪基站报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[32]' % str(a + 1))),
            '开盖报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[33]' % str(a + 1))),
            '内部电池低电报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[34]' % str(a + 1))),
            '震动报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[35]' % str(a + 1))),
            '进入深度睡眠报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[36]' % str(a + 1))),
            '进入电子围栏': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[37]' % str(a + 1))),
            '离开电子围栏': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[38]' % str(a + 1))),
            '超速报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[39]' % str(a + 1))),
            '位移报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[40]' % str(a + 1))),
            '低电报警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[41]' % str(a + 1))),
            'ACC关闭': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[42]' % str(a + 1))),
            'ACC开启': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[43]' % str(a + 1))),
            '进入围栏': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[44]' % str(a + 1))),
            '离线告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[45]' % str(a + 1))),
            '离开围栏': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[46]' % str(a + 1))),
            '超速报警(平台)': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[47]' % str(a + 1))),
            '风险点告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[48]' % str(a + 1))),
            '黑车围栏告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[49]' % str(a + 1))),
            '停留告警': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[50]' % str(a + 1))),
            '长时间不进': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[51]' % str(a + 1))),
            '长时间不出': float(self.driver.get_text('x,//*[@id="alarmReportTable"]/tbody/tr[%s]/td[52]' % str(a + 1))),
        }
        return data

    def get_last_week_begin_time(self):
        # 获取上周的开始时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count - datetime.timedelta(days=6)
        return str(week) + ' 00:00'

    def get_last_week_end_time(self):
        # 获取上周的结束时间
        today = datetime.date.today()
        days_count = datetime.timedelta(days=today.isoweekday())
        week = today - days_count
        return str(week) + ' 23:59'

    def search_alarm_detail_data(self):
        # 输入开始时间结束时间
        begin_time = self.get_last_week_begin_time()
        end_time = self.get_last_week_end_time()

        js = 'document.getElementById("startTime_alarmInfo").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('startTime_alarmInfo', begin_time)

        js = 'document.getElementById("endTime_alarmInfo").removeAttribute("readonly")'
        self.driver.execute_js(js)
        self.driver.operate_input_element('endTime_alarmInfo', end_time)

        # 点击搜索
        self.driver.click_element('x,//*[@id="getAlertInfo_btn"]')
        sleep(10)

    def get_per_line_data_alarm_detail(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[20]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[21]' % str(a + 1))
        if driver == '-':
            driver = ''
        handle_status = self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if handle_status == '查看处理':
            handle_status = '已处理'

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '所属账号': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '告警类型': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '告警时间': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '定位时间': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '定位状态': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '告警地址': 0.0,
            '处理状态': handle_status,
            '已读状态': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="alarmTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def switch_export_framea(self):
        sleep(5)
        self.driver.switch_to_iframe('x,/html/body/div[11]/div[2]/iframe')

    def click_export_button_in_alarm_detail_page(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[6]/div[2]/button')
        sleep(10)
        self.driver.click_element('x,//*[@id="exportList"]/div[1]/ul/li/a')
        sleep(10)

    def search_obd_mileage_data(self):
        # 搜索obd里程报表 数据
        # 输入日期
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="上月"]')
        sleep(2)

        # 输入imei搜索
        self.driver.operate_input_element('x,//*[@id="imeiInput_travelReport"]', '868120145148729')
        # 点击搜索
        self.driver.click_element('x,//*[@id="MileageFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_per_line_data_obd_mileage(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '日期': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '行驶里程(KM)': float(
                self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1))),
            '总油耗(L)': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1))),
            '平均油耗(L/100KM)': float(
                self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1))),
            '所属用户': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_obd_travel_data(self):
        # 搜索obd里程报表 数据
        # 输入日期
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="上月"]')
        sleep(2)

        # 输入imei搜索
        self.driver.operate_input_element('x,//*[@id="imeiInput_travelReport"]', '868120145148729')
        # 点击搜索
        self.driver.click_element('x,//*[@id="TravelFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_per_line_data_obd_travel(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[20]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[21]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '开始时间': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '结束时间': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '行程时长': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '行驶里程(KM)': float(
                self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1))),
            '总油耗(L)': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1))),
            '平均油耗(L/100KM)': float(
                self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1))),
            '急加(次)': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1))),
            '急减(次)': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1))),
            '所属用户': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_obd_car_condition_data(self):
        # 搜索obd里程报表 数据
        # 输入日期
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="上月"]')
        sleep(2)

        # 输入imei搜索
        self.driver.operate_input_element('x,//*[@id="imeiInput_travelReport"]', '868120145148729')
        # 点击搜索
        self.driver.click_element('x,//*[@id="CarConditionFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_per_line_data_obd_car_condition(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[19]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[20]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '时间': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '速度(KM/H)': float(
                self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1))),
            '发动机转速(R/S)': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1))),
            '水温(℃)': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1))),
            '电池电压(V)': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1))),
            '百公里油耗(L)': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1))),
            '总里程(KM)': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1))),
            '所属用户': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '客户名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '设备名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_obd_trouble_data(self):
        # 输入日期
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="上月"]')
        sleep(2)

        # 输入imei搜索
        self.driver.operate_input_element('x,//*[@id="imeiInput_travelReport"]', '868120145148729')
        # 点击搜索
        self.driver.click_element('x,//*[@id="FailureFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_per_line_data_obd_trouble(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[16]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[17]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[18]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '时间': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            '经度': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '纬度': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1))),
            '故障代码': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1))),
            '故障类型': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1))),
            '所属用户': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1))),
            '客户名称': (self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="travelDayTableContent"]/tbody/tr[%s]/td[12]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_guide_manchine_data(self):
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="本月"]')
        sleep(2)

        self.driver.click_element('x,//ins[@class="iCheck-helper"]')
        sleep(2)
        self.driver.click_element('x,//*[@id="formGuideMachine"]/div/div[5]/button')
        sleep(5)

    def get_per_line_data_guide(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[10]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[11]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''
        driver_number = self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[12]' % str(a + 1))
        if driver_number == '-':
            driver_number = ''
        id = self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[13]' % str(a + 1))
        if id == '-':
            id = ''
        driver_frame = self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[14]' % str(a + 1))
        if driver_frame == '-':
            driver_frame = ''
        driver = self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[15]' % str(a + 1))
        if driver == '-':
            driver = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '设备型号': self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '所属帐号': self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '可用次数': float(
                self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[6]' % str(a + 1))),
            '已使用次数': float(
                self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[7]' % str(a + 1))),
            '客户名称': self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[8]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="tableContentGuideMachine"]/tbody/tr[%s]/td[9]' % str(a + 1)),
            '司机名称': driver_name,
            '电话': driver_phone,
            '车牌号': driver_number,
            '身份证号': id,
            '车架号': driver_frame,
            '电动机／发动机号': driver,
        }
        return data

    def search_clock_data(self):
        self.driver.click_element('x,//*[@id="dateSelect_div"]/div/span[2]')
        sleep(2)
        self.driver.click_element('x,//li[@title="上月"]')
        sleep(2)

        self.driver.operate_input_element('deviceName', '23001')
        sleep(2)
        self.driver.click_element('x,//*[@id="PunchTheColockFrom"]/div[1]/div[5]/button')
        sleep(5)

    def get_per_line_data_clock(self, a):
        # 获取每一列的信息
        driver_name = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[8]' % str(a + 1))
        if driver_name == '-':
            driver_name = ''
        driver_phone = self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[9]' % str(a + 1))
        if driver_phone == '-':
            driver_phone = ''

        data = {
            '序号': float(self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[1]' % str(a + 1))),
            '设备名称': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[2]' % str(a + 1)),
            'IMEI': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[3]' % str(a + 1)),
            '打卡时间': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[4]' % str(a + 1)),
            '打卡类型': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[5]' % str(a + 1)),
            '位置': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[6]' % str(a + 1)),
            '所属用户': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[7]' % str(a + 1)),
            '客户名称': driver_name,
            '联系电话': driver_phone,
            '设备型号': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[10]' % str(a + 1)),
            '设备分组': self.driver.get_text('x,//*[@id="electricTableContent"]/tbody/tr[%s]/td[11]' % str(a + 1))
        }
        return data
