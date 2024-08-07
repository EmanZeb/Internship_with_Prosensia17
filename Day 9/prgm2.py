def values():
    numbers = [float(y) for y in input("Enter numbers separated by spaces: ").split()]
    threshold = float(input("Enter the threshold: "))
    numbers = [num for num in numbers if num > threshold]
    print(f"Numbers greater than {threshold}: {numbers}")
values()