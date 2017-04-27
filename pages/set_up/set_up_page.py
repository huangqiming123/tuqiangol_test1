from time import sleep

from pages.base.base_page import BasePage

# 设置页面
# author:zhangAo
from pages.base.new_paging import NewPaging


class SetUpPage(BasePage):
    # 常量
    # 控制台和设置元素的selector
    CONTROL_SELECTOR = 'x,//*[@id="index"]/a'
    SET_UP_SELECTOR = 'x,//*[@id="toSetUp"]/a'

    # 设置页面左侧导航元素的selector
    SET_UP_PAGE_SET_UP_LANDMARK_SELECTOR = 's,#dibiao'
    SET_UP_PAGE_SET_UP_EQUIPMENT_TYPE_SELECTOR = 'x,//*[@id="machineTypeName"]'
    SET_UP_PAGE_BLACK_CAR_ADRESS_LIBRARY_SELECTOR = 's,#blackCarAddressLibrary'
    SET_UP_PAGE_CLICK_SET_UP_AFTER_TITLE_TEST_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[1]/b'

    # 地标设置页面元素的selector
    SET_UP_LANDMARK_TITLE_TEXT_AFTER_CLICK_SET_UP_LANDMARK_SELECROT = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[1]/div/b'
    SET_UP_LANDMARK_ADD_LANDMARK_SELECTOR = 'x,//*[@id="toLandMarkMap"]'
    SET_UP_LANDMARK_CLILK_ADD_LANDMARK_TEST_SELECTOR = 'x,//*[@id="createGeoLand"]'
    SET_UP_LANDMARK_CLOSE_ADD_LANDMARK_SELECTOR = 's,#createFenceModal > div > div > div.modal-header > button > span'

    SET_UP_LANDMARK_OPERATION_LOOK_SELECTOR = 'x,//*[@id="lamkList"]/tr[1]/td[5]/a[1]'
    SET_UP_LANDMARK_TITLE_TEXT_AFTER_CLICK_LOOK_SELECTOR = 'x,//*[@id="checkGeo"]'
    SET_UP_LANDMARK_CLOSE_LANDMARK_SELECTOR = 's,#viewFenceModal > div > div > div.modal-header > button > span'
    SET_UP_LANDMARK_EXPECT_LANDMARK_TEXT_SELECTOR = 'x,//*[@id="lamkList"]/tr[1]/td[2]'

    SET_UP_LANDMARK_OPERATION_EDIT_SELECTOR = 'x,//*[@id="lamkList"]/tr/td[5]/a[2]'
    SET_UP_LANDMARK_TITLE_TEXT_AFTER_EDIT_SELECTOR = 'x,//*[@id="myModalLabel"]'
    SET_UP_LANDMARK_EDIT_LANDMARK_NAME_SELECTOR = 'x,//*[@id="geoname"]'
    SET_UP_LANDMARK_EDIT_LANDMARK_DESC_SELECTOR = 'x,//*[@id="description"]'
    SET_UP_LANDMARK_EDIT_SUBMIT_BUTTON_SELECTOR = 'x,//*[@id="saveBtn"]'
    SET_UP_LANDMARK_EDIT_CLOSE_SELECTOR = 's,#editFenceModal > div > div > div.modal-header > button > span'
    SET_UP_LANDMARK_EDIT_CANCEL_SELECTOR = 'x,//*[@id="editFenceModal"]/div/div/div[3]/button[2]'

    SET_UP_LANDMARK_OPERATION_DELETE_SELECTOR = 'x,//*[@id="lamkList"]/tr[1]/td[5]/a[3]'
    SET_UP_LANDMARK_TEXT_AFTER_DELETE_SELECTOR = 'x,/html/body/div[4]/div[3]/a[1]'
    SET_UP_LANDMARK_ENSURE_DELETE_LANDMARK_SELECTOR = 'x,/html/body/div[4]/div[3]/a[1]'
    SET_UP_LANDMARK_CLOSE_DELETE_LANDMARK_SELECTOR = 'x,/html/body/div[4]/span/a'
    SET_UP_LANDMARK_CANCEL_DELETE_LANDMARK_SELECTOR = 'x,//*[@id="layui-layer4"]/div[3]/a[2]'

    BLACK_CAR_ADDRESS_TEXT_CLICK_BLACK_CAR_ADDRESS_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[1]/div/b'
    BLACK_CAR_ADDRESS_CLICK_BLACK_CAR_ADDRESS_SELECTOR = 'x,//*[@id="toBlackCarMap"]'
    BLACK_CAR_ADDRESS_TITLE_TEXT_CLICK_BLACK_CAR_ADDRESS_SELECTOR = 'x,//*[@id="createGeoLand"]'
    BLACK_CAR_ADDRESS_CLOSE_CLICK_BLACK_CAR_ADDRESS_SELECTOR = 'x,//*[@id="createFenceModal"]/div/div/div[1]/button/span'

    BLACK_CAR_ADDRESS_OPERATION_LOOK_SELECTOR = 'x,//*[@id="blackCarList"]/tr[1]/td[7]/a[1]'
    BLACK_CAR_ADDRESS_EXPECT_NAME_SELECTOR = 'x,//*[@id="blackCarList"]/tr[1]/td[2]'
    BLACK_CAR_ADDRESS_TITLE_TEXT_CLICK_LOOK_BLACK_CAR_ADDRESS_SELECTOR = 'x,//*[@id="checkGeo"]'
    BLACK_CAR_ADDRESS_OPERATION_LOOK_CLOSE_SELECTOR = 'x,//*[@id="viewFenceModal"]/div/div/div[1]/button/span'

    BLACK_CAR_ADDRESS_OPERATION_EDIT_SELECTOR = 'x,//*[@id="blackCarList"]/tr[1]/td[7]/a[2]'
    BLACK_CAR_ADDRESS_CHECK_TITLE_TEXT_AFTER_OPERATION_EDIT_SELECTOR = 'x,//*[@id="createGeoLand"]'
    BLACK_CAR_ADDRESS_OPERATION_EDIT_CLOSE_SELECTOR = 'x,//*[@id="createFenceModal"]/div/div/div[1]/button/span'

    BLACK_CAR_ADDRESS_OPERATION_DELETE_SELECTOR = 'x,//*[@id="blackCarList"]/tr[1]/td[7]/a[3]'
    BLACK_CAR_ADDRESS_TITLE_TEXT_CLICK_DELETE_BLACK_CAR_ADDRESS_SELECTOR = 'x,/html/body/div[4]/div[3]/a[1]'
    BLACK_CAR_ADDRESS_OPERATION_DELETE_CLOSE_SELECTOR = 'x,/html/body/div[4]/span/a'
    BLACK_CAR_ADDRESS_OPERATION_DELETE_CANCEL_SELECTOR = 'x,/html/body/div[4]/div[3]/a[2]'
    BLACK_CAR_ADDRESS_OPERATION_DELETE_ENSURE_SELECTOR = 'x,/html/body/div[4]/div[3]/a[1]'

    # 设置设备型号
    SET_UP_EQUIPMENT_TYPE_TEXT_AFTER_CLICK_SELECTOR = 'x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[1]/div[1]/div/b'
    SET_UP_EQUIPMENT_TYPE_CLICK_SET_TYPE_BUTTON_SELECTOR = 'x,//*[@id="machineTypeName_tbody"]/tr[1]/td[4]/a'
    SET_UP_EQUIPMENT_TYPE_TEXT_AFTER_CLICK_SET_TYPE_BUTTON_SELECTOR = 'x,/html/body/div[1]/div[11]/div/div/div[1]/h4'
    SET_UP_EQUIPMENT_TYPE_NEW_TYPE_SELECTOR = 'x,/html/body/div[1]/div[11]/div/div/div[2]/div/div/form/div[2]/div/input'
    SET_UP_EQUIPMENT_TYPE_NEW_TYPE_ENSURE_BUTTON_SELECTOR = 'x,/html/body/div[1]/div[11]/div/div/div[3]/button[1]'
    SET_UP_EQUIPMENT_TYPE_NEW_TYPE_CLOSE_BUTTON_SELECTOR = 'x,/html/body/div[1]/div[11]/div/div/div[1]/button'
    SET_UP_EQUIPMENT_TYPE_NEW_TYPE_CANCEL_BUTTON_SELECTOR = 'x,/html/body/div[1]/div[11]/div/div/div[3]/button[2]'

    def click_control_after_click_set_up(self):
        # 点击控制中心之后点击设置
        current_handle = self.driver.get_current_window_handle()
        self.driver.click_element(self.CONTROL_SELECTOR)
        sleep(2)

        all_handle = self.driver.get_all_window_handles()

        for handle in all_handle:
            if handle != current_handle:
                self.driver.switch_to_window(handle)
                self.driver.click_element(self.SET_UP_SELECTOR)

    def check_url_after_click_set_up(self):
        # 检查点击设置之后的url
        actual_url_after_click_set_up = self.driver.get_current_url()
        return actual_url_after_click_set_up

    def check_title_text_after_click_set_up(self):
        # 检查点击设置之后左侧导航标题的文本
        actual_title_test_after_click_set_up = self.driver.get_text(
                self.SET_UP_PAGE_CLICK_SET_UP_AFTER_TITLE_TEST_SELECTOR)
        return actual_title_test_after_click_set_up

    def click_set_up_page_lift_list(self, type):
        """
        点击设置界面左侧的列表，其中type：
        set_up_landmark:地标设置
        set_up_equipment_type:设备型号设置
        black_car_adress_library:黑车地址库
        """
        if type == 'set_up_landmark':
            self.driver.click_element(self.SET_UP_PAGE_SET_UP_LANDMARK_SELECTOR)

        elif type == 'set_up_equipment_type':
            self.driver.click_element(self.SET_UP_PAGE_SET_UP_EQUIPMENT_TYPE_SELECTOR)

        elif type == 'black_car_adress_library':
            self.driver.click_element(self.SET_UP_PAGE_BLACK_CAR_ADRESS_LIBRARY_SELECTOR)

    def check_title_text_after_click_set_up_landmark(self):

        # 点击地标设置之后，检查右侧标题的文本
        actual_title_text_after_click_set_up_landmark = self.driver.get_text(
                self.SET_UP_LANDMARK_TITLE_TEXT_AFTER_CLICK_SET_UP_LANDMARK_SELECROT)
        return actual_title_text_after_click_set_up_landmark

    def click_set_up_landmark_page_add_landmark(self):
        # 地标设置页面的创建地标
        self.driver.click_element(self.SET_UP_LANDMARK_ADD_LANDMARK_SELECTOR)
        self.driver.implicitly_wait(5)

    def check_title_text_after_click_add_landmark(self):
        # 点击创建地标之后，检查标题文本
        actual_text_after_click_add_landmark = self.driver.get_text(
                self.SET_UP_LANDMARK_CLILK_ADD_LANDMARK_TEST_SELECTOR)
        return actual_text_after_click_add_landmark

    def close_add_landmark(self):
        # 关闭创建地标
        self.driver.click_element(self.SET_UP_LANDMARK_CLOSE_ADD_LANDMARK_SELECTOR)
        self.driver.implicitly_wait(2)

    def set_up_landmark_operation_click_look(self):
        # 点击查看地标
        try:
            self.driver.click_element(self.SET_UP_LANDMARK_OPERATION_LOOK_SELECTOR)
            self.driver.implicitly_wait(2)

        except:

            print("列表无数据！")

    def check_title_text_after_click_look_button(self):
        # 点击查看之后，返回地标标题的文本
        actual_title_text_after_click_look_button = self.driver.get_text(
                self.SET_UP_LANDMARK_TITLE_TEXT_AFTER_CLICK_LOOK_SELECTOR)
        return actual_title_text_after_click_look_button

    def expect_landmark_text(self):
        # 获取期望的地标文本
        expect_landmark_text = self.driver.get_text(self.SET_UP_LANDMARK_EXPECT_LANDMARK_TEXT_SELECTOR)
        return expect_landmark_text

    def close_landmark(self):
        # 打开之后，关闭查看的窗口
        self.driver.click_element(self.SET_UP_LANDMARK_CLOSE_LANDMARK_SELECTOR)
        self.driver.implicitly_wait(2)

    def set_up_landmark_operation_click_edit(self):
        # 点击编辑
        try:
            self.driver.click_element(self.SET_UP_LANDMARK_OPERATION_EDIT_SELECTOR)
            self.driver.implicitly_wait(2)
        except:
            print('列表无数据！')

    def check_title_text_after_click_edit_button(self):
        # 点击编辑之后，获取编辑框标题的文本
        actual_text = self.driver.get_text(self.SET_UP_LANDMARK_TITLE_TEXT_AFTER_EDIT_SELECTOR)
        return actual_text

    def edit_landmark(self, set_up_landmark_edit_data):

        # 传入编辑的数据
        self.driver.operate_input_element(self.SET_UP_LANDMARK_EDIT_LANDMARK_NAME_SELECTOR,
                                          set_up_landmark_edit_data['landmark_name'])
        self.driver.operate_input_element(self.SET_UP_LANDMARK_EDIT_LANDMARK_DESC_SELECTOR,
                                          set_up_landmark_edit_data['landmark_desc'])
        # 点击保存
        self.driver.click_element(self.SET_UP_LANDMARK_EDIT_SUBMIT_BUTTON_SELECTOR)
        self.driver.implicitly_wait(2)

    def close_landmark_edit(self):
        # 点击关闭编辑地标
        self.driver.click_element(self.SET_UP_LANDMARK_EDIT_CLOSE_SELECTOR)
        self.driver.implicitly_wait(3)

    def cancel_landmark_edit(self):
        # 点击取消编辑地标
        self.driver.click_element(self.SET_UP_LANDMARK_EDIT_CANCEL_SELECTOR)
        self.driver.implicitly_wait(3)

    def set_up_landmark_operation_click_delete(self):
        # 点击删除
        try:
            self.driver.click_element(self.SET_UP_LANDMARK_OPERATION_DELETE_SELECTOR)
            self.driver.implicitly_wait(2)
        except:
            print("列表无数据！")

    def check_text_after_click_delete(self):
        # 检查点击删除之后的文本
        actual_text = self.driver.get_text(self.SET_UP_LANDMARK_TEXT_AFTER_DELETE_SELECTOR)
        return actual_text

    def ensure_detele_landmark(self):
        # 确认删除地标
        self.driver.click_element(self.SET_UP_LANDMARK_ENSURE_DELETE_LANDMARK_SELECTOR)
        self.driver.implicitly_wait(3)

    def cancel_delete_landmark(self):
        # 点击取消删除地标
        self.driver.click_element(self.SET_UP_LANDMARK_CANCEL_DELETE_LANDMARK_SELECTOR)
        self.driver.implicitly_wait(2)

    def close_delete_landmark(self):
        # 点击关闭删除图标
        self.driver.click_element(self.SET_UP_LANDMARK_CLOSE_DELETE_LANDMARK_SELECTOR)
        self.driver.implicitly_wait(2)

    def check_text_after_click_black_car_address(self):
        # 检查点击黑车地址库后 右侧页面左上角的文本
        actual_text = self.driver.get_text('x,/html/body/div[1]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/b')
        return actual_text

    def click_add_black_car_address(self):
        # 点击创建黑车地址看

        self.driver.click_element(self.BLACK_CAR_ADDRESS_CLICK_BLACK_CAR_ADDRESS_SELECTOR)
        sleep(3)

    def check_title_text_after_click_add_black_address(self):
        # 检查点击创建黑车地址库地图title的文本
        expect_text = self.driver.get_text(self.BLACK_CAR_ADDRESS_TITLE_TEXT_CLICK_BLACK_CAR_ADDRESS_SELECTOR)
        return expect_text

    def click_close_add_black_car_address(self):
        # 点击关闭创建黑车地址库
        self.driver.click_element(self.BLACK_CAR_ADDRESS_CLOSE_CLICK_BLACK_CAR_ADDRESS_SELECTOR)
        sleep(3)

    def black_car_address_operation_look(self):
        # 点击查看黑车地址库
        try:
            self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_LOOK_SELECTOR)
        except:
            print('黑车地址库列表无数据！')

    def expect_black_car_address_name(self):
        # 获取期望的黑车地址库的名字
        try:
            expect_name = self.driver.get_text(self.BLACK_CAR_ADDRESS_EXPECT_NAME_SELECTOR)
            return expect_name
        except:
            print('黑车地址库列表无数据！')

    def check_title_text_black_car_address_operation_look(self):
        # 检查 点击查看之后地图为title文本
        expect_text = self.driver.get_text(self.BLACK_CAR_ADDRESS_TITLE_TEXT_CLICK_LOOK_BLACK_CAR_ADDRESS_SELECTOR)
        return expect_text

    def close_look_black_car_address(self):
        # 点击关闭查看黑车地址库
        self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_LOOK_CLOSE_SELECTOR)
        sleep(3)

    def black_car_address_operation_edit(self):
        # 点击编辑黑车地址库
        try:
            self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_EDIT_SELECTOR)
            sleep(3)
        except:
            print('黑车地址库列表无数据！')

    def check_title_text_after_click_edit_black_car_address(self):
        # 检查点击编辑黑车地址后的title的文本
        actual_text = self.driver.get_text(self.BLACK_CAR_ADDRESS_CHECK_TITLE_TEXT_AFTER_OPERATION_EDIT_SELECTOR)
        return actual_text

    def close_edit_black_car_address(self):
        # 点击关闭编辑黑车地址库
        try:
            self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_EDIT_CLOSE_SELECTOR)
            sleep(3)
        except:
            print('黑车地址库列表无数据！')

    def black_car_address_operation_delete(self):
        # 点击删除黑车地址库
        try:
            self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_DELETE_SELECTOR)
            sleep(5)
        except:
            print('黑车地址库列表无数据！')

    def check_title_text_after_click_delete_black_car_address(self):
        # 检查点击删除黑车地址库后的title的文本
        actual_text = self.driver.get_text(self.BLACK_CAR_ADDRESS_TITLE_TEXT_CLICK_DELETE_BLACK_CAR_ADDRESS_SELECTOR)
        return actual_text

    def close_delete_black_car_address(self):
        # 点击关闭删除
        self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_DELETE_CLOSE_SELECTOR)
        sleep(3)

    def cancel_delete_black_car_address(self):
        # 点击取消删除黑车地址库
        self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_DELETE_CANCEL_SELECTOR)
        sleep(3)

    def ensure_delete_black_car_address(self):
        # 点击确认删除
        self.driver.click_element(self.BLACK_CAR_ADDRESS_OPERATION_DELETE_ENSURE_SELECTOR)
        sleep(3)

    def check_text_after_click_set_up_equipment(self):
        # 点击设备型号设置后检查右侧页面左上角的文本
        actual_text = self.driver.get_text(self.SET_UP_EQUIPMENT_TYPE_TEXT_AFTER_CLICK_SELECTOR)
        return actual_text

    def set_up_equipment_type_click_set_type(self):
        # 点击设置型号
        try:
            self.driver.click_element(self.SET_UP_EQUIPMENT_TYPE_CLICK_SET_TYPE_BUTTON_SELECTOR)
            sleep(3)
        except:
            print('型号列表无数据！')

    def check_text_after_click_set_type(self):
        # 点击设置型号后，检查title的文本
        actual_text = self.driver.get_text(self.SET_UP_EQUIPMENT_TYPE_TEXT_AFTER_CLICK_SET_TYPE_BUTTON_SELECTOR)
        return actual_text

    def set_up_equipment_type(self, equipment_type_data):
        # 输入新型号，点击确定
        self.driver.operate_input_element(self.SET_UP_EQUIPMENT_TYPE_NEW_TYPE_SELECTOR, equipment_type_data['new_type'])
        # 点击确定
        self.driver.click_element(self.SET_UP_EQUIPMENT_TYPE_NEW_TYPE_CLOSE_BUTTON_SELECTOR)

    def set_up_equipment_type_close_set_new_type(self):
        # 点击关闭设置新型号页面
        self.driver.click_element(self.SET_UP_EQUIPMENT_TYPE_NEW_TYPE_CLOSE_BUTTON_SELECTOR)
        sleep(2)

    def set_up_equipment_type_cancel_set_new_type(self):
        # 点击取消设置新型号
        self.driver.click_element(self.SET_UP_EQUIPMENT_TYPE_NEW_TYPE_CANCEL_BUTTON_SELECTOR)
        sleep(2)

    def get_total_page_in_set_up_type(self):
        # 获取总共有多少
        a = self.driver.get_element('x,//*[@id="machineTypeName_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            number = new_paging.get_total_page('x,//*[@id="machineTypeName_paging"]')
            return number
        elif a == 'display: none;':
            return 0
        self.driver.refresh_browser()
        sleep(3)

    def set_up_type_click_next_page(self):
        number = self.get_total_page_in_set_up_type()
        self.driver.refresh_browser()
        sleep(3)
        if number == 0:
            print("页面无数据！")

        elif number == 1:
            print('页面就一页，不能点击下一页')

        else:
            self.driver.click_element('l,下一页')
            sleep(2)
            self.driver.click_element('1,上一页')

