from time import sleep

from pages.base.base_page import BasePage
from pages.base.base_paging_function import BasePagingFunction
from pages.base.new_paging import NewPaging


class CommandManagementPage(BasePage):
    '''
    指令管理页面的操作
    author：zhangAo
    '''

    # 常量
    CONTROL_SELECTOR = 'x,//*[@id="index"]/a'
    COMMAND_MANAGEMENT_SELECTOR = 'x,//*[@id="commandManagement"]/a'
    ACTUAL_TITLE_TEXT_AFTER_CLICK_COMMAND_MANAGEMENT_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[1]/b'

    # 左侧列表
    WORK_TYPE_TEMPLATE_MANAGEMENT_SELECTOR = 'x,//*[@id="templateList_li"]/a'

    ACTUAL_TITLE_TEXT_AFTER_CLICK_WORK_TYPE_MANAGEMENT_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[1]/div/b'

    WORK_TYPE_MANAGEMENT_CREATE_TEMPLATE_BUTTON_SELECTOR = 'x,//*[@id="create-instructionRules"]'
    WORK_TYPE_MANAGEMENT_ACTUAL_TITLE_TEXT_CLICK_CREATE_TEMPLATE_SELECTOR = 'x,/html/body/div[5]/div/div/div[1]/h4'
    WORK_TYPE_MANAGEMENT_CLOSE_CREATE_TEMPLATE_BUTTON_SELECTOR = 'x,/html/body/div[5]/div/div/div[1]/button'
    WORK_TYPE_MANAGEMENT_CANCEL_CREATE_TEMPLATE_BUTTON_SELECTOR = 'x,/html/body/div[5]/div/div/div[3]/button[2]'

    CREATE_WORK_TEMPLATE_FRAME_SELECTOR = 'x,//*[@id="customInstructionsModal"]/div/div/div[2]/iframe'
    CREATE_WORK_TEMPLATE_NAME_SELECTOR = 'x,//*[@id="tempName"]'
    CREATE_WORK_TEMPLATE_CHOOSE_TIME_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/span/div/span[2]'
    CREATE_WORK_TEMPLATE_CHOOSE_TIMES_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/span/div/div/ul/li[%s]'
    CREATE_WORK_TEMPLATE_FIRST_TIME_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]/div/ul/li/input'
    CREATE_WORK_TEMPLATE_FRIST_SLIDER_BAR_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/span'
    CREATE_WORK_TEMPLATE_FRIST_BAR_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]'
    CREATE_WORK_TEMPLATE_SECOND_BAR_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]'
    CREATE_WORK_TEMPLATE_SECOND_SLIDER_BAR_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/span'
    CREATE_WORK_TEMPLATE_SLIDER_ENSURE_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div[2]/div[2]/button[2]'
    CREATE_WORK_TEMPLATE_CIRCULATION_DAY_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[3]/div/input'
    CREATE_WORK_TEMPLATE_NOT_CIRCULATION_SELECTOR = 'x,/html/body/div/div/div/form/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div[3]/div/label[2]/div'
    CREATE_WORK_TEMPLATE_ENSURE_BUTTON_SELECTOR = 'x,/html/body/div[5]/div/div/div[3]/button[1]'

    CREATE_WORK_TEMPLATE_OPERATION_REVISE_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[5]/a[1]'
    CREATE_WORK_TEMPLATE_OPERATION_DELETE_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[5]/a[2]'
    CREATE_WORK_TEMPLATE_TEXT_AFTER_OPERATION_DELETE_SELECTOR = 'x,/html/body/div[13]/div[3]/a[1]'
    CREATE_WORK_TEMPLATE_CANCEL_OPERATION_DELETE_SELECTOR = 'x,/html/body/div[13]/div[3]/a[2]'
    CREATE_WORK_TEMPLATE_CLOSE_OPERATION_DELETE_SELECTOR = 'x,/html/body/div[13]/span/a'
    CREATE_WORK_TEMPLATE_ENSURE_OPERATION_DELETE_SELECTOR = 'x,/html/body/div[13]/div[3]/a[1]'

    CREATE_WORK_TEMPLATE_ISSUED_COMMAND_BUTTON_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[5]/a[3]'
    CREATE_WORK_TEMPLATE_TITLE_TEXT_AFTER_CLICK_ISSUED_COMMAND_BUTTON_SELECTOR = 'x,/html/body/div[3]/div/div/div[1]/h4'
    CREATE_WORK_TEMPLATE_CLOSE_ISSUED_COMMAND_SELECTOR = 'x,/html/body/div[3]/div/div/div[1]/button'

    CREATE_WORK_TEMPLATE_IMEI_ISSUED_COMMAND_SELECTOR = 'x,/html/body/div[3]/div/div/div[2]/form/div/div/div[1]/textarea'
    CREATE_WORK_TEMPLATE_ADD_IMEI_ISSUED_COMMAND_SELECTOR = 'x,/html/body/div[3]/div/div/div[2]/form/div/div/div[1]/div/div[3]/button[1]'
    CREATE_WORK_TEMPLATE_CANCEL_IMEI_ISSUED_COMMAND_SELECTOR = 'x,/html/body/div[3]/div/div/div[2]/form/div/div/div[1]/div/div[3]/button[2]'
    CREATE_WORK_TEMPLATE_DELETE_ADD_IMEI_ISSUED_COMMAND_SELECTOR = 'x,/html/body/div[3]/div/div/div[2]/form/div/div/div[2]/div/div[2]/table/tr/td[4]/a'
    CREATE_WORK_TEMPLATE_ENSURE_ISSUED_COMMAND_SELECTOR = 'x,/html/body/div[3]/div/div/div[2]/form/div/div/div[3]/button'

    ISSUED_WORK_TYPE_TASK_MANAGEMENT_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/ul/li[2]/a'
    ISSUED_WORK_TYPE_TASK_MANAGEMENT_TITLE_TEXT_CLICK_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[1]/div/b'

    ISSUED_WORK_TYPE_TASK_MANAGEMENT_SEARCH_BATCH_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/form/div[1]/input'
    ISSUED_WORK_TYPE_TASK_MANAGEMENT_SEARCH_TEMPLATE_NAME_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/form/div[2]/input'
    ISSUED_WORK_TYPE_TASK_MANAGEMENT_SEARCH_BUTTON_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[2]/form/div[3]/button'

    ISSUED_WORK_TYPE_TASK_ALL_TR_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[4]/table/tbody'
    ISSUED_WORK_TYPE_TASK_MANAGEMENT_ALL_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[4]/div[2]'

    ISSUED_WORK_TYPE_TASK_MANAGEMENT_LOOK_EQUIPMENT_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[4]/table/tbody/tr[1]/td[6]/a'
    ISSUED_WORK_TYPE_TASK_MANAGEMENT_TEXT_LOOK_EQUIPMENT_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[1]/div/b'

    ISSUED_WORK_TYPE_MANAGEMENT_SELECTOR = 'x,//*[@id="issuedStageLi"]/a'

    def click_control_after_click_command_management(self):
        # 点击控制台后点击指令管理
        current_handle = self.driver.get_current_window_handle()
        self.driver.click_element(self.CONTROL_SELECTOR)
        sleep(2)

        all_handle = self.driver.get_all_window_handles()

        for handle in all_handle:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.driver.click_element(self.COMMAND_MANAGEMENT_SELECTOR)

    def actual_url_click_command_management(self):
        # 获取点击指令管理之后的url
        actual_url = self.driver.get_current_url()
        return actual_url

    def actual_title_text_after_click_command_management(self):
        # 获取真实的左侧列表的title文本
        actual_text = self.driver.get_text(self.ACTUAL_TITLE_TEXT_AFTER_CLICK_COMMAND_MANAGEMENT_SELECTOR)
        return actual_text

    def click_lift_list(self, type):
        # 点击指令管理的左侧列表 ，其中type：
        # work_type_template_management：工作模式模板管理
        if type == 'work_type_template_management':
            self.driver.click_element(self.WORK_TYPE_TEMPLATE_MANAGEMENT_SELECTOR)
            sleep(3)

        elif type == 'issued_work_type_task_management':
            self.driver.click_element(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_SELECTOR)
            sleep(3)

        elif type == 'issued_work_type_management':
            # 下发工作模式管理
            self.driver.click_element(self.ISSUED_WORK_TYPE_MANAGEMENT_SELECTOR)
            sleep(3)

        elif type == 'issued_command_task_management':
            # 下发指令任务管理
            self.driver.click_element('x,//*[@id="batchInsTaskList_a"]')
            sleep(3)

        elif type == 'issued_command_management':
            # 点击下发指令管理
            self.driver.click_element('x,//*[@id="batchInsList_a"]')
            sleep(3)

    def actual_title_text_after_click_work_type_template_management(self):
        # 点击工作模式模板管理后，获取右侧页面左上角的文本
        actual_text = self.driver.get_text(self.ACTUAL_TITLE_TEXT_AFTER_CLICK_WORK_TYPE_MANAGEMENT_SELECTOR)
        return actual_text

    def click_create_template(self):
        # 点击创建模板
        self.driver.click_element(self.WORK_TYPE_MANAGEMENT_CREATE_TEMPLATE_BUTTON_SELECTOR)
        sleep(3)

    def actual_title_text_after_click_create_template(self):
        # 点击创建模板后，获取创建模板框框的title文本
        actual_text = self.driver.get_text(self.WORK_TYPE_MANAGEMENT_ACTUAL_TITLE_TEXT_CLICK_CREATE_TEMPLATE_SELECTOR)
        return actual_text

    def click_close_create_template(self):
        # 点击关闭创建模板
        self.driver.click_element(self.WORK_TYPE_MANAGEMENT_CLOSE_CREATE_TEMPLATE_BUTTON_SELECTOR)
        sleep(3)

    def click_cancel_create_template(self):
        # 点击取消创建模板
        self.driver.click_element(self.WORK_TYPE_MANAGEMENT_CANCEL_CREATE_TEMPLATE_BUTTON_SELECTOR)
        sleep(3)

    def add_create_template_data(self, work_template_time_data):
        # 创建模板 添加数据
        # 切换到frame
        self.driver.switch_to_frame(self.CREATE_WORK_TEMPLATE_FRAME_SELECTOR)
        # 输入模板名称
        self.driver.operate_input_element(self.CREATE_WORK_TEMPLATE_NAME_SELECTOR, work_template_time_data['name'])

        # 选择模式
        if work_template_time_data['type'] == '2':
            # 星期模式
            self.driver.click_element('x,//*[@id="stageList"]/div/div/div/div/div[1]/ul/li[2]/a')

            # 选择星期几
            self.driver.click_element(
                    'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[2]/div/div[1]/div/ul/li[%s]/a/label/div/ins' %
                    work_template_time_data['week'])

            self.driver.click_element('x,//*[@id="stageList"]/div/div/div/div/div[2]/div[2]/div/div[2]/div/input')
            self.driver.click_element('x,//*[@id="timePicker"]/div[2]/button[2]')

            if work_template_time_data['circulation1'] == '0':
                self.driver.click_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[2]/div/div[3]/div/label[2]/div/ins')
            elif work_template_time_data['circulation1'] == '1':
                self.driver.click_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[2]/div/div[3]/div/label[1]/div/ins')
                self.driver.operate_input_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[2]/div/div[3]/div/input',
                        work_template_time_data['circulation_day1'])

        elif work_template_time_data['type'] == '3':
            # 普通模式
            self.driver.click_element('x,//*[@id="stageList"]/div/div/div/div/div[1]/ul/li[3]/a')
            self.driver.click_element('x,//*[@id="stageList"]/div/div/div/div/div[2]/div[3]/div/div[1]/div/input')
            self.driver.click_element('x,//*[@id="timePicker"]/div[2]/button[2]')

            self.driver.click_element(
                    'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[3]/div/div[2]/div/div/div/span[3]')
            self.driver.click_element(
                    'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[3]/div/div[2]/div/div/div/div/ul/li[%s]' %
                    work_template_time_data['jiange'])

            if work_template_time_data['circulation2'] == '0':
                self.driver.click_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[3]/div/div[3]/div/label[2]/div/ins')
            elif work_template_time_data['circulation2'] == '1':
                self.driver.click_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[3]/div/div[3]/div/label[1]/div/ins')
                self.driver.operate_input_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[3]/div/div[3]/div/input',
                        work_template_time_data['circulation_day2'])
        else:
            # 选择多少天一次
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_CHOOSE_TIME_SELECTOR)
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_CHOOSE_TIMES_SELECTOR % work_template_time_data['day'])

            self.driver.click_element(
                    'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/span/div/span[3]')
            self.driver.click_element(
                    'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/span/div/div/ul/li')

            self.driver.click_element('x,//*[@id="stageList"]/div/div/div/div/div[2]/div[1]/div/div[2]/div/ul/li/input')
            self.driver.click_element('x,//*[@id="timePicker"]/div[2]/button[2]')

            if work_template_time_data['circulation'] == '0':
                self.driver.click_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[1]/div/div[3]/div/label[2]/div/ins')
            elif work_template_time_data['circulation'] == '1':
                self.driver.click_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[1]/div/div[3]/div/label[1]/div/ins')
                self.driver.operate_input_element(
                        'x,//*[@id="stageList"]/div/div/div/div/div[2]/div[1]/div/div[3]/div/input',
                        work_template_time_data['circulation_day'])
        # 退出frame
        self.driver.default_frame()

    def create_template_click_ensure(self):
        # 点击保存
        self.driver.click_element(self.CREATE_WORK_TEMPLATE_ENSURE_BUTTON_SELECTOR)
        sleep(3)

    def delete_add_new_template(self):
        # 删除新建的模板
        self.driver.click_element('x,//*[@id="templateBody"]/tr[1]/td[5]/a[2]')
        sleep(1)
        self.driver.click_element('x,/html/body/div[10]/div[3]/a[1]')
        sleep(2)

    def work_template_operation_revise(self):
        # 点击修改工作模板
        try:
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_OPERATION_REVISE_SELECTOR)
            sleep(2)
        except:
            print("列表无数据！")

    def work_template_operation_delete(self):
        # 点击删除
        try:
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_OPERATION_DELETE_SELECTOR)
            sleep(3)
        except:
            print('列表无数据！')

    def actual_text_after_click_delete(self):
        # 点击删除之后，获取删除框的文本
        actual_text = self.driver.get_text('x,/html/body/div[10]/div[3]/a[1]')
        return actual_text

    def cancel_work_template_operation_delete(self):
        # 点击取消删除
        self.driver.click_element('x,/html/body/div[10]/div[3]/a[2]')
        sleep(3)

    def close_work_template_operation_delete(self):
        # 点击关闭删除
        self.driver.click_element('x,/html/body/div[10]/span/a')
        sleep(3)

    def ensure_work_template_operation_delete(self):
        # 点击确定删除工作模板
        self.driver.click_element(self.CREATE_WORK_TEMPLATE_ENSURE_OPERATION_DELETE_SELECTOR)
        sleep(3)

    def click_issued_command(self):
        # 点击下发指令
        try:
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_ISSUED_COMMAND_BUTTON_SELECTOR)
            sleep(3)
        except:
            print("列表无数据！")

    def actual_title_text_after_click_issued_command(self):
        # 点击下发指令后，获取下发指令框的文本
        actual_text = self.driver.get_text(
                self.CREATE_WORK_TEMPLATE_TITLE_TEXT_AFTER_CLICK_ISSUED_COMMAND_BUTTON_SELECTOR)
        return actual_text

    def close_issued_command(self):
        # 点击关闭下发指令
        self.driver.click_element(self.CREATE_WORK_TEMPLATE_CLOSE_ISSUED_COMMAND_SELECTOR)
        sleep(3)

    def add_data_to_issued_command(self, issued_command_data):
        # 添加数据在指令下发里
        self.driver.click_element(self.CREATE_WORK_TEMPLATE_IMEI_ISSUED_COMMAND_SELECTOR)
        sleep(2)
        self.driver.operate_input_element(self.CREATE_WORK_TEMPLATE_IMEI_ISSUED_COMMAND_SELECTOR,
                                          issued_command_data['imei'])

        if issued_command_data['add'] == '1':
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_ADD_IMEI_ISSUED_COMMAND_SELECTOR)
            sleep(3)
        else:
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_CANCEL_IMEI_ISSUED_COMMAND_SELECTOR)
            sleep(2)

        if issued_command_data['add'] == '1' and issued_command_data['delete'] == '1':
            try:
                self.driver.click_element(self.CREATE_WORK_TEMPLATE_DELETE_ADD_IMEI_ISSUED_COMMAND_SELECTOR)
                sleep(2)
            except:
                print("列表无数据！")

        if issued_command_data['ensure'] == '1':
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_ENSURE_ISSUED_COMMAND_SELECTOR)
            sleep(3)
        else:
            self.driver.click_element(self.CREATE_WORK_TEMPLATE_CLOSE_ISSUED_COMMAND_SELECTOR)

    def actual_title_text_click_issued_work_type_task_management(self):
        # 点击下发工作模式任务管理后，获取右侧区域左上角的文本
        actual_text = self.driver.get_text(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_TITLE_TEXT_CLICK_SELECTOR)
        return actual_text

    def issued_work_type_task_management_search(self, id, name):
        # 填写下发工作模式任务管理
        self.driver.operate_input_element(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_SEARCH_BATCH_SELECTOR, id)

        self.driver.operate_input_element(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_SEARCH_TEMPLATE_NAME_SELECTOR, name)

        self.driver.click_element(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_SEARCH_BUTTON_SELECTOR)
        sleep(5)

    def search_total_number(self, type):
        self.base_paging_function = BasePagingFunction(self.driver, self.base_url)
        try:
            if type == 'issued_work_type_task':
                number = self.total_num(self.base_paging_function.get_actual_paging_sum('issued_work_type_task'),
                                        self.last_page_logs_num(self.ISSUED_WORK_TYPE_TASK_ALL_TR_SELECTOR,
                                                                self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_ALL_SELECTOR))
                return number

            elif type == 'issued_work_task':
                number = self.total_num(self.base_paging_function.get_actual_paging_sum('issued_work_task'),
                                        self.last_page_logs_num(
                                                'x,//*[@id="issuedStageBody"]',
                                                'x,//*[@id="issuedStegePaging"]'))

                return number

            elif type == 'issued_command_task':
                number = self.total_num(self.base_paging_function.get_actual_paging_sum('issued_command_task'),
                                        self.last_page_logs_num('x,//*[@id="batchInsTask-tbody"]',
                                                                'x,//*[@id="paging-batchInsTask"]'))

                return number

            elif type == 'issued_command_management':
                number = self.total_num(self.base_paging_function.get_actual_paging_sum('issued_command'),
                                        self.last_page_logs_num('x,//*[@id="batchIns-tbody"]',
                                                                'x,//*[@id="paging-batchInsLogs"]'))

                return number
        except:
            print('暂无数据！')
            return 0

    def click_look_equipment(self):
        # 点击查看设备
        try:
            self.driver.click_element(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_LOOK_EQUIPMENT_SELECTOR)
            sleep(3)
        except:
            print('列表无数据！')

    def actual_text_click_look_equipment(self):
        # 点击查看设备后，获取页面右上角的文本
        actual_text = self.driver.get_text(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_TEXT_LOOK_EQUIPMENT_SELECTOR)
        return actual_text

    def add_data_to_search(self, search_data):
        # 在搜索框添加数据
        self.driver.operate_input_element('x,//*[@id="issuedTemplateBatchId"]', search_data['batch'])

        # 选择执行状态   5：待发送，1：离线，2：发送成功，3：发送失败，4：取消
        sleep(3)
        if search_data['execute_state'] == '5':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/div/ul/li[2]')

        elif search_data['execute_state'] == '1':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/span[2]')
            sleep(3)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/div/ul/li[3]')

        elif search_data['execute_state'] == '2':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/div/ul/li[4]')

        elif search_data['execute_state'] == '3':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/div/ul/li[5]')

        elif search_data['execute_state'] == '4':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/div/ul/li[6]')
        else:
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[2]/div/span/div/div/ul/li[1]')

        # 选择状态

        if search_data['state'] == '1':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[3]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[3]/div/span/div/div/ul/li[2]')
        elif search_data['state'] == '2':
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[3]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[3]/div/span/div/div/ul/li[3]')
        else:
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[3]/div/span/div/span[2]')
            sleep(2)
            self.driver.click_element(
                    'x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[3]/div/span/div/div/ul/li[1]')

        # 输入imei
        self.driver.click_element('x,//*[@id="searchIssuedTemplateIMEI"]')
        sleep(1)
        self.driver.operate_input_element('x,//*[@id="searchIssuedTemplateIMEI"]', search_data['imei'])

        # self.driver.click_element(
        #    's,body > div.wrapper > div.main.oh > div > div > div.customer-rightsidebar.p-15.mih-400 > div.tab-con-sendworkmode.b1-ccc.bc-fff > div.funcbar.clearfix > form > div:nth-child(4) > div > div > div.fr > button.btn.btn-success.btn-sm.mw-80.js-add-results-btn')

        self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[5]/button')
        sleep(5)

    def click_look_issued_work_type(self):
        # 点击查看下发工作模式
        self.driver.click_element('x,//*[@id="js-view-SendWorkMode"]')
        sleep(3)

    def actual_text_after_click_look_issued(self):
        # 点击查看下发工作模式后，检查查看框的title文本
        actual_text = self.driver.get_text('x,/html/body/div[2]/div/div/div[1]/h4')
        return actual_text

    def click_list_input_issued_work_type(self):
        # 点击下发工作模式列表序号前面的框
        self.driver.click_element('x,//*[@id="issuedStageTableHeader"]/thead/tr/th[1]/span/div/ins')
        sleep(2)

    def actual_click_list_input_issued_work_type(self):
        # 点击框框后，返回true or false
        actual = self.driver.get_element(
                'x,//*[@id="issuedStageTableHeader"]/thead/tr/th[1]/span/div/input').is_selected()
        return actual

    def actual_click_list_input_issued(self):
        # 点击框框后，返回true or false
        actual = self.driver.get_element('x,//*[@id="issuedStageBody"]/tr[1]/td[1]/span/div/input').is_selected()
        return actual

    def click_close_look_issued_work_type(self):
        # 点击关闭查看
        self.driver.click_element('x,//*[@id="view-SendWorkMode"]/div/div/div[1]/button/span')
        sleep(3)

    def click_cancel_issued(self):
        # 点击取消指令
        try:
            self.driver.click_element('x,//*[@id="issuedStageBody"]/tr[1]/td[1]/span/div/ins')
            sleep(2)
            self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[6]/button[1]')
            sleep(2)
        except:
            return False

    def click_cancel_all_issued(self):
        # 点击全部取消
        self.driver.click_element('x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/form/div[6]/button[2]')
        sleep(2)

    def actual_succed_text(self):
        # 获取操作成功的文本
        actual_text = self.reset_passwd_stat_cont()
        return actual_text

    def actual_text_after_click_issued_command_task(self):
        # 点击下发指令任务管理后，获取页面右上角的文本
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[2]/div[4]/div[1]/div/b')
        return actual_text

    def issued_command_task_add_data_to_search(self, search_data):
        # 下发任务指令管理，增加数据去搜索
        self.driver.operate_input_element('x,//*[@id="batchInsTask-form"]/div[1]/input', search_data['batch'])
        self.driver.operate_input_element('x,//*[@id="batchInsTask-form"]/div[2]/input', search_data['name'])
        # 点击搜索
        self.driver.click_element('x,//*[@id="batchInsTask-form"]/div[3]/button')
        sleep(5)

    def click_look_equipment_in_issued_command_task(self):
        # 在下发指令任务管理页面点击查看设备
        try:
            self.driver.click_element('x,//*[@id="batchInsTask-tbody"]/tr[1]/td[9]/a')
            sleep(3)
        except:
            print('列表无数据！')

    def actual_text_after_click_look_equipment(self):
        # 点击查看设备后，返回真实的title文本
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[2]/div[5]/div[1]/div/b')
        return actual_text

    def issued_command_management_search_data(self, search_data):
        # 下发指令管理页面搜索 增加搜索的条件
        # 添加IMEI
        self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[1]/div/textarea')
        self.driver.operate_input_element('x,//*[@id="batchInsLogs-form"]/div[1]/div/textarea', search_data['imei'])

        # 添加批次号
        self.driver.operate_input_element('x,//*[@id="batchInsLogs-form"]/div[2]/input', search_data['batch'])

        # xx选择状态
        self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/span[2]')
        sleep(3)
        if search_data['statue'] == '5':
            # 在线发送
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[2]')
        elif search_data['statue'] == '6':
            # 离线发送
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[3]')
        elif search_data['statue'] == '0':
            # 失败
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[5]')
        elif search_data['statue'] == '1':
            # 成功
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[4]')
        elif search_data['statue'] == '3':
            # 待发送
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[7]')
        elif search_data['statue'] == '4':
            # 已取消
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[6]')
        else:
            self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[3]/div/span/div/div/ul/li[1]')
        sleep(3)
        # 点击搜索
        self.driver.click_element('x,//*[@id="batchInsLogs-form"]/div[4]/button')
        sleep(5)

    def search_total_number_with_issued_work_task(self):
        # 统计下发工作模式任务的条数
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number('x,//*[@id="issuedTemplatePaging"]', 'x,//*[@id="issuedTemplateBody"]')
            return total
        except:
            return 0

    def search_total_number_issued_work_type(self):
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number('x,//*[@id="issuedStegePaging"]', 'x,//*[@id="issuedStageBody"]')
            return total
        except:
            return 0

    def search_total_number_with_issued_command_task(self):
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number('x,//*[@id="paging-batchInsTask"]', 'x,//*[@id="batchInsTask-tbody"]')
            return total
        except:
            return 0

    def search_total_number_issued_command_management(self):
        new_paging = NewPaging(self.driver, self.base_url)
        try:
            total = new_paging.get_total_number('x,//*[@id="paging-batchInsLogs"]', 'x,//*[@id="batchIns-tbody"]')
            return total
        except:
            return 0

    def search_total_number_work_task_manage(self):
        a = self.driver.get_element('x,//*[@id="issuedTemplatePaging"]').get_attribute('style')
        if a == 'display: none;':
            return 0
        elif a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="issuedTemplatePaging"]', 'x,//*[@id="issuedTemplateBody"]')
            return total