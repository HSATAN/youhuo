# coding=utf8
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import signals
import sys

from scrapy.utils.project import get_project_settings
from youhuo.spiders.youhuo_spider import YouHuoSpider as spider

crawler = Crawler(spider, get_project_settings())
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.crawl()
reactor.run()