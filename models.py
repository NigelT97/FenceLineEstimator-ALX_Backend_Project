import sqlite3
from config import DATABASE_PATH

def get_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    conn = get_db()
    cursor = conn.cursor()
    conn.execute('''
                 CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL UNIQUE,
                 password TEXT NOT NULL,
                 email TEXT
                 );
                 ''')
    conn.commit()
    conn.close()
    
create_user_table()
