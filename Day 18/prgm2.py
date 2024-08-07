def print_value(dictionary, key):
    if key in dictionary:
        print(f"The value associated with '{key}' is: {dictionary[key]}")
    else:
        print(f"Key '{key}' not found in the dictionary.")
example_dict = {'key1': '1', 'key2': '2', 'key3': '3'}
print_value(example_dict, 'key2')
print_value(example_dict, 'key4')