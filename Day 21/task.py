#Hello,Welcome to eman's inventary system
inventory = []     #Initializing inventary list
def add_product():      #Function to add product
    product_name = input("Enter the product name: ")
    product_id = input("Enter the product ID: ")
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    
    product = {
        "name": product_name,
        "id": product_id,
        "quantity": quantity,
        "price": price
    }
    
    inventory.append(product)
    print("Product added successfully!\n")
def view_inventory():   #Function to view inventary
    if len(inventory) == 0:
        print("No products available in the inventory.\n")
    else:
        print("Current Inventory:")
        for product in inventory:
            print(f"ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}, Price: {product['price']}")
        print("")
def update_product_quantity():  #Function to add quantity
    product_id = input("Enter the product ID to update quantity: ")
    for product in inventory:
        if product['id'] == product_id:
            new_quantity = int(input("Enter the new quantity: "))
            product['quantity'] = new_quantity
            print("Product quantity updated successfully!\n")
            return
    print("Product ID not found.\n")
def remove_product():   #Function to remove product
    product_id = input("Enter the product ID to remove: ")
    for product in inventory:
        if product['id'] == product_id:
            inventory.remove(product)
            print("Product removed successfully!\n")
            return
    print("Product ID not found.\n")
def main():      #main function
    while True:
        print("Simple Inventory Management System")
        print("1. Add a New Product")
        print("2. View Inventory")
        print("3. Update Product Quantity")
        print("4. Remove a Product")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_product_quantity()
        elif choice == '4':
            remove_product()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
if _name_ == "_main_":
    main()