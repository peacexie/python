# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys, os
import json, re
from urllib.parse import urlparse

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class QuotesbotPipeline(object):
    def process_item(self, item, spider):
        return item

'''

import pymysql.cursors
class MySQLPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',  # 数据库地址
            port=3306,  # 数据库端口
            db='scrapyMysql',  # 数据库名
            user='root',  # 数据库用户名
            passwd='root',  # 数据库密码
            charset='utf8',  # 编码方式
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(
            """insert into mingyan(tag, cont)
            value (%s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['tag'],  # item里面定义的字段和表字段对应
             item['cont'],))
        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回

'''

class FzgnewsPipeline(object):

    def __init__(self):
        pass

    # save-file
    def process_item(self, item, spider):
        fbase = os.path.dirname(os.path.realpath(__file__)) + '/../../../../@tmps/pages/'
        catid = item['_catid']
        full = fbase + (catid if catid else 'all') + item['href'][0].replace('/','-')
        fp = open(full, "w", encoding='utf-8')  # gbk / utf-8
        data = str(item)
        fp.write(data)
        fp.close()
        return item  # 必须实现返回

    '''
    def thumb_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for iurl in item['thumb']:
            yield scrapy.Request(iurl)

    def detail_requests(self, item, info):
        for iurl in item['imgs']:
            yield scrapy.Request(iurl)
    '''


class ImagespiderPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):

        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield scrapy.Request(image_url, meta={'name':item['imgname']})  # 

        '''
        for image_url in item['imgurl']:
            yield scrapy.Request(image_url)
        '''

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        #return 'files/' + os.path.basename(urlparse(request.url).path)
        
        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        name = re.sub(r'[?\\*|"<>:/\']', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename