
#import os, sys, platform
import copy
from flask import g
from core import dbop, files, argv

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
        fctr = './views/'+g+'/_ctrls/'+c+'.py'
        ftpl = './views/'+tpl
        sctr = files.get(fctr)
        stpl = files.get(ftpl)
        data = {'stpl':stpl, 'sctr':sctr, 'ftpl':ftpl, 'fctr':fctr, 'fact':a}
        return data

    # `read`方法
    def readAct(self):
        sread = files.get("../README.md")
        data = {'sread':sread}
        return data
