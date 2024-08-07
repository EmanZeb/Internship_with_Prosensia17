def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Exmp ues
num1 = 10
num2 = 5
result = divide_numbers(num1, num2)
print(result)  

num1 = 10
num2 = 0
try:
    result = divide_numbers(num1, num2)
except ValueError as e:
    print(e)  