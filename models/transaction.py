from enum import Enum
from abc import ABC, abstractmethod


class TypeTransactions(Enum):
    INCOME = 'income'
    CREDIT = 'credit'
    EXPENSES = 'expenses'


class BaseTransaction(ABC):
    def __init__(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment

    @abstractmethod
    def apply(self, balance, amount):
        pass


class IncomeTransaction(BaseTransaction):
    def apply(self, balance, amount):
        log = (f"Баланс пополнен на {amount}. "
               f"Описание: {TypeTransactions.INCOME.value, self.get_comment()}. "
               f"Текущий баланс: {balance + amount}")
        return balance + amount, log


class CreditIncomeTransaction(IncomeTransaction):
    def apply(self, balance, amount):
        log = (f"Баланс пополнен на {amount}. "
               f"Описание: {TypeTransactions.CREDIT.value, self.get_comment()}. "
               f"Текущий баланс: {balance + amount}")
        return balance + amount, log


class ExpensesTransaction(BaseTransaction):
    def apply(self, balance, amount):
        if balance < amount:
            raise ValueError("Расход превышает баланс.")
        log = (f"Списано с баланса {amount}. "
               f"Описание: {TypeTransactions.EXPENSES.value, self.get_comment()}. "
               f"Текущий баланс: {balance - amount}")
        return balance - amount, log