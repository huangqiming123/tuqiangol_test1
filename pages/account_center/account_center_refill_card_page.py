from time import sleep

from selenium.webdriver.common.keys import Keys

from automate_driver.automate_driver_server import AutomateDriverServer

# 账户中心页面-充值卡页面
# author:戴招利
from pages.base.base_page_server import BasePageServer
from pages.base.new_paging import NewPaging


class AccountCenterRefillCardPage(BasePageServer):
    def __init__(self, driver: AutomateDriverServer, base_url):
        super().__init__(driver, base_url)

    # 点击充值卡
    def click_refill_card(self):
        self.driver.click_element("x,/html/body/div[1]/div[6]/div/div/div[1]/div/div[2]/ul/li[5]")
        sleep(2)

    # 充值卡页面iframe
    def refill_card_page_iframe(self):
        self.driver.switch_to_frame('x,/html/body/div[1]/div[6]/div/div/div[2]/div[3]/iframe')

    #获取右上角当前登录账号
    def get_current_login_account(self):
        return self.driver.get_text("x,/html/body/div[1]/header/div/div[2]/div[2]/div[1]/span/b")

    #获取我的账号
    def get_title_display_account(self):
        self.refill_card_page_iframe()
        user = self.driver.get_text("userAccount")
        self.driver.default_frame()
        return user

    #点击申请记录
    def click_apply_record(self):
        self.driver.click_element("x,/html/body/div[1]/div[2]/ul/li[1]")
        sleep(1)

    #点击  /html/body/div[1]/div[3]/div[1]/div[1]/div/div/div/ul/li[3]


    # 申请记录搜索(0:处理中，1成功，2失败，空全部)  /html/body/div[1]/div[3]/div[1]/div[1]/div/div/div/ul/li[2]
    def apply_record_search_data(self, type):
        self.driver.click_element("x,/html/body/div[1]/div[3]/div[1]/div[1]/div/div/span[2]")
        sleep(2)
        if type == "":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[1]/div[1]/div/div/div/ul/li[1]")
        elif type == "1":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[1]/div[1]/div/div/div/ul/li[2]")

        elif type == "2":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[1]/div[1]/div/div/div/ul/li[3]")
        elif type == "0":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[1]/div[1]/div/div/div/ul/li[4]")
        sleep(1)
        #点击搜索按钮
        self.driver.click_element("x,/html/body/div[1]/div[3]/div[1]/div[1]/button")
        sleep(5)


    #获取申请记录--列表条数
    def get_apply_record_number(self):
        a = self.driver.get_element('x,//*[@id="order_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="order_paging"]', 'x,//*[@id="order_tbody"]')
            return total
        elif a == 'display: none;':
            return 0


    #点击申请充值卡
    def click_apply_refill_card_button(self):
        self.refill_card_page_iframe()
        self.driver.click_element("x,/html/body/div[1]/div[1]/button[1]")
        sleep(2)
        self.driver.default_frame()


    #申请充值卡--提交
    def click_apply_refill_card_submit(self):
        self.driver.click_element("c,layui-layer-btn0")

    #申请充值卡--取消
    def click_apply_refill_card_cancel(self):
        self.driver.click_element("c,layui-layer-btn1")

    #申请充值卡--X
    def click_apply_refill_card_X(self):
        self.driver.click_element("c,layui-layer-close")

    #取消
    def apply_refill_card_cancel(self):
        self.click_apply_refill_card_button()
        self.click_apply_refill_card_cancel()
        sleep(1)
        self.click_apply_refill_card_button()
        self.click_apply_refill_card_X()
        sleep(1)

    #获取充值账号
    def get_refill_account(self):
        return self.driver.get_text("x,//*[@id='modalApply']/div/form/div[1]/div/label")

    # 添加充值卡
    def apply_refill_card_add(self, year_card, lifetime_card, name, phone, payment_account):
        # self.click_apply_refill_card_button()
        self.driver.operate_input_element("x,//*[@id='modalApply']/div/form/div[2]/div/input", year_card)
        self.driver.operate_input_element("x,//*[@id='modalApply']/div/form/div[3]/div/input", lifetime_card)
        self.driver.operate_input_element("x,//*[@id='modalApply']/div/form/div[4]/div/input", name)
        self.driver.operate_input_element("x,//*[@id='modalApply']/div/form/div[5]/div/input", phone)
        self.driver.operate_input_element("x,//*[@id='modalApply']/div/form/div[6]/div/input", payment_account)
        #下拉框
        """
        try:
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/div/form/div[7]/div/div/div')
            sleep(1)
            self.driver.click_element('x,/html/body/div[7]/div[2]/div/div/form/div[7]/div/div/div/div/ul/li[1]')
        except:
            pass
        """
        sleep(2)
        self.driver.click_element("c,layui-layer-btn0")
        sleep(2)


    #获取申请人信息  /html/body/div[7]/div[2]/div/form/div[2]/div/label
    def get_applicant_information(self):
        applicant_account = self.driver.get_text("x,/html/body/div[7]/div[2]/div/form/div[1]/div/label")
        year = self.driver.get_text("x,/html/body/div[7]/div[2]/div/form/div[2]/div/label")
        lifetime = self.driver.get_text("x,/html/body/div[7]/div[2]/div/form/div[3]/div/label")
        name = self.driver.get_text("x,/html/body/div[7]/div[2]/div/form/div[4]/div/label")
        phone = self.driver.get_text("x,/html/body/div[7]/div[2]/div/form/div[5]/div/label")
        payment_account = self.driver.get_text("x,/html/body/div[7]/div[2]/div/form/div[6]/div/label")
        data = {
            "applicant_account": applicant_account,
            "year": year,
            "lifetime": lifetime,
            "name": name,
            "phone": phone,
            "payment_account": payment_account,
        }
        print(data)
        #点击确定   layui-layer-btn0
        self.driver.click_element("x,/html/body/div[7]/div[3]/a[1]")
        return data

    #取转移成功的提示
    def get_operate_status(self):
        sleep(2)
        status_text = self.driver.get_element("c,layui-layer-content").text
        return status_text

    # 申请充值卡--取提示语
    def get_prompt(self, select):
        try:
            prompt = self.driver.get_text(select)
            return prompt
        except:
            prompt = ""
            return prompt

    # 申请充值卡--异常提示
    def get_apply_refill_card_exception_hint(self, year_card, lifetime_card, name, phone, payment_account):
        # 添加数据
        self.apply_refill_card_add(year_card, lifetime_card, name, phone, payment_account)

        # 取错误提示
        year_prompt2 = self.get_prompt("x,//*[@id='modalApply']/div/form/div[2]/div/label")
        lifetimet_prompt2 = self.get_prompt("x,//*[@id='modalApply']/div/form/div[3]/div/label")
        name_prompt2 = self.get_prompt("x,//*[@id='modalApply']/div/form/div[4]/div/label")
        phone_prompt2 = self.get_prompt("x,//*[@id='modalApply']/div/form/div[5]/div/label")
        account_prompt2 = self.get_prompt("x,//*[@id='modalApply']/div/form/div[6]/div/label")

        all_prompt = {
            "year_prompt2": year_prompt2,
            "lifetimet_prompt2": lifetimet_prompt2,
            "name_prompt2": name_prompt2,
            "phone_prompt2": phone_prompt2,
            "account_prompt2": account_prompt2,

        }
        print(all_prompt)
        return all_prompt

    # 取长度
    def get_length(self, element):
        len = int(self.driver.get_element(element).get_attribute("maxlength"))
        return len

    #获取申请充值卡长度
    def get_apply_refill_card_len(self):
        #self.click_apply_refill_card_button()
        year_len = self.get_length("x,//*[@id='modalApply']/div/form/div[2]/div/input")
        lifetime_len = self.get_length("x,//*[@id='modalApply']/div/form/div[3]/div/input")
        name_len = self.get_length("x,//*[@id='modalApply']/div/form/div[4]/div/input")
        phone_len = self.get_length("x,//*[@id='modalApply']/div/form/div[5]/div/input")
        account_len = self.get_length("x,//*[@id='modalApply']/div/form/div[6]/div/input")
        data_len = {
            "year_len": year_len,
            "lifetime_len": lifetime_len,
            "name_len": name_len,
            "phone_len": phone_len,
            "account_len": account_len,

        }

        print(data_len)
        sleep(1)
        #取消
        self.driver.click_element("c,layui-layer-btn1")

        return data_len

    #点击转移记录
    def click_transfer_record(self):
        self.driver.click_element("x,/html/body/div[1]/div[2]/ul/li[2]")
        sleep(2)

    # 搜索转移记录数据(1:转入，-1转出，空全部)
    def search_transfer_record_data(self, state):
        self.driver.click_element("x,/html/body/div[1]/div[3]/div[2]/div[1]/div/div")
        sleep(2)
        if state == "1":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/ul/li[2]")
        if state == "-1":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/ul/li[3]")
        if state == "":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/ul/li[1]")
        sleep(2)
        #点击搜索按钮
        self.driver.click_element("queryTransferBtn")
        sleep(5)


    #获取转移记录--列表条数**********没改
    def get_transfer_record_number(self):
        a = self.driver.get_element('x,//*[@id="transfer_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="transfer_paging"]', 'x,//*[@id="transfer_tbody"]')
            return total
        elif a == 'display: none;':
            return 0

    #点击充值记录
    def click_refill_record(self):
        self.driver.click_element("x,/html/body/div[1]/div[2]/ul/li[3]")
        sleep(2)

    # 充值记录搜索(1:一年充值卡,2:终身充值卡,空：全部)
    def refill_record_search_data(self, type, device_imei):
        self.driver.click_element("x,/html/body/div[1]/div[3]/div[3]/div[1]/div/div")
        sleep(2)
        if type == "1":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[3]/div[1]/div/div/div/ul/li[2]")
        elif type == "2":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[3]/div[1]/div/div/div/ul/li[3]")

        elif type == "":
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[3]/div[1]/div/div/div/ul/li[1]")
        sleep(2)
        #输入imei
        count = self.refill_record_search_imei(device_imei)
        print(count)

        #点击搜索按钮
        self.driver.click_element("queryRechargeBtn")
        sleep(8)
        return count

    # 充值记录--输入imei
    def refill_record_search_imei(self, device_imei):
        if "/" in device_imei:
            self.driver.get_element('searchIMEIs').click()
            self.driver.clear("searchIMEIs")
            self.driver.wait(1)
            value = device_imei.split("/")
            print(value)
            import_imei_count = []
            for i in value:
                add_sim = self.driver.get_element("searchIMEIs")
                self.driver.input_sim('searchIMEIs',i)
                add_sim.send_keys(Keys.ENTER)
                #去除空格，计数
                if i != "":
                    import_imei_count.append(i)

            #获取imei计数
            imei_count = self.get_refill_record_device_imei_count()
            data = {"import_count": len(import_imei_count),
                    "add_count": imei_count
                    }

            # 点击“添加”按钮
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[3]/div[1]/div[2]/div/div/div[2]/button[1]")
            self.driver.wait()
            return data
        else:
            #self.driver.get_element('searchIMEIs').click()
            add_sim = self.driver.get_element("searchIMEIs")
            self.driver.operate_input_element("searchIMEIs", device_imei)
            add_sim.send_keys(Keys.ENTER)
            self.driver.wait(1)
            imei_count = self.get_refill_record_device_imei_count()
            import_imei_count=[]
            if device_imei != "":
                import_imei_count.append(device_imei)

            data = {"import_count": len(import_imei_count),
                    "add_count": imei_count
                    }
            self.driver.click_element("x,/html/body/div[1]/div[3]/div[3]/div[1]/div[2]/div/div/div[2]/button[1]")
            self.driver.wait()
            return data



    #充值记录--imei个数
    def get_refill_record_device_imei_count(self):
        count = self.driver.get_text("ac_dev_num")
        sleep(1)
        return count



    #获取转移记录--列表条数**********没改
    def get_refill_record_number(self):
        a = self.driver.get_element('x,//*[@id="recharge_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_number('x,//*[@id="recharge_paging"]', 'x,//*[@id="recharge_tbody"]')
            return total
        elif a == 'display: none;':
            return 0


    #点击充值卡转移按钮
    def click_refill_card_transfer_button(self):
        self.refill_card_page_iframe()
        self.driver.click_element("x,/html/body/div[1]/div[1]/button[2]")
        sleep(2)
        self.driver.default_frame()

    #充值卡转移--取消
    def click_refill_card_transfer_cancel(self):
        self.driver.click_element("c,layui-layer-btn1")
        sleep(2)

    #充值卡转移--X  layui-layer-ico layui-layer-close layui-layer-close1
    def click_refill_card_transfer_x(self):
        self.driver.click_element("c,layui-layer-close")
        sleep(2)

    #充值卡转移取消
    def refill_card_transfer_cancel(self):
        #self.click_refill_card_transfer_button()
        self.click_refill_card_transfer_cancel()
        self.click_refill_card_transfer_button()
        self.click_refill_card_transfer_x()

    # 充值卡--转移
    def refill_card_transfer(self, user, year_number, lifetime_number):
        #self.click_refill_card_transfer_button()
        self.driver.click_element("x,//*[@id='modalTransfer']/form/div[1]/div/div[1]/span")
        sleep(2)
        self.driver.operate_input_element("search_user_text",user)
        #搜索
        self.driver.click_element("search_user_btn")
        try:
            sleep(3)
            self.driver.click_element("c,autocompleter-focus")
        except:
            sleep(7)
            self.driver.click_element("c,autocompleter-focus")
        sleep(1)
        # 输入卡张数
        self.driver.operate_input_element('x,//*[@id="modalTransfer"]/form/div[3]/div/input', year_number)
        self.driver.operate_input_element('x,//*[@id="modalTransfer"]/form/div[5]/div/input', lifetime_number)
        sleep(1)
        #提交
        self.driver.click_element('c,layui-layer-btn0')
        sleep(3)

    #获取充值卡--转移信息（目标用户+数量）
    def get_refill_card_transfer_data_information(self):
        # user = self.driver.get_text('x,/html/body/div[8]/div[2]/div/form/div[1]/div/label')
        user = self.driver.get_text('x,/html/body/div[7]/div[2]/div/form/div[1]/div/label')
        year_number = self.driver.get_text('x,/html/body/div[7]/div[2]/div/form/div[2]/div/label')
        lifetime_number = self.driver.get_text('x,/html/body/div[7]/div[2]/div/form/div[3]/div/label')
        data = {
            "target_user": user,
            "year_number": year_number,
            "lifetime_number": lifetime_number,
        }
        print(data)
        #点确定
        self.driver.click_element('c,layui-layer-btn0')
        return data


    #充值卡转移--数量
    def get_refill_card_transfer_quantity(self):
        year = self.driver.get_text('x,//*[@id="modalTransfer"]/form/div[2]/div/label')
        lifetime = self.driver.get_text('x,//*[@id="modalTransfer"]/form/div[4]/div/label')

        year_quantity = year.split()[0]
        lifetime_quantity = lifetime.split()[0]
        quantity = {
            "year_quantity": year_quantity,
            "lifetime_quantity": lifetime_quantity
        }
        print("充值卡转移显示的数量",quantity)
        return quantity

    #充值卡头部--充值卡数量
    def get_refill_card_page_top_quantity(self):
        self.refill_card_page_iframe()
        quantity = self.driver.get_text('userType')
        text = quantity.split("年")
        all_number = text[1].split("终身")
        year_number = all_number[0].split()[0]
        print(type(year_number))
        lifetime_number = all_number[1]

        number = {
            "year_number": year_number,
            "lifetime_number": lifetime_number
        }
        print("头部显示的数量",number)
        self.driver.default_frame()
        return number


    # 转移充值卡--异常提示
    def get_transfer_refill_card_exception_hint(self):
        # 取错误提示
        user_prompt2 = self.get_prompt("x,//*[@id='modalTransfer']/form/div[1]/div/label")
        year_prompt2 = self.get_prompt("x,//*[@id='modalTransfer']/form/div[3]/div/label")
        lifetimet_prompt2 = self.get_prompt("x,//*[@id='modalTransfer']/form/div[5]/div/label")


        all_prompt = {
            "user_prompt2": user_prompt2,
            "year_prompt2": year_prompt2,
            "lifetimet_prompt2": lifetimet_prompt2
        }
        print(all_prompt)
        return all_prompt

    # 点击客户树
    def click_transfer_target_user(self, number):
        #self.driver.click_element('x,/html/body/div[6]/div[2]/div/form/div[1]/div/div[1]/span')
        self.driver.click_element("x,//*[@id='modalTransfer']/form/div[1]/div/div[1]/span")
        sleep(2)
        self.driver.click_element(
            "x,/html/body/div[6]/div[2]/div/form/div[1]/div/div[2]/div/div/div[2]/ul/li/ul/li[" + str(number+3) +"]/a")
        sleep(2)

    #搜索用户获取提示
    def transfer_refill_card_search_user(self,user):
        self.driver.click_element("x,//*[@id='modalTransfer']/form/div[1]/div/div[1]/span")
        sleep(2)
        self.driver.operate_input_element("search_user_text",user)
        #搜索
        self.driver.click_element("search_user_btn")
        sleep(5)
        self.driver.click_element("c,autocompleter-focus")
        #sleep(2)



    #点击设备充值
    def click_equipment_refill(self):
        self.refill_card_page_iframe()
        self.driver.click_element("x,/html/body/div[1]/div[1]/button[3]")
        sleep(2)
        self.driver.default_frame()

    #获取设备充值--我的充值卡数量
    def get_equipment_refill_number(self):
        text = self.driver.get_text("x,//*[@id='layui-layer1']/div[2]/div/div/form/div[1]/div/label")
        print(text)
        number = text.split(',')
        year_quantity = number[0].split('年')[1]
        lifetime_quantity = number[1].split('身')[1]
        data = {
            "year_quantity": year_quantity,
            "lifetime_quantity": lifetime_quantity,
        }
        print(data)
        return data


    #设备充值-添加imei
    def inport_equipment(self, device_imei):
        # 一个/多个
        if "/" in device_imei:
            self.driver.get_element('searchIMEI').click()
            self.driver.clear("searchIMEI")
            self.driver.wait(1)
            value = device_imei.split("/")
            print(value)
            for i in value:
                add_sim = self.driver.get_element("searchIMEI")
                self.driver.input_sim('searchIMEI',i)
                add_sim.send_keys(Keys.ENTER)

            #获取imei计数
            imei_count = self.get_import_device_imei_count()
            data = {"import_count": len(value),
                    "add_count": imei_count
                    }
            sleep(1)
            # 点击“添加”按钮
            self.driver.click_element("x,/html/body/div[7]/div[2]/div/div/form/div[3]/div/div/div/div/div[2]/button[1]")
            #self.driver.click_element("x,/html/body/div[8]/div[2]/div/div/form/div[3]/div/div/div/div/div[2]/button[1]")
            self.driver.wait()
            return data
        else:
            self.driver.operate_input_element("searchIMEI", device_imei)
            self.driver.wait(1)
            imei_count = self.get_import_device_imei_count()
            #获取imei计数
            imei_count = self.get_import_device_imei_count()
            data = {"import_count": 1,
                    "add_count": imei_count
                    }
            print(data)
            self.driver.click_element(
                "x,//*[@id='layui-layer1']/div[2]/div/div/form/div[3]/div/div/div/div/div[2]/button[1]")
            self.driver.wait()
            return data


    #设备续费
    def equipment_refill(self,type,imei):
        #选择续费年限
        self.driver.click_element('x,//*[@id="layui-layer1"]/div[2]/div/div/form/div[2]/div/div/div')
        sleep(1)
        if type =="一年":
            self.driver.click_element("x,//*[@id='layui-layer1']/div[2]/div/div/form/div[2]/div/div/div/div/ul/li[1]")
        if type =="终身":
            self.driver.click_element("x,//*[@id='layui-layer1']/div[2]/div/div/form/div[2]/div/div/div/div/ul/li[2]")
        sleep(1)
        #输入imei
        import_imei_number = self.inport_equipment(imei)

        data = {
            "import_imei_number": import_imei_number,

        }
        print(data)
        return data


    #获取输入imei个数
    def get_import_device_imei_count(self):
        dev_num = self.driver.get_element("ac_dev_num").text
        return dev_num

    #设备充值--充值提示--取消
    def equipment_refill_hint_cancel(self):
        #self.driver.click_element('x,/html/body/div[9]/div[3]/a[2]')
        self.driver.click_element('x,//*[@id="layui-layer2"]/div[3]/a[2]')
        sleep(2)

    #设备充值--充值提示--X
    def equipment_refill_hint_x(self):
        self.driver.click_element('x,/html/body/div[9]/span[1]')
        #self.driver.click_element("x,/html/body/div[10]/span[1]/a")
        sleep(2)

    #充值提示--X
    def equipment_refill_hint(self):
        self.click_equipment_refill_button()
        self.equipment_refill_hint_cancel()
        self.click_equipment_refill_button()
        self.equipment_refill_hint_x()

    #点击续费按钮
    def click_equipment_refill_button(self):
        self.driver.click_element('c,layui-layer-ico')
        sleep(2)

    #设备充值--充值提示
    def equipment_refill_hint_data(self):
        self.click_equipment_refill_button()
        # 设备数
        prompt_refill = self.driver.get_text('x,/html/body/div[9]/div[2]/span')
        text = self.driver.get_text('x,/html/body/div[9]/div[2]')
        time_limit = text.split(":")[2]
        data={
            "prompt_refill_count":prompt_refill,
            "time_limit":time_limit
        }
        print(data)
        #确定充值
        #self.driver.click_element('c,layui-layer-btn0')
        return data

   #确定充值
    def click_confirm_refill(self):
        self.driver.click_element('x,/html/body/div[9]/div[3]/a[1]')


    #添加成功列表--imei数
    def get_list_imei_number(self):
        number = len(self.driver.get_elements('x,//*[@id="deviceinfotobody"]/tr'))
        try:
            imei = self.driver.get_text("x,//*[@id='deviceinfotobody']/tr/td[1]")
        except:
            imei = ""
        data = {
            "number": number,
            "imei":imei
        }
        print(data)
        return data

    #取设备充值成功的提示
    def get_equipment_status(self):
        # sleep(1)
        status_text = self.driver.get_element("c,layui-layer-dialog").text
        return status_text


    #设备--添加结果信息
    def equipment_refill_add_results_data(self):
        imei=[]
        cause=[]
        succeed_unmber = self.driver.get_text("successNum")
        fail_unmber = self.driver.get_text("errorNum")
        list_len = len(self.driver.get_elements("x,//*[@id='errortiptbody']/tr"))
        for i in range(list_len):
            imei.append(self.driver.get_text('x,//*[@id="errortiptbody"]/tr[' + str(i + 1) + ']/td[1]'))
            cause.append(self.driver.get_text('x,//*[@id="errortiptbody"]/tr[' + str(i + 1) +']/td[2]'))

        data = {
            "imei": imei,
            "cause": cause,
            "succeed_unmber": int(succeed_unmber),
            "fail_unmber":int(fail_unmber)
        }
        print(data)
        return data


    #设备充值-取消
    def equipment_refill_cancel(self):
        #self.inport_equipment(imei)
        #取消
        self.driver.click_element('c,layui-layer-close')
        sleep(1)

    #添加imei--添加结果行数
    def list_failure_count(self):
        return len(self.driver.get_elements("x,//*[@id='errortiptbody']/tr"))

    #设备充值-添加结果--x
    def add_results_x(self):
        # 取消
        self.driver.click_element('x,/html/body/div[9]/span[1]/a')
        sleep(2)


    # 设备充值--删除 /html/body/div[7]/div[2]/div/div/form/div[4]/div/table/tbody/tr[2]/td[5]/a
    def delete_list_device(self):
        count = len(self.driver.get_elements('x,//*[@id="deviceinfotobody"]/tr'))
        print("长度",count)
        if count > 1:
            for i in range(count):
                self.driver.click_element(
                    "x,/html/body/div[8]/div[2]/div/div/form/div[4]/div/table/tbody/tr[1]/td[5]/a")
                self.driver.wait(2)
        else:
            self.driver.click_element("x,/html/body/div[8]/div[2]/div/div/form/div[4]/div/table/tbody/tr[1]/td[5]/a")
            sleep(2)

    #重置
    def click_reset_button(self):
        self.driver.click_element('x,/html/body/div[7]/div[3]/a[2]')
        sleep(2)

    #获取充值记录第一条的最后时间
    def get_article_one_time(self):
        self.refill_card_page_iframe()
        time = self.driver.get_text('x,//*[@id="recharge_tbody"]/tr[1]/td[7]')
        print("$$",time)
        self.driver.default_frame()
        return time

    #获取申请记录有多少个分页
    def get_total_page_number_search_apply_record(self):
        a = self.driver.get_element('x,//*[@id="order_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page_and_total_number('x,//*[@id="order_paging"]',
                                                               'x,//*[@id="order_tbody"]')
            return total
        else:
            return [0, 0]

    #暂无数据
    def get_refill_card_page_no_data_text(self):
        text = self.driver.get_text("x,//*[@id='order_nodata']/div/span")
        return text

    #上一页class属性
    def get_up_page_class_active_in_apply_search(self):
        return self.driver.get_element('x,//*[@id="order_paging"]/ul/li[1]').get_attribute('class')

    #点击每一页
    def click_per_page(self, n):
        self.driver.click_element('l,%s' % str(n + 1))
        sleep(3)

    #得到
    def get_per_frist_number_in_apply_search(self):
        return self.driver.get_text('x,//*[@id="order_tbody"]/tr[1]/td[1]')

    #选择每页多少条
    def click_per_page_number(self):
        self.driver.click_element('c,page-select')
        sleep(2)
        self.driver.get_element('c,page-select').send_keys(Keys.DOWN + Keys.ENTER)
        sleep(5)

    #转移记录
    def click_per_page_number_transfer_record(self):
        count = len(self.driver.get_elements("x,//*[@id='transfer_paging']/ul/li"))
        print(count)
        self.driver.click_element("x,//*[@id='transfer_paging']/ul/li[" + str(count) +"]/select")
        sleep(2)
        self.driver.get_element("x,//*[@id='transfer_paging']/ul/li[" + str(count) + "]/select").send_keys(Keys.DOWN + Keys.ENTER)
        sleep(5)

    #充值记录
    def click_per_page_number_refill_record(self):
        count = len(self.driver.get_elements("x,//*[@id='recharge_paging']/ul/li"))
        print(count)
        self.driver.click_element("x,//*[@id='recharge_paging']/ul/li[" + str(count) +"]/select")
        sleep(2)
        self.driver.get_element("x,//*[@id='recharge_paging']/ul/li[" + str(count) + "]/select").send_keys(Keys.DOWN + Keys.ENTER)
        sleep(5)


    #申请记录
    def click_per_page_number_apply_record(self):
        count = len(self.driver.get_elements("x,//*[@id='order_paging']/ul/li"))
        print(count)
        self.driver.click_element("x,//*[@id='order_paging']/ul/li[" + str(count) +"]/select")
        sleep(2)
        self.driver.get_element("x,//*[@id='order_paging']/ul/li[" + str(count) + "]/select").send_keys(Keys.DOWN + Keys.ENTER)
        sleep(5)


    def get_page_number_in_apply_record_search(self):
        new_paging = NewPaging(self.driver, self.base_url)
        total = new_paging.get_total_page('x,//*[@id="order_paging"]')
        return total

    #获取转移记录有多少个分页
    def get_total_page_number_search_transfer_record(self):
        a = self.driver.get_element('x,//*[@id="transfer_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page_and_total_number('x,//*[@id="transfer_paging"]',
                                                               'x,//*[@id="transfer_tbody"]')
            return total
        else:
            return [0, 0]

    #转移记录--暂无数据
    def get_transfer_record_page_no_data_text(self):
        text = self.driver.get_text("x,//*[@id='transfer_nodata']/div/span")
        return text


    #转移记录--上一页class属性
    def get_up_page_class_active_in_transfer_search(self):
        return self.driver.get_element('x,//*[@id="transfer_paging"]/ul/li[1]').get_attribute('class')

    #得到
    def get_per_frist_number_in_transfer_search(self):
        return self.driver.get_text('x,//*[@id="transfer_tbody"]/tr[1]/td[1]')

    def get_page_number_in_transfer_record_search(self):
        new_paging = NewPaging(self.driver, self.base_url)
        total = new_paging.get_total_page('x,//*[@id="transfer_paging"]')
        return total


    #获取充值记录有多少个分页
    def get_total_page_number_search_refill_record(self):
        a = self.driver.get_element('x,//*[@id="recharge_paging"]').get_attribute('style')
        if a == 'display: block;':
            new_paging = NewPaging(self.driver, self.base_url)
            total = new_paging.get_total_page_and_total_number('x,//*[@id="recharge_paging"]',
                                                               'x,//*[@id="recharge_tbody"]')
            return total
        else:
            return [0, 0]

    #充值记录--暂无数据
    def get_refill_record_page_no_data_text(self):
        text = self.driver.get_text("x,//*[@id='recharge_nodata']/div/span")
        return text

    #充值记录--上一页class属性
    def get_up_page_class_active_in_refill_search(self):
        return self.driver.get_element('x,//*[@id="recharge_paging"]/ul/li[1]').get_attribute('class')

    #充值记录--得到
    def get_per_frist_number_in_refill_search(self):
        return self.driver.get_text('x,//*[@id="recharge_tbody"]/tr[1]/td[1]')

    def get_page_number_in_refill_record_search(self):
        new_paging = NewPaging(self.driver, self.base_url)
        total = new_paging.get_total_page('x,//*[@id="recharge_paging"]')
        return total

    #充值记录--导出
    def click_export_button(self):
        self.driver.click_element("export")