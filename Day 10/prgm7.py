def compareStrings(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both inputs must be strings")
    if s1 < s2:
        return "First string comes before the second string"
    elif s1 > s2:
        return "First string comes after the second string"
    else:
        return "Both strings are equal"

# Exmp used
print(compareStrings("apple", "banana"))  
print(compareStrings("hello", "hello"))  