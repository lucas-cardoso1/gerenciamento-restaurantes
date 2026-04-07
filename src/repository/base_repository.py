import sqlite3

class BaseRepository:
    def __init__(self, db_name="restaurante.db"):
        self.db_name = db_name

    def query(self, sql, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor

    def fetch_all(self, sql, params=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.fetchall()