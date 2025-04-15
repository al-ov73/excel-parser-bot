import sqlite3
import os
import pandas as pd

DB_PATH = "laptop.db"

def init_db() -> None:
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL UNIQUE,
                xpath TEXT NOT NULL
            )
        """)
        conn.commit()


def save_to_db(df: pd.DataFrame) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        for _, row in df.iterrows():
            title: str = row["title"]
            url: str = row["url"]
            xpath: str = row["xpath"]

            cursor.execute("SELECT 1 FROM sites WHERE url = ?", (url,))
            if cursor.fetchone():
                continue

            cursor.execute(
                "INSERT INTO sites (title, url, xpath) VALUES (?, ?, ?)",
                (title, url, xpath)
            )

        conn.commit()

def get_all_sources() -> list[tuple[str, str, str]]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT title, url, xpath FROM sites")
        return cursor.fetchall()