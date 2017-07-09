# coding:utf-8
from django.db import models

# Create your models here.

class Job_info(models.Model):
    companyName = models.CharField(max_length=100, verbose_name=u'公司名称')
    jobBasicInformation = models.TextField(verbose_name=u'职位基本信息', null=True)
    jobAttract = models.TextField(verbose_name=u'职位优势', null=True)
    jobDescription = models.TextField(verbose_name=u'职位描述', null=True)

    def __unicode__(self):
        return self.companyName


