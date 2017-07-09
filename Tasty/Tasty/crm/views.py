#coding:utf-8

from django.http import HttpResponse
import json
from DB.redisDb import redisHandle

redisHandle = redisHandle()

def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)

    userLoginInfo = redisHandle.hget('userLoginInfo', username)
    if userLoginInfo == None:
        data = {'returnStatus': '000001'}
        return HttpResponse(json.dumps(data))

    userLoginInfo = json.loads(userLoginInfo)
    if userLoginInfo['password'] == password:
        userId = userLoginInfo['userId']
        services = []
        userInfo = json.loads(redisHandle.hget(userId,'serviceInfo'))
        for serviceId in userInfo:
            serviceInfo = json.loads(redisHandle.hget('serviceClass',serviceId))
            serviceInfo.pop('serviceTable')
            serviceInfo['serviceId'] = serviceId
            services.append(serviceInfo)
        data = {'returnStatus':'000000','userId':userId,'services':services}
        return HttpResponse(json.dumps(data))
    else:
        data = {'returnStatus': '000001'}
        return HttpResponse(json.dumps(data))
'''
    data = {'returnStatus':'000000','userId':'1','services':[{'serviceId':1,'servicePath':'novel/novelList.html','serviceName':'小说1'},{'serviceId':2,'servicePath':'job/jobList.html','serviceName':'拉钩'}]}
    return HttpResponse(json.dumps(data))
'''


