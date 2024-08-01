def calculate_operations():

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  sum_result = num1 + num2
  difference = num1 - num2
  product = num1 * num2

  # Handle division by zero
  if num2 != 0:
    quotient = num1 / num2
  else:
    quotient = "Division by zero is not allowed"

  print("Sum:", sum_result)
  print("Difference:", difference)
  print("Product:", product)
  print("Quotient:", quotient)

if _name_ == "_main_":
  calculate_operations()