import sqlite3

class Database():
    def __init__(self):
        self.name = 'SQlite_telegramm.db'

    def create_db(self):
        try:
            sqliteConnection = sqlite3.connect(self.name)
            cursor = sqliteConnection.cursor()
            sqlite_create_table_query = '''CREATE TABLE users (
                                       id INTEGER PRIMARY KEY,
                                       link TEXT NOT NULL,
                                       joiningDate timestamp);'''
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("База данных создана и успешно подключена к SQLite")
            cursor.close()   
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    def add_user(self, link, date):
        try: 
            sqliteConnection = sqlite3.connect(self.name)
            cursor = sqliteConnection.cursor()
            sqlite_insert_with_param = """INSERT INTO 'users'
                          ('link', 'joiningDate') 
                          VALUES (?, ?);"""
            data_tuple = (link, date)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    def show_users(self):
        users = []

        try:
            sqliteConnection = sqlite3.connect(self.name)
            cursor = sqliteConnection.cursor()
            cursor.execute('select link from users')
            records = cursor.fetchall()
            users = [i[0] for i in records]
            cursor.close()
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
        
        return users



    

db = Database()
#print(db.show_users())
db.create_db()
#db.add_user('ffs', datetime.datetime.now())