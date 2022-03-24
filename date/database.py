from asyncio.windows_events import NULL
import sqlite3



class DB:
    def __init__(self):
        self.conn = sqlite3.connect('jobhunter.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS posts(id integer primary key, id_user text, type text, contacts text, description text, payment text, publication_date text)''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS users(id integer primary key, login text, password text, type text, description text)''')
        self.conn.commit()

    def insert_data(self, id_user, type, contacts, description, payment, publication_date):
        self.c.execute('''INSERT INTO posts (id_user, type, contacts, description, payment, publication_date) VALUES (?, ?, ?, ?, ?, ?)''',
                       (id_user, type, contacts, description, payment, publication_date))
        self.conn.commit()
    
    def insert_users(self,login,password, type, description):
        self.c.execute('''INSERT INTO Users(login, password, type, description) VALUES (?, ?, ?, ?)''',
                       (login, password, type, description))
        self.conn.commit()