# -*- coding:utf-8 -*-

import scrapy
from demobot.items import ImagespiderItem

class ImgspiderSpider(scrapy.Spider):

    name = 'imgsp'
    custom_settings = {
        'ITEM_PIPELINES': {'demobot.pipelines.ImagespiderPipeline':300}
    }
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html',
        'http://lab.scrapyd.cn/archives/57.html',
    ]

    def parse(self, response):
        item = ImagespiderItem()  # 实例化item
        # 注意这里是一个集合也就是多张图片
        item['imgurl'] = response.css(".post img::attr(src)").extract()
        # 抓取文章标题作为图集名称
        item['imgname'] = response.css(".post-title a::text").extract_first()
        yield item
        pass
