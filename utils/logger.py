import os.path


class Logger:
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs", "app.log")

    @staticmethod
    def logging(log):
        with open(Logger.LOG_FILE, 'a', encoding="utf-8") as f:
            f.write(log + '\n')