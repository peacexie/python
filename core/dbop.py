
from flask import g
import pymysql, sqlite3 #, pymssql, 
#from contextlib import closing

class dbm:
    def __init__(self, cfgs={}):
        cfgs = cfgs if cfgs else g.cdb
        self.cfgs = cfgs

    def dbcon(self):
        if hasattr(self, 'cur'): #hasattr(self, 'cur'): self.key in self.curs
            return self.cur
        if self.cfgs['type']=='sqlite3':
            self.con = sqlite3.connect(self.cfgs['name'])
        else:
            drive = __import__(self.cfgs['type']) #g.db['type']
            self.con = drive.connect(host=self.cfgs['host'], user=self.cfgs['user'], password=self.cfgs['pass'], database=self.cfgs['name'], charset="utf8")
        cur = self.con.cursor()
        if not cur:
            raise(NameError, "Database Error!")
        else:
            self.cur = cur
            return cur

    def close(self):
        self.cur.close()
        self.con.close()

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

def xx_conn(cfgs, type='sqlite'):
    return ''
    cfg = cfgs['cdb']
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = sqlite3.connect('./data' + cfgs['blog']['file'])
    return db

# '''

'''
dbsql = '\
drop table if exists entries;\
create table entries (\
    id integer primary key autoincrement,\
    title string not null,\
    text string not null\
);\

'''
