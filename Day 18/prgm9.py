example_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
key_to_access = 'key4'

try:
    value = example_dict[key_to_access]
    print(f"The value for '{key_to_access}' is: {value}")
    except KeyError:
        print(f"Error: The key '{key_to_access}' does not exist in the dictionary.")