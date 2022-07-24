from cmath import log
from sqlalchemy import create_engine, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.schema import Table, MetaData, Column
import sqlite3
import datetime
import logging


class Database():

    def __init__(self):
        self.name = 'SQlite_telegramm.db'

    def create_db(self):
        try:
            sqliteConnection = sqlite3.connect('SQlite_telegramm.db')
            sqliteConnection.close()
            sqlEngine = create_engine(f'sqlite:///{self.name}')

            meta = MetaData()
            meta.reflect(bind=sqlEngine)

            group = Table('Group', meta,
                Column('id_group', Integer, primary_key=True),
                Column('name', String(150), nullable=False)
            )

            users = Table('Users', meta,
                Column('id_user', Integer, primary_key=True),
                Column('link', String(150), nullable=False),
                Column('group_id', Integer, ForeignKey('Group.id_group')),
                Column('joiningDate', DateTime,),
                Column('send_mes', Boolean, default=False, nullable=False)
            )

            meta.create_all(sqlEngine)

        except Exception as ex:
            logging.error('error with work db')
            logging.error(ex)
        finally:
            print('successfully create db')

    def add_group(self, group_name):
        try:
            sqlEngine = create_engine(f'sqlite:///{self.name}')
            meta = MetaData(sqlEngine)
            group = Table('Group', meta, autoload=True)
            conn = sqlEngine.connect()
            ins_group_query = group.insert().values(name = group_name)
            conn.execute(ins_group_query)
            last_query_id = group.select()
            res = conn.execute(last_query_id)
            a = [i.id_group for i in res.fetchall()]
        except Exception as ex:
            logging.error('error with work db')
            logging.error(ex)
        finally:
            logging.info('Группа успешна добавлена')
            return a[-1]

    def add_user(self, link, group_id, date, mes):
        try:
            sqlEngine = create_engine(f'sqlite:///{self.name}')
            meta = MetaData(sqlEngine)
            group = Table('Users', meta, autoload=True)
            conn = sqlEngine.connect()
            ins_group_query = group.insert().values(link = link, group_id = group_id, joiningDate = date, send_mes = mes)
            conn.execute(ins_group_query)
        except Exception as ex:
            logging.error('error with work db')
            logging.error(ex)
        finally:
            logging.info('Пользователь был добавлен')

    def get_user(self):
        try:
            sqlEngine = create_engine(f'sqlite:///{self.name}')
            meta = MetaData(sqlEngine)
            users = Table('Users', meta, autoload=True)
            conn = sqlEngine.connect()
            get_user_query = users.select()
            result = conn.execute(get_user_query)
            res = [i.link for i in result.fetchall()]
            print(res)
        except Exception as ex:
            logging.error('error with work db')
            logging.error(ex)
        finally:
            logging.info('Успешно получены пользователи из базы')
            return res

    def update_user(self, link):
        try:
            sqlEngine = create_engine(f'sqlite:///{self.name}')
            meta = MetaData(sqlEngine)
            users = Table('Users', meta, autoload=True)
            conn = sqlEngine.connect()
            get_user_query = users.update().where(users.c.link == link).values(send_mes = True)
            conn.execute(get_user_query)
        except Exception as ex:
            logging.error('error with work db')
            logging.error(ex)
        finally:
            logging.info('пользователь обновлен')

    def sended_users(self):
        try:
            sqlEngine = create_engine(f'sqlite:///{self.name}')
            meta = MetaData(sqlEngine)
            users = Table('Users', meta, autoload=True)
            conn = sqlEngine.connect()
            get_user_query = users.select().where(users.c.send_mes == True)
            result = conn.execute(get_user_query)
            res = [i.link for i in result.fetchall()]
        except Exception as ex:
            logging.error('error with work db')
            logging.error(ex)
        finally:
            logging.info('Получены пользователи участвовавшие в рассылке')
            return res