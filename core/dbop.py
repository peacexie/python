
from flask import g
import imp # 动态加载: pymysql, sqlite3, pymssql ... 
#from contextlib import closing

class dbm:
    def __init__(self, cfgs={}):
        cfgs = cfgs if cfgs else g.cdb
        self.cfgs = cfgs
        self.dbcon()

    def dbcur_comm(self, cfgs):
        drive = __import__(cfgs['type'])
        host = cfgs['host']; user = cfgs['user']; pwd = cfgs['pass']; name = cfgs['name']
        self.con = drive.connect(host=host, user=user, password=pwd, database=name, charset="utf8")
        self.cur = self.con.cursor(cursor=drive.cursors.DictCursor)

    def dbcur_sqlite3(self, cfgs):
        self.con = __import__('sqlite3').connect(cfgs['name'])
        def cur_dict(cursor, row): 
            d = {} 
            for idx, col in enumerate(cursor.description): 
                d[col[0]] = row[idx] 
            return d
        self.con.row_factory = cur_dict
        self.cur = self.con.cursor()

    def dbcon(self):
        cfgs = self.cfgs
        func = 'dbcur_' + cfgs['type']
        if func in dir(self):
            method = getattr(self, func) 
            method(cfgs)
        else:
           self.dbcur_comm(cfgs)
        if not self.cur:
            print('Database Error!')
            #raise(NameError, "Database Error!")

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
        cur = self.cur
        cur.execute(self.table(sql), parms)
        if not re:
            res = cur.fetchall()
        elif re==1:
            res = cur.fetchone()
        else:
            res = cur.fetchmany(re)
        return res

    def exe(self, sql, parms=(), mod=None):
        cur = self.cur
        if type(parms) == list :
            res = cur.executemany(self.table(sql), parms)
        else:
            res = cur.execute(self.table(sql), parms)
        self.con.commit()
        return res

    def script(self, sql, parms=''):
        self.exe(sql)

