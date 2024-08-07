def check_range(number):
    if 10 <= number <= 20:
        print("Within range")
    else:
        print("Out of range")

number = int(input("Enter an integer: "))
check_range(number)
