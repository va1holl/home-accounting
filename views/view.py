import tkinter as tk
from controllers.controller import Controller


class View:
    def __init__(self):
        self.controller = Controller()
        self.root = tk.Tk()
        self.root.title("Домашняя бухгалтерию")

        self.balance_label = tk.Label(self.root, text=f'Баланс: {self.controller.get_balance()}')
        self.balance_label.pack()

        self.income_button = tk.Button(self.root, text='Добавить прибыль', command=self.add_income)
        self.income_button.pack()

        self.expense_button = tk.Button(self.root, text='Добавить расход', command=self.add_expense)
        self.expense_button.pack()

    def add_income(self):
        self.controller.process_income(100, 'Тест_доход_100')
        self.update_balance()

    def add_expense(self):
        try:
            self.controller.process_expense(50, 'Тест_расход_50')
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