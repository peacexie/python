# url抓取(py=爬)相关函数

# sys-import
import sys, os, io, re, requests
from core import files
from urllib import request
from urllib.parse import urljoin

def page(url, cset='', ziped=0, head={}):
    agent = {"User-Agent": "Mozilla/5.0 (Window 7) Chrome/31.0"}
    if head:
        head = dict(agent, **head)
    r = requests.get(url, headers=head)
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
    file = files.autnm(url)
    fp = path + '/' + sdir + '/' + file
    with open(fp, "wb") as fo:
        fo.write(data) #写文件用bytes而不是str
    return file

def fxurl(url, base=''):
    if not '://' in url:
        url = urljoin(base, url)
    return url
