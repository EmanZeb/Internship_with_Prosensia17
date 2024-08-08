def sort_dict_by_values(d):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
my_dict = {'a': 10, 'b': 1, 'c': 22}
print(sort_dict_by_values(my_dict))