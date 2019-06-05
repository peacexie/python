#coding=UTF-8

import copy, re, time
from core import argv, dbop, files, urlpy
from urllib import parse
from urllib.parse import urljoin
from pyquery import PyQuery as pyq

def skips(rule, rowb, rowd):
    # 内容为空:返回过滤原因代码
    if not rowd['detail']:
        return 'no-detail'
    tf = ['title','dfrom']
    key = rule['field'] #tf[i0]
    val = rowb['title'] if key=='title' else rowb['dfrom']
    op = rule['fop'] # inc-包含, exc-排除
    fval = rule['fval'] # A特征, B特征
    # 没设置有效值:不过滤,返回空
    if len(key)==0 or len(op)==0 or len(fval)==0:
        return ''
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
            if res:
                return res
    return ''

# 取一个(<pqs>)选择器的 值/属性
def pqone(dom, pqs, attr='text'):
    e = pyq(dom).find(pqs)
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
            'url':{}, 'save':{},
        }
    # end
    debug['run']['stamp2'] = time.time()
    debug['run']['end'] = now,
    debug['run']['timen'] = debug['run']['stamp2'] - debug['run']['stamp1']
    data = str(debug)
    fp = time.strftime("%m%d-%H%M%S", time.localtime()) + '.txt'
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