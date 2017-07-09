# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime, time, re, urllib2, gevent
from lxml import etree
from DB.novelDb import insertMySQLDb

#现在selenium调用的是有GUI的chrom浏览器，在linux上暂不支持，放在这里做备份用

class LGW:
    def __init__(self,jobName):
        self.file = r'E:\jobInfo.txt'
        self.firstPage = True
        browser = webdriver.Chrome()
        browser.get("http://www.lagou.com/")
        element = browser.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')  # 选取北京区
        element.send_keys(Keys.RETURN)
        element = browser.find_element_by_xpath('//*[@id="search_input"]')  # 寻找搜索框
        element.send_keys(jobName.decode('gbk'))  # 搜索框内容键入
        element.send_keys(Keys.RETURN)
        self.browser = browser

    # 判断是否是第一页
    def ifFirstPage(self):
        return self.firstPage

    # 第一页状态赋值
    def setFirstPage(self, state):
        self.firstPage = state

    # 获取某个职位总的页面数
    def getTotalPageNum(self):
        browser = self.browser
        pageCode = etree.HTML(browser.page_source)  # 获取页面代码
        totalPageNumObject = pageCode.xpath('//*[@id="s_position_list"]/div[2]/div/span[last()-1]/text()')
        totalPageNum = int(re.search(r'\d+', str(totalPageNumObject[0])).group())  # 获取搜索内容总页数
        return totalPageNum

    # 将页面里的职位的url放入列表中
    def getJobList(self, browser):
        pageCode = etree.HTML(browser.page_source)  # 获取页面代码
        jobHref = pageCode.xpath(
            '/html/body/div[@id="content-container"]/div[@id="main_container"]/div[@class="content_left"]/div[@id="s_position_list"]/ul[@class="item_con_list"]/li//div[@class="p_top"]//a/@href')  # 获取每页职位url
        return jobHref

    # 获取某个公司该职位的具体信息
    def getJobInfo(self, href):
        f = open(self.file, 'a')
        href = 'http:' + href
        print href + '\n'
        href=href.replace(r'//','http://')
        print href + '\n'
        page = urllib2.urlopen(href, timeout=35).read().decode('utf-8').encode('gb18030')  # 获取页面代码
        jobPageCode = etree.HTML(page.decode('gb18030'))

        companyName = jobPageCode.xpath('//h2[@class="fl"]/text()')[0].replace(' ', '').replace('\n', '').encode(
            'gb18030')  # 获取公司名称
        jobBasicInformation = ' '.join(
            jobPageCode.xpath('//div[@id="container"]//dd[@class="job_request"]/p/span/text()')).encode(
            'gb18030')  # 获取职位基本信息
        jobAttract = jobPageCode.xpath('//div[@id="container"]//dd[@class="job_request"]/p[2]/text()')[0].encode(
            'gb18030')  # 获取职位待遇

        jobDescriptionUnform = re.search(r'(<h3 class="description">职位描述</h3>)(.*?)(</p>.....</dd>|</dd>)', page,
                                         re.S).group()  # 获取职位描述
        jobDescription = re.sub(r'<.*?>', '', jobDescriptionUnform).replace('&nbsp;', '').replace(' ', '')  # 职位描述格式化

        print companyName
        print jobBasicInformation
        print jobAttract
        print jobDescription

        f.write(
            companyName + '\n' + jobBasicInformation + '\n' + jobAttract + '\n' + jobDescription + '\n\n')  # 职位信息写入文件
        f.close()

        # 插入数据库
        companyName = companyName.decode('gb18030').encode('utf-8')
        jobBasicInformation = jobBasicInformation.decode('gb18030').encode('utf-8')
        jobAttract = jobAttract.decode('gb18030').encode('utf-8')
        jobDescription = jobDescription.decode('gb18030').encode('utf-8')

        #        query = {"companyName":companyName,"jobBasicInformation":jobBasicInformation,"jobAttract":jobAttract,"jobDescription":jobDescription}
        sql = "insert into job_jobinfo values('','" + companyName + "','" + jobBasicInformation + "','" + jobAttract + "','" + jobDescription + "');"

        #        mydb.insertDb(query)
        insertMySQLDb(sql)

    # 点击下一页
    def clickNextPage(self):
        browser = self.browser
        element = browser.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[last()]')  # 获取下一页
        element.click()
        # 如果不sleep的话，会将上一页的browser信息返回，目前还不清楚为什么
        time.sleep(30)
        return browser

    # 对每页的url进行非阻塞访问
    def asynchronous(self, browser):
        threads = []
        jobHref = self.getJobList(browser)
        for href in jobHref:
            threads.append(gevent.spawn(self.getJobInfo, href))
        gevent.joinall(threads)

    # 开始
    def start(self):
        totalPageNum = self.getTotalPageNum()
        for i in range(totalPageNum - 1):
            if self.ifFirstPage():
                self.asynchronous(self.browser)
                self.setFirstPage(False)
            browser = self.clickNextPage()
            self.asynchronous(browser)

# 判重
# def judgeRepeat(self):


