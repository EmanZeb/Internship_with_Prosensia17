def evaluate_polynomial(coefficients, x):
    degree = len(coefficients) - 1
    result = 0

    if degree == 1:  # Linear
        result = coefficients[0] + coefficients[1] * x
    elif degree == 2:  # Quadratic
        result = coefficients[0] + coefficients[1] * x + coefficients[2] * x ** 2
    elif degree == 3:  # Cubic
        result = coefficients[0] + coefficients[1] * x + coefficients[2] * x ** 2 + coefficients[3] * x ** 3
    else:
        for i, coefficient in enumerate(coefficients):
            result += coefficient * x ** (degree - i)

    return result

# Exmp used
coefficients = [1, 2, 3]  # 1 + 2x + 3x^2
x = 2
print(evaluate_polynomial(coefficients, x))  
