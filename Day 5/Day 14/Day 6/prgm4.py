def is_leap_year(year):

  if year % 4 == 0:
    if year % 100 == 0:
      return year % 400 == 0
    else:
      return True
  else:
    return False

def main():
  year = int(input("Enter a year: "))
  if is_leap_year(year):
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")

if _name_ == "_main_":
  main()