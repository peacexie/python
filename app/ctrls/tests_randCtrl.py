
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

    # `data`方法
    def dataAct(self):
        data = {}
        tp = argv.get('type', 'su')
        mi = argv.get('min', '1')
        ma = argv.get('max', '200')
        cm = argv.get('cm', '5')
        primes = rands.Primes(int(mi), int(ma));
        data['tabs'] = rands.strg(primes, int(cm), 1);
        data['argv'] = {'tp':tp, 'ma':ma, 'mi':mi, 'cm':cm};
        return data

    # chart
    def chartAct(self):
        data = {}
        mi = argv.get('min', '3200')
        ma = argv.get('max', '6400')
        ax = argv.get('all', '12')
        do = argv.get('dot', '2')
        ins = argv.get('ins', '200') 
        s0 = rands.rd(int(mi), int(ma), int(ax), int(do), int(ins));
        data['tabs'] = ', '.join(s0); #rands.strg(s0, int(cm));
        data['argv'] = {'ma':ma, 'mi':mi, 'ins':ins, 'ax':ax, 'do':do};
        return data

'''

'''
