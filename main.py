# main.py
from decimal import Decimal, InvalidOperation
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def calculate_and_print(num1_str, num2_str, operation_str):
    # Map string operation names to actual function objects
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    try:
        # Convert string inputs to Decimal
        num1 = Decimal(num1_str)
        num2 = Decimal(num2_str)
        
        # Get the operation function based on operation_str
        operation = operations.get(operation_str)
        
        # Handle unknown or unsupported operations
        if operation is None:
            print("Unknown operation.\n")
            return
        
        # Create and perform the calculation
        calc = Calculation(num1, num2, operation)
        result = calc.perform()
        print(f"The result of {num1} {operation_str} {num2} is equal to {result}\n")
    except InvalidOperation:
        print("An error occurred: Invalid literal for Decimal.\n")
    except ZeroDivisionError:
        print("An error occurred: Division by zero.\n")
    except Exception as e:
        # Generic error handling to catch any unexpected errors
        print(f"An unexpected error occurred: {e}\n")
