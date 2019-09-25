# -*- coding: utf-8 -*-
import scrapy


class Fzg1010Spider(scrapy.Spider):
    name = "fzg1010"
    maxpage = 5
    li = list(range(maxpage))
    start_urls = []
    for p in li:
        start_urls.append('http://hy.fzg360.com/news/lists/catid/1010/page/'+str(p)+'.html')
    '''
    start_urls = [
        'http://hy.fzg360.com/news/lists/catid/1010/page/1.html',
    ]
    '''

    def parse(self, response):
        for item in response.css("div.box_news"):
            yield {
                'title': item.css("h3 > a::text").extract(),
                'remark': item.css("p::text").get(),
                'thumb': item.css("img::attr(src)").extract_first()
                #'tags': item.css("div.tags > a.tag::text").extract()
            }

        '''
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
        '''

