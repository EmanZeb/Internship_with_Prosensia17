def format_string(template, values):    #Func

  return template.format(**values)

# Exmp used
template_string = "Hello, my name is {name} and I am {age} years old."
values = {"name": "Eman", "age": 19}
formatted_string = format_string(template_string, values)
print(formatted_string)  