import tkinter as tk
from controllers.controller import Controller
from utils.validator import IntegerValidator, PositiveNumberValidator


class View:
    def __init__(self):
        self.controller = Controller()
        self.validator = PositiveNumberValidator()
        self.root = tk.Tk()
        self.root.title("Домашняя бухгалтерию")
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()
        self.root.geometry(f'{int(self.x * 0.4)}x{int(self.y * 0.4)}')

        self.balance_label = tk.Label(self.root, text=f'Баланс: {self.controller.get_balance()}')
        self.balance_label.pack()

        self.entry_amount = tk.Entry(self.root)
        self.entry_amount.pack()

        self.income_button = tk.Button(self.root, text='Добавить прибыль', command=self.add_income)
        self.income_button.pack()

        self.expense_button = tk.Button(self.root, text='Добавить расход', command=self.add_expense)
        self.expense_button.pack()

        self.expense_button = tk.Button(self.root, text='Взять кредит', command=self.take_credit)
        self.expense_button.pack()

    def add_income(self):
        try:
            self.controller.process_income(PositiveNumberValidator.validate(self.validator, self.entry_amount.get()), 'Тест_доход_100')
            self.update_balance()
        except ValueError as e:
            print(str(e))

    def add_expense(self):
        try:
            self.controller.process_expense(PositiveNumberValidator.validate(self.validator, self.entry_amount.get()), 'Тест_расход_50')
            self.update_balance()
        except ValueError as e:
            print(str(e))

    def take_credit(self):
        try:
            self.controller.process_credit(PositiveNumberValidator.validate(self.validator, self.entry_amount.get()), 'Тест_кредит_20')
            self.update_balance()
        except ValueError as e:
            print(str(e))

    def update_balance(self):
        self.balance_label.config(text=f'Баланс: {self.controller.get_balance()}')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    view = View()
    view.run()