#coding=UTF-8

import sys, os, time
from core import argv, config, dbop, vjef, vext
from flask import Flask, g

def init():
    cfgs = config.init()
    #app = Flask(__name__)
    #g.run = {} 
    #cfgs['args'] = sys.argv
    #for key in cfgs:
    #    setattr(g, key, cfgs[key])
    #g.db = dbop.dbm(cfgs['cdb'])
    #return app

def app():
    pass
    