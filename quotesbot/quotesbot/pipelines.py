# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class QuotesbotPipeline(object):
    def process_item(self, item, spider):
        return item


class Fzg1010Pipeline(ImagesPipeline):

    def thumb_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for iurl in item['thumb']:
            yield scrapy.Request(iurl)

    def detail_requests(self, item, info):
        for iurl in item['imgs']:
            yield scrapy.Request(iurl)


class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            yield scrapy.Request(image_url)
