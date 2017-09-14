#coding=utf-8

from scrapy import Spider
import scrapy
import re, json
from scrapy.selector import Selector
import sys
import logging
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")


class YouHuoSpider(Spider):
    name = 'youhuo'
    start_urls=[
        'https://item.yohobuy.com/51647398.html'
    ]
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'

    }
    def detail(self, response):
        sel = Selector(response)
        nav_node = sel.xpath('//div[@class="third-nav-wrapper"]//dd/a/@href').extract()
        if nav_node:
            print(nav_node)


    def parse(self, response):
        text=response.body.decode("utf-8")
        sel=Selector(response)

        price_info=re.findall('PING_YOU_VIEW_ITEM =(.*?);',response.body.decode("utf-8"),re.S)
        if price_info:
            price_info=json.loads(price_info[0].replace('// 宽x高','').replace("'",'"'))
            origin_price=price_info['orig_price']
            current_price=price_info['price']
        print(current_price)
        print(origin_price)
        print(price_info)
        currency_code = price_info['currency_code']
        url = response.url
        categorys = price_info['category'].split('>')
        category_first_name = categorys[1]
        category_last_name = categorys[2]
        brand = price_info['brand']
        name = price_info['name']
        colors = sel.xpath('//div[@class="chose-color row clearfix"]//'
                           'ul[@class="colors pull-left clearfix"]/li/@data-color').extract()

        color_num = len(colors)
        print(colors)

        sizes = sel.xpath('//div[@class="size-wrapper pull-left"]/ul')
        sku_list = []
        for index, size_node in enumerate(sizes):
            data = {}
            size_list = size_node.xpath('./li')
            data['color'] = colors[index]
            print(index)
            data['sku']=[]
            for  size_li in size_list:
                sku_item = {}
                data_sku = size_li.xpath('./@data-sku').extract()
                data_num = size_li.xpath('./@data-num').extract()
                data_name = size_li.xpath('./@data-name').extract()
                data_info = size_li.xpath('./@data-info').extract()
                # print(data_sku)
                # print(data_num)
                # print(data_name)
                # print(data_info)
                sku_item['sku_id'] = data_sku[0]
                sku_item['sku_num'] = data_num[0]
                sku_item['sku_name'] = data_name[0]
                sku_item['sku_info'] = data_info[0]
                data['sku'].append(sku_item)

            sku_list.append(data)

        for item in sku_list:
            print(item)
        info_data = {}



        info_node = sel.xpath('//ul[@class="basic clearfix"]/li/em')
        for index, info_sub_node in enumerate(info_node):
            try:
                key = info_sub_node.xpath('./span[@class="keySpace"]/text()').extract()[0].strip()
                value = info_sub_node.xpath('./span[@class="value-space"]/text()').extract()[0].strip()
                info_data[index] = {'key': key, 'value': value}
            except Exception as e:
                logging.error(e)
        print(info_data)

        comfort_data = []
        # comfort_node = response.selector.xpath('//ul[@class="comfort clearfix"]')
        # print comfort_node
        # for comfort_sub_node in comfort_node:
        #     print('============================')
        #     low_level = comfort_sub_node.xpath('./span[@class="min-des"]/text()').extract()[0].strip()
        #     title = comfort_sub_node.xpath('./span[@class="comfort-title"]/text()').extract()[0].strip()
        #     high_level = comfort_sub_node.xpath('./span[@class="max-des"]/text()').extract()[0].strip()
        #     rank = len(comfort_sub_node.xpath('./span[contains(@class,"comfort-block")]/text()').extract())
        #     data = {}
        #     data['low_level'] = low_level
        #     data['high_level'] = high_level
        #     data['title'] = title
        #     data['rank'] = rank
        #     comfort_data.append(data)
        # print(comfort_data)
        #
        # if not comfort_node:
        #     comfort_node = re.findall('comfort clearfix">(.*?)</ul>', response.body, re.S)
        #     print comfort_node
        # with open('page.html', 'w') as f:
        #     f.writelines(response.body)

        desc_node = sel.xpath('//div[@id="details-html"]/em[@class="details-word"]/text()').extract()
        if desc_node:
            desc = desc_node[0]
        print desc
        print color_num