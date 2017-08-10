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

    # 记住默认选项
    def account_center_facility_Model_number_title(self):
        return "设备型号设置"
