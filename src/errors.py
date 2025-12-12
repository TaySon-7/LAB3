class NegativeValueError(Exception):
    def __init__(self, func):
        super().__init__(f"нельзя использваоть отрицательное значение в {func.__name__}")


class EmptyError(Exception):
    def __init__(self):
        super().__init__("Данную операцию нельзя применить к пустому массиву")


class GeneratorError(Exception):
    def __init__(self, message):
        super().__init__(message)


