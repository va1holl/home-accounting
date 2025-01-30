import datetime
import os.path
from datetime import datetime
from models.database import DataBaseInsert


class Logger:
    @staticmethod
    def time_now():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class LocalLogger(Logger):
    """Класс логгера. Все логи в папке logs/app.log"""
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "app.log")

    @classmethod
    def logging(cls, log):
        with open(cls.LOG_FILE, 'a', encoding="utf-8") as f:
            f.write(f'[{super().time_now()}]{log}\n')


class DataBaseLogger(Logger):
    local_logger = LocalLogger()
    db = DataBaseInsert()

    def logging(self, log):
        self.local_logger.logging(log)
        date = super().time_now()
        full_log = (date,) + log
        self.db.insert(full_log)