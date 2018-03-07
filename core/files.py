# files:文件相关

import os, time
from urllib import parse
#import re

def get(fp, cset='utf-8', mode='rb'):
    flag = os.path.exists(fp)
    if not flag:
        return ''
    data = ''
    fh = open(fp, mode)
    data = fh.read()
    fh.close()
    if cset:
        data = data.decode(cset)
    return data

def put(fp, data): 
    with open(fp,'w', encoding='utf-8') as f:
        f.write(data)
    f.close()

# 自动文件名
def autnm(url):
    base = os.path.basename(url) # file.php?mod=ext&key=key
    if len(base)==0:
        base = 'index.htm'
    if base.find('?')>0:
        pos = base.find('?')
        pstr = base[(pos+1):len(base)]
        base = base[0:pos]
    else:
        pstr = ''
    exts = os.path.splitext(base) #['/index','.htm']
    base = exts[0]
    ext = exts[1] if len(exts[1])>0 else '.htm'
    exts = '(.asp|.php|.jsp|.aspx|.do)'
    if exts.find(ext)>0 and len(pstr)>0:
        file = base + '---' + pstr + '.htm'
    else:
        file = base if base.find('.')>0 else base + ext
    return file
'''
    tmp1 = 'http://192.168.1.228/'
    tmp2 = 'http://192.168.1.228/dgfzg/admina.php'
    tmp3 = 'http://192.168.1.228/dgfzg/admina.php?'
    tmp4 = 'http://192.168.1.228/dgfzg/admina.php?mod=ext&caid=504'
    tmp5 = 'http://192.168.1.228/dgfzg/admina.jpg?mod=ext&ext=list'
'''

def fulnm(url):
    tmp = parse.urlsplit(url)
    file = tmp[2].replace('/','!')
    if len(tmp[3])>0:
        file += '---' + tmp[3].replace('&',',')
    return file
    pass

# 未超时判断
def tmok(fp, tmout=6):
    flag = os.path.exists(fp)
    if not flag:
        return 0
    ft = os.path.getmtime(fp)
    st = time.time()
    return 1 if st-ft<6*3600 else 0
