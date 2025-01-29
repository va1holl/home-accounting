import os.path


class Logger:
    """Класс логгера. Все логи в папке logs/app.log"""
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "app.log")

    @classmethod
    def logging(cls, log):
        with open(cls.LOG_FILE, 'a', encoding="utf-8") as f:
            f.write(log + '\n')