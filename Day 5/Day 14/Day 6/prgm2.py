def celsius_to_fahrenheit():

  celsius = float(input("Enter temperature in Celsius: "))
  fahrenheit = (celsius * 9/5) + 32
  print("Temperature in Fahrenheit:", fahrenheit)

if _name_ == "_main_":
  celsius_to_fahrenheit()