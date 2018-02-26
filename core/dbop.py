
from flask import g
import pymysql, sqlite3
#from contextlib import closing

# get(1,n,None), exe(sql,parms), batch

def conn(cfgs, type='sqlite'):
    cfg = cfgs['cdb']
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = sqlite3.connect('./data' + cfg['file'])
    return db

def init_sqlite(sql):
    with closing(connect_db()) as db:
        #with app.open_resource('./schema.sql') as f:
        #    db.cursor().executescript(f.read()) 
        # ValueError: script argument must be unicode.
        db.cursor().executescript(sql)
        db.commit()
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

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():

    ms = MSSQL(host="127.0.0.1:1541",user="sa",pwd="写你的密码",db="写你的数据库")
    resList = ms.ExecQuery("SELECT * FROM students")
    print(resList)

if __name__ == '__main__':
    main()

'''
