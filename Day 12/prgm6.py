class InvalidInputError(Exception):
    pass

def sequential_subtraction(numbers):
    if len(numbers) < 2:
        raise InvalidInputError("List must contain at least two numbers")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise InvalidInputError("List must only contain numbers")
    
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    
    return result

# Exmp
try:
    numbers = [10, 6, 5, 1]
    result = sequential_subtraction(numbers)
    print(result)  
except InvalidInputError as e:
    print(e)
