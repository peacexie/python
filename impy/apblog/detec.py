#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import threading
import httplib
import re
import time

class Myclass(threading.Thread):
        def __init__(self,host,path):
                threading.Thread.__init__(self)
                self.host = host
                self.path = path
                self.result = []

        def run(self):
                if "https://" in self.host:
                        conn = httplib.HTTPSConnection(self.host,80,None,None,False,10)
                else:
                        conn = httplib.HTTPConnection(self.host,80,False,10)

                i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-Us; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept": "text/plain"}
                conn.request('GET',self.path,headers = i_headers)
                r1 = conn.getresponse()

                text = r1.read()
                text1 = text.lstrip()

                #size = text.count("\n")
                test = open('ip.txt','a+')
                test.write(text1)


                b = open("ip.txt",'r')
                c = open("ids.txt",'w')
                for line in b.readlines():
                        m = re.search(r'(IP:\d*.\w*.\d*.\d*.\d*)',line)        
                        mm =  m.group(0)
                        owa = mm.replace("IP:","").strip().replace("\n","")
                        self.result =  owa.replace("\n","")
                        c.write(self.result)
                        c.write("\n")
                        #print("write success")
                g = open("ids.txt",'r')
                for lines in g.readlines():
                        getsip =  lines.replace("\n","")
                        try:
                                conns = httplib.HTTPConnection("bgp.he.net",80,False,10)
                        except Exception:
                                print("[-]:connection out time")
                                break
                        else:
                                conns.request('GET','/ip/%s' % getsip,headers = i_headers)
                                r2 = conns.getresponse()
                                texts = r2.read()
                        try:
                                line_split = re.search(r'(<u>.*\d+\D+.*.title=)',texts)
                                obj =  line_split.group(0)
                                print("server:",obj.replace("<u>","").replace("</u>","").replace("\n","").replace("(<a href=\"","search domain:").replace("\" title=","").replace("/dns/",""))
                        
                        except Exception: #e:
                                pass
                        time.sleep(5)
                        #print line_split)

def main():
        if len(sys.argv) < 3:
                print("[*]:Usage python info.py 127.0.0.1 /path")
                sys.exit(1)
        Mythread = Myclass(sys.argv[1],str(sys.argv[2]))
        Mythread.start()

if __name__ == "__main__":
        main()