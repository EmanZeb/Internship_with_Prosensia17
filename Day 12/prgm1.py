def convert_to_int(input_string, default_value):
    try:
        return int(input_string)
    except ValueError:
        return default_value

# Exmp used
input_str = "356"
default_val = 0
result = convert_to_int(input_str, default_val)
print(result) 