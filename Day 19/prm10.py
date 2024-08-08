def dict_to_sorted_tuples(d):
    reversed_tuples = [(v, k) for k, v in d.items()]
    sorted_tuples = sorted(reversed_tuples)
    return sorted_tuples
example_dict = {'a': 10, 'b': 1, 'c': 22}
print(dict_to_sorted_tuples(example_dict))