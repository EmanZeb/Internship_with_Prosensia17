def fibonacci():
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    fibSequence = [0, 1]
    while len(fibSequence) < N:
        fibSequence.append(fibSequence[-1] + fibSequence[-2])
    print(f"First {N} numbers in the Fibonacci sequence: {fibSequence[:N]}")

fibonacci()