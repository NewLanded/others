# coding:utf-8
import datetime, time, re, urllib2, sys
from lxml import etree
import lxml
from DB import novelDb
import chardet
from LOG.logger import Logger


# 获取笔趣阁中小说目录及内容，需传入小说页面url      django-crontab
class Novel:
    def __init__(self):
        self.retryFaildList = []
        self.logger = Logger(logname='/root/Log/spider/novel.log', loglevel=1, logger="novel").getlog()

    # 获取url内容
    def getUrlText(self, url):
        try:
            page = urllib2.urlopen(url, timeout=30).read()
            return page
        except (urllib2.HTTPError, urllib2.URLError):
            try:
                page = urllib2.urlopen(url, timeout=30).read()
                return page
            except Exception, e:
                self.logger.error(url)
                self.logger.error(e)
                return 0
        except Exception, e:
            self.logger.error(url)
            self.logger.error(e)
            return 0

    # lxml.etree实例化
    def etreeReturn(self, page, url):
        try:
            PageCode = etree.HTML(page)
            return PageCode
        except lxml.etree.XMLSyntaxError:  # lxml.etree.XMLSyntaxError: line 58: htmlParseEntityRef: expecting ';'
            page = self.getUrlText(url)
            if page == 0:
                return 0
            try:
                PageCode = etree.HTML(page)
                return PageCode
            except Exception, e:
                self.logger.error(url)
                self.logger.error(e)
                return 0
        except Exception, e:
            self.logger.error(url)
            self.logger.error(e)
            return 0

    # 插入数据库失败后行为
    def insertFaildAction(self, actionFunction, *args):
        result = actionFunction(*args)

    # 获取小说的标题及章节url
    def getTotalChapters(self, url):
        page = self.getUrlText(url)
        if page == 0:
            sys.exit()
        PageCode = self.etreeReturn(page, url)
        if PageCode == 0:
            sys.exit()
        try:
            novelName = PageCode.xpath('//*[@id="info"]/h1')[0].text.encode('utf-8')  # 获取小说名称
            self.logger.info('开始爬取'+ novelName + url)
            novelauthor = PageCode.xpath('//*[@id="info"]/p[1]')[0].text.encode('utf-8')  # 获取小说作者

            novelUrl = url  # 获取小说地址
            workdate = time.strftime('%Y%m%d', time.localtime())  # 工作日期
            worktime = time.strftime('%H%M%S', time.localtime())  # 工作时间
            chaptersUrls = []
            chaptersUrl_original = PageCode.xpath('//*[@id="list"]/dl//a/@href ')  # 获取小说章节的url
            for i in chaptersUrl_original:
                chaptersUrls.append(url + i)
            self.logger.error(novelName+'  小说共有'+str(len(chaptersUrls))+'章')
        except Exception,e:
            self.logger.error(e)
            sys.exit()
        return novelName, novelauthor, workdate, worktime, novelUrl, chaptersUrls

    # 获取数据库中这本小说的id，若这本小说不存在，状态返回0
    def getExistNovelId(self, novelName):
        sql = 'select id from novel_novel where novelname = "' + novelName + '";'
        self.logger.info('获取数据库中当前小说的id  '+sql)
        result = novelDb.queryDb(sql)
        if result[0] == 0:
            # 做点什么呢？
            return 0
        elif result[0] == 2:
            return 0
        else:
            return result[3][0][0]

    # 获取数据库中这本小说的总章节数量
    def getExistClapterNum(self, novelId):
        sql = 'select count(1) from novel_novel_detail where novel_id = ' + str(novelId) + ';'
        result = novelDb.queryDb(sql)
        if result[0] == 0:
            # 做点什么呢？
            return 0
        elif result[0] == 2:
            return 0
        else:
            self.logger.info('数据库中当前小说的章节数  ' + str(result[3][0][0]))
            return result[3][0][0]

    # 将数据库取出的章节总数与从笔趣阁获取的章节总数作比较，以判断是否更新数据库及获取更新的url
    def compareChapterNum(self, chaptersNum, dbChaptersNum, chaptersUrls):
        num = chaptersNum - dbChaptersNum
        chaptersUrls = chaptersUrls[len(chaptersUrls) - num:]
        return chaptersUrls

    # 将小说信息存入数据库
    def storeInfoToMysql(self, novelName, novelauthor, workdate, worktime, novelUrl):
        sql = 'insert into novel_novel (novelname,author,workdate,worktime,url) values("' + novelName + '","' + novelauthor + '","' + workdate + '","' + worktime + '","' + novelUrl + '");'
        result = novelDb.insertMySQLDb(sql)
        return result

    # 将获取的小说内容存入数据库
    def storeTextToMysql(self, novelId, novelchapter, chapterText):
        sql = 'insert into novel_novel_detail (novel_id,chapter_name,chapter_text) values(' + str(
            novelId) + ',"' + novelchapter + '","' + chapterText + '");'
        result = novelDb.insertMySQLDb(sql)
        time.sleep(1)  # 没有使用代理，避免被封
        return result

    # 依据url获取小说章节内容
    def getChapterText(self, chaptersUrl):
        self.logger.info(chaptersUrl)
        page = self.getUrlText(chaptersUrl)
        if page == 0:
            self.retryFaildList.append(chaptersUrl)
            return 0, 0
        PageCode = self.etreeReturn(page, chaptersUrl)
        if PageCode == 0:
            self.retryFaildList.append(chaptersUrl)
            return 0, 0
        chapter_name = PageCode.xpath(r'//*[@class="bookname"]/h1')[0].text.encode('utf-8')
        chapter_text_original = PageCode.xpath('//*[@id="content"]/text()')
        chapter_text = ''
        for i in chapter_text_original:
            chapter_text += i.replace('&nbsp;', '').replace(';', '').replace('"', '').encode('utf-8')  # 这些特殊字符好2
        return chapter_name, chapter_text

    # 开始函数
    def start(self, url):
        novelName, novelauthor, workdate, worktime, novelUrl, chaptersUrls = self.getTotalChapters(url)
        novelId = self.getExistNovelId(novelName)
        if novelId == 0:  # 数据库中没有这本书的信息
            result = self.storeInfoToMysql(novelName, novelauthor, workdate, worktime, novelUrl)
            if result[0] != 1:
                sys.exit(1)
            novelId = self.getExistNovelId(novelName)  # 插入数据库后要重新获取novelId，否则是0
            for chaptersUrl in chaptersUrls:  #将小说正文插入数据库
                chapter_name, chapter_text = self.getChapterText(chaptersUrl)  # 循环url获取章节内容
                if chapter_name == 0:
                    self.logger.error(chaptersUrl + '11111111111111111111111111111111111111111111111111111')
                    self.insertFaildAction(self.storeTextToMysql, novelId, 'faild', chaptersUrl)
                    continue
                result = self.storeTextToMysql(novelId, chapter_name, chapter_text)
                if result[0] != 1:
                    self.logger.error(chaptersUrl + '2222222222222222222222222222222222222222222222222222')
                    self.logger.error(result[1])
                    self.insertFaildAction(self.storeTextToMysql, novelId, 'faild', chaptersUrl)
            self.logger.info('小说爬取结束')

        else:  # 数据库中有这本书的信息
            totalNum = self.getExistClapterNum(novelId)
            chaptersUrls = self.compareChapterNum(len(chaptersUrls), totalNum,
                                                  chaptersUrls)  # 在chaptersUrls中删除数据库中已存在的章节url
            for chaptersUrl in chaptersUrls:  #将小说正文插入数据库
                chapter_name, chapter_text = self.getChapterText(chaptersUrl)
                if chapter_name == 0:
                    self.logger.error(chaptersUrl + '333333333333333333333333333333333333333333333333333333')
                    self.insertFaildAction(self.storeTextToMysql, novelId, 'faild', chaptersUrl)
                    continue
                result = self.storeTextToMysql(novelId, chapter_name, chapter_text)
                if result[0] != 1:
                    self.logger.error(chaptersUrl + '444444444444444444444444444444444444444444444444444444')
                    self.logger.error(result[1])
                    self.insertFaildAction(self.storeTextToMysql, novelId, 'faild', chaptersUrl)
            self.logger.info('小说爬取结束')


#novel = Novel()
# novel.start('http://www.biquge.la/book/168/')
# novel.start('http://www.biquge.la/book/285/')
#novel.start('http://www.biquku.com/0/761/')

