from abc import ABC, abstractmethod


class Validator(ABC):
    """Абстрактный класс для валидаторов"""
    # Должно быть положительное, целое число
    @abstractmethod
    def validate(self, value):
        pass


class EmptyStrValidator(Validator):
    """Валидатор для проверки пустоты строки"""
    def validate(self, value):
        if value is None or value == "":
            raise ValueError("Ошибка! Поле не должно быть пустым!")
        return value


class IntegerValidator(EmptyStrValidator):
    """Валидатор для проверки целых чисел"""
    def validate(self, value):
        value = super().validate(value)
        try:
            return int(value)
        except ValueError:
            raise ValueError("Ошибка: Введите целое число.")


class PositiveNumberValidator(IntegerValidator):
    """Валидатор для проверки положительных чисел"""
    def validate(self, value):
        number = super().validate(value)
        if number <= 0:
            raise ValueError("Ошибка: Введите положительное число.")
        return number


class CommentValidator(Validator):
    """Валидатор для комментариев"""
    def validate(self, comment):
        if not (5 <= len(comment) <= 60):
            raise ValueError("Комментарий должен иметь от 5 до 60 символов!")
        return comment