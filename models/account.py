from models.transaction import BaseTransaction
from utils.logger import Logger
from utils.balance_loader import BalanceLoader


class Account:
    """Класс счёта пользователя"""
    def __init__(self, initial_balance=0):
        self.logger = Logger()
        self.balance_loader = BalanceLoader()
        self.__balance = self.balance_loader.load_balance()

    def apply_transaction(self, transaction: BaseTransaction, amount):
        self.__balance, log = transaction.apply(self.__balance, amount)
        self.logger.logging(log)

    def get_balance(self):
        return self.__balance