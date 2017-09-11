# _*_ coding:utf-8 _*_
from scrapy import Spider
import scrapy
class GongJiJin(Spider):

    name = 'gjj'
    start_urls = ['http://www.bjgjj.gov.cn/wsyw/wscx/gjjcx-choice.jsp']
    def start_requests(self):
        for url in self.start_urls:
            data = {'bh1':'522130199107162455',
                    'mm1':'651102',
                    'gjjcxjjmyhpppp1':'z8ch',
                    'lb':'1',
                    'lk':'16'}
            yield scrapy.FormRequest(url=url, formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)
