import sys

sys.path.append("..")
import impy.core.comStr
import impy.test.Test1

t2 = impy.test.Test1.fact(60) #960
print(t2);

t1 = impy.core.comStr.filSafe4("<b>Hi,impy!</b>")
print(t1);

t2 = impy.test.Test1.fact(5)
print(t2);

"""
try:
    f = open('./test1.py', 'r')
    s = f.read()
    print(s)
finally:
    if f:
        f.close()
"""
