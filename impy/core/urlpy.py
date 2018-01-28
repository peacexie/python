# url抓取(py=爬)相关函数

#from lxml import *
#from pyquery import PyQuery as pq

import os
import re
from urllib import request as req

def page(url, cset='utf-8'):
    page = req.urlopen(url)
    html = page.read()
    html = html.decode(cset, 'ignore')
    return html

def list(html, key='pics', no=0):
    dict = {
        'links': r'<a [^\>]*href=[\'\"]?([^\'\"]+)[\'\"]?[^\>]*>(.*?)</a>',
        'pics':  r'src=[\'\"]?([^\'\"]+\.(jpg|gif|png))[\'\"]?',
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
        #print(val)
        itms.append(val)
    return itms

def cut(html, tag, end=''):
    p1 = html.find(tag)
    if p1<0:
        return ''
    slen = len(html)
    html = html[p1:slen]
    p1 = html.find(end)
    if p1<0 or end=='':
        return html
    p1 += len(end)
    html = html[0:p1]
    return html

def save(ulist, udir, base):
    no = 0
    for itm in ulist:
        print(type(itm))
        if isinstance(itm, list): #type(itm) == list:
            url = itm[0]
        else:
            url = itm;
        if url.find('://')!=0:
            url = base+url;
        file = os.path.basename(url);
        req.urlretrieve(url, '../cache/'+udir+'/'+str(no)+'-%s'%file)
        no += 1
    return no
