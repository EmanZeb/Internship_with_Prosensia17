def search_replace(s, search_term, replacement_term):
    if not isinstance(s, str) or not isinstance(search_term, str) or not isinstance(replacement_term, str):
        raise ValueError("All inputs must be strings")
    return s.replace(search_term, replacement_term)

# Exmp used
print(search_replace("hello eman", "eman", "see"))