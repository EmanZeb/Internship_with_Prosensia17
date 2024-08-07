def binary_conversion(binary_string, fixed_length):    #func

  integer_value = int(binary_string, 2)
  binary_back = format(integer_value, f'0{fixed_length}b')
  return binary_back

# Exmp used
binary_str = "10110"
fixed_length = 8
result = binary_conversion(binary_str, fixed_length)
print(result)  