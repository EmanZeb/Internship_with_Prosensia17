class DivisionByZeroError(Exception):
    def __init__(self, message="Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)

def divide_numbers(dividend, divisor, precision):
    if divisor == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    result = dividend / divisor
    return round(result, precision)

# Exmp
try:
    dividend = 10
    divisor = 5
    precision = 2
    result = divide_numbers(dividend, divisor, precision)
    print(result)  
except DivisionByZeroError as e:
    print(e)

try:
    dividend = 10
    divisor = 0
    precision = 2
    result = divide_numbers(dividend, divisor, precision)
except DivisionByZeroError as e:
    print(e)