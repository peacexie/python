
import time

print('Status: 200 OK')
print('Content-Type: text/html')
print("\n")

print("<!DOCTYPE html><html><head>")
print("<meta charset='utf-8'>")
print("<meta http-equiv='X-UA-Compatible' content='IE=edge,chrome=1'>")
print("<meta name='viewport' content='width=device-width'>")
print("<meta name='robots' content='noindex, nofollow'>")
print("<title>Python-CGI Sample Page</title>")
print("</head><body>")

print("<h1>Python-CGI Sample Page</h1>")

for i in range(5):
    print(i)

print("<p>")
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print("</p>")

print("</body></html>")
