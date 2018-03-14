#coding=UTF-8
import sys
import os
sys.path.append("../")

from core import files

tmp1 = 'http://192.168.1.228/'
tmp2 = 'http://192.168.1.228/dgfzg/admina.php'
tmp3 = 'http://192.168.1.228/dgfzg/admina.php?'
tmp4 = 'http://192.168.1.228/dgfzg/admina.php?mod=ext&caid=504'
tmp5 = 'http://192.168.1.228/dgfzg/admina.jpg?mod=ext&ext=list'

file = files.autnm(tmp5)
print('file='+file) # .php
