# import sqlite3
#
# #Подключаемся к базе данных
# conn = sqlite3.connect('db.sqlite')
#
# #создаем курсор для выполнения запросов
# cur = conn.cursor()
#
# #создаем таблицу
# cur.execute('''
#     CREATE TABLE survey_results (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT
#     )
# ''')
# conn.commit()
# -----------------------------------------------




import aiosqlite
from DataBase.queries import Queries

class Database:
    def __init__(self, path):
        self.path = path

    async def create_table(self):
        async with aiosqlite.connect(self.path) as conn:
            async with conn.cursor() as cur:
                #Создание всех таблиц
                await cur.execute(Queries.CREATE_SURVEY_TABLE)
                #Здесь может быть создание других таблиц которые нам нужны
                await  conn.commit()

    async def execute(self, query,params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()
database = Database('db.sqlite')