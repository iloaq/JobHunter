import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS Users (id integer primary key, login text, password text)''')
        self.conn.commit()

    def insert_data(self, description, costs, total):
        self.c.execute('''INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)''',
                       (description, costs, total))
        self.conn.commit()

    def insert_users(self,login,password):
        self.c.execute('''INSERT INTO Users(login, password) VALUES (?, ?)''',
                       (login, password))
        self.conn.commit()