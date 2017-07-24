import datetime
import robot
import redis

print((datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H") + ':00')
r = robot.get_version()
print(r)
re = redis.Redis()
re.set('name', 'zhangsan')
re.mget('', '')
re.setex('', '', '')
re.psetex('', '', '')
re.getrange('', '', '')
re.setrange('', '', '')
re.setbit('', '', '')
re.bitcount('', '')
re.strlen('')
re.incr('')
re.incrbyfloat('')
re.hset('', '', '')
re.hget('', '')
re.hgetall('')
re.brpoplpush('', '')
