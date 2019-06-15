from .operation_source import OperationSource

class Value:
    def __init__(self, value, source=None):
        self.value = value
        self.source = source

    def __add__(self, other):
        added = Value(self.value + other.value, OperationSource(f"{self.value} + {other.value}", self, other))
        return added

    def __sub__(self, other):
        subtracted = Value(self.value - other.value, OperationSource(f"{self.value} - {other.value}", self, other))
        return subtracted

    def __mul__(self, other):
        multiplied = Value(self.value * other.value, OperationSource(f"{self.value} * {other.value}", self, other))
        return multiplied

    def __truediv__(self, other):
        divided = Value(self.value / other.value, OperationSource(f"{self.value} / {other.value}", self, other))
        return divided

    @property
    def roots(self):
        if (self.source):
            return f"from: {self.source}"

        return 'i am who i am.'

    def narrate(self):
        return f"i am {self.value}. {self.roots}"