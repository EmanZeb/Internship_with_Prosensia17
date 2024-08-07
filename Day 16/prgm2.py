filename = 'data.txt'    #File name
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line, end='') 

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError as e:
    print(f"Error: An I/O error occurred. Details: {e}")
