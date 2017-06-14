import requests

# 接口测试
# 参数化
playload = {
    'electricity': 100,
    'mcType': '',
    'containSubordinate': 0,
    'userId': 12875,
    'pageNo': 1,
    'pageSize': 10
}
# 定制请求头 携带cookie
headers = {
    'Cookie': 'JSESSIONID=0F3EDD7A72D86C3521C3F80F5719140B'
}
# request库提交post请求，其中包含请求参数，请求头
r = requests.post('http://tuqiangol.com/electricityReportController/list', params=playload, headers=headers)
# 请求的url
print(r.url)
# 响应正文
print(r.text)
# 获取相应的数据，evel为强制把字符串转换为字典类型
# 获取相应的json格式
print(r.json())
# 获取响应的状态码
print(r.status_code)
