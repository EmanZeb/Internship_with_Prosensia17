def convert_to_integers(string_list):
    integer_list = []
    for string in string_list:
        try:
            integer_list.append(int(string))
        except ValueError:
            pass
    return integer_list

# Example usage:
string_list = ["1", "2", "three", "4", "five"]
integer_list = convert_to_integers(string_list)
print(integer_list)  