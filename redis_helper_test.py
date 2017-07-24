from redis_helper import RedisHelper

obj = RedisHelper()
obj.publish('hello world')

obj2 = RedisHelper()
redis_sub = obj2.subscribe()

msg = redis_sub.parse_response()
print(msg)
