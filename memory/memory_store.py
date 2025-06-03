# memory/memory_store.py

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "memory.db")

class MemoryStore:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                format TEXT,
                intent TEXT,
                data TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_record(self, source, format_type, intent, data):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO memory (source, format, intent, data)
            VALUES (?, ?, ?, ?)
        ''', (source, format_type, intent, data))
        self.conn.commit()

    def fetch_all(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM memory')
        return cursor.fetchall()