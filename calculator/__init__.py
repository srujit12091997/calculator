# __init__.py in the calculator directory

# Remove the incorrect import statement
# from calculator import Calculator

#from .calculation import Calculation

from .calculation import Calculation


'''
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
            result = self.operand1 + self.operand2
        elif self.operation == 'subtract':
            result = self.operand1 - self.operand2
        elif self.operation == 'multiply':
            result = self.operand1 * self.operand2
        elif self.operation == 'divide':
            if self.operand2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = self.operand1 / self.operand2
        else:
            raise ValueError("Invalid operation.")
        
        Calculation.history.append(self)  # Add this calculation to the history
        return result

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
            operation_display = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}\
                .get(calc.operation, "Unknown operation")
            print(f"{calc.operand1} {operation_display} {calc.operand2} = {calc.result}")

# The following code only runs when this file is executed as the main script,
# and won't run when imported as a module.
if __name__ == "__main__":
    # Example of using the Calculation class to perform operations and manage history
    Calculation.clear_history()  # Ensure history is clear before starting

    calculation1 = Calculation(10, 5, 'add')
    print("Calculation 1 performed successfully.")

    try:
        calculation2 = Calculation(10, 0, 'divide')
    except ValueError as e:
        print(f"Calculation 2 failed: {e}")

    Calculation.print_history()  # Prints all calculations
    Calculation.clear_history()  # Clears the calculation history after demonstration

'''