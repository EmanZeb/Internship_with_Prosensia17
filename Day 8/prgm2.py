def max_value(s):
    s = s.replace(" ", "").upper()
    return max(s)
result = max_value("Hello World")
print(result)