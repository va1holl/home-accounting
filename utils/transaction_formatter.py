from models.transaction import TypeTransactions


class TransactionFormatter:
    """Форматирует транзу с БД в красивый текст"""
    @staticmethod
    def format(data):
        max_amount = max([len(str(trans[2])) for trans in data]) + 3
        max_balance = max([len(str(trans[4])) for trans in data]) + 3
        print(max_amount, max_balance)

        returned_list = []

        for trans in data:
            date = trans[0].strftime("%Y-%m-%d %H:%M:%S")
            transaction_type = '-' if trans[1] == TypeTransactions.EXPENSES.value else '+'
            amount = trans[2]
            comment = trans[3]
            current_balance = trans[4]

            part_1 = f'{transaction_type}{amount}'.ljust(max_amount)
            part_2 = f'{current_balance},'.ljust(max_balance)

            returned_list.append(
                f'[{date}]'
                f' {part_1}'
                f'Остаток: {part_2}'
                f'Описание: {comment}'
                )

        return returned_list