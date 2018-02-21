# url抓取(py=爬)相关函数

# sys-import
import os, re
from urllib import request as req
from core import files


# 从url保存一个文件
def svurl(url, sdir, file='', path='./_cache'):
    if url.find('://')<0:
        return ''
    data = req.urlopen(url).read()
    if len(data)==0:
        return ''
    file = files.autnm(url)
    fp = path + '/' + sdir + '/' + file
    with open(fp, "wb") as fo:
        fo.write(data) #写文件用bytes而不是str
    return file
'''
.jpg,jpeg,png,bmp,gif
.json,xml,txt
.html,htm,js,css,
.asp,php,jsp,aspx,do
'''


# --- 以下函数,尽量使用PyQuery代替,这里出现只是练习的意义 --- 

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