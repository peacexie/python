#coding=UTF-8

import sys
import io
sys.path.append("../")
#sys.path.append("../imps/")

from core import urlpy
#from core import pycls

# gb18030,
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# 
"""
http://txmao.txjia.com/
https://tieba.baidu.com/p/2460150866
"""
url = "http://txmao.txjia.com/chn.php?cargo"
html = urlpy.page(url)
#print(html)

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

base = 'http://txmao.txjia.com'
for itm in itmp:
    url = itm[0]
    if url.find('://')<=0:
        url = base+url
    #file = urlpy.svurl(url, 'pics')
    #print(file)

# http://blog.csdn.net/eastmount/article/details/51082253
#print(getImg(html,url))
# print()
