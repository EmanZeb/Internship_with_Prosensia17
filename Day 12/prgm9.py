def conditional_join(input_string, delimiter1, delimiter2):
    elements = input_string.split(delimiter1)
    filtered_elements = [element for element in elements if len(element) > 3]
    joined_string = delimiter2.join(filtered_elements)
    
    return joined_string

# Exmp used
input_string = "hello,world,abc,defghi,jkl"
delimiter1 = ","
delimiter2 = "-"
result = conditional_join(input_string, delimiter1, delimiter2)
print(result)  