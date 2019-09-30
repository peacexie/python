# -*- coding:utf-8 -*-

import json
import scrapy
from quotesbot.items import ImagespiderItem

domain = 'http://dg.fzg360.com'

class Fzg1010Spider(scrapy.Spider):

    name = "fzg1010"

    maxpage = 3
    li = [2,3] #list(range(maxpage))
    start_urls = []
    for p in li:
        start_urls.append(domain+'/news/lists/catid/1010/page/'+str(p)+'.html')
    '''
    start_urls = [
        'http://hy.fzg360.com/news/lists/catid/1010/page/1.html',
    ]
    '''

    def parse(self, response):
        for ili in response.css("div.box_news"):

            item = {}  # ImagespiderItem()  # 实例化item
            item['title'] = ili.css("h3>a::text").get(),
            item['href'] = ili.css("a::attr(href)").get(),
            item["thumb"] = ili.css("img::attr(src)").get(),
            item["remark"] = ili.css("p::text").get()

            #yield item

            yield scrapy.Request(
                domain+item["href"][0],
                callback = self.get_detail,
                meta = {"item":item},
            )

        '''
        # 翻页处理
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        '''

    # 爬取详情
    def get_detail(self, response): #处理详情页

        item = response.meta["item"]
        item["detail"] = response.css(".detailcon").get()
        item["imgs"] = response.css(".detailcon img::attr(src)").getall()
        #item["imgs"] = ["http://ss.xx_yy.com"+i for i in item["imgs"]]

        # save-file
        fbase = 'E:/www/peace/wepy.git/@tmps/pages/'
        fp = open(fbase+item['href'][0].replace('/','-'), "w", encoding='utf-8')  # gbk / utf-8
        data = json.dumps(item, ensure_ascii=False)  # .encode("utf-8")
        fp.write(data)
        fp.close()

        # save-output
        yield item
