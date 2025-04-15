from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
import pandas as pd

from .db import get_all_sources, save_to_db
from .utils import format_sources, format_sources_output, validate_dataframe

router = Router()

kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить все источники")]
    ],
    resize_keyboard=True
)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "Привет! Чтобы добавить сайты для парсинга:\n\n"
        "Прикрепите Excel-файл (`.xlsx`) с колонками:\n"
        "- `title` — название\n"
        "- `url` — ссылка\n"
        "- `xpath` — путь к цене\n\n"
    )
    await message.answer(text, reply_markup=kb)

@router.message(lambda msg: msg.document is not None)
async def handle_file(message: types.Message):
    doc = message.document
    if not doc.file_name.endswith((".xlsx", ".xls")):
        await message.reply("Пожалуйста, загрузите файл Excel (.xlsx или .xls).")
        return

    file_path = f"data/files/{doc.file_name}"
    await message.bot.download(doc, destination=file_path)

    try:
        df = pd.read_excel(file_path)
        if not validate_dataframe(df):
            await message.reply("Файл должен содержать столбцы: title, url, xpath.")
            return

        formatted = format_sources_output(df)
        await message.reply(f"Содержимое файла:\n\n{formatted}")
        save_to_db(df)
        await message.reply("Данные сохранены в базу данных.")

    except Exception as e:
        await message.reply(f"Ошибка при обработке файла: {e}", reply_markup=kb)
        
@router.message(F.text == "Получить все источники")
async def handle_get_sources(message: Message) -> None:
    sources = get_all_sources()

    if not sources:
        await message.answer("Список источников пуст.")
        return

    text = format_sources(sources)
    await message.answer(text, reply_markup=kb)
