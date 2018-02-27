
from flask import g
import pymysql, sqlite3
#from contextlib import closing

class dbm:
    def __init__(self, cfgs={}):
        #self.conn = conn
        self.cfgs = cfgs if cfgs else g.cdb

    def dbcon(self):
        if hasattr(self, 'cur'):
            return self.cur
        if self.cfgs['type']=='sqlite3':
            self.conn = sqlite3.connect(self.cfgs['host'])
        else:
            drive = __import__(self.cfgs['type']) #g.db['type']
            self.conn = drive.connect(host=self.cfgs['host'], user=self.cfgs['user'], password=self.cfgs['pass'], database=self.cfgs['name'], charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError, "Database Error!")
        else:
            self.cur = cur
            return cur

    def close(self):
        self.cur.close()
        self.conn.close()

    def table(self, tbname, sql=1):
        pre = self.cfgs['tbpre']
        fix = self.cfgs['tbfix']
        if sql: # {base_catalog}
            return tbname.replace('{', pre).replace('}', fix)
        else:
            return pre + tbname + fix

    def get(self, sql, parms=(), re=None): # re = 1,n,None
        cur = self.dbcon()
        cur.execute(self.table(sql), parms)
        if not re:
            res = cur.fetchall()
        elif re==1:
            res = cur.fetchone()
        else:
            res = cur.fetchmany(re)
        self.close()
        return res

    def exe(self, sql, parms=(), mod=None):
        cur = self.dbcon()
        if type(a) == list :
            res = cur.executemany(self.table(sql), parms)
        else:
            res = cur.execute(self.table(sql), parms)
        self.conn.commit()
        self.close()
        return res

    def script(self, sql, parms=''):
        self.exe(sql)


# get(1,n,None), exe(sql,parms), batch

def x_dbc(cfgs={}):  
    return dbm(cfgs)

def xxx_close():
    if hasattr(g, 'db'):
        g.db.close()

def conn(cfgs, type='sqlite'):
    cfg = cfgs['cdb']
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = sqlite3.connect('./data' + cfgs['blog']['file'])
    return db

def init_sqlite(sql):
    with closing(connect_db()) as db:
        #with app.open_resource('./schema.sql') as f: 
        #    db.cursor().executescript(f.read()) 
        # ValueError: script argument must be unicode.
        db.cursor().executescript(sql)
        db.commit()

# '''

'''
dbsql = '\
drop table if exists entries;\
create table entries (\
    id integer primary key autoincrement,\
    title string not null,\
    text string not null\
);\

#coding=utf-8 
# sqlserver的连接
import pymssql

def main():

    ms = MSSQL(host="127.0.0.1:1541",user="sa",pwd="写你的密码",db="写你的数据库")
    resList = ms.ExecQuery("SELECT * FROM students")
    print(resList)

if __name__ == '__main__':
    main()

'''
