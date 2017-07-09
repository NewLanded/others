# -*- coding: utf-8 -*-
import scrapy
import time

from baidu_tieba.items import BaiduTiebaItem



DEBUG = False

class TiebaSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["baidu.com"]

    def start_requests(self):
        start_url = 'http://tieba.baidu.com/f?kw=lx7&fr=index'
        yield scrapy.Request(start_url,meta={})

    def parse(self, response):
        global DEBUG

        #for sel in response.xpath('//*[@id="thread_list"]'):
        # 获取帖子链接
        tiezi_urls = response.xpath('//a[@class="j_th_tit "]/@href').extract()
        for tiezi_url in tiezi_urls:
            tiezi_url = 'http://tieba.baidu.com' + tiezi_url
            time.sleep(5)
            yield scrapy.Request(tiezi_url, callback=self.tiezi_parse, meta={})

        try:  # 下一页，没有下一页就返回
            next_page = response.xpath('//*[@id="frs_list_pager"]/a[@class="next pagination-item "]/@href').extract()[0]
        except Exception,e:
            print e
            return 

        yield scrapy.Request(next_page, callback=self.parse,meta={})

    def tiezi_parse(self, response):
        global DEBUG
        for sel in response.xpath('//*[@id="j_p_postlist"]'):
            text = sel.xpath('//*[@class="d_post_content j_d_post_content  clearfix"]/text()').extract()[0]
            yield BaiduTiebaItem(name='tiezi', content=text, context='')

        
        
