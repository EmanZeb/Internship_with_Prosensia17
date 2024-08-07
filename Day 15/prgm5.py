class NotANumberError(Exception):
    pass

def add_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise NotANumberError("Both inputs must be numbers")
    return a + b

# Exmp used
try:
    result = add_numbers(3, 5)
    print(result)  # Output: 8
except NotANumberError as e:
    print(e)

try:
    result = add_numbers(3, "five")
    print(result)
except NotANumberError as e:
    print(e) 