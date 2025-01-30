from models.transaction import BaseTransaction
from utils.loaders import BalanceLoader
from utils.logger import DataBaseLogger


class Account:
    """Класс счёта пользователя"""
    def __init__(self, initial_balance=0):
        self.balance_loader = BalanceLoader()
        self.db = DataBaseLogger()
        self.__balance = self.balance_loader.load_balance()

    def apply_transaction(self, transaction: BaseTransaction, amount):
        self.__balance, log = transaction.apply(self.__balance, amount)
        self.db.logging(log)

    def get_balance(self):
        return self.__balance