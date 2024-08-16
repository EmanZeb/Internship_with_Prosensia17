def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        
        category = input("Enter the category (e.g., food, transportation, entertainment): ").strip().lower()
        if category not in ["food", "transportation", "entertainment", "other"]:
            print("Invalid category. Please choose from food, transportation, entertainment, or other.")
            return

        description = input("Enter a brief description of the expense: ").strip()

        expense = {"amount": amount, "category": category, "description": description}
        expenses.append(expense)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

def display_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category.capitalize()}: ${total:.2f}")

def main():
    expenses = []
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add a new expense")
        print("2. View summary")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_summary(expenses)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()