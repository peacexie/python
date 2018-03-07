
import copy
from flask import request, g
from core import dbop, files, urlpy, req
from pyquery import PyQuery as pyq


def area(db, act):

    if act=='view':
        return db.get("SELECT * FROM {attr} ")

    url = g.cjcfg['url'].replace('{page}','1') #'http://newhouse.jx.fang.com/house/s/'
    html = urlpy.page(url, 'gb2312', {"Accept-Encoding":"gzip"});
    doc = pyq(html)
    itms = doc('#quyu_name')

    res = {}
    for i in itms:  
        for j in pyq(i).find('a'):  
            fid = pyq(j).attr('href').replace('/house/s/','').replace('/','')
            title = pyq(j).text()
            row = db.get("SELECT * FROM {attr} WHERE title=%s", (title,), 1)
            if not row:
                if act=='done':
                    db.get("INSERT INTO {attr} (title, fid) VALUES (%s, %s) ", (title,fid), 1)
                res[title] = 'add';
            else:
                res[title] = 'skip';
    return res
    #

