def squares():
    N = int(input("Enter a positive integer: "))
    total = sum(i * i for i in range(1, N + 1))
    print(f"Sum of squares: {total}")
squares()