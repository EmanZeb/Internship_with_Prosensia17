def are_anagrams(string1, string2):     #Func

  def clean_string(string):
    return re.sub(r'\W+', '', string.lower())

  cleaned_string1 = clean_string(string1)
  cleaned_string2 = clean_string(string2)

  if len(cleaned_string1) != len(cleaned_string2):
    return False, {}, {}

  char_count1 = {}
  char_count2 = {}

  for char in cleaned_string1:
    char_count1[char] = char_count1.get(char, 0) + 1

  for char in cleaned_string2:
    char_count2[char] = char_count2.get(char, 0) + 1

  return char_count1 == char_count2, char_count1, char_count2

# Exmp used
string1 = "Anagram"
string2 = "Nag a ram"
is_anagram, freq1, freq2 = are_anagrams(string1, string2)
print(is_anagram)  # Output: True
print(freq1)  
print(freq2)  