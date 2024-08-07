def clean_and_check_palindrome(input_string):
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    is_palindrome = cleaned_string == cleaned_string[::-1]
    char_frequency = {char: cleaned_string.count(char) for char in set(cleaned_string)}
    
    return is_palindrome, char_frequency

# Exmp uesd
input_string = "A girl, a pen, a camel: Panama"
is_palindrome, char_frequency = clean_and_check_palindrome(input_string)
print(f"Is palindrome: {is_palindrome}")  
print(f"Character frequency: {char_frequency}")