# coding:utf-8
from django.db import models

# Create your models here.
'''
关系型数据库设计
客户信息表
                客户号id        姓名             性别    昵称    客户级别            状态              手机号    邮箱        服务类别 创建时间
0000000001    00000000001      liyanbin     0(男)1(女)  yanbin    1         0(不可用) 1(正常)2(注销)   123      123@qq.com


服务类别对应表
服务类别id  服务名称   服务表  服务主页


客户服务开通表
服务类别id  客户id   客户开通服务id

'''

'''
redis设计
客户信息表
                userId          name           sex      nickname   userLevel       status             phoneNum   emailNum        serviceInfo                                               createTime
  key           客户号id        姓名             性别    昵称    客户级别            状态              手机号    邮箱        服务类别id及服务id（服务id举例为：小说服务下的某几本小说的id） 创建时间
0000000001    00000000001      liyanbin     0(男)1(女)  yanbin    1         0(不可用) 1(正常)2(注销)   123      123@qq.com   '{"1":"1-2-3","2":"1-2-3"}'
hmset 0000000001 userId 00000000001 name liyanbin sex 0 nickname 艳彬 userLevel 1 status 1 phoneNum 123 emailNum 123@qq.com serviceInfo '{"1":"1-2-3","2":"1-2-3"}' createTime 20160920121212


服务类别对应表
                 serviceId   serviceName  serviceTable  serviceIndexPage
key            服务类别id  服务名称   服务表    服务主页
serviceClass      1           小说      novel     novel/novelList.html
                  2           拉勾网    job       job/jobList.html
hset serviceClass 1 '{"serviceName":"小说","serviceTable":"novel","serviceIndexPage":"novel/novelList.html"}'
hset serviceClass 2 '{"serviceName":"拉勾网","serviceTable":"job","serviceIndexPage":"job/jobList.html"}'



用户表
key
userLoginInfo
键                             值
username     '{"password":"123456","userId":"0000000001"}'
hset userLoginInfo liyanbin '{"password":"123456","userId":"0000000001"}'


插入数据举例
import redis
pool = redis.ConnectionPool(host='115.28.6.1', password='123456',port=6379, db=0)
r = redis.StrictRedis(connection_pool = pool)
r.hset('02','service','{"1":"1-2-3-4","2":"1-2-3-4"}')  -----必须外面是单引号，否则hget出的数据不能被json解析

取出数据
a = r.hget('02','service')
b = json.loads(a)
'''