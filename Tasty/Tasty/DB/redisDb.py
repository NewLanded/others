#coding:utf-8

import redis

def redisHandle():
        pool = redis.ConnectionPool(host='115.28.6.1', password='ijeYKN#kd#iPLkdtwWdskf', port=6379, db=0)
        handle = redis.StrictRedis(connection_pool=pool)
        return handle