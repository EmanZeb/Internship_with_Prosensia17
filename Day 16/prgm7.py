def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
        
        print(f"Contents copied from {source_path} to {destination_path}.")
    
    except FileNotFoundError:
        print(f"The file {source_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
source_path = 'data.txt'
destination_path = 'data_copy.txt'
copy_file(source_path, destination_path)
