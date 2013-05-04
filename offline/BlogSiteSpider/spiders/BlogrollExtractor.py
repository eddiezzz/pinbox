#!/usr/bin/python2.7
#coding=utf-8

from scrapy.selector import HtmlXPathSelector 
from scrapy.http.response.text import TextResponse as Response
import re,sys
from urlparse import urlparse
import pdb

reload(sys)
sys.setdefaultencoding('utf8')

class BlogrollExtractor():

    roll_tags = ['blogroll', '友情链接', '推荐博客', '推荐链接', '非链不可'] 
    area_begin = '<ul'
    area_end = '</ul>'
    filt_url = ['shop', 'maijia', 'taobao.com', 'https:']
    not_filt_url = ['blog']
    filt_name = ['网', '下载', '酒店', '店铺', '商场', '源码', 'wordpress', '小说', '直播', '视频', '求职', '漫画', '导航', '动画', '游戏', '论坛','欣赏', '美文', '吧', '情感', '散文', '腹黑', '电影', '影音', '事件', '模板', '中国', '电视剧', '社区', '快播', '宣传', '阅读', '申请', '旗舰店', '男装', '女装', '服装', ':', ',', '，']
    not_filt_name = ['博客', 'blog', 'Blog', 'BLOG']

    trim_end_tag = ['index.php', 'index.asp', 'index.aspx', 'index.html']

    def need_extract(self, body):
        for tag in self.roll_tags:
            if tag in body:
                return tag
        return False

    def not_filt_by_url(self, url):
         for url_tag in self.not_filt_url:
            if url_tag in url:
                return True
    def filt_by_url(self, url):
        for url_tag in self.filt_url:
            if (url_tag in url) and (not self.not_filt_by_url(url)):
                return True

    def not_filt_by_name(self, name):
         for name_tag in self.not_filt_name:
            if name_tag in name:
                return True
    def filt_by_name(self, name):
        for name_tag in self.filt_name:
            if (name_tag in name) and (not self.not_filt_by_name(name)):
                return True

    def select_area(self, body, tag):
        tag_start_index = body.find(tag)
        if tag_start_index < 0:
            return False
        start_index = body.rfind('<', 0, tag_start_index) 
        start_index = body.find(self.area_begin, start_index)
        if start_index < 0:
            return False 
        end_index = body.find(self.area_end, tag_start_index + len(self.area_begin))
        if end_index < 0:
            return False
        end_index += len(self.area_end)
        return body[start_index:end_index]

    def do_filt(self, hosturl, to_filt_url, name):
        #filt begin
        if (not to_filt_url[0].isalpha()) and (not to_filt_url[0].isdigit()):
            return None
        if len(to_filt_url) > 60:
            return None

        #filt not blog page
        if 'about' in to_filt_url and 'me' in to_filt_url:
            return None

        #filt by filt_url
        if self.filt_by_url(to_filt_url): 
            return None
        if self.filt_by_name(name): 
            return None

        ori_to_filt_url = None
        #trim end_tag in the end
        for end_tag in self.trim_end_tag:
            if end_tag in to_filt_url:
                ori_to_filt_url = to_filt_url.split(end_tag)[0]
            else:
                ori_to_filt_url = to_filt_url

        #filt '/' in the end
        if to_filt_url[-1] == '/':
            ori_to_filt_url = to_filt_url[0:-1]
        else:
            ori_to_filt_url = to_filt_url
        #pdb.set_trace()

        if 'http://' not in to_filt_url:
            ori_to_filt_url = 'http://' + ori_to_filt_url
        to_filt_url = urlparse(ori_to_filt_url)[1]#net loc

        #format schema
        if not hosturl:
            return to_filt_url
        if 'http://' not in hosturl:
            hosturl = 'http://' + hosturl
        hosturl = urlparse(hosturl)[1]
        if hosturl == to_filt_url:
            return None
        return ori_to_filt_url

    def extract(self, body, hosturl):
        items = []
        tag = self.need_extract(body)
        if not tag:
            print "not found tag"
            return items
        print "found tag:%s" % tag
        area = self.select_area(body, tag)
        if not area:
            return items
        #print "by tag:%s, get area: %s" % (tag, area)
        response = Response('demo.html', body = '<html><body>' + area + '<body></html>')
        hxs = HtmlXPathSelector(response)
        lis = hxs.select('//ul/li')
        for li in lis:
            url = li.select('a/@href').extract()[0]
            name = ''.join(li.select('a/text()').extract())
            url = self.do_filt(hosturl, url, name)
            if not url:
                #print "filted:", url, name
                continue
            #print name, url 
            #name = name.encode('utf8')
            items.append((name, url))
        for item in items:
            pass
            #print item
        return items

if __name__ == '__main__':
    extractor = BlogrollExtractor()
    blog_file = open(sys.argv[1], 'r')
    if not blog_file:
        print "file open error:%s" % sys.argv[1]
        exit(1)
    body = ''.join(blog_file.readlines())
    blog_file.close()
    items = extractor.extract(body, sys.argv[1])
    print items
