## Бот для парсинга excel-файлов

Бот необходим для добавления источников цен в общую базу данных.<br>
Пример данных:<br>
![image](https://github.com/user-attachments/assets/760a1439-36fe-4d89-9a30-88ab7be8346f)

Пример вывода сообщения:<br>
![image](https://github.com/user-attachments/assets/1a969a0e-1535-4c57-876b-7c8f97e2fc56)

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
