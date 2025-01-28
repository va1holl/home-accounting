class BaseTransaction:
    def __init__(self, comment):
        self._comment = comment

    def get_comment(self):
        return self._comment


class IncomeTransaction(BaseTransaction):
    @staticmethod
    def apply(balance, amount):
        return balance + amount


class CreditIncomeTransaction(IncomeTransaction):
    @staticmethod
    def credit(balance, amount):
        return balance + amount


class ExpensesTransaction(BaseTransaction):
    @staticmethod
    def spend(balance, amount):
        if balance < amount:
            raise ValueError("Расход превышает баланс.")
        return balance - amount