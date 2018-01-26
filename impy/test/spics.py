#coding=UTF-8

import os
from urllib import request as req; #import urllib.request
import re

def getHtml(url):
    page = req.urlopen(url)
    html = page.read()
    return html

def getImg(html,base):
    reg = r'src="(.+?\.jpg)"' # pic_ext
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        imgurl = base+imgurl; # (base+imgurl).replace('//', '/');
        file = os.path.basename(imgurl);
        print(imgurl)
        req.urlretrieve(imgurl,'../cache/tmpic/'+str(x)+'-%s' % file)
        x+=1
    return x

# 
"""
http://txmao.txjia.com/
https://tieba.baidu.com/p/2460150866
"""
url = "http://txmao.txjia.com/"
html = getHtml(url)
html = html.decode('utf-8', 'ignore')
print(html)

print(getImg(html,url))
# print()
