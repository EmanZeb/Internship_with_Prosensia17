filename = 'new_output.txt'

try:
    with open(filename, 'w') as file:
        file.write("Hello, World!")
    print(f"Successfully wrote to {filename}")

except PermissionError as e:
    print(f"Permission error: {e}")

except Exception as e:
    print(f"An error occurred: {e}")
