def concatenate(str1, str2):
    concatenated = str1 + str2
    if concatenated.isdigit():
        return int(concatenated)
    else:
        return concatenated

# Exmp used
print(concatenate("146", "234"))  
print(concatenate("Eman", "Zeb"))  

