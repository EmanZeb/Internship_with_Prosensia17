def convert_to_integers(string_list):
    integer_list = []
    error_log = []

    for string in string_list:
        try:
            integer_list.append(int(string))
        except ValueError:
            error_log.append(f"Error converting '{string}' to integer")

    return integer_list, error_log

# Exmp used
string_list = ["1", "2", "three", "4", "five"]
integers, errors = convert_to_integers(string_list)
print("Integers:", integers)
print("Error log:", errors)
