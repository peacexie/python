# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#'''
class ImagespiderItem(scrapy.Item):
    imgurl = scrapy.Field()
    imgname = scrapy.Field()
    pass
#'''

class FzgmysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    thumb = scrapy.Field()
    remark = scrapy.Field()
    detail = scrapy.Field()
    imgs = scrapy.Field()
    _catid = scrapy.Field()
    pass

