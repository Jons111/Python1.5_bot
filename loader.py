from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.baza_bilan_ishlash import Database
from data import config

bot = Bot(token='5406652340:AAFwewyBxfdkrTs6U_6jth0oQL5ogEj3jWQ', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

base = Database(path_to_db='baza.db')