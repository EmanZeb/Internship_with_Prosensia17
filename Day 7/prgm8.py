def compute_gross_pay(hours, rate):
    overtime_threshold = 40
    if hours > overtime_threshold:
        overtime_hours = hours - overtime_threshold
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = overtime_threshold * rate
        total_pay = regular_pay + overtime_pay
    else:
       total_pay = hours * rate
    return total_pay

hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
gross_pay = compute_gross_pay(hours_worked, hourly_rate)
print(f"Gross pay: {gross_pay}")