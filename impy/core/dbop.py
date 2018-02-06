
import sqlite3
from contextlib import closing

def conn(dbcfgs):
    return sqlite3.connect(dbcfgs['path'])

def init_sqlite(dbsql):
    with closing(connect_db()) as db:
        #with app.open_resource('./schema.sql') as f:
        #    db.cursor().executescript(f.read()) 
        # ValueError: script argument must be unicode.
        db.cursor().executescript(dbsql)
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
