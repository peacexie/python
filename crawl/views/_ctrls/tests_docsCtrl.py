
#import os, sys, platform
import copy
from core import dbop, files, argv
from flask import g

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # exdb, blog

    def indexAct(self):
        data = {}
        return data

    # `dev`方法
    def devAct(self):
        fp = argv.get('fp', 'doc-note.txt')
        slink = files.get("./static/root/doc/"+fp)
        title = '项目计划/开发记录' if fp.find('note')>0 else '学习资料/参考链接'
        data = {'slink':slink, 'fp':fp, 'title':title}
        return data

    def udirAct(self):
        data = {}
        data['d'] = {'tpname':'dir', 'message':'/front/blog'} # dir
        return data

    def uerrAct(self):
        data = {}
        data['d'] = {'code':500, 'message':'Test-500 Message --- 控制器自定义错误'} # err
        return data

    # `detail`方法
    def _detailAct(self):
        data = {'_detailAct_msg':'from _detailAct'}
        return data

    # 默认非`detail`方法
    def _defAct(self):
        #d = {'tpname':'home/info'} # 指定模板
        #d = {'code':404} # 显示错误访问
        d = {}
        data = {'_defAct_msg':'from _defAct', 'd':d}
        return data 

'''
    data['d'] = {}
    #data['d'] = {'tpname':'json'} # 指定模板
    #data['d'] = {'tpname':'xml'} # 指定模板
    #data['d'] = {'tpname':'dir', 'message':'/front/blog'} # dir
    #data['d'] = {'code':500, 'message':'500 Message'} # dir
'''
