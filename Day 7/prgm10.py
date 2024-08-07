def check_number_type(number):
    if number > 0:
        if number % 2 == 0:
            print("Positive and even")
        else:
            print("Positive but odd")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter a number: "))
check_number_type(num)