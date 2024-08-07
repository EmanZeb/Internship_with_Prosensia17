def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)  
    return merged_dict
dict1 = {'a': 2, 'b': 2, 'c': 5}
dict2 = {'b': 8, 'd': 9}
merged_dict = merge_dictionaries(dict1, dict2)
print("Merged Dictionary:", merged_dict)