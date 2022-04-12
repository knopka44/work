class Calculator:

    @staticmethod
    def validation(x, y):
        assert all(isinstance(number, int) for number in (x, y)), \
            "x or y must be int"
        return True

    def sum(self, x, y):
        self.validation(x, y)
        result = x + y
        return result

    def sub(self, x, y):
        self.validation(x, y)
        result = x - y
        return result

    def mult(self, x, y):
        self.validation(x, y)
        result = x * y
        return result

    def div(self, x, y):
        assert y != 0, 'y must not be 0'
        self.validation(x, y)
        result = x / y
        return result
