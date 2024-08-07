example_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
key_to_retrieve = 'key4'
value = example_dict.get(key_to_retrieve, 0)
print(f"The value for '{key_to_retrieve}' is: {value}")