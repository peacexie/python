
#import os, sys, platform
import copy
from core import dbop, files, argv
from flask import g

# 方法格式: {xxx}Act
# xxx优先顺序 : mkvs.key > mkvs._type > '_def'

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}

    # `coder`方法
    def coderAct(self):
        g = argv.get('g', 'root')
        c = argv.get('c', 'homeCtrl')
        a = argv.get('a', 'coderAct')
        tpl = argv.get('tpl', 'root/home/coder.htm')
        fctr = './ctrls/'+c+'.py'
        ftpl = './views/'+tpl
        sctr = files.get(fctr)
        stpl = files.get(ftpl)
        data = {'stpl':stpl, 'sctr':sctr, 'ftpl':ftpl, 'fctr':fctr, 'fact':a}
        return data

    # `read`方法
    def readAct(self):
        sread = files.get("../README.md")
        sread = sread.replace('\n', '<br>\n').replace(' ', '&nbsp;')
        data = {'sread':sread}
        return data

'''

        data['d'] = {}
        #data['d'] = {'tpname':'json'} # 指定模板
        #data['d'] = {'tpname':'xml'} # 指定模板
        #data['d'] = {'tpname':'dir', 'message':'/blog/'} # dir
        #data['d'] = {'code':500, 'message':'500 Message'} # dir

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
