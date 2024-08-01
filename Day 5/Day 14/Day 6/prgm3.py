def number_check():

  number = float(input("Enter a number: "))

  if number > 0:                         #conditions checking
    print("The number is positive.")
  elif number < 0:
    print("The number is negative.")
  else:
    print("The number is zero.")

if _name_ == "_main_":
  number_check()