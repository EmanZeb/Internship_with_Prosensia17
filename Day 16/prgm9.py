def read_file_using_context_manager(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("File contents:")
        print(content)
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_path = 'data.txt'
read_file_using_context_manager(file_path)