# files:文件相关

import os
#import re

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
