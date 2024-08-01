def divide_numbers():

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  if num2 == 0:
    print("Division by zero is not allowed.")
  else:
    quotient = num1 / num2
    print("The quotient is:", quotient)

if _name_ == "_main_":
  divide_numbers()