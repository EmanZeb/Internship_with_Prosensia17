def compute_pay(hours_worked, hourly_rate):
    overtime_threshold = 40
    if hours_worked <= overtime_threshold:
        return hours_worked * hourly_rate
    else:
        overtime_hours = hours_worked - overtime_threshold
        regular_pay = overtime_threshold * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        return regular_pay + overtime_pay
pay = compute_pay(45, 10)
print(pay)