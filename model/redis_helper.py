# -*- coding:utf-8 -*-
import redis


class RedisHelper(object):
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1', port=6379)
        self.channel = 'monitor'

    def publish(self, msg):
        self.__conn.publish(self.channel, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.channel)
        pub.parse_response()
        return pub
