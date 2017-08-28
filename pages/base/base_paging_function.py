from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from pages.base.base_page import BasePage
from pages.base.new_paging import NewPaging


class BasePagingFunction(BasePage):
    """
    页面分页功能的操作
    author:ZhangAo
    """
    # 常量
    # 设置页面
    SET_UP_LANDMARK_PAGING_SUM_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[3]/div[1]'
    SET_UP_EQUIPMENT_TYPE_PAGING_SUM_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[3]/div[3]'
    BLACK_CAR_ADDRESS_PAGING_SUM_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[3]/div[1]'
    WORK_TYPE_TEMPLATE_PAGING_SUM_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[1]/div[4]/div[2]'
    ISSUED_WORK_TYPE_TASK_MANAGEMENT_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div[2]/div[4]/div[2]'

    NEXT_PAGE_SELECTOR = 'l,下一页'
    PREVIOUS_PAGE_SELECTOR = 'l,上一页'
    SKIP_PAGE_SELECTOR = 'c,page-btn'
    SECOND_PAGE_SELECTOR = 'l,2'
    INPUT_SKIP_NUMBER_SELECTOR = 'c,page-text'
    CURRENT_PAGE_SELECTOR = 'c,current'
    NUMBER_PAGE_SELECTOR = 'l,%s'
    PER_PAGE_NUMBER_SELECTOR = 'c,page-select'

    def get_paging_sum(self, type):
        '''获取页面下的分页总共有几页,其中type：
        set_up_landmark:地标设置页面
        set_up_equipment_type:设备型号设置
        '''
        try:
            if type == 'set_up_landmark':
                sum_pages = self.get_total_pages_num(self.SET_UP_LANDMARK_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'set_up_equipment_type':
                sum_pages = self.get_total_pages_num(self.SET_UP_EQUIPMENT_TYPE_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'black_car_address':
                sum_pages = self.get_total_pages_num(self.BLACK_CAR_ADDRESS_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'work_type_template_management':
                sum_pages = self.get_total_pages_num(self.WORK_TYPE_TEMPLATE_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'issued_work_type_task':
                sum_pages = self.get_total_pages_num(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_SELECTOR)
                return sum_pages

            elif type == 'issued_work_task':
                sum_pages = self.get_total_pages_num('x,//*[@id="issuedStegePaging"]')
                return sum_pages

            elif type == 'issued_command_task':
                sum_pages = self.get_total_pages_num('x,//*[@id="paging-batchInsTask"]')
                return sum_pages
            elif type == 'issued_command':
                sum_pages = self.get_total_pages_num('x,//*[@id="paging-batchInsLogs"]')
                return sum_pages
            elif type == 'set_up_alarm':
                sum_pages = self.get_total_pages_num('x,//*[@id="pagination-geozoneList"]')
                return sum_pages
        except:
            print('暂无数据！')
            return 0

    def get_actual_paging_sum(self, type):
        '''获取页面下的分页总共有几页,其中type：
        set_up_landmark:地标设置页面
        set_up_equipment_type:设备型号设置
        '''
        try:
            if type == 'set_up_landmark':
                sum_pages = self.get_actual_pages_number(self.SET_UP_LANDMARK_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'set_up_equipment_type':
                sum_pages = self.get_actual_pages_number(self.SET_UP_EQUIPMENT_TYPE_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'black_car_address':
                sum_pages = self.get_actual_pages_number(self.BLACK_CAR_ADDRESS_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'work_type_template_management':
                sum_pages = self.get_actual_pages_number(self.WORK_TYPE_TEMPLATE_PAGING_SUM_SELECTOR)
                return sum_pages

            elif type == 'issued_work_type_task':
                sum_pages = self.get_actual_pages_number(self.ISSUED_WORK_TYPE_TASK_MANAGEMENT_SELECTOR)
                return sum_pages

            elif type == 'issued_work_task':
                sum_pages = self.get_actual_pages_number('x,//*[@id="issuedStegePaging"]')
                return sum_pages

            elif type == 'issued_command_task':
                sum_pages = self.get_actual_pages_number('x,//*[@id="paging-batchInsTask"]')
                return sum_pages
            elif type == 'issued_command':
                sum_pages = self.get_actual_pages_number('x,//*[@id="paging-batchInsLogs"]')
                return sum_pages
            elif type == 'set_up_alarm':
                sum_pages = self.get_actual_pages_number('x,//*[@id="pagination-geozoneList"]')
                return sum_pages
        except:
            print('暂无数据！')
            return 0

    def click_paging_next_page(self):
        # 如果页数大于1页，先点击下一页
        new_paging = NewPaging(self.driver, self.base_url)
        pages = new_paging.get_total_page('x,//*[@id="pagination-blackCarList"]')
        if pages == 1:
            print("失败，列表页数只有一页，不能点击下一页！")
        else:
            self.driver.click_element(self.NEXT_PAGE_SELECTOR)
            sleep(3)
            check = self.check_click_next_page()
            if check == True:
                print('点击下一页成功！')
            else:
                print('点击下一页失败！')

    def check_click_next_page(self):
        # 检查上一页是否激活
        check = self.driver.get_element(self.PREVIOUS_PAGE_SELECTOR).is_enabled()
        return check

    def click_paging_previous_page(self, type):
        # 如果点击下一页成功，请点击上一页
        pages = self.get_actual_paging_sum(type)
        if pages == 1:
            print("失败，列表页数只有一页，不能点击上一页！")
        else:
            self.driver.click_element(self.PREVIOUS_PAGE_SELECTOR)
            sleep(3)
            check = self.check_second_page_after_click_previous_page()
            if check == True:
                print("点击上一页成功！")
            else:
                print("点击上一页失败！")

    def check_second_page_after_click_previous_page(self):
        # 点击上一页后，检查第二页是否激活
        check = self.driver.get_element(self.SECOND_PAGE_SELECTOR).is_enabled()
        return check

    def click_skip_paging(self, type01, type, web_page, page):
        # 点击跳转页面
        pages = self.get_paging_sum(type01)
        page_num = self.get_actual_paging_sum(type)
        if page <= int(page_num) and page > 0:
            if web_page == 'black_car':
                # 黑车地址库
                self.driver.operate_input_element(
                    'x,//*[@id="pagination-blackCarList"]/ul/li[%s]/input' % (int(pages) + 3),
                    page)
                sleep(2)
                self.driver.click_element('x,//*[@id="pagination-blackCarList"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)
            elif web_page == 'set_up_equipment':
                # 设置型号设备
                self.driver.operate_input_element(
                    'x,//*[@id="machineTypeName_paging"]/ul/li[%s]/input' % (int(pages) + 3),
                    page)
                self.driver.click_element('x,//*[@id="machineTypeName_paging"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)

            elif web_page == 'set_up_landmark':
                # 设置地标
                self.driver.operate_input_element('x,//*[@id="pagination-lamkList"]/ul/li[%s]/input' % (int(pages) + 3),
                                                  page)
                self.driver.click_element('x,//*[@id="pagination-lamkList"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)

            elif web_page == 'work_type_template':
                # 工作模式模板管理
                self.driver.operate_input_element('x,//*[@id="templatePaging"]/ul/li[%s]/input' % (int(pages) + 3),
                                                  page)
                self.driver.click_element('x,//*[@id="templatePaging"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)

            elif web_page == 'issued_work_type_task':
                # 下发工作模式任务
                self.driver.operate_input_element(
                    'x,//*[@id="issuedTemplatePaging"]/ul/li[%s]/input' % (int(pages) + 3),
                    page)
                self.driver.click_element('x,//*[@id="issuedTemplatePaging"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)
            elif web_page == 'issued_work_task':
                # 下发工作模式任务
                self.driver.operate_input_element('x,//*[@id="issuedStegePaging"]/ul/li[%s]/input' % (int(pages) + 3),
                                                  page)
                self.driver.click_element('x,//*[@id="issuedStegePaging"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)

            elif web_page == 'issued_command_task':
                # 下发工作模式任务
                self.driver.operate_input_element('x,//*[@id="paging-batchInsTask"]/ul/li[%s]/input' % (int(pages) + 3),
                                                  page)
                self.driver.click_element('x,//*[@id="paging-batchInsTask"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)

            elif web_page == 'issued_command':
                # 下发 指令管理
                self.driver.operate_input_element('x,//*[@id="paging-batchInsLogs"]/ul/li[%s]/input' % (int(pages) + 3),
                                                  page)
                self.driver.click_element('x,//*[@id="paging-batchInsLogs"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)

            elif web_page == 'set_up_alarm':
                # 下发 指令管理
                self.driver.operate_input_element(
                    'x,//*[@id="pagination-geozoneList"]/ul/li[%s]/input' % (int(pages) + 3),
                    page)
                self.driver.click_element('x,//*[@id="pagination-geozoneList"]/ul/li[%s]/button' % (int(pages) + 3))
                sleep(2)
        else:
            print('列表只有一页，不能跳转！')

    def check_current_page_text_after_click_skip(self):
        # 检查当前的页数
        number = self.driver.get_text(self.CURRENT_PAGE_SELECTOR)
        return number

    def click_number_ship(self, type):
        # 循环点击每一页
        pages = self.get_actual_paging_sum(type)
        if pages == 1:
            print('列表只有一页！')
        else:
            for page in range(int(pages) + 1):
                if page == 0:
                    print(page)
                else:
                    self.driver.click_element(self.NUMBER_PAGE_SELECTOR % page)
                    sleep(3)

    def select_per_page_numbers(self, type, web_page, number):
        # 点击选择每页显示多少行
        pages = self.get_paging_sum(type)
        if web_page == 'black_car':
            # 黑车地址库页面
            select_element = self.driver.get_element(
                'x,//*[@id="pagination-blackCarList"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="pagination-blackCarList"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'set_up_equipment':
            # 设置型号设备页面
            select_element = self.driver.get_element(
                'x,//*[@id="machineTypeName_paging"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="machineTypeName_paging"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'set_up_landmark':
            # 设置地标
            select_element = self.driver.get_element(
                'x,//*[@id="pagination-lamkList"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="pagination-lamkList"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'work_type_template':
            # 工作模式模板
            select_element = self.driver.get_element(
                'x,//*[@id="templatePaging"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="templatePaging"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'issued_work_type_task':
            # 下发工作模式模板
            select_element = self.driver.get_element(
                'x,//*[@id="issuedTemplatePaging"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="issuedTemplatePaging"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'issued_work_task':
            # 下发工作模式模板
            select_element = self.driver.get_element(
                'x,//*[@id="issuedStegePaging"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="issuedStegePaging"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'issued_command_task':
            # 下发指令任务
            select_element = self.driver.get_element(
                'x,//*[@id="paging-batchInsTask"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="paging-batchInsTask"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'issued_command':
            # 下发指令任务
            select_element = self.driver.get_element(
                'x,//*[@id="paging-batchInsLogs"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="paging-batchInsLogs"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)

        elif web_page == 'set_up_alarm':
            # 下发指令任务
            select_element = self.driver.get_element(
                'x,//*[@id="pagination-geozoneList"]/ul/li[%s]/select' % (pages + 3))
            self.driver.click_element('x,//*[@id="pagination-geozoneList"]/ul/li[%s]/select' % (pages + 3))
            sleep(3)
            if number == '10':
                select_element.send_keys(Keys.ENTER)
            elif number == '30':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '50':
                select_element.send_keys(Keys.DOWN + Keys.ENTER)
            elif number == '100':
                select_element.send_keys(Keys.DOWN + Keys.DOWN + Keys.DOWN + Keys.ENTER)
            sleep(3)
