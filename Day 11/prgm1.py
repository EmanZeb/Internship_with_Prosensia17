def convert_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        return None

# Exmp used
print(convert_to_int("123"))  
print(convert_to_int("eman"))  