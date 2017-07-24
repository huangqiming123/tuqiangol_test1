import redis

re = redis.Redis(host='127.0.0.1', port=6379, db=0)
re.set('name', 'zhangsan')
print(re.get('name'))

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name1', 'lisi')
print(r.get('name1'))

pipe = r.pipeline(transaction=True)
r.set('name', 'zhangao')
r.set('name', 'zhangwu')
pipe.execute()
print(r.get('name'))
