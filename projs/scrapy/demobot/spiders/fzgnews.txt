# -*- coding:utf-8 -*-

import sys, os
import json
import scrapy
from demobot.items import ImagespiderItem

domain = 'http://dg.fzg360.com'
catid = ''

class FzgnewsSpider(scrapy.Spider):

    name = "fzgnews"
    custom_settings = {
        'ITEM_PIPELINES': {}
    }

    '''
    start_urls = [  # li = [2,3] #list(range(maxpage))
        #domain+'/news/lists.html'  # 不分栏目,所有新闻
        domain + '/news/lists/catid/1012/page/1.html',  # 1010,1012 
    ]
    '''

    def start_requests(self):
        global catid
        catid = getattr(self, 'catid', '')  # 获取catid值，也就是爬取时传过来的参数
        url = domain + '/news/lists/' + ('catid/'+catid+'/' if catid else '') + 'page/1.html'
        #print(url); exit()
        yield scrapy.Request(url, self.parse)  # 发送请求爬取参数内容

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
            break  # 一页爬一条就是了...

        # 翻页处理
        next_url = None
        items = response.css(".pager a")
        for itm in items:
            if '下页' in itm.get():
                next_url = itm.attrib['href']
                #print('next_url ==== ', next_url)
                break
        if next_url is not None:
            yield scrapy.Request(response.urljoin(next_url))

    # 爬取详情
    def get_detail(self, response): #处理详情页

        item = response.meta["item"]
        item["detail"] = response.css(".detailcon").get()
        item["imgs"] = response.css(".detailcon img::attr(src)").getall()
        #item["imgs"] = ["http://ss.xx_yy.com"+i for i in item["imgs"]]

        # save-file
        fbase = os.path.dirname(os.path.realpath(__file__)) + '/../../../../../@tmps/pages/'
        global catid
        full = fbase + (catid if catid else 'all') + item['href'][0].replace('/','-')

        fp = open(full, "w", encoding='utf-8')  # gbk / utf-8
        data = json.dumps(item, ensure_ascii=False)  # .encode("utf-8")
        data = data.replace('"], "', "\"], \n\"")
        data = data.replace('", "', "\", \n\"")
        fp.write(data)
        fp.close()

        # save-output
        yield item

