def conditional_join(input_string, delimiter1, delimiter2):
    elements = input_string.split(delimiter1)
    result = delimiter2.join([element for element in elements if len(element) > 3])
    
    return result

# Exmp used
input_string = "hello,world,abc,defghi,jkl"
delimiter1 = ","
delimiter2 = "-"
print(conditional_join(input_string, delimiter1, delimiter2))  