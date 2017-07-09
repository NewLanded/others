#coding:gbk
import re,urllib2
import gevent
from gevent import monkey

monkey.patch_all()

class QSBK:
#���廷������
    def __init__(self):
        self.url_part = r'http://www.qiushibaike.com/hot/page/'
        self.url_list = [self.url_part+str(i+1) for i in range(10) ]  #������Ҫ��ȡ��ҳ��
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}

#��ȡ����
    def getPage(self,url):
        try:
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request,timeout=5)
            pageCode = response.read().decode('utf-8')
#            print url
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print "�������°ٿ�ʧ�ܣ� ",e.code
            if hasattr(e,"reason"):
                print "�������°ٿ�ʧ�ܣ� ",e.reason
            else:
                print e

#����������
    def getPageItems(self,url):
        pageStories = []
        pageCode = self.getPage(url)
        if not pageCode:
            print '�������°ٿ�ʧ��'
            return None
        pattern = re.compile(r'<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>(.*?)<div class="stats">',re.S) #/1�����ߣ�/2�����ݣ�/3����ͼƬ����
        items = re.findall(pattern,pageCode)
        for item in items:
            if not re.search(r'img',item[2]):  #ѡȡû��ͼƬ�Ķ���
                item_data = re.sub(r'<br/>','\n',item[1])
                pageStories.append([item[0],item_data])
        return pageStories

#д���ļ�
    def writePage(self,url):
        pageStories = self.getPageItems(url)
        file = r'E:\qsbk.txt'
        with open(file,'a') as f:
            f.write('Page:%s' %(url[-1])) #��ʶҳ��
            for data in pageStories:
                f.write(data[1].encode('utf-8'))
#Э������ִ�к���
    def asynchronous(self):
        threads = []  #greenlet�б�������
        for url in self.url_list:
            threads.append(gevent.spawn(self.writePage,url))
        gevent.joinall(threads)  #joinall����������ǰ���̲�ִ�и�����greenlet
#��ʼ����
    def start(self):
        self.asynchronous()
    

qsbk = QSBK()
qsbk.start()
        



