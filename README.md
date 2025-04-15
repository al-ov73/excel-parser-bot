## Бот для парсинга excel-файлов

Бот необходим для добавления источников цен в общую базу данных.<br>
Пример данных:<br>

Пример вывода сообщеня:<br>

---
Развернуть бота локально:<br>
1. Клонировать репозиторий:
```commandline
git clone git@github.com:al-ov73/excel-parser-bot.git
cd excel-parser-bot
```

2. Установить зависимости
```python
poetry install
```

3. Заполнить файл `.env` 
```commandline
BOT_TOKEN=your_telegram_token
```
4. Запустить бота:
```python
make start
```