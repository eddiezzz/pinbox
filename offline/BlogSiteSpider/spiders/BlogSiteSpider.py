#!/usr/bin/python2.7
#coding=utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from ..items import SiteLinkItem
from BlogrollExtractor import BlogrollExtractor
import re,sys
from ..storage.MysqlHelper import MysqlHelper

#reload(sys)
#sys.setdefaultencoding('utf8')

class BlogSiteSpider(BaseSpider):
    name = "BlogSiteSpider"
    #allowed_domains = ['coolshell.cn']
    start_urls = [
        'http://coolshell.cn',
        ]
    total_cnt = 0
    cnt_constrain = 2000
    extractor = BlogrollExtractor()
    crawled_dict = {}
    
    def print_detail(self):
        self.log('spider over, print detail:')
        for key in crawled_dict.keys():
            self.log("url:%s, rank:%d" % (key, crawled_dict[key]))

    def is_enough(self):
        self.total_cnt = self.total_cnt + 1
        if self.total_cnt > self.cnt_constrain:
            self.log("total_cnt:%d, exit" % self.total_cnt)
            return True
        return False

    def is_duplicate(self, url):
        if url in self.crawled_dict.keys():
            self.crawled_dict[url] += 1 
            return True
        if [url+'/blog'] in self.crawled_dict.keys():
            self.crawled_dict[url] += 1 
            return True
        if ('/blog' in url) and (len(url) > len('/blog')) and (url.split('/blog')[0] in self.crawled_dict.keys()):
            self.crawled_dict[url] += 1 
            return True
        self.crawled_dict[url] = 1
        return False

    def parse(self, response):
        enough = self.is_enough()

        fpage = open('./pages/%s' % response.url.split('/')[2], 'w')
        fpage.write(response.body)
        fpage.close()

        items =  self.extractor.extract(response.body, response.url)
        if len(items) <= 0:
            self.log('no blogroll in url:%s' % (response.url.split('/')[2]))
            return
        self.log('got %d blogroll in url:%s' % (len(items), response.url.split('/')[2]))

        for name_url in items:
            item = SiteLinkItem()
            #print "parse get name_url:", name_url
            item['name'] = name_url[0]
            item['url'] = name_url[1]
            if self.is_duplicate(item['url']):
                continue
            if not enough:
                yield Request(item['url'])
            yield item

    def __del__(self):
        dbname = 'pinbox'
        username = 'root'
        password = 'hello1234'
        tbname = 'table_site_weight'
        storage = MysqlHelper(username=username, password=password)
        if not storage.connect(dbname):
            self.log('stop_spider connect to dbname:%s error' % dbname)
            return
        self.log('stop_spider connect to dbname:%s succ, start to write %d url to table:%s' % (dbname, len(self.crawled_dict.keys()), tbname))
        for url in self.crawled_dict.keys():
            weight = self.crawled_dict[url]
            cmd = 'insert into %s(link,weight) values("%s",%d)' % (tbname, url, weight)
            if not storage.execute(cmd):
                self.log('cmd: %s execute error' % cmd)

        self.log('stop_spider write url weight to table:%s succ' % (tbname))

