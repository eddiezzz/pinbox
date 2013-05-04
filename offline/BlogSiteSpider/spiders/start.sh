#!/bin/bash
scrapy crawl BlogSiteSpider -o items.json -t json > crawl.log 2>&1 &
