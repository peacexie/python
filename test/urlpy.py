#coding=UTF-8

import sys, io
sys.path.append("../")
from core import config, urlpy
#_cfgs = config.init()

# gb18030,utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 
"""
http://txmao.txjia.com/
https://tieba.baidu.com/p/2460150866
"""
url = "http://txmao.txjia.com/chn.php?cargo"
html = urlpy.page(url)
#print(html)


url = "http://z6m.me"
z6m = urlpy.page(url)
itms = urlpy.list(z6m, 'pics')
print(itms)
#urlpy.save(list, 'tmpic', 'http://z6m.me');
for itm in itms:
    url = itm[0]
    if url.find('://')<=0:
        url = base+url
    file = urlpy.svurl(url, 'pics') # path
    print(file)


print('')
str = urlpy.block(html, '<div class="pgf_menu">', '</div>')
print(str)

print('')
itms = urlpy.list(html, 'links') # links,title
#print(itms)

print('')
itmp = urlpy.list(html, 'pics')
#print(itmp)
#urlpy.save(list, 'tmpic', 'http://txmao.txjia.com');

urlpy.svurl(url, 'tmps')
pic = 'http://dg.fzg360.com/template/default/images/logo306.gif'
urlpy.svurl(pic, 'tmps')

pag1 = 'http://txmao.txjia.com/chn.php?mkv=cargo&stype=p2012&price=300~500&brand=huawei'
urlpy.svurl(pag1, 'tmps')


'''
asp,php,jsp,aspx,do
'''

_envs = config.envs()
base = 'http://txmao.txjia.com'
itms = itmp[1:3]
for itm in itms:
    url = itm[0]
    if url.find('://')<=0:
        url = base+url
    file = urlpy.svurl(url, 'pics') # path
    print(file)

# http://blog.csdn.net/eastmount/article/details/51082253
#print(getImg(html,url))
# print()
