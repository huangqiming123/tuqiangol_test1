import requests

# 接口测试
# 参数化
playload = {
    'status': '1,10,11,12,128,13,14,15,16,17,18,19,192,194,195,2,22,23,3,4,5,6,9,90,ACC_OFF,ACC_ON,in,offline,out,sensitiveAreasFence,stayAlert,stayTimeIn,stayTimeOut',
    'imei': '868120145233604,121201234567000',
    'userId': 12875,
    'startTime': '2017-06-01 00:00',
    'endTime': '2017-06-15 09:12'
}
# 定制请求头 携带cookie
headers = {
    'Cookie': 'JSESSIONID=DA4D4C232AE4097C30F48D9000642050'
}
# request库提交post请求，其中包含请求参数，请求头
r = requests.post('http://tuqiangol.com/alarmInfo/getAlarmReport', params=playload, headers=headers)
# 请求的url
print(r.url)
# 响应正文
print(r.text)
# 获取相应的数据，evel为强制把字符串转换为字典类型
# 获取响应的状态码
print(r.status_code)
