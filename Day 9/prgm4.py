def removeDuplicates():
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
    uniqueNumbers = list(set(numbers))
    print(f"List without duplicates: {uniqueNumbers}")
removeDuplicates()