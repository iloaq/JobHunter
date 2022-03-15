from asyncio.windows_events import NULL
import sqlite3
import datetime


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('jobhunter.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS posts(id integer primary key, id_user int, type int, contacts text, description text, payment text, publication_date date, completion_date date, status boolean)''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS users(id integer primary key, login text, password text, type text, description text)''')
        self.conn.commit()

    def insert_data(self, id_user, type, contacts, description, payment):
        self.c.execute('''INSERT INTO posts(id_user, type, contacts, description, payment, publication_date, completion_date, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (id_user, type, contacts, description, payment, datetime.datetime.now(), NULL, True))
        self.conn.commit()
    
    def insert_users(self,login,password, type, description):
        self.c.execute('''INSERT INTO Users(login, password, type, description) VALUES (?, ?, ?, ?)''',
                       (login, password, type, description))
        self.conn.commit()