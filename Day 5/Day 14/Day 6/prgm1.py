def calculate_pay():

  hours_worked = float(input("Enter the number of hours worked: "))
  hourly_rate = float(input("Enter the hourly wage rate: "))

  total_pay = hours_worked * hourly_rate

  print("Total pay:", total_pay)

if _name_ == "_main_":
  calculate_pay()