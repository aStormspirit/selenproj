import sqlite3
import datetime

class Database():
    def __init__(self):
        self.name = 'SQlite_telegramm.db'

    def create_db(self):
        try:
            sqliteConnection = sqlite3.connect(self.name)
            cursor = sqliteConnection.cursor()
            sqlite_create_users_query = '''CREATE TABLE IF NOT EXISTS users (
                                       id INTEGER PRIMARY KEY,
                                       link TEXT NOT NULL,
                                       groupName TEXT NOT NULL,
                                       joiningDate timestamp);'''
            cursor.execute(sqlite_create_users_query)
            sqliteConnection.commit()
            print("База данных создана и успешно подключена к SQLite")
            cursor.close()   
        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")

    def add_user(self, link, date, groupId):
        try: 
            sqliteConnection = sqlite3.connect(self.name)
            cursor = sqliteConnection.cursor()
            sqlite_insert_with_param = """INSERT INTO 'users'
                          ('link','groupName','joiningDate') 
                          VALUES (?, ?, ?);"""
            data_tuple = (link, date, groupId)
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