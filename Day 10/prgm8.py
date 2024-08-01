def strings(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return {
        "lowercase": s.lower(),
        "uppercase": s.upper(),
        "titlecase": s.title(),
        "original": s  
    }

# Exmp uesd
print(strings("hello Eman Zeb"))