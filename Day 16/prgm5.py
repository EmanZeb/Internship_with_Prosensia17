filename = 'data.txt'
try:
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1
    print(f"The number of lines in '{filename}' is: {line_count}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")