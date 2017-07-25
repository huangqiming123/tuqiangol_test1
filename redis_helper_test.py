import redis

from redis_helper import RedisHelper

'''obj = RedisHelper()
obj.publish('hello world')

obj2 = RedisHelper()
redis_sub = obj2.subscribe()

msg = redis_sub.parse_response()
print(msg)'''
re = redis.Redis(host='127.0.0.1', port=6379)
# 单个设置
re.set('name', 'zhangsan')
print(re.get('name'))
print(re.strlen('name'))
# 批量设置
re.mset(name1='zhangwu', name2='lisi')
print(re.mget('name1', 'name2', 'name3'))

print(re.getrange('name', 1, 3))

re.setrange('name', 2, 'c')
print(re.get('name'))

str = '345'
re.set('name', str)
for i in str:
    print(i, ord(i), bin(ord(i)))

re.setbit('name', 5, 1)
print(re.get('name'))

# 获取相应位置的二进制数
print(re.getbit('name', 4))
re.set('name', '345')
