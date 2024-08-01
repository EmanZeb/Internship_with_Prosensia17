def find():
    numbers = [float(y) for y in input("Enter numbers separated by spaces: ").split()]
    if numbers:
        largest = max(numbers)
        smallest = min(numbers)
        print(f"Largest: {largest}, Smallest: {smallest}")
    else:
        print("No numbers were entered.")
find()
