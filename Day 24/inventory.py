inventory = []
def add_product(name, price, quantity):#Function to check product already exits 
    for product in inventory:
        if product['name'] == name:
            print(f"Product '{name}' already exists in the inventory.")
            return
    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print(f"Product '{name}' added successfully.")
def update_quantity(name, quantity):
    for product in inventory:
        if product['name'] == name:
            product['quantity'] = quantity
            print(f"Quantity for product '{name}' updated to {quantity}.")
            return
    print(f"Product '{name}' not found in the inventory.")

def display_inventory():
    if not inventory:
        print("The inventory is empty.")
        return
    
    print("\nCurrent Inventory:")
    print(f"{'Name':<20} {'Price':<10} {'Quantity':<10}")
    print("-" * 40)
    for product in inventory:
        print(f"{product['name']:<20} ${product['price']:<10.2f} {product['quantity']:<10}")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add a new product")
        print("2. Update product quantity")
        print("3. Display inventory")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter product name: ").strip()
            try:
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                add_product(name, price, quantity)
            except ValueError:
                print("Invalid input. Price must be a number and quantity must be an integer.")

        elif choice == '2':
            name = input("Enter product name to update: ").strip()
            try:
                quantity = int(input("Enter new quantity: "))
                update_quantity(name, quantity)
            except ValueError:
                print("Invalid input. Quantity must be an integer.")

        elif choice == '3':
            display_inventory()

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")
if __name__ == "__main__":
    main()
