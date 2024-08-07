def format_integer(num, format_spec):
    return format(num, format_spec)

# Exmp
num = 12345
format_spec = "05d"  
result = format_integer(num, format_spec)
print(result)  