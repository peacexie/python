# url抓取(py=爬)相关函数

# sys-import
import sys, os, io, re, gzip
from core import files
from urllib import parse, request as ureq
#from posixpath import normpath

# head : {"Accept-Encoding":"gzip"}
def page(url, cset='', ziped=0, head={}):
    agent = {"User-Agent": "Mozilla/5.0 (Window 7) Chrome/31.0"}
    if head:
        head = dict(agent, **head)
    req = ureq.Request(url, headers=head)
    data = ureq.urlopen(req).read()
    if ziped>0:
        dbyte = io.BytesIO(data)
        data = gzip.GzipFile(fileobj=dbyte, mode="rb").read()
    cset = fxcset(data, cset)
    html = data.decode(cset, 'ignore')
    return html

# 从url保存一个文件
def svurl(url, sdir, file='', path='./_cache'):
    if url.find('://')<0:
        return ''
    data = ureq.urlopen(url).read()
    if len(data)==0:
        return ''
    file = files.autnm(url)
    fp = path + '/' + sdir + '/' + file
    with open(fp, "wb") as fo:
        fo.write(data) #写文件用bytes而不是str
    return file

def fxurl(url, base=''):
    url = parse.urljoin(base, url)
    return url

# 获取编码设置(注意不是字符串,不依赖chardet )
def fxcset(data, cset=''):
    if cset:
        return cset
    p1 = data.find(b'charset')
    s1 = data[p1:p1+36]
    s2 = s1[0:s1.find(b'>')]
    s3 = s2.decode() # 'utf-8'
    cset = s3.replace('charset','').replace('"','').replace("'",'').replace(' ','')
    return cset.lower()

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
