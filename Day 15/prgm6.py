class InvalidInputError(Exception):
    pass

def sequential_subtraction(numbers):
    if len(numbers) < 2 or not all(isinstance(num, (int, float)) for num in numbers):
        raise InvalidInputError("Input must be a list of at least two numbers")
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

# Exmp used
try:
    numbers = [10, 3, 2, 1]
    result = sequential_subtraction(numbers)
    print(result)  
except InvalidInputError as e:
    print(e)
