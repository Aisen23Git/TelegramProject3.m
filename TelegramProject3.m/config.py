from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
from DataBase.database import Database


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()

database = Database("db.sqlite")