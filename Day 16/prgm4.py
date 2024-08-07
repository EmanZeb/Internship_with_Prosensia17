filename = 'data.txt'

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line, end='')  

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
