# -*- coding: UTF-8 -*-
import cgitb; cgitb.enable()
print("Status: 200 OK")
print("Content-type: text/html")

print()
print("<h3>Python,你好!</h3>")
#help(5)

def myfunc(a,b):
    c = a + b
    return c

a = 3; b = 2; c = myfunc(a,b)
print(''+str(a)+'+'+str(b)+'='+str(c))

