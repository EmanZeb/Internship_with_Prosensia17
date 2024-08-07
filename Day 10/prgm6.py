def substringWithIndices(s, start, end):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end indices must be integers")
    if start < 0:
        start = 0
    if end > len(s):
        end = len(s)
    return s[start:end]

# Exmp used
print(substringWithIndices("eman", 2, 4))
