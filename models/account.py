class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def apply_transaction(self, transaction, amount):
        self.__balance = transaction(self.__balance, amount)

    def get_balance(self):
        return self.__balance