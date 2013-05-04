#!/usr/bin/python2.7
#coding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from storage.MysqlHelper import MysqlHelper
from items import SiteLinkItem, SiteWeightItem
from scrapy.exceptions import DropItem

class StoragePipeline(object):
    dbname = "pinbox"
    site_link_tbname = "table_site_link"
    site_weight_tbname = "table_site_weight"
    username = "root"
    password = "hello1234"
    storage = None

    def __init__(self):
        self.storage = MysqlHelper(username=self.username, password=self.password)
        if not self.storage.connect(self.dbname):
            return False
       
    def process_item(self, item, spider):
        cmd = None
        if isinstance(item, SiteLinkItem):
            cmd = 'insert into %s(name, link) values("%s","%s")' % (self.site_link_tbname, item['name'], item['url'])
        elif isinstance(item, SiteWeightItem):
            cmd = 'insert into %s(link, weight) values("%s","%d")' % (self.site_weight_tbname, item['url'], item['weight'])
        
        if cmd:
            if not self.storage.execute(cmd):
                print "insert url:%s into storage error" % (item['url'])
        raise DropItem('url:%s droped' % item['url'])
