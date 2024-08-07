def index(s, index):
    if index < 0 or index >= len(s):
        return "Index out of bounds"
    else:
        return s[index]

# Exmp used
print(index("Eman", 2)) 
print(index("Zeb", 10)) 