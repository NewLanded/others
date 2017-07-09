#coding:gb18030
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import datetime,time,re,urllib2,gevent
from lxml import etree
import mydb

class LGW:
    def __init__(self):
        self.file = r'E:\jobInfo.txt'
        self.firstPage = True
        browser = webdriver.Chrome()
        browser.get("http://www.lagou.com/")
        element = browser.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a')  #ѡȡ������
        element.send_keys(Keys.RETURN)
        element = browser.find_element_by_xpath('//*[@id="search_input"]')  #Ѱ��������
        element.send_keys("����".decode('gbk'))  #���������ݼ���
        element.send_keys(Keys.RETURN)
        self.browser = browser

    #�ж��Ƿ��ǵ�һҳ
    def ifFirstPage(self):
        return self.firstPage
    #��һҳ״̬��ֵ
    def setFirstPage(self,state):
        self.firstPage = state

    #��ȡĳ��ְλ�ܵ�ҳ����
    def getTotalPageNum(self):
        browser = self.browser
        pageCode = etree.HTML(browser.page_source)  #��ȡҳ�����
        totalPageNumObject = pageCode.xpath('//*[@id="s_position_list"]/div[2]/div/span[last()-1]/text()')
        totalPageNum = int(re.search(r'\d+',str(totalPageNumObject[0])).group())  #��ȡ����������ҳ��
        return totalPageNum
    #��ҳ�����ְλ��url�����б���
    def getJobList(self,browser):
        pageCode = etree.HTML(browser.page_source)  #��ȡҳ�����
        jobHref = pageCode.xpath('/html/body/div[@id="content-container"]/div[@id="main_container"]/div[@class="content_left"]/div[@id="s_position_list"]/ul[@class="item_con_list"]/li//div[@class="p_top"]//a/@href') #��ȡÿҳְλurl
        return jobHref
    #��ȡĳ����˾��ְλ�ľ�����Ϣ
    def getJobInfo(self,href):
        f = open(self.file,'a')
        print href+'\n'
        page = urllib2.urlopen(href,timeout = 35).read().decode('utf-8').encode('gb18030')  #��ȡҳ�����
        jobPageCode = etree.HTML(page.decode('gb18030'))
    
        companyName = jobPageCode.xpath('//h2[@class="fl"]/text()')[0].replace(' ','').replace('\n','').encode('gb18030')  #��ȡ��˾����
        jobBasicInformation = ' '.join(jobPageCode.xpath('//div[@id="container"]//dd[@class="job_request"]/p/span/text()')).encode('gb18030')  #��ȡְλ������Ϣ
        jobAttract = jobPageCode.xpath('//div[@id="container"]//dd[@class="job_request"]/p[2]/text()')[0].encode('gb18030')  #��ȡְλ����
            
        jobDescriptionUnform = re.search(r'(<h3 class="description">ְλ����</h3>)(.*?)(</p>.....</dd>|</dd>)',page,re.S).group()  #��ȡְλ����
        jobDescription = re.sub(r'<.*?>','',jobDescriptionUnform).replace('&nbsp;','').replace(' ','') #ְλ������ʽ��
            
        print companyName
        print jobBasicInformation
        print jobAttract
        print jobDescription

        f.write(companyName+'\n'+jobBasicInformation+'\n'+jobAttract+'\n'+jobDescription+'\n\n')  #ְλ��Ϣд���ļ�
        f.close()
        
        #�������ݿ�
#        query = {"companyName":companyName,"jobBasicInformation":jobBasicInformation,"jobAttract":jobAttract,"jobDescription":jobDescription}
        companyName = companyName.decode('gb18030').encode('utf-8')
        jobBasicInformation = jobBasicInformation.decode('gb18030').encode('utf-8')
        jobAttract= jobAttract.decode('gb18030').encode('utf-8')
        jobDescription = jobDescription.decode('gb18030').encode('utf-8')
        
#        query = {"companyName":companyName,"jobBasicInformation":jobBasicInformation,"jobAttract":jobAttract,"jobDescription":jobDescription}
        sql = "insert into jobinfo values('','"+ companyName +"','"+ jobBasicInformation +"','"+ jobAttract +"','"+ jobDescription +"');"

#        mydb.insertDb(query)
        mydb.insertMySQLDb(sql)
    #�����һҳ
    def clickNextPage(self):
        browser = self.browser
        element = browser.find_element_by_xpath('//*[@id="s_position_list"]/div[2]/div/span[last()]') #��ȡ��һҳ
        element.click()
    #�����sleep�Ļ����Ὣ��һҳ��browser��Ϣ���أ�Ŀǰ�������Ϊʲô
        time.sleep(2)
        return browser
    #��ÿҳ��url���з���������
    def asynchronous(self,browser):
        threads = []
        jobHref = self.getJobList(browser)
        for href in jobHref:
            threads.append(gevent.spawn(self.getJobInfo,href))
        gevent.joinall(threads)
    #��ʼ
    def start(self):
        totalPageNum = self.getTotalPageNum()
        for i in range(totalPageNum-1):
            if self.ifFirstPage():
                self.asynchronous(self.browser)
                self.setFirstPage(False)
            browser = self.clickNextPage()
            self.asynchronous(browser)
            
    #����
#    def judgeRepeat(self):
        

lgw = LGW()
lgw.start()

