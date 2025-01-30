import tkinter as tk
from tkinter import ttk
from utils.loaders import HistoryLoader
from controllers.controller import Controller
from utils.validator import PositiveNumberValidator, CommentValidator
from utils.transaction_formatter import TransactionFormatter


class View:
    """Класс для отображения окна приложения"""
    def __init__(self):
        self.controller = Controller()
        self.validator = PositiveNumberValidator()
        self.comm_validator = CommentValidator()
        self.hl = HistoryLoader()
        self.formatter = TransactionFormatter()
        self.root = tk.Tk()
        self.root.title("Домашняя бухгалтерию")
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()
        self.root.geometry(f'{int(self.x * 0.6)}x{int(self.y * 0.6)}')

        self.balance_label = ttk.Label(self.root, text=f'Баланс: {self.controller.get_balance()}')
        self.balance_label.pack()

        self.label_entry = ttk.Label(self.root, text='Сумма')
        self.label_entry.pack()

        self.entry_amount = ttk.Entry(self.root)
        self.entry_amount.pack()

        self.label_entry = ttk.Label(self.root, text='Комментарий')
        self.label_entry.pack()

        self.entry_comment = ttk.Entry(self.root, name='comment')
        self.entry_comment.pack()

        self.income_button = ttk.Button(self.root, text='Добавить прибыль', command=self.add_income)
        self.income_button.pack()

        self.expense_button = ttk.Button(self.root, text='Добавить расход', command=self.add_expense)
        self.expense_button.pack()

        self.expense_button = ttk.Button(self.root, text='Взять кредит', command=self.take_credit)
        self.expense_button.pack()

        self.transaction_history = tk.Text(self.root, height=5, width=100)
        self.transaction_history.pack()

        transactions = self.formatter.format(self.hl.load_history())

        for i, trans in enumerate(transactions, start=1):
            self.transaction_history.insert(f"{i}.0", trans + "\n")

    def add_income(self):
        try:
            comment = self.comm_validator.validate(self.entry_comment.get())
            self.controller.process_income(PositiveNumberValidator.validate(self.validator, self.entry_amount.get()),
                                           comment)
            self.update_balance()
        except ValueError as e:
            print(str(e))

    def add_expense(self):
        try:
            comment = self.comm_validator.validate(self.entry_comment.get())
            self.controller.process_expense(PositiveNumberValidator.validate(self.validator, self.entry_amount.get()),
                                            comment)
            self.update_balance()
        except ValueError as e:
            print(str(e))

    def take_credit(self):
        try:
            comment = self.comm_validator.validate(self.entry_comment.get())
            self.controller.process_credit(PositiveNumberValidator.validate(self.validator, self.entry_amount.get()),
                                           comment)
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