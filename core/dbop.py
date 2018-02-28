
from flask import g
import pymysql, sqlite3 #, pymssql, 
#from contextlib import closing

class dbm:
    def __init__(self, cfgs={}):
        cfgs = cfgs if cfgs else g.cdb
        self.cfgs = cfgs
        self.dbcon()

    def dbcon(self):
        cfgs = self.cfgs
        if cfgs['type']=='sqlite3':
            self.con = sqlite3.connect(cfgs['name'])
            def dict_factory(cursor, row): 
                d = {} 
                for idx, col in enumerate(cursor.description): 
                    d[col[0]] = row[idx] 
                return d
            self.con.row_factory = dict_factory
            self.cur = self.con.cursor()
        else:
            drive = __import__(self.cfgs['type']) #g.db['type']
            self.con = drive.connect(host=cfgs['host'], user=cfgs['user'], password=cfgs['pass'], database=cfgs['name'], charset="utf8")
            self.cur = self.con.cursor(cursor=drive.cursors.DictCursor)

        if not self.cur:
            raise(NameError, "Database Error!")

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
        if type(a) == list :
            res = cur.executemany(self.table(sql), parms)
        else:
            res = cur.execute(self.table(sql), parms)
        self.conn.commit()
        return res

    def script(self, sql, parms=''):
        self.exe(sql)

