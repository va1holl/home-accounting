from models.account import Account
from models.transaction import IncomeTransaction, ExpensesTransaction


class Controller:
    def __init__(self, initial_balance=0):
        self.account = Account(initial_balance)

    def process_income(self, amount, comment=""):
        transaction = IncomeTransaction(comment)
        self.account.apply_transaction(transaction.apply, amount)

    def process_expense(self, amount, comment=""):
        transaction = ExpensesTransaction(comment)
        self.account.apply_transaction(transaction.spend, amount)

    def get_balance(self):
        return self.account.get_balance()