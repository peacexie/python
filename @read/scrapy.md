


https://w3techs.com/
Content Management Systems
Server-side Programming Languages

https://www.cnblogs.com/nica/archive/2017/01/04/6248376.html
说一说从php转python的感想

https://www.liaoxuefeng.com/wiki/1016959663602400/1017075323632896
Python简介

python 1991~
php 1995~
asp 1996年推出一种Web应用开发技术ASP


http://ourhouse.txjia.com/home.php/ocar

3.1+2.7+0.9+0.4
(7)


---------------------------

https://j.map.baidu.com/55/BNM
莞太路 - 昆盈厂

---------------------------

https://www.runoob.com/go/go-tutorial.html
Go 语言教程

https://www.kancloud.cn/hello123/beego/126087
beego 是一个快速开发 Go 应用的 HTTP 框架

https://studygolang.com/
Go语言爱好者的学习家园


https://www.php.cn/python-tutorials-421849.html
Selenium+PhantomJs解析渲染Js的基本操作


https://www.cnblogs.com/yoyoketang/p/6128655.html
Selenium2+python自动化17-JS处理滚动条


https://www.jianshu.com/p/1531e12f8852
Python+Selenium基础入门及实践


https://www.jianshu.com/nb/25665695
jianshu Scrapy

https://blog.csdn.net/peiwang245/article/details/100071316
scrapy框架不同的爬虫程序设置不同pipelines


http://www.scrapyd.cn/jiaocheng/150.html
scrapy scrapyd 部署原来这么玩！以前看的都是假教程（一）：概述（不看毁一生）


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
  - scrapy crawl cname -a tag=美女
  - scrapy crawl fzgnews -a catid=1012

* Extracting data
  - scrapy shell 'http://quotes.toscrape.com/page/1/'
  - response.css('title')
  - response.css('title::text').get()
  - response.xpath('//title')
  - response.css("div.quote")

  - li = response.css("div.box_news")[3]
  - li.getall()


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



