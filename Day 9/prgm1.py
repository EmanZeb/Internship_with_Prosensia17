sum = 0
count = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        number = float(user_input)
        sum += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

if count > 0:
    average = sum / count
    print(f"Sum: {sum}")
    print(f"Average: {average}")
else:
    print("No numbers entered.")