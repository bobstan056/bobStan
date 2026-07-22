import sqlite3
from datetime import datetime


def init_db(db_path="transcriptions.db"):
    with sqlite3.connect(db_path) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS transcriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            text TEXT,
            words INTEGER,
            sentences INTEGER,
            date TEXT
        )""")
        conn.commit()


def save_transcription(filename, text, words, sentences, db_path="transcriptions.db"):
    with sqlite3.connect(db_path) as conn:
        conn.execute("""INSERT INTO transcriptions(
                       filename,text,words,sentences,date)
                       VALUES(?,?,?,?,?)""", (filename, text, words, sentences, datetime.now().isoformat()))
        conn.commit()


def get_all(db_path="transcriptions.db"):
    with sqlite3.connect(db_path) as conn:
        return conn.execute("SELECT * FROM transcriptions").fetchall()
