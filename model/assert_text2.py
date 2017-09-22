class AssertText2(object):

    def account_center_home_page_setting_prompt(self):
        return '设置成功，下次登录生效'

    def account_center_home_page_setting_state(self):
        return '已默认'

    def account_center_home_page_no_setting_state(self):
        return '设置默认'

    def home_page_edit_password_success(self):
        return '密码修改成功'

    def account_center_default_home_setting_title(self):
        return '默认首页设置'

    # 跳转页面，期望地址
    def get_page_expect_url(self, page_url):
        if page_url == "库存" or page_url == "设备管理":
            return '/device/toDeviceManage'

        elif page_url == "总进货数":
            return '/device/toDeviceManage?lowerDevFlag=1'

        elif page_url == "即将到期":
            return '/device/toDeviceManage?statusFlag=aboutToExpirate&lowerDevFlag=1'

        elif page_url == "已过期":
            return '/device/toDeviceManage?statusFlag=expirated&lowerDevFlag=1'

        elif page_url == "已激活":
            return '/device/toDeviceManage?statusFlag=actived&lowerDevFlag=1'

        elif page_url == "未激活":
            return '/device/toDeviceManage?statusFlag=inactive&lowerDevFlag=1'

    # 包含下级设备
    def account_center_page_contains_lower_dev_text(self):
        return '包含下级设备'

    # 记住默认选项
    def account_center_memorization_default_options(self):
        return "记住默认选项"

    # 设备型号设置
    def account_center_facility_Model_number_title(self):
        return "设备型号设置"

    def login_no_permissions(self):
        return "没有权限登录"

    def dev_manage_select_send_command(self):
        return "选中发送指令"

    def dev_manage_select_all_send_command(self):
        return "本次查询全部发送指令"

    def dev_manage_setting_working_mode(self):
        return "选中设置工作模式"

    def dev_manage_setting_all_working_mode(self):
        return "本次查询全部设置工作模式"

    def comm_manage_send_working_mode_task_manage(self):
        return "下发工作模式任务管理"

    def comm_manage_send_working_mode_manage(self):
        return "下发工作模式管理"

    def comm_manage_command_task_manage(self):
        return "下发指令任务管理"

    def cust_manage_exist_facility_cannot_del(self):
        return "该用户下面已有设备，不能删除"

    def cust_manage_exist_user_cannot_del(self):
        return "该用户有下级用户,无法删除"

    def cust_manage_select_user_unable_superior(self):
        return "选择的用户不能做为上级用户"

    def account_center_download_app_text(self):
        return "扫描二维码，下载手机APP客户端"

    def account_center_fast_sale_typeface(self):
        return "快速销售"

    def account_center_please_select(self):
        return "请选择"

    def account_center_refill_card_apply_succeed(self):
        return "提交申请成功!"

    def account_center_refill_card_transfer_succeed(self):
        return "转移充值卡成功!"

    def account_center_refill_card_refill_succeed(self):
        return "续费成功!"

    def cust_manage_sell_shift_agent_prompt(self):
        return '转移客户中不能包含销售'

    def cust_manage_sell_shift_user_prompt(self):
        return '转移的客户中不能包含代理商和销售'

    def cust_manage_shift_user_prompt(self):
        return '转移的客户中不能包含代理商和销售'
