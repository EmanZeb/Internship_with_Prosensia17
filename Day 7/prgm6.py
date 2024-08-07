def categorize_number():
    number = int(input("Enter an integer: "))
    if number < 10:
        print("Small")
    elif 10 <= number <= 20:
        print("Medium")
    else:
        print("Large")

categorize_number()