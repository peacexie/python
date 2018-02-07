#coding=UTF-8

import sys

sys.path.append("../")
sys.path.append("../imps")

from pyquery import PyQuery as pyq

# ------ txjia.com

doc = pyq(url=r'http://txjia.com/tip/')  
itms = doc('div.home-b')  

for i in itms:  
    print('\n====', pyq(i).find('b').text(), '====')  
    for j in pyq(i).find('ul a'):  
        print(pyq(j).attr('href'), pyq(j).text(),)

# ------ fzg360.com

doc = pyq(url=r'http://m.dg.fzg360.com/index.php?caid=46')  
itms = doc('div.zgzjsp-box')  
   
for i in itms:  
    print('\n====', pyq(i).find('.tit p').text(), '====')  
    for j in pyq(i).find('.content_box a'):
        fli = pyq(j).find('li:first')
        print(pyq(j).attr('href'), pyq(fli).text(),) 
