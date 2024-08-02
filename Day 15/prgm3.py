import math

def round_float(num, strategy):
    if strategy == "up":
        return math.ceil(num)
    elif strategy == "down":
        return math.floor(num)
    elif strategy == "nearest":
        return round(num)
    else:
        raise ValueError("Invalid rounding strategy")

# Example usage:
num = 3.7
print(round_float(num, "down"))  
print(round_float(num, "nearest"))  