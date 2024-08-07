def exponentiation_table(base, exponent_range):
    table = []
    for i in range(1, exponent_range + 1):
        result = base ** i
        table.append(f"{base}^{i} = {result}")
    return table

# Exmp used
base = 2
exponent_range = 5
table = exponentiation_table(base, exponent_range)
for entry in table:
    print(entry)
