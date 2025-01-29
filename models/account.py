from models.transaction import BaseTransaction
from utils.logger import Logger


class Account:
    """Класс счёта пользователя"""
    def __init__(self, initial_balance=0):
        self.logger = Logger()
        self.__balance = initial_balance

    def apply_transaction(self, transaction: BaseTransaction, amount):
        self.__balance, log = transaction.apply(self.__balance, amount)
        self.logger.logging(log)

    def get_balance(self):
        return self.__balance