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
                await cur.execute(Queries.CREATE_FEEDBACK_TABLE)
                #await cur.execute(Queries.DROP_CATEGORIES_TABLE)#
                #await cur.execute(Queries.DROP_ORDERS_TABLE)#
                await cur.execute(Queries.CREATE_CATEGORIES_TABLE)
                await cur.execute(Queries.CREATE_ORDERS_TABLE)
                #Здесь может быть создание других таблиц которые нам нужны
                await  conn.commit()

    async def execute(self, query: str , params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()

    async def fetch(self, query: str, params: tuple = (), fetch_type: str = "all"):
        async with aiosqlite.connect(self.path) as conn:
            conn.row_factory = aiosqlite.Row
            data = await conn.execute(query, params)
            if fetch_type == "one":
                result = await data.fetchone()
                return dict(result)
            else:
                result = await data.fetchall()
                return [dict(row) for row in result]