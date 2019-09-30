


https://www.jianshu.com/p/a412c0277f8a
使用FilesPipeline和ImagesPipeline


==================================


### python爬虫库scrapy


* scrapy 教程

非常专业的 python爬虫库scrapy
https://docs.scrapy.org/en/latest/intro/tutorial.html
有兴趣/有时间，可了解...

http://www.scrapyd.cn/doc/165.html
scrapy1.5中文文档

https://www.runoob.com/python3/python3-tutorial.html
Python 3 菜鸟教程




### 基本操作

* Creating a project
  - scrapy startproject tutorial

* How to run our spider
  - scrapy crawl quotes
  - scrapy crawl quotes -o quotes.json

* Extracting data
  - scrapy shell 'http://quotes.toscrape.com/page/1/'
  - response.css('title')
  - response.css('title::text').get()
  - response.xpath('//title')
  - response.css("div.quote")

  - li = response.css("div.box_news")[3]
  - li.getall()

### fzg1010.py

```
class Fzg1010Spider(scrapy.Spider):
    name = "fzg1010"
    maxpage = 5
    li = list(range(maxpage))
    start_urls = []
    for p in li:
        start_urls.append('http://hy.fzg360.com/news/lists/catid/1010/page/'+str(p)+'.html')

    def parse(self, response):
        for item in response.css("div.box_news"):
            yield {
                'title': item.css("h3 > a::text").extract(),
                'remark': item.css("p::text").get(),
                'thumb': item.css("img::attr(src)").extract_first()
                #'tags': item.css("div.tags > a.tag::text").extract()
            }
```

### run: 运行
    > scrapy crawl fzg1010 -o list1010.json
    // 记得到 列表结果（json文件）


### doc

* Scrapy Tutorial
  - https://docs.scrapy.org/en/latest/intro/tutorial.html
* scrapy框架下爬虫实现详情页抓取
  - https://www.cnblogs.com/zhiliang9408/p/10006364.html
* 爬虫框架Scrapy的安装与基本使用
  - https://www.jianshu.com/p/6bc5a4641629
* 三大解析库的使用
  - https://mp.weixin.qq.com/s?__biz=MzU0NDg3NDg0Ng==&mid=2247483766&idx=1&sn=86d61115ebb7a4083e17a54f1acffdf1&chksm=fb74c947cc03405122d74b1172a9a96ef35af65753666f3f7900a9318290c4326736c2d6e69e&scene=21#wechat_redirect
* scrapy学习笔记(有示例版）
  - https://www.jianshu.com/p/1e669c17c7ad
* 神一般的Scrapy框架，Python中Scrap的基本结构和去重原理
  - https://baijiahao.baidu.com/s?id=1617383606262037206&wfr=spider&for=pc



