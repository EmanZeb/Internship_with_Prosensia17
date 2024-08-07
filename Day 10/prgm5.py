def count(s, char):
    if not isinstance(s, str) or not isinstance(char, str):
        raise ValueError("Both inputs must be strings")
    if len(char) != 1:
        raise ValueError("char must be a single character")
    return s.count(char)

# Exmp used
print(count("eman", "l")) 