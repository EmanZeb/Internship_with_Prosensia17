def calculate_pay():
    try:
        hours_worked = float(input("Enter hours worked: "))
        hourly_rate = float(input("Enter hourly rate: "))
        total_pay = hours_worked * hourly_rate
        print(f"Total pay: ${total_pay:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculate_pay()