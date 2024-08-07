import re
from collections import Counter

def clean_and_check_palindrome(input_string):
    cleaned_string = re.sub(r'\W+', '', input_string).lower()
    is_palindrome = cleaned_string == cleaned_string[::-1]
    char_frequencies = Counter(cleaned_string)
    
    return is_palindrome, char_frequencies

# Exmp used
input_string = "A girl, a pen, a camel: Panama"
is_palindrome, char_frequencies = clean_and_check_palindrome(input_string)
print("Is Palindrome:", is_palindrome)
print("Character Frequencies:", char_frequencies)
