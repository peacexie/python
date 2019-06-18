
'''
import cgi
import cgitb
cgitb.enable()
'''

#print()
print('Status: 200 OK')
print('Content-Type: text/html')
print("\n")

print('<HTML><HEAD><TITLE>Python Sample CGI</TITLE></HEAD>')
print('<BODY>')
print('<H1>Python Sample CGI</H1>')

print('<p>') #this is a comment
print('See this is just like most other HTML')
print('</p><br>')


for i in range(5):
    print(i)


print('</BODY>')
