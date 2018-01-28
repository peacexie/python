#coding=UTF-8

import sys
import io
sys.path.append("../")
sys.path.append("../imps/")

from core import urlpy
#from core import pycls

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

# 
"""
http://txmao.txjia.com/
https://tieba.baidu.com/p/2460150866
"""
url = "http://txmao.txjia.com/chn.php?cargo"
html = urlpy.page(url)
#print(html)

print('')
str = urlpy.cut(html, '<div class="pgf_menu">', '</div>')
print(str)

print('')
list = urlpy.list(html, 'pics')
print(list)
urlpy.save(list, 'tmpic', 'http://txmao.txjia.com');

print('')
list = urlpy.list(html, 'links') # links,title
print(list)


# http://blog.csdn.net/eastmount/article/details/51082253
#print(getImg(html,url))
# print()
