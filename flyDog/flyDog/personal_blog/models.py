# coding:utf-8

from django.db import models

'''
class Author(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return self.name
'''

'''
class Page_struct(models.Model):

    结构表，存储页面展示目录的结构

    这个函数可以将dict的内容分级取出，现在没用了
    def get_catalog(op_dict):
        a = ''
        for i_id,v_dict in op_dict.items():
            a+=str(i_id)
            a+=get_catalog(v_dict)
        return a

    帖子id
    bid = models.IntegerField(default=0)
    结构分类id
    struct_id = models.IntegerField(default=0)
    结构标题
    struct_title = models.CharField(max_length=2048, default="")
    结构体，存储json key是页面的id，value是页面名称
    op_dict = models.CharField(max_length=20480, default="")
    结构体深度，用于展示层级结构
    depth = models.IntegerField()

    def __unicode__(self):
        return self.struct_title
'''
p_type = {
    0:'python',
    1:'JS',
    2:'golang',
    3:'django',
    4:'html/css',
    5:'git',
    6:'book',
    7:'other',
    8:'navigation',
}


class Page_struct(models.Model):
    '''
    结构表，存储页面展示目录的结构
    '''
    title = models.CharField(max_length=2048, default="", verbose_name=u'帖子标题')
    p_type = models.IntegerField(verbose_name=u'帖子类型')
    rel_type = models.IntegerField(verbose_name=u'关联帖子类型')
    p_seq = models.IntegerField(verbose_name=u'显示顺序')

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    '''
    博客信息表
    '''
    # 标题
    title = models.CharField(max_length=2048, default="", verbose_name=u'帖子标题')
    # 帖子素材信息
    body = models.TextField(verbose_name=u'帖子内容')
    p_type = models.IntegerField(verbose_name=u'帖子类型')
    # p_seq = models.IntegerField(verbose_name=u'显示顺序')
    # author = models.ForeignKey(Author)
    # page_struct = models.ForeignKey(Page_struct)
    # 帖子时间信息
    release_time = models.DateTimeField(db_index=True,
                                        auto_created=True,
                                        auto_now=True,
                                        verbose_name=u'发布时间')
    update_time = models.DateTimeField(auto_created=True, auto_now=True, verbose_name=u'更新时间')

    def __unicode__(self):
        return self.title


class Read(models.Model):
    '''
    阅读相关
    '''
    # 帖子id
    bid = models.IntegerField()
    # 阅读量
    total = models.IntegerField(default="1")

    def __unicode__(self):
        return self.tid













