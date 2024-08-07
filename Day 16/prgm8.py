def append_to_file(file_path, text_to_append):
    try:
        with open(file_path, 'a') as file:

            file.write(text_to_append + '\n')
        
        print(f"Successfully appended text to {file_path}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
file_path = 'output.txt'
text_to_append = 'End of file'
append_to_file(file_path, text_to_append)
