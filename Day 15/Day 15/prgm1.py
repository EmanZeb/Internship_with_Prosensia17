def complex_operation(num1, num2, operation):
    try:
        real1, imag1 = num1
        real2, imag2 = num2

        if operation == 'add':
            result = (real1 + real2, imag1 + imag2)
        elif operation == 'subtract':
            result = (real1 - real2, imag1 - imag2)
        elif operation == 'multiply':
            result = (real1 * real2 - imag1 * imag2, real1 * imag2 + real2 * imag1)
        elif operation == 'divide':
            denominator = real2 ** 2 + imag2 ** 2
            if denominator == 0:
                raise ValueError("Cannot divide by zero")
            result = ((real1 * real2 + imag1 * imag2) / denominator, (imag1 * real2 - real1 * imag2) / denominator)
        else:
            raise ValueError("Invalid operation")

        return result

    except ValueError as e:
        print(f"Error: {e}")
        return None

# Exmp used
num1 = (1, 2)
num2 = (3, 4)
print(complex_operation(num1, num2, 'add'))  
print(complex_operation(num1, num2, 'subtract'))  
print(complex_operation(num1, num2, 'multiply'))  
print(complex_operation(num1, num2, 'divide'))  