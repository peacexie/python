#coding=UTF-8

import os
import keyword

a = 'abc,'
b = a * 3
print(b)

num = 25 # float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

import cmath
num = 234 # int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

getcwd = os.getcwd()
print(getcwd)

kws = keyword.kwlist
print(kws)

a=2; b=3;
print(a+b)

x="a"
y="b"
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print( x, end="," )
print( y, end="," )
print( x, end="" )
print( y, end="" )
print()

a, b, c = 1, 2, "runoob"
print(a,b,c)

del a
del b, c

# 用户输入数字
num1 = 1 # input('输入第一个数字：')
num2 = 1 # input('输入第二个数字：')
 
# 求和
sum = float(num1) + float(num2)
 
# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

#help('print')



"""


"""



