fruits = ('apple', 'banana', 'cherry')

try:
    fruits[1] = 'blueberry'
except TypeError as e:
    print("Error: Tuples are immutable. You cannot change their elements.")
    print("Detailed Error:", e)