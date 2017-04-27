from time import sleep

from automate_driver.automate_driver import AutomateDriver
from pages.base.base_page import BasePage

# 账户中心页面-虚拟账号管理的元素及操作
# author:孙燕妮

class AccountCenterVisualAccountPage(BasePage):
    def __init__(self,driver:AutomateDriver,base_url):
        super().__init__(driver,base_url)

    # 点击虚拟账号管理
    def enter_visual_account(self):
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[1]/div/div[2]/ul/li[3]/a")
        self.driver.wait()

    # 获取虚拟账号管理title
    def get_visual_account_title(self):
        title = self.driver.get_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[1]/div/b").text
        return title

    # 添加虚拟账户-输入虚拟账户信息
    def add_visual_account(self,visual_account,visual_passwd):
        # 点击添加
        self.driver.click_element("x,/html/body/div[1]/div[4]/div/div/div[2]/div[3]/div[2]/div[1]/form/div/button")
        self.driver.wait(1)
        # 输入虚拟账号名称
        self.driver.operate_input_element("x,//*[@id='fictitiousAccountForm']/div[1]/div/input",visual_account)
        # 输入虚拟账号密码
        self.driver.operate_input_element("fictitious_password",visual_passwd)
        # 确认密码
        self.driver.operate_input_element("password",visual_passwd)


    # 添加虚拟账户-选择修改数据权限
    def choose_modify_data_limit(self):
        self.driver.click_element("x,//*[@id='fictitiousAccountForm']/div[4]/div/ul/li[1]/label/div/ins")

    # 获取修改数据权限box状态
    def modify_data_limit_status(self):
        status = self.driver.get_element("x,//*[@id='fictitiousAccountForm']/div[4]/div/ul/li[1]/label/div/ins").is_selected()
        return status


    # 添加虚拟账户-选择下发指令权限
    def choose_assign_comm_limit(self):
        self.driver.click_element("x,//*[@id='fictitiousAccountForm']/div[4]/div/ul/li[2]/label/div/ins")

    # 获取下发指令权限box状态
    def assign_comm_status(self):
        status = self.driver.get_element("x,//*[@id='fictitiousAccountForm']/div[4]/div/ul/li[2]/label/div/ins").is_selected()
        return status

    # 添加虚拟账户-保存
    def save_add_info(self):
        self.driver.click_element("x,//*[@id='addVirtualAccountModal']/div/div/div[3]/button[1]")
        self.driver.wait(1)

    # 获取保存成功对话框的文本内容
    def get_save_status(self):
        save_status = self.driver.get_element("c,layui-layer-content").text
        return save_status


    # 添加虚拟账户-取消
    def dis_save_add_info(self):
        self.driver.click_element("x,//*[@id='addVirtualAccountModal']/div/div/div[3]/button[3]")

    # 编辑虚拟账户
    def edit_visu_account(self,edit_passwd):
        sleep(2)
        self.driver.click_element("x,//*[@id='fictitiousAccount_tbody']/tr[1]/td[4]/a[1]")
        self.driver.wait(1)
        # 编辑密码
        self.driver.operate_input_element("fictitious_password",edit_passwd)
        # 编辑再次输入密码
        self.driver.operate_input_element("password",edit_passwd)
        # 保存
        self.driver.click_element("x,//*[@id='addVirtualAccountModal']/div/div/div[3]/button[2]")
        self.driver.wait()

    # 取消编辑
    def dis_edit(self):
        self.driver.click_element("x,//*[@id='fictitiousAccount_tbody']/tr[1]/td[4]/a[1]")
        self.driver.wait(1)
        # 点击取消
        self.driver.click_element("x,//*[@id='addVirtualAccountModal']/div/div/div[3]/button[3]")

    # 删除虚拟账户
    def del_visu_account(self):
        self.driver.click_element("x,//*[@id='fictitiousAccount_tbody']/tr[1]/td[4]/a[2]")
        self.driver.wait(1)
        # 确定
        self.driver.click_element("c,layui-layer-btn0")
        self.driver.wait(1)






