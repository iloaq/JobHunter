from date.database import DB

class auth:
    def register():
        DB.insert_users('User', 'Password')


    def login():
        True
