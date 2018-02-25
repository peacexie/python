
import sqlite3
from contextlib import closing

def conn(cfgs):
    return sqlite3.connect('./data' + cfgs['blog']['file'])

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
'''
