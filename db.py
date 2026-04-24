import sqlite3
from flask import g

def get_db_con():
    g.db_con = sqlite3.connect('path/to/db.sqlite')
    return g.db_con

def close_db_con():
    g.db_con.close()
    g.pop('db_con')
    
