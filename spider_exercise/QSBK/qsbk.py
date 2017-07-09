#coding:gbk
import re,urllib2
import gevent
from gevent import monkey

monkey.patch_all()

class QSBK:
#定义环境变量
    def __init__(self):
        self.url_part = r'http://www.qiushibaike.com/hot/page/'
        self.url_list = [self.url_part+str(i+1) for i in range(10) ]  #定义所要爬取的页面
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent':self.user_agent}

#爬取数据
    def getPage(self,url):
        try:
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request,timeout=5)
            pageCode = response.read().decode('utf-8')
#            print url
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print "连接糗事百科失败： ",e.code
            if hasattr(e,"reason"):
                print "连接糗事百科失败： ",e.reason
            else:
                print e

#正则处理数据
    def getPageItems(self,url):
        pageStories = []
        pageCode = self.getPage(url)
        if not pageCode:
            print '连接糗事百科失败'
            return None
        pattern = re.compile(r'<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>(.*?)<div class="stats">',re.S) #/1是作者，/2是内容，/3包含图片链接
        items = re.findall(pattern,pageCode)
        for item in items:
            if not re.search(r'img',item[2]):  #选取没有图片的段子
                item_data = re.sub(r'<br/>','\n',item[1])
                pageStories.append([item[0],item_data])
        return pageStories

#写入文件
    def writePage(self,url):
        pageStories = self.getPageItems(url)
        file = r'E:\qsbk.txt'
        with open(file,'a') as f:
            f.write('Page:%s' %(url[-1])) #标识页码
            for data in pageStories:
                f.write(data[1].encode('utf-8'))
#协程阻塞执行函数
    def asynchronous(self):
        threads = []  #greenlet列表存放容器
        for url in self.url_list:
            threads.append(gevent.spawn(self.writePage,url))
        gevent.joinall(threads)  #joinall函数阻塞当前流程并执行给定的greenlet
#开始方法
    def start(self):
        self.asynchronous()
    

qsbk = QSBK()
qsbk.start()
        



