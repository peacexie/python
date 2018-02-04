#coding=UTF-8

import configparser

conf = configparser.ConfigParser()
conf.read("../data/config.ini")
secs = conf.sections()
print(secs)

tmp = conf.get("db", "user")
print(tmp)
tmp = conf.items("db")
print(tmp)

print()
print()

from urllib.parse import urlparse

url = 'http://www.txjia.com/articles/437.html'
items = urlparse(url); print(items)

url = 'http://www.txjia.com'
items = urlparse(url); print(items)

url = '/root/home/index?pa=a1'
items = urlparse(url); print(items)

print('')
print(items.path)
tmp = items.path.split('/')
print(tmp)
print(tmp[0])
print(tmp[1])
print(tmp[2])

import sys
sys.path.append("../")

from core import start
#from core import config as _cfg

print(start._cfg)
