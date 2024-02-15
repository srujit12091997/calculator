# calculator.py

class Calculation:
    """Stores details of a calculation operation."""
    history = []  # Class variable to store history of all calculations

    def __init__(self, operand1, operand2, operation):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation = operation
        self.result = self.perform_operation()

    def perform_operation(self):
        """Performs the calculation based on the operation type."""
        if self.operation == 'add':
            return self.operand1 + self.operand2
        elif self.operation == 'subtract':
            return self.operand1 - self.operand2
        elif self.operation == 'multiply':
            return self.operand1 * self.operand2
        elif self.operation == 'divide':
            if self.operand2 == 0:
                raise ValueError("Cannot divide by zero.")
            return self.operand1 / self.operand2

        Calculation.history.append(self)  # Add this calculation to the history

    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history = []

    @classmethod
    def get_history(cls):
        """Returns a list of all performed calculations."""
        return cls.history

    @classmethod
    def print_history(cls):
        """Prints the history of all calculations."""
        for calc in cls.history:
            print(f"{calc.operand1} {calc.operation} {calc.operand2} = {calc.result}")

# Example of using the Calculation class to perform operations and manage history
calculation1 = Calculation(10, 5, 'add')
calculation2 = Calculation(10, 0, 'divide')
Calculation.print_history()  # Prints all calculations
Calculation.clear_history()  # Clears the calculation history
