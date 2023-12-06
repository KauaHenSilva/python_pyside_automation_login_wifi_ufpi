import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / 'dbUserPassword.db'

def create_table_if_not_exists():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS login_info (
                id INTEGER PRIMARY KEY,
                user TEXT,
                password TEXT
            )
        ''')

def loginSave(login: str, password: str):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO login_info (user, password) VALUES (?, ?)", (login, password))

def loginRecover() -> list[str]:
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user, password FROM login_info ORDER BY id DESC LIMIT 1")
            result = cursor.fetchone()
        
        if result is not None:
            return list(result)
        else:
            return ['', '']

    except sqlite3.OperationalError as e:
        create_table_if_not_exists()
        return ['', '']
        
