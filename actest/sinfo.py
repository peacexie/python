#coding=UTF-8

import os,sys

# http://blog.csdn.net/maoyongfan3/article/details/44752251
import platform

from multiprocessing import cpu_count 
print(cpu_count())

tmp = platform.architecture()
print(tmp)
tmp = platform.system()
print(tmp)
tmp = platform.version()
print(tmp)

root = os.path.dirname(__file__)
print("root=%s" % root)
#print("__dir__=%s" % __dir__)
print()

print("__file__=%s" % __file__)
print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
#print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])　
print("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))
print("os.getcwd()=%s" % os.getcwd())
print("sys.path[0]=%s" % sys.path[0])
print("sys.argv[0]=%s" % sys.argv[0])

