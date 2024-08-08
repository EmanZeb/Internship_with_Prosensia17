my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list.append(4)
print(my_list)

try:
    my_tuple.append(4)
except AttributeError as e:
    print("Error:", e)