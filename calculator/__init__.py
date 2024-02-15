# calculator.py

class Calculation:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def add(self):
        return self.operand1 + self.operand2

    def subtract(self):
        return self.operand1 - self.operand2

    def multiply(self):
        return self.operand1 * self.operand2

    def divide(self):
        if self.operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return self.operand1 / self.operand2

class Calculator:
    @staticmethod
    def perform_operation(operation, a, b):
        calculation = Calculation(a, b)
        return getattr(calculation, operation)()
