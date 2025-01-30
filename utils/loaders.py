from models.database import DataBaseSelect


class Loader:
    db = DataBaseSelect()


class BalanceLoader(Loader):
    """Класс для загрузки баланса с логов"""
    def load_balance(self):
        sql = "SELECT * FROM accounting_logger"
        data = self.db.select(sql)
        current_balance = int(data[-1][-1])
        return current_balance


class HistoryLoader(Loader):
    """Класс для загрузки последних транзакций"""
    def load_history(self):
        sql = "SELECT * FROM accounting_logger"
        data = self.db.select(sql)
        history = data[-10:]
        return history