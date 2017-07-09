#coding:UTF-8

from django.core.mail import send_mail
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import json
from job.models import Job_info

def joblist_app(request):
    companys = Job_info.objects.all()
    company_info = []
    for company in companys:
        company_info.append([company.id, company.companyName])
    return HttpResponse(json.dumps(company_info))

def jobinfo_app(request):
    id=request.POST.get('id')
    job_info = Job_info.objects.get(id=id)
    job_info = {'id':id, 'jobBasicInformation':job_info.jobBasicInformation, 'jobAttract':job_info.jobAttract, 'jobDescription':job_info.jobDescription}
    return HttpResponse(json.dumps(job_info))

'''
def jobList(request):
    companyNames = novelDb.queryDb('SELECT id,companyName FROM job_jobinfo;')[3]
#    cursor = connection.cursor()
#    cursor.execute("""SELECT companyName FROM jobinfo""")
#    companyNames = cursor.fetchall()
#    print companyNames[0][0]
    return render_to_response('jobList.html',{'companyNames':companyNames})


def getJobInfo(request):
    getData = request.POST
    id=getData.get('id')
    selectJobInfo = novelDb.queryDb('SELECT jobBasicInformation,jobAttract,jobDescription FROM job_jobinfo where id='+id+';')[3][0]
    jobInfo = {'id':id,'jobBasicInformation':selectJobInfo[0],'jobAttract':selectJobInfo[1],'jobDescription':selectJobInfo[2]}
    return HttpResponse(json.dumps(jobInfo))


def sendEmail(request):
    getData = request.POST
    id = getData.get('id')
    print id
    print id
    emailAddress = getData.get('emailAddress','l1141041@163.com')
    print emailAddress
    selectJobInfo = novelDb.queryDb('SELECT companyName,jobBasicInformation,jobAttract,jobDescription FROM job_jobinfo where id=' + id + ';')[3][0]
    jobInfo = ''
    for i in selectJobInfo:
        jobInfo = jobInfo+i+'\n'
    send_mail('subject',
              jobInfo,
              'l1141041@163.com',  #发件人
              [emailAddress,], ) #收件人列表
    return HttpResponse('邮件已发送lalala')

def setJob(request):
    return render_to_response('setJobInfo.html')

#暂不支持
def setJobInfo(request):
    getData = request.POST
    jobName = getData.get('jobName',0)
    if jobName:
        lgw = LGW(jobName)
        lgw.start()
        setStatus = 1
        return HttpResponse(json.dumps({'setStatus':setStatus}))
    else:
        setStatus = 0
        return HttpResponse(json.dumps({'setStatus':setStatus}))
'''


