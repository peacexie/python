
#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
程序分析：关键是计算出每一项的值。

>>> reduce(add, range(1, 11)) Traceback (most recent call last): 
File "", line 1, in <</span>module> reduce(add, range(1, 11)) 
NameError: name 'reduce' is not defined
这种情况是因为在3.3里面，map(),filter()这些的返回值已经不再是list,而是iterators, 
所以想要使用，只用将iterator 转换成list 即可， 比如  list(map()) 

"""

Tn = 0
Sn = []
n = int(input('n = :\n'))
a = int(input('a = :\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print (Tn)

#Sn = list(Sn)
Sn = reduce(lambda x,y : x + y,Sn)
print (Sn)

end = input('\n end:\n')
