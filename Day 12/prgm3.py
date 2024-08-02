def round_float_to_int(float_num, strategy):
    if strategy == "up":
        return math.ceil(float_num)
    elif strategy == "down":
        return math.floor(float_num)
    elif strategy == "nearest":
        return round(float_num)
    else:
        raise ValueError("Invalid rounding strategy")

# Exmp
float_num = 4.7
strategy = "up"
result = round_float_to_int(float_num, strategy)
print(result)