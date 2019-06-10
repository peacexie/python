# url抓取(py=爬)相关函数

# sys-import
import sys, os, io, re, requests
from core import files
from urllib import request
from urllib.parse import urljoin

def page(url, head={}, proxy={}):
    agent = {"User-Agent": "Mozilla/5.0 (Window 7) Chrome/72.0"}
    if head:
        head = dict(agent, **head)
    r = requests.get(url, headers=head, proxies=proxy)
    if r.encoding == 'ISO-8859-1':
        c = re.search(r'charset=["\']?([^\'"]*)', r.text)
        if c:
            r.encoding = c.group(1)
    html = r.text
    return html

# 从url保存一个文件
def svurl(url, sdir, file='', path='../_cache'):
    if url.find('://')<0:
        return ''
    data = request.urlopen(url).read()
    if len(data)==0:
        return ''
    file = file if file else files.autnm(url)
    fp = path + '/' + sdir + '/' + file
    with open(fp, "wb") as fo:
        fo.write(data) #写文件用bytes而不是str
    return file

def fxurl(url, base=''):
    if not '://' in url:
        url = urljoin(base, url)
    return url

# --- 以下函数,尽量使用PyQuery代替,这里出现只是练习的意义 --- 

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