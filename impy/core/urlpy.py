# url抓取(py=爬)相关函数

#from lxml import *
#from pyquery import PyQuery as pq

import os
import re
from urllib import request as req

#import files

def page(url, cset='utf-8'):
    page = req.urlopen(url)
    html = page.read()
    html = html.decode(cset, 'ignore')
    return html

def block(html, tag, end=''):
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

# 保存文本
def svurl(url, sdir, file=''):
    if url.find('://')<0:
        return ''
    data = req.urlopen(url).read()
    if len(data)==0:
        return ''
    if file.find('.')<1:
        base = os.path.basename(url)
        file = file.replace('?', '~')
    fp = '../cache/' + sdir + '/' + file
    with open(fp+".htm", "wb") as fo:
        fo.write(data) #写文件用bytes而不是str，所以要转码 ???
    return file

'''
.jpg,jpeg,png,bmp,gif
.json,xml,txt
.html,htm,js,css,
.asp,php,jsp,aspx,do
'''

'''


def x_save(ulist, udir, base):
    no = 0
    for itm in ulist:
        print(type(itm))
        if isinstance(itm, list): #type(itm) == list:
            url = itm[0]
        else:
            url = itm;
        if url.find('://')!=0:
            url = base+url
        file = os.path.basename(url);
        req.urlretrieve(url, '../cache/'+udir+'/'+str(no)+'-%s'%file)
        no += 1
    return no

# 打开一个文件
fo = open("foo.txt", "wb")
fo.write( "www.runoob.com!\nVery good site!\n")
 
# 关闭打开的文件
fo.close()
'''
