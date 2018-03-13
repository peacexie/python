# url抓取(py=爬)相关函数

# sys-import
import sys, os, io, re, gzip #, importlib
from core import files
from urllib import parse, request as freq

# head : {"Accept-Encoding":"gzip"}
def page(url, cset='utf-8', ziped=0, head={}):

    defHeaders = { #发送HTTP请求时的HEAD信息，用于伪装为浏览器
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/6.1 (Windows NT 6.3) Chrome/31.0'
    }
    '''
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'PSTM=1504071547; BIDUPSID=0D6BE29FCDAD70E7CABA760AA9004EB3; BAIDUID=8B73EED70E3C8BBE655FC3E13DE1B861:FG=1; __cfduid=dc0f141ff64af6b8b06a6b6baedea40811509062676; BDUSS=g5dFZZdTZ-eUpjaEw4SnJIcDVzdXczZn5vSWlJS1NTTG9BSVFFNWR4RFl6SDlhQUFBQUFBJCQAAAAAAAAAAAEAAADyvtNFUGVhY2VYaWV5cwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANg~WFrYP1haRH; ispeed_lsm=0; MCITY=-%3A; BD_UPN=12314353; H_PS_645EC=92d6F35mfgmDM5M9J%2FqJ1M3FijOaUONOzEWRGqmn65KPbL%2BaSQrShMJLo0LsG%2Be3gh3o; BD_CK_SAM=1; PSINO=7; H_PS_PSSID=1444_21120_20930; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSVRTM=0',
        #'Host': 'www.baidu.com',
        #'Pragma': 'no-cache',
        'Referer': 'http://txjia.com/tools/?mod=full',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    '''
    #agent = {"User-Agent": "Mozilla/5.0 (Window 7) Chrome/31.0"}
    if head:
        head = dict(defHeaders, **head)
    req = freq.Request(url, headers=head)
    data = freq.urlopen(req).read()
    if ziped>0:
        dbyte = io.BytesIO(data)
        data = gzip.GzipFile(fileobj=dbyte, mode="rb").read()
    html = data.decode(cset, 'ignore')
    return html
    #'''

# 从url保存一个文件
def svurl(url, sdir, file='', path='./_cache'):
    if url.find('://')<0:
        return ''
    data = freq.urlopen(url).read()
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
