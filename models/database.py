import os
from dotenv import load_dotenv
import psycopg2


class DataBase:
    def __init__(self):
        load_dotenv(dotenv_path="D:\\HomeAccountingProject\\db.env")
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")

    def connect(self):
        try:
            conn = psycopg2.connect(
                dbname=self.DB_NAME,
                user=self.DB_USER,
                password=self.DB_PASSWORD,
                host=self.DB_HOST,
                port=self.DB_PORT
            )
            return conn
        except Exception as e:
            print(f"Ошибка подключения к базе данных: {e}")
            return None


class DataBaseSelect(DataBase):
    def select(self):
        """ Метод для получения данных из базы данных """
        conn = super().connect()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM accounting_logger")
                results = cursor.fetchall()
                return results
            except Exception as e:
                print(f"Ошибка выполнения запроса: {e}")
            finally:
                cursor.close()
                conn.close()  # Закрытие соединения после выполнения запроса
        return None


class DataBaseInsert(DataBase):
    def insert(self, log):
        conn = super().connect()
        if conn is not None:
            try:
                cursor = conn.cursor()
                sql = "INSERT INTO accounting_logger VALUES (%s, %s, %s, %s, %s)"
                val = log
                cursor.execute(sql, val)
                conn.commit()
            except Exception as e:
                print(f"Ошибка выполнения запроса: {e}")
        return None