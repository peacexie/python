
#import os, sys, platform
#import configparser

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app, request, g):
        self.app = app
        self.request = request
        self.g = g
        self.data = {}

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs.type > '_def'

    def indexAct(self):
        data = {'indexAct_msg':'from indexAct'}
        return data

    # `detail`方法
    def _detailAct(self):
        data = {'_detailAct_msg':'from _detailAct'}
        return data

    # 默认非`detail`方法
    def _defAct(self):
        d = {} #{'tpname':'modi/actid'} # 指定模板
        data = {'_defAct_msg':'from _defAct', 'd':d}
        return data 


'''

'''
