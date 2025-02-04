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
        self.root.title("Домашняя бухгалтерия")
        self.x = self.root.winfo_screenwidth()
        self.y = self.root.winfo_screenheight()
        self.root.geometry(f'{int(self.x * 0.55)}x{int(self.y * 0.5)}')

        self.balance_label = ttk.Label(self.root, text=f'Баланс: {self.controller.get_balance()}')
        self.balance_label.place(x=75, y=5)

        self.label_entry = ttk.Label(self.root, text='Сумма:')
        self.label_entry.place(x=10, y=30)

        self.entry_amount = ttk.Entry(self.root)
        self.entry_amount.place(x=95, y=28)

        self.label_entry = ttk.Label(self.root, text='Комментарий:')
        self.label_entry.place(x=10, y=55)

        self.entry_comment = ttk.Entry(self.root)
        self.entry_comment.place(x=95, y=53)

        self.income_button = ttk.Button(self.root, text='Добавить прибыль', command=self.add_income)
        self.income_button.place(x=10, y=80)

        self.expense_button = ttk.Button(self.root, text='Добавить расход', command=self.add_expense)
        self.expense_button.place(x=125, y=80)

        self.expense_button = ttk.Button(self.root, text='Взять кредит', command=self.take_credit)
        self.expense_button.place(x=105, y=105)

        self.transaction_history = tk.Text(self.root, height=8, width=100)
        self.transaction_history.place(x=10, y=200)

        self.start_date_label = ttk.Label(self.root, text='Введите дату в формате "YYYY-MM-DD". C')
        self.start_date_label.place(x=10, y=338)

        self.start_date = ttk.Entry(self.root)
        self.start_date.place(x=250, y=335)

        self.end_date_label = ttk.Label(self.root, text='до')
        self.end_date_label.place(x=380, y=338)

        self.end_date = ttk.Entry(self.root)
        self.end_date.place(x=400, y=335)

        self.get_history_button = ttk.Button(self.root, text='Выбрать дату', command=self.input_history)
        self.get_history_button.place(x=10, y=370)

        transactions = self.formatter.format(self.hl.load_history())
        for i, trans in enumerate(transactions, start=1):
            self.transaction_history.insert(f"{i}.0", trans + "\n")

    def input_history(self):
        if self.start_date.get() == "" and self.end_date.get() == "":
            transactions = self.formatter.format(self.hl.load_history())
        else:
            transactions = self.formatter.format(self.hl.load_history(
            sql=f"SELECT * FROM accounting_logger WHERE date BETWEEN '{self.start_date.get()}' and '{self.end_date.get()}'")
            )
        self.transaction_history.delete("1.0", tk.END)

        if transactions == None:
            print('За данную дату транзакций нет!')
        else:
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