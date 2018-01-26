# url抓取(py=爬)相关函数

import os
import re
from urllib import request as req

#from lxml import *
#from pyquery import PyQuery as pq


def page(url, cset='utf-8'):
    page = req.urlopen(url)
    html = page.read()
    html = html.decode(cset, 'ignore')
    return html

def list(html, key='pics', no=0):
    dict = {
        'links': r'<a [^\>]*href=[\'\"]?([^\'\"]+)[\'\"]?[^\>]*>(.*?)</a>',
        'pics': r'src="(.+?\.(jpg|gif|png))"',
    }
    if key in dict:
        reg = dict[key]
    else:
        reg = r'<'+key+'[^\>]*>(.*?)</'+key+'>'
        no = -1
    #rcom = re.compile(reg)
    res = re.findall(reg, html, re.S|re.M)
    itms = []
    for itm in res:
        if 'links' in dict:
            val = [itm[0], itm[1]] if len(itm)>=2 else itm[0]
        else:
            val = itm[no] if no>=0 else itm
        print(val)
        itms.append(val)
    return itms

def cut(html, tag, end):
    #<div class="pgf_menu">
    p = html.find(tag)
    return html

def save(html, base):
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

