#coding=UTF-8
import sys
sys.path.append("../")
sys.path.append("../imps/")

from core import urlpy
#from core import pycls


# 
"""
http://txmao.txjia.com/
https://tieba.baidu.com/p/2460150866
"""
url = "http://txmao.txjia.com/chn.php?cargo"
html = urlpy.page(url)
#print(html)

print('')
list = urlpy.list(html, 'pics')
print(list)

print('')
list = urlpy.list(html, 'links') # links,title
print(list)


# http://blog.csdn.net/eastmount/article/details/51082253
#print(getImg(html,url))
# print()
