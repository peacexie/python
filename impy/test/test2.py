#coding=UTF-8
import sys
sys.path.append("../")

from core import pyfun
from core import pycls

# 函数使用
re = pyfun.add(1, 2)
print(re)
re = pyfun.sub(3, 4)
print(re)

# 类使用(1.初始化+隐含self参数)
cls1 = pycls.cls1()
re = cls1.add(3,4);
print('3+4=',re)
print('3+4=',pycls.cls1.add(0,3,4))

# 类使用(2.无初始化)
re = pycls.cls2.area(5, 6)
print(re)

# 类使用(初始化)
cls2 = pycls.cls2
re = cls2.area(5, 6)
print(re)
re = cls2.around(7)
print(re)



'''
bart = Student.info('Bart Simpson', 59)
lisa = Student.info('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
'''
