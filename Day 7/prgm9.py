def check_positivity(a, b):
    if a > 0 and b > 0:
        print("Both are positive")
    elif a > 0 or b > 0:
        print("One is positive")
    else:
        print("None are positive")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
check_positivity(number1, number2)
