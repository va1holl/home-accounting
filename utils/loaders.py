import os
from models.database import DataBaseSelect


class BalanceLoader:
    """Класс для загрузки баланса с логов"""
    def __init__(self):
        self.db = DataBaseSelect()

    def load_balance(self):
        data = self.db.select()
        current_balance = int(data[-1][-1])
        return current_balance