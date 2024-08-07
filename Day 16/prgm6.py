def search_for_errors(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if 'error' in line.lower():
                    print(line.strip())
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_path = 'log.txt'
search_for_errors(file_path)
