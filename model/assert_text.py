class AssertText(object):
    def log_in_page_account_type(self, types):
        if types == 8:
            self.type = "代理商"
        elif types == 9:
            self.type = "用户"
        elif types == 11:
            self.type = "销售"
        elif types == 3:
            self.type = "用户"
        return self.type

    def log_in_page_find_password_text(self):
        return '找回密码'

    def log_in_page_log_in_text(self):
        return '登录'

    def log_in_page_account_or_password_not_null(self):
        return '用户名或密码不能为空'

    def log_in_page_account_not_exist(self):
        return '账号不存在'

    def log_in_page_password_error(self):
        return '密码错误'

    def account_center_page_operation_done(self):
        return '操作成功'

    def account_center_page_message_center_text(self):
        return '消息中心'

    def account_center_page_no_data_text(self):
        return '暂无数据'

    def account_center_page_virtual_account_manager(self):
        return '虚拟账号管理'

    def account_center_page_alarm_manager_text(self):
        return ' 报警管理'

    def account_center_page_statistical_form_text(self):
        return '统计报表'

    def account_center_page_sport_overview_text(self):
        return '运动总览'

    def account_center_page_area_alarm_text(self):
        return '区域预警'

    def account_center_page_all_dev_text(self):
        return '全部设备'

    def account_center_page_issued_command_manager(self):
        return '下发指令管理'

    def account_center_page_mark_point_text(self):
        return '标注点'

    def account_center_page_alarm_details_text(self):
        return '告警详情'

    def account_center_page_expiring_text(self):
        return '平台即将过期'

    def account_center_page_expire_status_text(self):
        return '过期状态'

    def account_center_page_expired_text(self):
        return '平台已过期'

    def account_center_page_actived_text(self):
        return '已激活'

    def account_center_page_active_status_text(self):
        return '激活状态'

    def account_center_page_activing_text(self):
        return '未激活'

    def account_center_page_password_len_text(self):
        return '密码长度至少6位以上'

    def account_center_page_password_unlike(self):
        return '两次输入的密码不一致'

    def account_center_page_password_formart_text(self):
        return '密码格式错误，必须为字母和数字的组合'

    def account_center_page_account_exist(self):
        return '账号已存在'

    def command_manager_page_command_type(self):
        return '指令类型'

    def command_manager_page_work_type_template_management(self):
        return '工作模式模板管理'

    def command_manager_page_new_command_text(self):
        return '新建自定义指令'

    def command_manager_page_ensure_text(self):
        return '确定'

    def command_manager_page_work_type_task_manager_text(self):
        return '工作模式任务管理'

    def command_manager_page_issued_work_type(self):
        return '下发工作模式'

    def command_manager_page_issued_work_look_type(self):
        return '下发工作模式查看'

    def command_manager_page_issued_command_task(self):
        return '下发指令任务'

    def command_manager_page_issued_command_manager(self):
        return '下发指令管理'

    def command_manager_page_template_name(self):
        return '模板名称'

    def command_manager_page_not_null(self):
        return '该项不能为空'

    def command_manager_page_must_be_integer(self):
        return '该项只能填写正整数'

    def command_manager_page_must_than_90(self):
        return '该项不能大于90'

    def command_manager_page_must_than_15(self):
        return '该项不能大于15'

    def cust_page_are_you_reset_this_password(self):
        return '您确定要重置密码？'

    def cust_page_user_name_not_null(self):
        return '用户名不能为空'

    def cust_page_user_name_more_than_3(self):
        # return '昵称长度至少3位'
        return '用户名称至少3位'

    def cust_page_user_account_not_null(self):
        return '账号不能为空'

    def cust_page_user_account_len(self):
        return '账号长度至少3位、不超过30位字符'

    def cust_page_user_password_not_null(self):
        # return '请输入密码'
        return "密码不能为空"

    def cust_page_user_password_len(self):
        return '密码长度不能小于6位'

    def cust_page_user_password_formate(self):
        return '密码格式错误，必须为字母和数字的组合'

    def cust_page_password_unlike(self):
        return '两次输入的密码不一致'

    def cust_page_user_email_formate_error(self):
        return '邮箱格式不正确'

    def dev_page_track_replay_text(self):
        return '轨迹回放'

    def dev_page_driving_record_text(self):
        return '行车记录'

    def dev_page_track_preset_text(self):
        return '实时跟踪'

    def dev_page_fail_text(self):
        return '失败'

    def dev_page_repetition_text(self):
        return '重复'

    def dev_page_inexistence_text(self):
        return '不存在'

    def dev_page_closing_down(self):
        return '停机'

    def dev_page_starting_up(self):
        return '开机'

    def glob_search_page_search_dev_text(self):
        return 'IMEI/设备名称'

    def glob_search_page_search_account_text(self):
        return '请输入客户名称/账号'

    def glob_search_please_add_dev_text(self):
        return '请添加设备'

    def glob_search_please_add_account_text(self):
        return '请选择用户'

    def glob_search_page_date_formate_error(self):
        return '日期不符合格式，请重新选择。'

    def glob_search_page_text(self, type):
        if type == 'imei':
            return '请输入IMEI号'
        elif type == '车牌号':
            return '请输入车牌号'
        elif type == 'sn':
            return '请输入SN'
        elif type == '车架号':
            return '请输入车架号'
        elif type == 'sim':
            return '请输入SIM卡号'
        elif type == 'name':
            return '请输入设备名称'

    def safe_area_page_edit_text(self):
        return '编辑'

    def safe_area_page_geo_fence(self):
        return '平台围栏'

    def safe_area_page_black_car_address_text(self):
        return '黑车地址库'

    def safe_area_page_choose_delete_content(self):
        return '请选择要删除的记录!'

    def safe_area_page_map_text(self):
        return '请在地图上单击左键开始绘制，双击完成'

    def statistical_form_page_alarm_overview(self):
        return '告警总览'

    def statistical_form_electric_report(self):
        return '电量统计'

    def statistical_form_mile_form(self):
        return '里程报表'

    def statistical_form_sport_overview_form(self):
        return '运动总览'

    def statistical_form_tracl_form(self):
        return '行程报表'

    def statistical_form_over_speed_form(self):
        return '超速报表'

    def statistical_form_stay_form(self):
        return '停留报表'

    def statistical_form_stay_not_shut_down(self):
        return '停车未熄火报表'

    def statistical_form_acc_form(self):
        return 'ACC报表'

    def statistical_form_guide_machine_report(self):
        return '导游播报统计'

    def statistical_form_oil_form(self):
        return '油感报表'

    def statistical_form_on_line_form(self):
        return '在线统计'

    def statistical_form_off_line_form(self):
        return '离线统计'

    def statistical_form_date_formate(self):
        return '必须是正整数！'

    def statistical_form_page_static_report_text(self):
        return '静止报表'

    def cust_page_user_name_more_than_3s(self):
        return '昵称长度至少3位'

    def cust_page_user_password_not_nulls(self):
        return '请输入密码'

    def feedback_page_error_content(self):
        return '请输入描述内容'

    def feedback_page_error_contact(self):
        return '请输入联系人'

    def feedback_page_error_phone(self):
        return '请输入联系电话'

    def feedback_page_error_contents(self):
        return '描述内容不能超过2000个字符'

    def feedback_page_error_contacts(self):
        return '联系人不能超过100个字符'

    def feedback_page_error_phones(self):
        return '联系电话格式不正确'

    def feedback_page_error_phoness(self):
        return '联系电话长度不正确'

    def feedback_page_ensuer_succeed_text(self):
        return '感谢你的反馈意见'

    def batch_sale_text(self):
        return '批量销售'

    def per_20_page(self):
        return '每页20条'

    def text_with_abnormal_dev_send_command(self, state):
        if state == '停机':
            return '停机'
        if state == '用户到期':
            return '用户到期'
        if state == '平台到期':
            return '平台到期'
        if state == '不支持':
            return '不支持'
        if state == '停机+用户到期':
            return '停机'
        if state == '停机+平台到期':
            return '平台到期'
        if state == '停机+不支持':
            return '不支持'
        if state == '用户到期+平台到期':
            return '平台到期'
        if state == '用户到期+不支持':
            return '不支持'
        if state == '平台到期+不支持':
            return '不支持'
        if state == '停机+用户到期+平台到期':
            return '平台到期'
        if state == '停机+用户到期+不支持':
            return '不支持'
        if state == '停机+平台到期+不支持':
            return '不支持'
        if state == '用户到期+平台到期+不支持':
            return '不支持'
        if state == '平台到期+用户到期+停机+不支持':
            return '不支持'

    def no_authority_text(self):
        return '没有权限'

    def select_issued_command_text(self):
        return '选中发送指令'

    def all_issued_command_text(self):
        return '本次查询全部发送指令'

    def select_issued_work_type_text(self):
        return '选中设置工作模式'

    def all_issued_work_type_text(self):
        return '本次查询全部设置工作模式'

    def no_login_authority_text(self):
        return '没有权限登录'

    def please_select_text(self):
        return '请选择'

    def the_selected_user_cannot_be_the_superior(self):
        return '选择的客户不能作为上级'

    def batch_set_user_overdue_time_text(self):
        return '批量设置用户到期'

    def glob_search_page_search_account_texts(self):
        return '请输入客户名称/账号/IMEI'

    def dev_total_mileage_text1(self):
        return '必须为数字(最多保留两位小数)'

    def dev_total_mileage_text2(self):
        return '必须在0 ~ 9999999.99之间'

    def dev_type_is_different(self):
        return '所选设备的设备类型不一致，不能发送指令'

    def no_dev_to_issued_command(self):
        return '没有可发送指令的设备'

    def account_center_page_no_data_texts(self):
        return '暂无数据'

    def user_name_not_null(self):
        return '用户名不能为空'

    def user_name_not_to_long(self):
        return '用户名称不超过50位'

    def user_email_format_error(self):
        return '邮箱格式不正确'

    def user_name_not_to_shot(self):
        return '用户名称至少3位'
