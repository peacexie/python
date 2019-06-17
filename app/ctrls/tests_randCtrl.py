
#import os, sys, platform
import copy
from core import argv, dbop, files
from libs import rands
from flask import g

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # exdb, blog

    def indexAct(self):
        data = {}
        tp = argv.get('type', '0')
        rn = argv.get('rn', '10') # 10/20
        cm = argv.get('cm', '2')
        ax = argv.get('all', '100')
        s0 = rands.rn(tp, int(ax));
        data['tabs'] = rands.strg(s0, int(rn), int(cm));
        data['argv'] = {'tp':tp, 'rn':rn, 'cm':cm, 'ax':ax};
        #data['pk'] = rands.puke();
        return data

    # `puke`方法
    def pukeAct(self):
        data = {}
        rn = argv.get('rn', '6') # 8/7/6/5
        cm = argv.get('cm', '1')
        puke = rands.puke();
        data['tabs'] = rands.strg(puke, int(rn), int(cm));
        data['argv'] = {'rn':rn, 'cm':cm};
        return data

    # chart
    def chartAct(self):
        data = {}
        tp = argv.get('type', '0')
        rn = argv.get('rn', '20') # 10/20
        cm = argv.get('cm', '2')
        ax = argv.get('all', '100')
        s0 = rands.rn(tp, int(ax));
        data['tabs'] = rands.strg(s0, int(rn), int(cm));
        data['argv'] = {'tp':tp, 'rn':rn, 'cm':cm, 'ax':ax};
        return data

'''

'''
