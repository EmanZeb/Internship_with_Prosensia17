def convert_strings_to_ints(string_list):
    int_list = []
    error_log = []
    
    for string in string_list:
        try:
            int_list.append(int(string))
        except ValueError:
            error_log.append(f"Error converting '{string}' to int")
    
    return int_list, error_log

# Exmp
string_list = ["1", "2", "three", "4", "five"]
int_list, error_log = convert_strings_to_ints(string_list)
print("Int List:", int_list)
print("Error Log:", error_log)