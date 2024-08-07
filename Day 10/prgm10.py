def remove_whitespace(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ' '.join(s.split())

# Exmp used
print(remove_whitespace("   Eman         Zeb   "))  