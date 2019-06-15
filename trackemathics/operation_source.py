class OperationSource:
    def __init__(self, operation, *operands):
        self.operation = operation
        self.operands = operands

    def __repr__(self):
        nl = '\n'
        operandss = [op.narrate() for op in self.operands]
        return f"{self.operation}{nl}where:{nl}{nl.join(operandss)}"