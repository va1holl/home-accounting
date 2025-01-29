import os


class BalanceLoader:
    """Класс для загрузки баланса с логов"""
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "app.log")

    @classmethod
    def load_balance(cls):
        with open(cls.LOG_FILE, 'r', encoding='utf-8') as f:
            content = f.readlines()
            return int(content[-1].split()[-1])