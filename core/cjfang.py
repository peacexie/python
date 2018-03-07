
import copy
from urllib import parse
from flask import request, g
from core import dbop, files, urlpy, req
from pyquery import PyQuery as pyq

def test():
    tmp = files.fulnm('https://i.xxx.com/index.aspx?aa=bb&cc=dd#ee')
    print(tmp[2].replace('/','@')+'!'+tmp[3].replace('&',',')) # @index!aa=bb,cc=dd
    print(tmp)

def area(db, act):

    if act=='view':
        return db.get("SELECT * FROM {attr} ORDER BY id")

    dic = [{'type':'area', 'dmkey':'#quyu_name'}, # 区域
        {'type':'price', 'dmkey':'#sjina_D03_08'}] # 价格区间
    
    res = {}
    for dk in dic:

        itms = ritms(g.cjcfg['url'].replace('{page}','1'), dk['dmkey'])
        for i in itms:  
            for j in pyq(i).find('a'):  
                fid = pyq(j).attr('href').replace('/house/s/','').replace('/','')
                title = pyq(j).text()
                sql = "SELECT * FROM {attr} WHERE title=%s AND type=%s"
                row = db.get(sql, (title,dk['type']),1)
                if not row:
                    if act=='done':
                        sql = "INSERT INTO {attr} (title,fid,type) VALUES (%s,%s,%s) "
                        db.exe(sql, (title,fid,dk['type']))
                    res[dk['type']+':'+title] = 'add';
                else:
                    res[dk['type']+':'+title] = 'skip';
    
    return res
    #


def ritms(url, dkey):
    #url = 'http://newhouse.jx.fang.com/house/s/'
    fp = '.' + g.dir['cache'] + '/pages/' + files.fulnm(url)
    ok = files.tmok(fp, 6)
    if ok:
        html = files.get(fp, 'utf-8')
        print('cache')
    else:
        html = urlpy.page(url, 'gb2312', {"Accept-Encoding":"gzip"})
        files.put(fp, html)
        print('from-url')
    doc = pyq(html)
    return doc(dkey)
    #



