# Scrapy settings for BlogSiteSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'BlogSiteSpider'

SPIDER_MODULES = ['BlogSiteSpider.spiders']
NEWSPIDER_MODULE = 'BlogSiteSpider.spiders'

ITEM_PIPELINES = ['BlogSiteSpider.pipelines.StoragePipeline',]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'BlogSiteSpider(+http://www.yourdomain.com)'
