class ChangeData(object):
    # 为了切换测试和线上环境准备
    def switch_tuqiang_url(self):
        # 测试
        # return 'http://172.16.0.116:8690'
        return 'http://tujunsat.jimicloud.com'

        # 线上
        # return 'http://120.76.232.176:8180'
        # return 'http://www.tuqiangol.com'

        # 天眼在线测试
        # return 'http://www.skyzaixian.com:8680'
        # 天眼在线线上
        # return 'http://www.skyzaixian.com'
