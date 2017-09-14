# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YouhuoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    spu_id = scrapy.Field()
    origin_price = scrapy.Field()
    current_price = scrapy.Field()
    sizes = scrapy.Field()
    url = scrapy.Field()
    info = scrapy.Field()
    size_info = scrapy.Field()
    brand = scrapy.Field()
    catogory_first_id = scrapy.Field()
    category_first_name = scrapy.Field()
    category_last_id = scrapy.Field()
    category_last_name = scrapy.Field()
    colors = scrapy.Field()
    color_num = scrapy.Field()  # 颜色数目
    image_urls = scrapy.Field()
    description = scrapy.Field()
    sku_list = scrapy.Field()
    currency_code = scrapy.Field()

