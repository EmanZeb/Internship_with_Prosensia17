file_path = 'data.txt'     #File name  is data.txt

try:
    with open(file_path, 'r') as file:
        content = file.read()            #To read the content present in the fie 
        print(content)           
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except IOError:
    print(f"An error occurred while trying to read the file '{file_path}'.")