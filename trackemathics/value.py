class Value:
    def __init__(self, value, source=None):
        self.value = value
        self.source = source

    @property
    def roots(self):
        if (self.source):
            return f"from: {self.source}"

        return 'i am who i am.'

    def narrate(self):
        return f"i am {self.value}. {self.roots}"