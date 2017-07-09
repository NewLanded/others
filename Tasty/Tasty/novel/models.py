# coding:utf-8
from django.db import models

# Create your models here.

class Novel(models.Model):
    novelname = models.CharField(max_length=60, verbose_name=u'小说名称')
    author = models.CharField(max_length=100, verbose_name=u'小说作者')
    # workdate = models.DateTimeField(auto_created=True, auto_now=True, verbose_name=u'收录时间')
    workdate = models.CharField(max_length=8, verbose_name=u'收录时间')
    worktime = models.CharField(max_length=6, null=True, verbose_name=u'收录时间')
    url = models.URLField(verbose_name=u'收录地址')
    ext1 = models.TextField()
    ext2 = models.TextField()

    def __unicode__(self):
        return u'%s:%s' %(self.id,self.novelname)



class Novel_detail(models.Model):
    novel_id = models.CharField(max_length=10, verbose_name=u'小说id')
    chapter_name = models.CharField(max_length=200, verbose_name=u'章节名称')
    chapter_text = models.TextField(verbose_name=u'章节内容')

    def __unicode__(self):
        return u'%s:%s' %(self.id,self.chapter_name)


