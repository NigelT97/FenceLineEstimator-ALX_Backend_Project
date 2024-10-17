import sqlite3

def get_db():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    conn = get_db()
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
