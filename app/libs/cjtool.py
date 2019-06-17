#coding=UTF-8

import copy, re, time
from core import argv, dbop, files, urlpy
from urllib import parse
from urllib.parse import urljoin
from pyquery import PyQuery as pyq


# <xml id="DocumentsDataSrc12">(*)</xml>
def htmDeel(rule, html, key): # key=pre_list/pre_cont
    rg = re.search(key+'=='+'([^\n|\r])+', rule['cfgs']) #, re.I
    if not rg:
        return html
    rp = rg.span() #;print(rp)
    cfg = rule['cfgs'][rp[0]+10:rp[1]] #;print(cfg)
    if not '(*)' in cfg:
        return html
    tab = cfg.split('(*)')
    html = urlpy.block(html, tab[0], tab[1])
    if len(html)>48000: # 500多K文本，2400多条记录，空白（可能是溢出）
        html = html[0:36000] +' ... '+ html[-2400:]
    #print(html)
    return html

# 图片地址替换
def repImgs(url, html):
    if not html:
        return ''
    reg = r'\<img([^\n\r]+)src=[\'\"]?([^\'\"]+)[\'\"]?'
    res = re.findall(reg, html, re.S) #|re.M
    for i in range(len(res)):
        iv = res[i][1]
        if not iv or 'data:image/' in iv or '://' in iv:
            continue
        iurl = urlpy.fxurl(iv, url)
        html = html.replace(iv, iurl)
        #print(iurl)
    return html

# 内容替换：tab_repd==阳光网=房掌柜@@<UCAPCONTENT>@@</UCAPCONTENT>@@
def repCont(cfgs, key, val):
    if not cfgs or not val:
        return val
    rg = re.search(key+'=='+'([^\n|\r])+', cfgs) #, re.I
    if not rg:
        return val
    rp = rg.span() #;print(rp)
    cfg = cfgs[rp[0]+len(key)+2:rp[1]] #;print(cfg)
    tab = re.split('@@', cfg)
    for i in range(len(tab)):
        iv = tab[i] #;print(iv)
        if not iv:
            continue
        tb2 = re.split('=', iv)
        if tb2[0] and '=' in iv and tb2[1]:
            val = val.replace(tb2[0], tb2[1])
        else:
            reg = re.compile(re.escape(iv), re.IGNORECASE)
            val = reg.sub('', val)
            #val.replace(iv, '')
        #print(val)
    return val;

def skips(rule, rowb, rowd):
    # 内容为空:返回过滤原因代码
    if not rowd['detail']:
        return 'no-detail'
    tf = ['title','dfrom']
    key = rule['field'] #tf[i0]
    op = rule['fop'] # inc-包含, exc-排除
    fval = rule['fval'] # A特征, B特征
    # 没设置有效值:不过滤,返回空
    if len(key)==0 or len(op)==0 or len(fval)==0:
        return ''
    else:
        val = rowb[key] if (key=='title' or key=='url') else rowd[key]
        if len(val)==0:
            return 'skip-Null.'+key
    # 包含统计
    tab = re.split(r'[,]', pqs) if (',' in fval) else [fval]
    incs = 0 # 包含次数
    for i in range(len(tab)):
        if tab[i] in val:
            incs += 1
    r1 = op=='inc' and incs==0
    r2 = op=='exc' and incs>0
    #print(r1,r2,op,incs,val,fval)
    # 返回过滤原因代码
    if r1 or r2:
        return 'skip-'+key
    return ''


# 取多个选择器(<pqs1>,<pqs2>)中一个的 值/属性
def pqv(dom, pqs, attr='text'):
    if not ',' in pqs:
        return pqone(dom, pqs, attr)
    else:
        tab = re.split(r'[;,]', pqs)
        for i in range(len(tab)):
            res = pqone(dom, tab[i], attr)
            #print(tab[i]+' :::: '+str(res))
            if res:
                return res
    return ''

# 取一个(<pqs>)选择器的 值/属性
def pqone(dom, pqs, attr='text'):
    e = pyq(dom).find(pqs) if pqs else pyq(dom)
    if attr=='text':
        return pyq(e).text()
    elif attr=='html':
        return pyq(e).html()
    else:
        return pyq(e).attr(attr)

def debug(debug={}):
    now = time.strftime("%m-%d %H:%M:%S", time.localtime())
    # start
    if 'run' not in debug.keys():
        return {
            'run':{'stamp1':time.time(), 'start':now},
            'link':{}, 'cont':{},
        }
    # end
    debug['run']['stamp2'] = time.time()
    debug['run']['end'] = now,
    debug['run']['timen'] = debug['run']['stamp2'] - debug['run']['stamp1']
    data = str(debug)
    fp = time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.txt'
    files.put('../_cache/debug/'+fp, data)
    return debug

# 
def today(str):
    today = time.strftime("%Y-%m-%d", time.localtime())
    #print(today, str, str==today)
    return str==today


'''

'''

'''
if 'a.' in attr: # pqs=='a.'
    if attr=='a.href':
        return pyq(e).attr('href')
    else:
        return pyq(e).text()
# res='a' if x > y else 'b' #三元表达式
else:
    if attr=='text':
        return pyq(e).text()
    elif attr=='html':
        return pyq(e).html()
    else:
        return pyq(e).attr(attr)
'''