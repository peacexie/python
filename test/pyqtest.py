#coding=UTF-8

import sys

sys.path.append("../")
sys.path.append("../imps")

from core import config, urlpy
from pyquery import PyQuery as pyq

'''
* 下图片设置：
    url,      url
    selector, 选择器 img
    inurl,    包含url
    preurl,   url前缀
* 下资料设置
    urlbase   基本url
    urlpages  1,2,3...
'''

# ------ z6m.me(下小黄图)
doc = pyq(url=r'http://z6m.me')  
itms = doc('img')
#print(itms)
for itm in itms:
    url = pyq(itm).attr('src')
    if url.find('/attachment/')>0:
        url = 'http://z6m.me/'+url 
        file = urlpy.svurl(url, 'pics') # path
        print(url)

# ------ txjia.com

doc = pyq(url=r'http://txjia.com/tip/')  
itms = doc('div.home-b')  

for i in itms:  
    print('\n====', pyq(i).find('b').text(), '====')  
    for j in pyq(i).find('ul a'):  
        #print(pyq(j).attr('href'), pyq(j).text(),)
        pass

# ------ fzg360.com

doc = pyq(url=r'http://m.dg.fzg360.com/index.php?caid=46')
itms = doc('div.zgzjsp-box')  
   
for i in itms:  
    print('\n====', pyq(i).find('.tit p').text(), '====')  
    for j in pyq(i).find('.content_box a'):
        fli = pyq(j).find('li:first')
        #print(pyq(j).attr('href'), pyq(fli).text(),) 
        pass
