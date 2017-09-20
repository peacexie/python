#coding=UTF-8

from urllib import request as req; #import urllib.request
import re

def getHtml(url):
    page = req.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"' # pic_ext
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        #req.urlretrieve(imgurl,'../cache/tmpic/%s.jpg' % x)
        x+=1

# 
"""
http://txmao.txjia.com/
https://tieba.baidu.com/p/2460150866
"""
html = getHtml("http://txmao.txjia.com/")
html = html.decode('utf-8', 'ignore')
#print(html)

print(getImg(html))
# print()
